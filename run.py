#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import datetime
import time
import os
import json
import sys
import traceback
sys.dont_write_bytecode = True
from github_help import GithubClient

# 保存数据
data = {}
data_file = 'data.json'

# 项目清单
with open('repos.md','r',encoding='utf8') as fr:
    repos = fr.readlines()
    for repo in repos[2:]:
        if '|' in repo:
            try:
                type_1, type_2, url = repo.split('|')[1:4]
            except:
                print('[repo error]', repo)
                continue
            if len(url[19:].split('/', 1)) != 2:
                print('[url error]', url)
                continue
            data.setdefault(type_1, {})
            data[type_1].setdefault(type_2, {})
            data[type_1][type_2].setdefault(url, {})

# 更新数据
gc = GithubClient(os.getenv('GH_TOKEN'))
for type_1 in data:
    for type_2 in data[type_1]:
        for url in data[type_1][type_2]:
            if gc.limit > 0:
                print('[{}] {}'.format(gc.limit, url))
            else:
                continue
            author, repo = url[19:].split('/', 1)
            item = data[type_1][type_2][url]
            try:
                rs1 = gc.repos(author, repo)
                item['created_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(
                    rs1['created_at'], "%Y-%m-%dT%H:%M:%SZ")) if rs1.get('created_at') else ''
                item['description'] = rs1.get('description')
                rs2 = gc.repos_commits(author, repo)
                for rs in rs2[:1]:
                    item['commit_date'] = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(
                        rs['commit']['committer']['date'], "%Y-%m-%dT%H:%M:%SZ")) if rs['commit']['committer']['date'] else ''
                    item['commit_message'] = rs['commit']['message'] if rs['commit']['message'] else ''
                rs3 = gc.repos_releases_latest(author, repo)
                item['release_tag'] = rs3.get('tag_name')
                item['release_date'] = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(
                    rs3['published_at'], "%Y-%m-%dT%H:%M:%SZ")) if rs3.get('published_at') else ''
                item['release_message'] = rs3.get('body')
            except:
                print('[fail 1]', url)
                traceback.print_exc()

# 更新README.md
n = 7

release_md = '''
## 近{}天release更新记录
| 类型| 项目名称 | 更新时间 | 版本 | 更新内容 |
| :---- | :---- | :---- | :---- | :---- |
'''.format(n)

commit_md = '''
## 近{}天commit提交记录
| 类型| 项目名称 | 提交时间 | 更新内容 |
| :---- | :---- | :---- | :---- |
'''.format(n)

total_md = '## 所有项目\n'

for type_1 in data:
    total_md += '### {}\n'.format(type_1)
    for type_2 in data[type_1]:
        total_md += '#### {}\n'.format(type_2)
        total_md += '| 项目名称| 最近提交时间 | 版本 | 项目描述 |\n'
        total_md += '| :---- | :---- | :---- | :---- |\n'
        for url in data[type_1][type_2]:
            print('to_md', url)
            try:
                item = data[type_1][type_2][url]
                author, repo = url[19:].split('/', 1)
                created_at = item.get('created_at', '')
                description = item.get('description', '')
                release_tag = item.get('release_tag', '')
                release_date = item.get('release_date', '')
                release_message = item.get('release_message', '')
                commit_date = item.get('commit_date', '')
                commit_message = item.get('commit_message', '')
                if release_date:
                    if time.mktime(time.strptime(release_date, "%Y-%m-%d %H:%M:%S")) > time.mktime((datetime.datetime.now() - datetime.timedelta(days=n)).timetuple()):
                        release_md += '| {} | [{}]({}) | {} | {} | {} |\n'.format(
                            type_2, repo, url, release_date, release_tag, release_message.replace('\r\n', '<br>').replace('\n', '<br>'))
                if commit_date:
                    if time.mktime(time.strptime(commit_date, "%Y-%m-%d %H:%M:%S")) > time.mktime((datetime.datetime.now() - datetime.timedelta(days=n)).timetuple()):
                        commit_md += '| {} | [{}]({}) | {} | {} |\n'.format(
                            type_2, repo, url, commit_date, commit_message.replace('\r\n', '<br>').replace('\n', '<br>'))
                total_md += '| [{}]({}) | {} | {} | {} |\n'.format(repo, url,commit_date, release_tag, description.replace('\r\n', '<br>').replace('\n', '<br>'))
            except:
                print('[fail 2]', url)
                traceback.print_exc()

with open("README.md", 'w', encoding='utf8') as fd:
    fd.write(release_md + commit_md + total_md)

# 写入data历史
with open(data_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
