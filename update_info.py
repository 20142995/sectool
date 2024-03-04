import time
import os
import json
import asyncio
import aiohttp
import datetime
import yaml
import sys
from bs4 import BeautifulSoup


async def get_other_url_status(session, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        async with session.get(url, headers=headers) as r:
            status_code = r.status
            # html = await r.text()
            content = await r.read()
            html = content.decode('utf8',errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string.strip() if soup.title and soup.title.string else ''
            return {'url': url, 'status_code': status_code, 'description': title}
    except aiohttp.ClientError as e:
        return {}


async def get_github_url_status(session, url):
    token = os.getenv("GH_TOKEN", "")
    headers = {
        "Authorization": f"Bearer {token}",
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

            item['url'] = 'https://github.com/' + \
                '/'.join(url[29:].split("/")[:2])

            return item
    except aiohttp.ClientError as e:
        return {}


async def check_url(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            if url.startswith('https://github.com'):
                author, repo = url[19:].split("/", 1)
                for _url in [
                    f'https://api.github.com/repos/{author}/{repo}',
                    f'https://api.github.com/repos/{author}/{repo}/commits',
                        f'https://api.github.com/repos/{author}/{repo}/releases/latest']:
                    task = asyncio.ensure_future(
                        get_github_url_status(session, _url))
                    tasks.append(task)
            else:
                task = asyncio.ensure_future(
                    get_other_url_status(session, url))
                tasks.append(task)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            if 'url' in response:
                url = response['url']
                del response['url']
                current_data.setdefault(url, {})
                current_data[url].update(response)


def yaml2json(path, encoding="utf8"):
    with open(path, 'r', encoding=encoding) as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
    return data


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.argv.append('0-90')
    start, end = map(int, sys.argv[1].split('-'))
    current_time = datetime.datetime.now()
    start, end = current_time - \
        datetime.timedelta(days=start), current_time - \
        datetime.timedelta(days=end)

    def parse_time_str(x): return datetime.datetime.strptime(
        x, "%Y-%m-%d %H:%M:%S")

    # 读取历史结果
    data_file = "data.json"
    data = json.loads(open(data_file, "r", encoding="utf8").read())
    data_github = {url: data[url]
                   for url in data if data[url].get('commit_date')}
    data_github_pass = {url: data_github[url] for url in data_github if start < parse_time_str(data_github[url]["commit_date"]) or parse_time_str(data_github[url]["commit_date"]) < end}

    # 遍历url
    repos = yaml2json("repos.yaml")
    urls = []

    def parse_dict(dic):
        for _, v in dic.items():
            if isinstance(v, list):
                urls.extend(v)
            else:
                parse_dict(v)
    parse_dict(repos)

    urls = set(urls)
    urls = [url for url in urls if url not in data_github_pass]
    current_data = {}
    # 检查url
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check_url(urls))
    for k, v in current_data.items():
        if v:
            data[k] = v
        else:
            print(f'[-] {k}')
    # 写入data
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
