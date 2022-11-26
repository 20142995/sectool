#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import requests

requests.packages.urllib3.disable_warnings()


class GithubClient:

    def __init__(self, token):
        self.url = 'https://api.github.com'
        self.headers = {
            'Authorization': 'Bearer {}'.format(token),
            'Connection': 'close',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
        }
        self.limit = 0
        self.users_octocat()


    def connect(self, method, resource, data=None):
        '''访问api'''
        time.sleep(0.1)
        if method == 'GET':
            r = requests.get('{0}{1}'.format(
                self.url, resource), params=data, headers=self.headers, verify=False, allow_redirects=False)
        elif method == 'POST':
            r = requests.post('{0}{1}'.format(
                self.url, resource), data=data, headers=self.headers, verify=False, allow_redirects=False)
        r.encoding = r.apparent_encoding
        if 'X-RateLimit-Remaining' in r.headers.keys():
            self.limit = int(r.headers['X-RateLimit-Remaining'])
        try:
            return r.status_code, r.headers, r.json()
        except:
            return r.status_code, r.headers, r.content

    def search_code(self, keyword, page=1, per_page=10):
        '''搜索代码'''
        try:
            time.sleep(2)
            data = {'q': keyword, 'sort': 'indexed',
                    'order': 'desc', 'page': page, 'per_page': per_page}
            _, _, rs = self.connect("GET", '/search/code', data=data)
            return rs
        except:
            return {}

    def repos(self, author, repo):
        '''项目信息'''
        try:
            _, _, rs = self.connect("GET", '/repos/{}/{}'.format(author, repo))
            return rs
        except:
            return {}

    def repos_commits(self, author, repo):
        '''项目commit信息'''
        try:
            _, _, rs = self.connect(
                "GET", '/repos/{}/{}/commits'.format(author, repo))
            return rs
        except:
            return {}

    def repos_releases_latest(self, author, repo):
        '''项目最新release'''
        try:
            _, _, rs = self.connect(
                "GET", '/repos/{}/{}/releases/latest'.format(author, repo))
            return rs
        except:
            return {}

    def users_octocat(self):
        '''检查速率限制'''
        try:
            _, _, _ = self.connect(
                "GET", '/users/octocat')
        except:
            pass