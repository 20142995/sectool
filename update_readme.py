import yaml
import json
from urllib.parse import urlparse


def yaml2json(path, encoding="utf8"):
    # 将yaml文件转换为json格式
    with open(path, 'r', encoding=encoding) as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
    return data


def main():
    # 加载json文件中的数据
    data = json.loads(open("data.json", "r", encoding="utf8").read())
    # 加载repos.yaml文件中的数据
    repos = yaml2json("repos.yaml")
    total_md = "## 所有项目\n"
    msg = []  # 存储项目信息的列表

    def parse_tree(dic, path=1):
        # 递归遍历数据结构
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
                        description = data.get(url, {}).get("description", "")
                    else:
                        repo = data.get(url, {}).get(
                            "title", urlparse(url).netloc)
                        description = data.get(url, {}).get("description", "")
                    if len(repo) < 85:
                        if len(description) > (85-len(repo)):
                            m = f'[{repo}]({url}) {description[:85-len(repo)-3]}...'
                        else:
                            m = f'[{repo}]({url}) {description}'
                    else:
                        m = f'[{repo[:83]}...]({url}) '
                    msg.append(
                        f'- <img src="https://favicon.qqsuu.cn/{urlparse(url).netloc}" alt="" style="height: 20px;"> {m}')
            else:
                parse_tree(v, path=path + 1)  # 递归调用处理嵌套的数据结构

    parse_tree(repos, path=1)  # 调用函数开始处理数据
    total_md += "\n".join(msg)  # 将项目信息拼接为Markdown格式字符串
    with open("README.md", "w", encoding="utf8") as fd:
        fd.write(total_md)  # 将Markdown格式字符串写入README.md文件


if __name__ == '__main__':
    main()
