#-*- coding: utf-8 -*-
import ssl
import numpy as np
import requests
import os
import json
Javalists = [
    "apache/logging-log4j2",
    'ReactiveX/RxJava',
    "apache/cassandra",
    "apache/camel",
    "apache/hive",
    "apache/commons-lang"
    ]

def getstars():
    i = 0
    stars = ['','','','','','']
    for Ja in Javalists:
        Ja_url = 'https://api.github.com/repos/%s' % Ja  # 确定url
        JaInfo = readURL('Data/%s' % (Ja), Ja_url)  # 访问url得到数据
        JaInfo = JaInfo and json.loads(JaInfo)  # 将数据类型转换
        stars[i] = int(JaInfo['watchers_count'])
        i=i+1
        # 提取想要的信息保存
    stars.append(int(np.mean(stars)))  # 加入均值
    stars.append(int(np.var(stars)))  # 加入方差
    stars.append(int(np.percentile(stars, 50)))  # 加入中位数
    stars.append(int(np.percentile(stars, 25)))  # 加入四分位数
    return stars


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

