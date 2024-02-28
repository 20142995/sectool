import yaml
import json
from urllib.parse import urlparse

def yaml2json(path, encoding="utf8"):
    with open(path, 'r', encoding=encoding) as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
    return data

def main():
    data = json.loads(open("data.json", "r", encoding="utf8").read())
    repos = yaml2json("repos.yaml")
    total_md = "## 所有项目\n"
    # 总的
    msg = []
    # 
    def parse_tree(dic, path=1):
        for k, v in dic.items():
            msg.append("{} {}".format("#" * path, k))
            if isinstance(v, list):
                v = sorted(v,key=lambda x:data.get(x, {}).get("commit_date",''),reverse=True)
                for url in v:
                    if url.startswith("https://github.com/"):
                        repo = url[19:].split("/", 1)[1]
                        if data.get(url, {}).get("release_tag", ""):
                            repo += ' ' + data[url]['release_tag']
                        description = data.get(url, {}).get("description", "")
                        if len(repo) < 85:
                            if len(description) > (85-len(repo)):
                                m = f'[{repo}]({url}) {description[:85-len(repo)-3]}...'
                            else:
                                m = f'[{repo}]({url}) {description}'
                        else:
                            m = f'[{repo[:83]}...]({url}) '
                        # msg.append(f'- <img src="https://favicon.qqsuu.cn/{url}">{m}')
                        msg.append(f'![Logo](https://favicon.qqsuu.cn/{url}) {m}')
            else:
                parse_tree(v, path=path + 1)

    parse_tree(repos, path=1)
    total_md += "\n".join(msg)
    with open("README.md", "w", encoding="utf8") as fd:
        fd.write(total_md)
if __name__ == '__main__':
    main()