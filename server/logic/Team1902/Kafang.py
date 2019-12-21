import pandas as pd
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

#读取url的信息，并建立缓存
def readURL(cache,url):

    #看看该url是否访问过
    cache = 'data/cache/%s' % cache
    #print(os.getcwd(),cache)
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

author = []
period = []
allJMH = []
sha = []
file_name = []
changedNum = []

JMH_url = 'https://api.github.com/search/code?q=org.openjdk.jmh+in:file+language:java+repo:apache/logging-log4j2&page=1'  # 确定url
JMH = readURL('jmh/apache/logging-log4j2', JMH_url)  # 访问url得到数据
JMH = JMH and json.loads(JMH)  # 将数据类型转换
for i in range(len(JMH['items'])):
    allJMH.append(JMH['items'][i]['path'])

for i in range(20):
    Ja_url = 'https://api.github.com/repos/apache/logging-log4j2/commits'  # 确定url
    Info = readURL('jianyan/apache/logging-log4j2', Ja_url)  # 访问url得到数据
    Info = Info and json.loads(Info)  # 将数据类型转换
    author.append(Info[i]['commit']['author']['name'])
    period.append(Info[i]['commit']['author']['date'])
    sha.append(Info[i]['sha'])

for sh in sha:
    Sh_url = ('https://api.github.com/repos/apache/logging-log4j2/commits/%s'%sh)
    # 确定url
    shInfo = readURL('jianyan/apacheS/logging-log4j2', Sh_url)  # 访问url得到数据
    shInfo = shInfo and json.loads(shInfo)  # 将数据类型转换
    for shaa in shInfo['files']:
        file_name.append(shaa['filename'])
    changedNum.append(len(set(file_name)-set(allJMH)))

data=[{"author":author[0],"period":period[0],"changenum":changedNum[0]},
      {"author":author[1],"period":period[1],"changenum":changedNum[1]},
      {"author":author[2],"period":period[2],"changenum":changedNum[2]},
      {"author":author[3],"period":period[3],"changenum":changedNum[3]},
      {"author":author[4],"period":period[4],"changenum":changedNum[4]},
      {"author":author[5],"period":period[5],"changenum":changedNum[5]},
      {"author":author[6],"period":period[6],"changenum":changedNum[6]},
      {"author":author[7],"period":period[7],"changenum":changedNum[7]}]
df=pd.DataFrame(data,columns=['author','period','changenum'])    #index=
print(df)



