#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import datetime
import time
import os
import json
import traceback
import time
import re
import requests
import yaml

requests.packages.urllib3.disable_warnings()


class GithubClient:
    def __init__(self, token):
        self.url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Connection": "close",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
        }
        self.limit = 0
        self.users_octocat()

    def connect(self, method, resource, data=None):
        """访问api"""
        time.sleep(0.1)
        if method == "GET":
            r = requests.get(
                "{0}{1}".format(self.url, resource),
                params=data,
                headers=self.headers,
                verify=False,
                allow_redirects=False,
            )
        elif method == "POST":
            r = requests.post(
                "{0}{1}".format(self.url, resource),
                data=data,
                headers=self.headers,
                verify=False,
                allow_redirects=False,
            )
        r.encoding = r.apparent_encoding
        if "X-RateLimit-Remaining" in r.headers.keys():
            self.limit = int(r.headers["X-RateLimit-Remaining"])
        try:
            return r.status_code, r.headers, r.json()
        except:
            return r.status_code, r.headers, r.content

    def search_code(self, keyword, page=1, per_page=10):
        """搜索代码"""
        try:
            time.sleep(2)
            data = {
                "q": keyword,
                "sort": "indexed",
                "order": "desc",
                "page": page,
                "per_page": per_page,
            }
            _, _, rs = self.connect("GET", "/search/code", data=data)
            return rs
        except:
            return {}

    def repos(self, author, repo):
        """项目信息"""
        try:
            _, _, rs = self.connect("GET", f"/repos/{author}/{repo}")
            return rs
        except:
            return {}

    def repos_commits(self, author, repo):
        """项目commit信息"""
        try:
            _, _, rs = self.connect("GET", f"/repos/{author}/{repo}/commits")
            if isinstance(rs, dict):
                if rs.get("message", "") == "Moved Permanently" and "url" in rs:
                    _, _, rs1 = self.connect("GET", rs["url"][18:])
                    if isinstance(rs1, list):
                        return rs1
            elif isinstance(rs, list):
                return rs
        except:
            pass
        return []

    def repos_releases_latest(self, author, repo):
        """项目最新release"""
        try:
            _, _, rs = self.connect("GET", f"/repos/{author}/{repo}/releases/latest")
            return rs
        except:
            return {}

    def users_octocat(self):
        """检查速率限制"""
        try:
            _, _, _ = self.connect("GET", "/users/octocat")
        except:
            pass


def json2yaml(path, data, encoding="utf8"):
    with open(path, "w", encoding=encoding) as f:
        yml = yaml.YAML()
        yml.indent(mapping=4, sequence=4, offset=4)
        yml.dump(data, f)

def yaml2json(path, encoding="utf8"):
    with open(path, 'r', encoding=encoding) as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
    return data


def parse_len(x, y):
    def chr_len2(s):
        return int((len(s.encode("utf-8")) - len(s)) / 2 + len(s))
    x = x if x else ""
    x = x.replace("<br>", "")
    x = re.sub(r"\s+", " ", x)
    x = re.sub(r"\!\[.*?\]\(.*?\)", "", x)
    x = re.sub(r"\[.*?\]\(.*?\)", "", x)
    x = re.sub(r"<[^>]+>", "", x)
    x = x.replace("`", "")[:180]
    s = ""
    n = 0
    for i in x:
        n += chr_len2(i)
        if n >= y:
            s += "<br>"
            n = 0
        s += i
    return s


