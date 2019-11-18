#-*- coding: utf-8 -*-
from app import route, response, redirect, config
<<<<<<< HEAD

import logic.Team1902.projectInfo as p

<<<<<<< HEAD
@route('/hello.py.html')
def projectInfo(cookies):
	info = p.getProjectInfo()
	#将info返回给页面
	return response(projectInfo=info)
=======
import ssl
import requests
import os
import json

repos = ['cxsjclassroom/webserver',"octocat/Hello-World"]

@route('/hello.py.html')
def projectInfo(cookies):
	info = {}
	for repo in repos:
		repo_url = 'https://api.github.com/repos/%s'%repo #确定url
		repoInfo = readURL('Repositories/reposInfo/%s'%(repo),repo_url )#访问url得到数据
		repoInfo = repoInfo and json.loads(repoInfo)#将数据类型转换
		#提取想要的信息保存在info中
		info[repo] = {
			"stargazers_count":repoInfo['stargazers_count'],
			'watchers_count':repoInfo['watchers_count'],
			'created_at':repoInfo['created_at'],
			'size':repoInfo['size'],
			'forks_count':repoInfo['forks_count'],
			'open_issues':repoInfo['open_issues']

		}
	#将info返回给页面
	return response(projectInfo=info)

=======
import logic.Team1902.projectInfo as P
import logic.Team1902.branches as Q
import logic.Team1902.commits as C
@route('/hello.py.html')
def projectInfo(cookies):
>>>>>>> e7c35f6862d52b16758a3bcac043f59b74a3cda0

	info = [P.getProjectInfo(),Q.getbranches(),C.getcommits()]

<<<<<<< HEAD
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
>>>>>>> 0e7796a61d4391ba51e3a9e21d3cdcd64a0ba8a4
=======
	#将info返回给页面
	return response(projectInfo=info)
>>>>>>> e7c35f6862d52b16758a3bcac043f59b74a3cda0
