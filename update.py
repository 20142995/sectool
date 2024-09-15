import os
import re
import sys
import yaml
import json
import time
import asyncio
import aiohttp
import datetime
import tempfile

from urllib.parse import urlparse


async def get_other_url_status(session, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        async with session.get(url, headers=headers) as r:
            status_code = r.status
            content = await r.read()
            html = content.decode('utf8', errors='ignore')
            title = re.search('<title>(.*?)</title>', html, re.I).group(
                1) if re.search('<title>(.*?)</title>', html, re.I) else ''
            return {'url': url, 'status_code': status_code, 'title': title}
    except aiohttp.ClientError as e:
        return {}


async def get_github_url_status(session, url):
    token = os.getenv("GH_TOKEN", "")
    headers = {
        "Authorization": f"token {token}",
        "Connection": "close",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
    }
    def parse_github_date(x): return time.strftime(
        "%Y-%m-%d %H:%M:%S", time.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    try:
        async with session.get(url, headers=headers) as r:
            rj = await r.json()
            item = {}
            # description
            if 'created_at' in rj:
                item['created_at'] = parse_github_date(rj['created_at'])
            if 'description' in rj:
                item['description'] = rj['description']
            # commit
            if isinstance(rj, list):
                if len(rj) > 0:
                    rl = rj[0]
                    if 'commit' in rl:
                        if 'message' in rl['commit']:
                            item['commit_message'] = rl['commit']['message']
                        if 'committer' in rl['commit']:
                            if 'date' in rl['commit']['committer']:
                                item["commit_date"] = parse_github_date(
                                    rl['commit']['committer']["date"])
            # release
            if 'published_at' in rj:
                item['release_date'] = parse_github_date(rj['published_at'])
            if 'body' in rj:
                item['release_message'] = rj['body']
            if 'tag_name' in rj:
                item['release_tag'] = rj['tag_name']
            if item:
                item['url'] = 'https://github.com/' + \
                    '/'.join(url[29:].split("/")[:2])
            return item
    except aiohttp.ClientError as e:
        return {}


async def check_url(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            if url.startswith('https://api.github.com'):
                task = asyncio.ensure_future(
                    get_github_url_status(session, url))
                tasks.append(task)
            else:
                task = asyncio.ensure_future(
                    get_other_url_status(session, url))
                tasks.append(task)
        responses = await asyncio.gather(*tasks)
        results = []
        for response in responses:
            if 'url' in response:
                results.append(response)
        return results


def get_urls_info(urls):
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(check_url(urls))
    return results


def yaml2json(path, encoding="utf8"):
    '''yaml转json'''
    with open(path, 'r', encoding=encoding) as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
    return data


def list_cmp(lst_1, lst_2):
    """
    对比两个列表 减少 遗留 新增
    """
    return [_ for _ in lst_1 if _ not in lst_2], [_ for _ in lst_1 if _ in lst_2], [_ for _ in lst_2 if _ not in lst_1]


def gen_githun_api_url(urls, desc=True, commit=True, release=True):
    new_urls = []
    for url in urls:
        author, repo = url[19:].split("/")[:2]
        if desc:
            new_urls.append(f'https://api.github.com/repos/{author}/{repo}')
        if commit:
            new_urls.append(
                f'https://api.github.com/repos/{author}/{repo}/commits')
        if release:
            new_urls.append(
                f'https://api.github.com/repos/{author}/{repo}/releases/latest')
    return new_urls


def parse_time_str(x): return datetime.datetime.strptime(
    x, "%Y-%m-%d %H:%M:%S")


def update_release():
    data = json.loads(open("data.json", "r", encoding="utf8").read())

    data_github = {url: data[url] for url in data if url.startswith('https://github.com') and data[url].get(
        'commit_date') and parse_time_str(data[url].get('commit_date')) > datetime.datetime.now() - datetime.timedelta(days=730)}
    data_github.update({url: data[url] for url in data if url.startswith(
        'https://github.com') and not data[url].get('commit_date')})

    api_github_urls = gen_githun_api_url(
        data_github.keys(), desc=False, commit=False, release=True)
    for item in get_urls_info(api_github_urls):
        url = item['url']
        if url in data:
            if data[url].get('release_tag', '') != item.get('release_tag', ''):
                print(url[19:].split(
                    "/")[:2][1], data[url].get('release_tag', ''), '->', item.get('release_tag', ''))
                data[url].update(item)
                del data[url]['url']
                data[url]['updated_at'] = time.strftime("%Y-%m-%d %H:%M:%S")
    # 写入data
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def update_readme():
    '''更新README.md'''
    data = json.loads(open("data.json", "r", encoding="utf8").read())
    repos = yaml2json("repos.yaml")
    total_md = "## 所有项目\n"
    msg = []

    def parse_tree(dic, path=1):

        for k, v in dic.items():
            msg.append("{} {}".format("#" * path, k))  # 添加标题
            if isinstance(v, list):
                # 如果值是列表，则对列表进行排序
                v = sorted(v, key=lambda x: data.get(
                    x, {}).get("commit_date", ''), reverse=True)
                for url in v:
                    if url.startswith("https://github.com/"):
                        repo = url[19:].split("/", 1)[1]
                        if data.get(url, {}).get("release_tag", ""):
                            repo += ' ' + data[url]['release_tag']
                        description = data.get(url, {}).get("description", "") if data.get(
                            url, {}).get("description", "") else ''
                    else:
                        repo = ''
                        description = ''
                        if data.get(url, {}).get("title", ''):
                            repo = data.get(url, {}).get("title", '')
                            description = data.get(url, {}).get("description", "") if data.get(
                                url, {}).get("description", "") else ''
                        if data.get(url, {}).get("description", ''):
                            repo = data.get(url, {}).get("description", '')
                            description = ''
                        if repo == '':
                            repo = urlparse(url).netloc
                            description = ''

                    if len(repo) < 85:
                        if len(description) > (85-len(repo)):
                            m = f'[{repo}]({url}) {description[:85-len(repo)-3]}...'
                        else:
                            m = f'[{repo}]({url}) {description}'
                    else:
                        m = f'[{repo[:83]}...]({url}) '
                    bucket = '<img alt="" src="https://avatars.githubusercontent.com/u/16618068?s=20" width="20" height="20">'
                    msg.append(
                        f'- {bucket + "|" if data.get(url, {}).get("bucket") else ""}<img src="https://favicon.qqsuu.cn/{urlparse(url).netloc}" alt="" style="height: 20px;"> {m}')
            else:
                parse_tree(v, path=path + 1)  # 递归调用处理嵌套的数据结构

    parse_tree(repos, path=1)  # 调用函数开始处理数据
    total_md += "\n".join(msg)  # 将项目信息拼接为Markdown格式字符串
    with open("README.md", "w", encoding="utf8") as fd:
        fd.write(total_md)  # 将Markdown格式字符串写入README.md文件


def update_change():
    '''检查链接新增和删除'''
    data = json.loads(open("data.json", "r", encoding="utf8").read())
    old_urls = list(data.keys())
    repos = yaml2json("repos.yaml")
    new_urls = []

    def parse_tree(dic):
        for k, v in dic.items():
            if isinstance(v, list):
                for url in v:
                    new_urls.append(url)
            else:
                parse_tree(v)
    parse_tree(repos)
    a, _, c = list_cmp(old_urls, new_urls)
    # 删除无效数据
    if len(a) > 0:
        data = {k: v for k, v in data.items() if k not in a}
        print(f'删除: {len(a)}个,{a}')
    # 添加新增数据
    if len(c) > 0:
        not_github_urls = [
            url for url in c if not url.startswith('https://github.com')]
        github_urls = [url for url in c if url.startswith(
            'https://github.com')]
        if not_github_urls:
            for item in get_urls_info(not_github_urls):
                url = item['url']
                data[url] = {'created_at': time.strftime(
                    "%Y-%m-%d %H:%M:%S"), 'updated_at': time.strftime("%Y-%m-%d %H:%M:%S")}
                data[url].update(item)
                del data[url]['url']
        if github_urls:
            api_github_urls = gen_githun_api_url(github_urls)
            for item in get_urls_info(api_github_urls):
                url = item['url']
                if url in data:
                    data[url].update(item)
                    data[url]['updated_at'] = time.strftime(
                        "%Y-%m-%d %H:%M:%S")
                    del data[url]['url']
                else:
                    data[url] = {}
                    data[url].update(item)
                    data[url]['updated_at'] = time.strftime(
                        "%Y-%m-%d %H:%M:%S")
                    del data[url]['url']
        print(f'新增: {len(c)}个,{c}')
    # 写入data
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def clone_repo(url):
    temp_dir = tempfile.TemporaryDirectory().name
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    os.chdir(temp_dir)
    os.system('git clone {}'.format(url))
    return os.path.join(temp_dir, url[19:].split('/', 1)[1])


def update_bucket():
    root_path = os.path.dirname(os.path.abspath(__file__))
    repo_path = clone_repo('https://github.com/20142995/scoop-bucket')
    results = {}
    if os.path.exists(repo_path):
        for root, _, files in os.walk(repo_path):
            for file in files:
                if not file.endswith('.json'):
                    continue
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf8') as f:
                    content = f.read()
                try:
                    rj = json.loads(content)
                    if 'version' in rj and 'description' in rj and 'homepage' in rj:
                        results[rj['homepage']] = rj
                except:
                    continue
    os.chdir(root_path)
    data = json.loads(open("data.json", "r", encoding="utf8").read())
    for url in results:
        if url in data:
            if not data[url].get('bucket'):
                print(f'in bucket: {url}')
                data[url]['bucket'] = True
        else:
            print(f'bucket not in: {url}')
    # 写入data
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'readme':
            update_readme()
        elif sys.argv[1] == 'release':
            update_release()
        elif sys.argv[1] == 'change':
            update_change()
        elif sys.argv[1] == 'bucket':
            update_bucket()