def main():
    # 读取历史
    data = {}
    data_file = "data.json"
    if os.path.exists(data_file):
        try:
            data = json.loads(open(data_file, "r", encoding="utf8").read())
        except:
            with open(data_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
    else:
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    # 跳过commit_date为空的
    data_b = {url: data[url] for url in data if data[url].get("commit_date", "") != ""}
    # 跳过commit_date距今超过90天的
    data_b = {
        url: data_b[url]
        for url in data_b
        if (
            datetime.datetime.now()
            - datetime.datetime.strptime(
                data_b[url]["commit_date"], "%Y-%m-%d %H:%M:%S"
            )
        ).days
        > 90
    }
    # 读取项目列表
    repos = yaml2json("repos.yaml")
    urls = []

    def parse_dict(dic):
        for k, v in dic.items():
            if isinstance(v, list):
                if k in ['未分类']:
                    continue
                urls.extend(v)
            else:
                parse_dict(v)

    parse_dict(repos)
    urls = set(urls)
    # 更新数据
    count_i = 1
    gc = GithubClient(os.getenv("GH_TOKEN", ""))
    for url in urls:
        if not url.startswith("https://github.com/"):
            continue
        if url in data_b:
            continue
        # print(f"[{count_i}] get {url}")
        try:
            author, repo = url[19:].split("/", 1)
            item = {}
            rs1 = gc.repos(author, repo)
            item["created_at"] = (
                time.strftime(
                    "%Y-%m-%d %H:%M:%S",
                    time.strptime(rs1["created_at"], "%Y-%m-%dT%H:%M:%SZ"),
                )
                if rs1.get("created_at")
                else ""
            )
            item["description"] = (
                rs1.get("description", "") if rs1.get("description", "") else ""
            )
            rs2 = gc.repos_commits(author, repo)
            for rs in rs2[:1]:
                item["commit_date"] = (
                    time.strftime(
                        "%Y-%m-%d %H:%M:%S",
                        time.strptime(
                            rs["commit"]["committer"]["date"], "%Y-%m-%dT%H:%M:%SZ"
                        ),
                    )
                    if rs.get("commit", {}).get("committer", {}).get("date")
                    else ""
                )
                item["commit_message"] = (
                    rs["commit"]["message"]
                    if rs.get("commit", {}).get("message")
                    else ""
                )
            rs3 = gc.repos_releases_latest(author, repo)
            item["release_tag"] = (
                rs3.get("tag_name", "") if rs3.get("tag_name", "") else ""
            )
            item["release_date"] = (
                time.strftime(
                    "%Y-%m-%d %H:%M:%S",
                    time.strptime(rs3["published_at"], "%Y-%m-%dT%H:%M:%SZ"),
                )
                if rs3.get("published_at")
                else ""
            )
            item["release_message"] = rs3.get("body", "") if rs3.get("body", "") else ""
        except:
            print("[fail 1]", url)
            traceback.print_exc()
        data.setdefault(url, {})
        data[url].update(item)
        count_i += 1

    # 更新README.md

    n = 15
    # n天前
    nd = time.mktime((datetime.datetime.now() - datetime.timedelta(days=n)).timetuple())

    release_md = f"""
## 近{n}天release更新记录
| 更新时间 | 项目名称 | 版本 | 更新内容 |
| :---- | :---- | :---- | :---- |
"""
    commit_md = f"""
## 近{n}天commit提交记录
| 提交时间 | 项目名称 | 更新内容 |
| :---- | :---- | :---- |
"""

    commits = []
    releases = []
    for url in data:
        # print(f"[to_md] {url}")
        try:
            _, repo = url[19:].split("/", 1)
            item = data[url]
            author, repo = url[19:].split("/", 1)
            repo = parse_len(repo, 18)
            # created_at = parse_len(item.get('created_at'), 25)
            # description = parse_len(item.get('description'), 65)
            release_tag = parse_len(item.get("release_tag"), 8)
            release_date = parse_len(item.get("release_date"), 23)
            release_message = parse_len(item.get("release_message"), 38)
            commit_date = parse_len(item.get("commit_date"), 23)
            commit_message = parse_len(item.get("commit_message"), 52)
            if release_date:
                if time.mktime(time.strptime(release_date, "%Y-%m-%d %H:%M:%S")) > nd:
                    releases.append(
                        [release_date, repo, url, release_tag, release_message]
                    )
            if commit_date:
                if time.mktime(time.strptime(commit_date, "%Y-%m-%d %H:%M:%S")) > nd:
                    commits.append([commit_date, repo, url, commit_message])
        except:
            print(f"[fail 2] {url}")
            traceback.print_exc()
    releases = sorted(releases, key=lambda x: x[0], reverse=True)
    release_md += "\n".join(
        [
            f"|{release_date}|[{repo}]({url})|{release_tag}|{release_message}|"
            for release_date, repo, url, release_tag, release_message in releases
        ]
    )
    commits = sorted(commits, key=lambda x: x[0], reverse=True)
    commit_md += "\n".join(
        [
            f"|{commit_date}|[{repo}]({url})|{commit_message}|"
            for commit_date, repo, url, commit_message in commits
        ]
    )
    total_md = "## 所有项目\n"
    # 总的
    msg = []

    def parse_tree(dic, path=1):
        for k, v in dic.items():
            msg.append("{} {}".format("#" * path, k))
            if isinstance(v, list):
                msg.append("| 项目名称 | 版本 | 项目描述 | 提交时间 |")
                msg.append("| :---- | :---- | :---- | :---- |")
                for url in v:
                    if url.startswith("https://github.com/"):
                        try:
                            _, repo = url[19:].split("/", 1)
                            msg.append(
                                "| [{}]({}) | {} | {} | {} |".format(
                                    parse_len(repo, 18),
                                    url,
                                    parse_len(
                                        data.get(url, {}).get("release_tag", ""), 8
                                    ),
                                    parse_len(
                                        data.get(url, {}).get("description", ""), 53
                                    ),
                                    parse_len(data.get(url, {}).get("commit_date"), 23),
                                )
                            )
                        except:
                            print("[fail 2]", url)
                            traceback.print_exc()
                    else:
                        urln = url.split('|')
                        if len(urln) == 3:
                            msg.append("|[{}]({}) | | {} |".format(urln[1],urln[0],urln[2]))
                        else:
                            msg.append("| | | {} |".format(url))

            else:
                parse_tree(v, path=path + 1)

    parse_tree(repos, path=1)
    total_md += "\n".join(msg)
    with open("README.md", "w", encoding="utf8") as fd:
        fd.write(
            "# 更新于 {}\n".format(
                datetime.datetime.utcnow()
                .replace(tzinfo=datetime.timezone.utc)
                .astimezone(
                    datetime.timezone(
                        datetime.timedelta(hours=8),
                        name="Asia/Shanghai",
                    )
                )
                .strftime("%Y-%m-%d %H:%M:%S")
            )
            + release_md
            + commit_md
            + total_md
        )
    # 写入data
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
