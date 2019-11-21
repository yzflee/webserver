#-*- coding: utf-8 -*-
import ssl
import numpy as np
import requests
import datetime
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

def getdaydiffers():
    now = datetime.datetime.now()
    i = 0
    daydiffer = ['','','','','','']
    for Ja in Javalists:
        Ja_url = 'https://api.github.com/repos/%s' % Ja  # 确定url
        JaInfo = readURL('Data/%s' % (Ja), Ja_url)  # 访问url得到数据
        JaInfo = JaInfo and json.loads(JaInfo)  # 将数据类型转换
        daydiffer[i] = int((now.year-int(JaInfo['created_at'][0:4]))*365+(now.month-int(JaInfo['created_at'][5:7]))*30+(now.day-int(JaInfo['created_at'][8:10])))
        i=i+1
        # 提取想要的信息保存
    daydiffer.append(int(np.mean(daydiffer)))  # 加入均值
    daydiffer.append(int(np.var(daydiffer)))  # 加入方差
    daydiffer.append(int(np.percentile(daydiffer, 50)))  # 加入中位数
    daydiffer.append(int(np.percentile(daydiffer, 25)))  # 加入四分位数
    return daydiffer


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