#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import json
import re
import time
import requests
requests.packages.urllib3.disable_warnings()

DINGTALK_TOKEN = os.getenv('DINGTALK_TOKEN')
GH_TOKEN = os.getenv('GH_TOKEN')


def send_text(text, token):
    headers = {'Content-Type': 'application/json'}
    data = {"msgtype": "text", "text": {"content": text},
            "at": {"atMobiles": [], "isAtAll": False}, }
    url = "https://oapi.dingtalk.com/robot/send?access_token={}".format(token)
    r = requests.post(url, json=data, headers=headers)
    return r.json()


# 项目
repos = '''
半自动化漏洞利用工具|https://github.com/lz520520/railgun
半自动化漏洞利用工具|https://github.com/gobysec/Goby
数据库利用工具|https://github.com/SafeGroceryStore/MDUT
数据库利用工具|https://github.com/Liqunkit/LiqunKit_
数据库利用工具|https://github.com/n0b0dyCN/redis-rogue-server
Shell管理工具|https://github.com/rebeyond/Behinder
Shell管理工具|https://github.com/BeichenDream/Godzilla
'''
data = {}
# 读取历史
data_file = 'data.json'
if os.path.exists(data_file):
    try:
        data = json.loads(open(data_file, 'r', encoding='utf8').read())
    except:
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
else:
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
for repo in repos.split('\n'):
    if '|' in repo:
        _type, url = repo.split('|', 1)
        data.setdefault(_type, {})
        data[_type].setdefault(url, {})

# 更新数据
headers = {"Authorization": "token {}".format(GH_TOKEN)}
for _type in data:
    for url in data[_type]:
        print(url)
        name = url[19:]
        # 项目描述
        try:
            rj1 = requests.get('https://api.github.com/repos/{}'.format(name),
                               headers=headers, verify=False).json()
            description = rj1['description']
            if description is None:
                description = ''
            if data[_type][url].get('description', '') != description:
                data[_type][url]['description_change'] = True
            data[_type][url]['description'] = description
            time.sleep(0.1)
        except:
            pass
        # 最近提交
        try:
            rj2 = requests.get('https://api.github.com/repos/{}/commits'.format(name),
                               headers=headers, verify=False).json()
            for commit in rj2[:1]:
                date = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(
                    commit['commit']['committer']['date'], "%Y-%m-%dT%H:%M:%SZ"))
                if data[_type][url].get('commit_date', '') != date:
                    data[_type][url]['commit_change'] = True
                data[_type][url]['commit_date'] = date
                data[_type][url]['commit_message'] = commit['commit']['message']
            time.sleep(0.1)
        except:
            pass
        # 最近release版本
        try:
            rj3 = requests.get('https://api.github.com/repos/{}/releases/latest'.format(
                name), headers=headers, verify=False).json()
            release_version = rj3['name']
            if data[_type][url].get('release_version', '') != release_version:
                data[_type][url]['release_version_change'] = True
            data[_type][url]['release_version'] = release_version
            time.sleep(0.1)
        except:
            pass
# 提取更新记录
msg = []
for _type in data:
    for url in data[_type]:
        author, name = url[19:].split('/', 1)
        if data[_type][url].get('description_change', False):
            msg.append([name, url, "description", data[_type]
                       [url].get('description', '')])
            data[_type][url]['description_change'] = False
        if data[_type][url].get('commit_change', False):
            msg.append([name, url, "commit", "{}:{}".format(data[_type][url].get(
                'commit_date', ''), data[_type][url].get('commit_message', ''))])
            data[_type][url]['commit_change'] = False
        if data[_type][url].get('release_version_change', False):
            msg.append([name, url, "release", data[_type]
                       [url].get('release_version', '')])
            data[_type][url]['release_version_change'] = False
# 钉钉通知
if msg:
    text = ''
    for _, url, change_type, message in msg:
        text += 'URL:{}\n{}:{}\n'.format(url, change_type, message)
    headers = {'Content-Type': 'application/json'}
    _data = {"msgtype": "text", "text": {"content": text},
             "at": {"atMobiles": [], "isAtAll": False}, }
    url = "https://oapi.dingtalk.com/robot/send?access_token={}".format(
        DINGTALK_TOKEN)
    requests.post(url, json=_data, headers=headers)

# 更新README.md
md = '[TOC]\n'
if msg:
    md += '## 更新记录\n'
    md += '| 项目名称 | 变更类型 | 变更内容 |\n'
    md += '| :----: | :----: | :---- |\n'
    for name, url, change_type, message in msg:
        md += '| [{}]({}) | {} | {} |\n'.format(name, url,
                                                change_type, message.replace('\n', '</br>'))
md += '## 所有项目\n'
for _type in data:
    md += '### {}\n'.format(_type)
    md += '| 项目名称 | 作者 | 最近提交时间 | 版本 | 项目描述 |\n'
    md += '| :----: | :----: | :----: | :---- | :---- |\n'
    for url in data[_type]:
        author, name = url[19:].split('/', 1)
        md += '| [{}]({}) | {} | {} | {} | {} |\n'.format(name, url, author, data[_type][url].get('commit_date',
                                                                                                  ''), data[_type][url].get('release_version', ''), data[_type][url].get('description', ''))

with open("README.md", 'w', encoding='utf8') as fd:
    fd.write(md)

# 写入历史
with open(data_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
