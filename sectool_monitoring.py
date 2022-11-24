#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import json
import time
import requests
import datetime
requests.packages.urllib3.disable_warnings()

# 项目
repos = '''
信息收集|资产测绘采集|https://github.com/ExpLangcn/InfoSearchAll
信息收集|资产测绘采集|https://github.com/xzajyjs/ThunderSearch

信息收集|子域名收集|https://github.com/projectdiscovery/subfinder

信息收集|目录扫描|https://github.com/maurosoria/dirsearch
信息收集|目录扫描|https://github.com/pingc0y/URLFinder

信息收集|指纹识别|https://github.com/EdgeSecurityTeam/EHole

信息收集|端口扫描|https://github.com/4dogs-cn/TXPortMap

漏洞发现&利用|半自动化漏洞利用|https://github.com/lz520520/railgun
漏洞发现&利用|半自动化漏洞利用|https://github.com/gobysec/Goby

漏洞发现&利用|半自动漏洞扫描|https://github.com/chaitin/xray
漏洞发现&利用|半自动漏洞扫描|https://github.com/d3ckx1/Fvuln
漏洞发现&利用|半自动漏洞扫描|https://github.com/projectdiscovery/nuclei
漏洞发现&利用|半自动漏洞扫描|https://github.com/zan8in/afrog
漏洞发现&利用|半自动漏洞扫描|https://github.com/zhzyker/vulmap

漏洞发现&利用|数据库利用|https://github.com/SafeGroceryStore/MDUT
漏洞发现&利用|数据库利用|https://github.com/Liqunkit/LiqunKit_
漏洞发现&利用|数据库利用|https://github.com/n0b0dyCN/redis-rogue-server

漏洞发现&利用|Shell管理|https://github.com/rebeyond/Behinder
漏洞发现&利用|Shell管理|https://github.com/BeichenDream/Godzilla

漏洞发现&利用|中间件&框架漏洞利用|https://github.com/tpt11fb/AttackTomcat
漏洞发现&利用|中间件&框架漏洞利用|https://github.com/SummerSec/SpringExploit
漏洞发现&利用|中间件&框架漏洞利用|https://github.com/wyzxxz/shiro_rce_tool
漏洞发现&利用|中间件&框架漏洞利用|https://github.com/SummerSec/ShiroAttack2
漏洞发现&利用|中间件&框架漏洞利用|https://github.com/j1anFen/shiro_attack
漏洞发现&利用|中间件&框架漏洞利用|https://github.com/c0ny1/FastjsonExploit
漏洞发现&利用|中间件&框架漏洞利用|https://github.com/wyzxxz/fastjson_rce_tool
漏洞发现&利用|中间件&框架漏洞利用|https://github.com/mrknow001/fastjson_rec_exploit
漏洞发现&利用|中间件&框架漏洞利用|https://github.com/joaomatosf/jexboss
漏洞发现&利用|中间件&框架漏洞扫描|https://github.com/rabbitmask/WeblogicScan
漏洞发现&利用|中间件&框架漏洞扫描|https://github.com/Weik1/Artillery

漏洞发现&利用|重点CMS利用|https://github.com/LittleBear4/OA-EXPTOOL

漏洞发现&利用|漏洞检测利用仓库|https://github.com/ybdt/poc-hub
漏洞发现&利用|漏洞检测利用仓库|https://github.com/Threekiii/Awesome-Exploit

内网渗透|密码提取|https://github.com/Potato-py/getIntrInfo

相关资源|工具集成环境|https://github.com/makoto56/penetration-suite-toolkit

相关资源|知识库|https://github.com/makoto56/penetration-suite-toolkit
相关资源|知识库|https://github.com/Threekiii/Awesome-Redteam

工具&插件|Burpsuite插件|https://github.com/NeoTheCapt/PowerScanner
工具&插件|Burpsuite插件|https://github.com/F6JO/RouteVulScan
工具&插件|Burpsuite插件|https://github.com/metaStor/SpringScan
工具&插件|xray|https://github.com/zema1/yarx
工具&插件|xray|https://github.com/phith0n/xray-poc-generation
工具&插件|pocsuite3|https://github.com/smallfox233/ExpToPocsuite3
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
        type_1, type_2, url = repo.split('|', 2)
        data.setdefault(type_1, {})
        data[type_1].setdefault(type_2, {})
        data[type_1][type_2].setdefault(url, {})

data_change = {}
# 更新数据
headers = {"Authorization": "token {}".format(os.getenv('GH_TOKEN'))}
for type_1 in data:
    for type_2 in data[type_1]:
        for url in data[type_1][type_2]:
            name = url[19:]
            # 项目描述
            try:
                rj1 = requests.get('https://api.github.com/repos/{}'.format(name),
                                   headers=headers, verify=False).json()
                description = rj1['description']
                if description is None:
                    description = ''
                data[type_1][type_2][url]['description'] = description
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
                    data[type_1][type_2][url]['commit_date'] = date
                    data[type_1][type_2][url]['commit_message'] = commit['commit']['message']
                time.sleep(0.1)
            except:
                pass
            # release版本
            try:
                rj3 = requests.get('https://api.github.com/repos/{}/releases/latest'.format(
                    name), headers=headers, verify=False).json()
                date = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(
                    rj3['published_at'], "%Y-%m-%dT%H:%M:%SZ"))
                release_version = rj3['name']
                if data[type_1][type_2][url].get('release_version','') != release_version:
                    headers = {'Content-Type': 'application/json'}
                    data = {"msgtype": "text", "text": {"content": "{}\n\n版本升级:{}-{}".format(url,data[type_1][type_2][url].get('release_version',''),release_version)},
                            "at": {"atMobiles": [], "isAtAll": False}, }
                    url = "https://oapi.dingtalk.com/robot/send?access_token={}".format(os.getenv('DINGTALK_TOKEN'))
                    requests.post(url, json=data, headers=headers)

                data[type_1][type_2][url]['release_version'] = release_version
                data[type_1][type_2][url]['release_date'] = date
                data[type_1][type_2][url]['release_message'] = rj3['body']
                time.sleep(0.1)
            except:
                pass

# 更新README.md
n = 7
md = ''
md += '## 近{}天release更新记录\n'.format(n)
md += '| 类型| 项目名称 | 更新时间 | 版本 | 更新内容 |\n'
md += '| :---- | :---- | :---- | :---- | :---- |\n'
for type_1 in data:
    for type_2 in data[type_1]:
        for url in data[type_1][type_2]:
            author, name = url[19:].split('/', 1)
            date = data[type_1][type_2][url].get('release_date')
            if not date:
                continue
            version = data[type_1][type_2][url].get('release_version')
            message = data[type_1][type_2][url].get('release_message')
            if time.mktime(time.strptime(date, "%Y-%m-%d %H:%M:%S")) > time.mktime((datetime.datetime.now() - datetime.timedelta(days=n)).timetuple()):
                md += '| {} | [{}]({}) | {} | {} | {} |\n'.format(type_2, name,
                                                                  url, date, version, message.replace('\r\n', '<br>').replace('\n', '<br>'))


md += '## 近{}天commit提交记录\n'.format(n)
md += '| 类型| 项目名称 | 提交时间 | 更新内容 |\n'
md += '| :---- | :---- | :---- | :---- |\n'
for type_1 in data:
    for type_2 in data[type_1]:
        for url in data[type_1][type_2]:
            author, name = url[19:].split('/', 1)
            date = data[type_1][type_2][url].get('commit_date')
            if not date:
                continue
            message = data[type_1][type_2][url].get('commit_message')
            if time.mktime(time.strptime(date, "%Y-%m-%d %H:%M:%S")) > time.mktime((datetime.datetime.now() - datetime.timedelta(days=n)).timetuple()):
                md += '| {} | [{}]({}) | {} | {} |\n'.format(type_2,
                                                             name, url, date, message.replace('\r\n', '<br>').replace('\n', '<br>'))

md += '## 所有项目\n'
for type_1 in data:
    md += '### {}\n'.format(type_1)
    for type_2 in data[type_1]:
        md += '#### {}\n'.format(type_2)
        md += '| 项目名称 | 作者 | 最近提交时间 | 版本 | 项目描述 |\n'
        md += '| :---- | :---- | :---- | :---- | :---- |\n'
        for url in data[type_1][type_2]:
            author, name = url[19:].split('/', 1)
            md += '| [{}]({}) | {} | {} | {} | {} |\n'.format(name, url, author, data[type_1][type_2][url].get('commit_date',
                                                                                                                ''), data[type_1][type_2][url].get('release_version', ''), data[type_1][type_2][url].get('description', '').replace('\r\n', '<br>').replace('\n', '<br>'))

with open("README.md", 'w', encoding='utf8') as fd:
    fd.write(md)

# 写入历史
with open(data_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
