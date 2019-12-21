#-*- coding: utf-8 -*-

repos = [

    "apache/logging-log4j2",
	"ReactiveX/RxJava",
    "apache/cassandra",
    "apache/camel",
    "apache/hive",
    "apache/commons-lang"
    ]

def getProjectInfo():

	info = {}
	for repo in repos:
		fp = open('F:/webserver/data/gitRepo/%s/log.txt'% (repo),encoding='utf-8')
		repoInfo = fp.read()
		fp.close()
		# 提取想要的信息保存在info中
		info[repo] = {
			'repoInfo':repoInfo
		}
	return info
getProjectInfo()

