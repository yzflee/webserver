#-*- coding: utf-8 -*-
import ssl
import requests
import os
import json
repos = ['branches']

def getbranches():
    info={}
    for repo in repos:
        repo_url = 'https://api.github.com/repos/cxsjclassroom/webserver/%s' % repo  # 确定url
        repoInfo = readURL('Repositories/reposInfo/%s' % (repo), repo_url)  # 访问url得到数据
        repoInfo = repoInfo and json.loads(repoInfo)  # 将数据类型转换
        # 提取想要的信息保存在info中

        info[repo]={
            "name": repoInfo[0]['name'],
            "name1": repoInfo[1]['name'],
            "name2": repoInfo[2]['name'],
            "name3": repoInfo[3]['name'],
            "name4": repoInfo[4]['name']
        }
    return info
#读取url的信息，并建立缓存
def readURL(cache,url):
    #看看该url是否访问过
    cache = 'data/cache/%s' % cache
    if os.path.isfile(cache):
        with open(cache, 'r') as f:
            content = f.read()
        return content

    content = requests.get(url).content.decode()

    #吧文件内容保存下来，以免多次重复访问url，类似于缓存
    folder = cache.rpartition('/')[0]
    not os.path.isdir(folder) and os.makedirs(folder)
    with open(cache, 'w') as f:
        f.write(content)
    return content