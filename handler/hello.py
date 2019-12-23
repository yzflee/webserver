#-*- coding: utf-8 -*-
from app import route, response, redirect, config
<<<<<<< HEAD
# import os
# import numpy as np
# #import logic.Team1902.projectInfo as P
# import logic.Team1902.stars as Q
# import logic.Team1902.watchers as R
# import logic.Team1902.differdate as S
import logic.Team1902.Test as T


# repos = [
#
#     "apache/logging-log4j2",
# 	"ReactiveX/RxJava",
#     "apache/cassandra",
#     "apache/camel",
#     "apache/hive",
#     "apache/commons-lang"
#     ]
#
#
# for name in repos:
# #def gitClone(name):
# 	projectPath = os.path.abspath('F:/webserver/data/gitRepo/%s' % (name))
# 	not os.path.isdir(projectPath) and os.makedirs(projectPath)
# 	#cmd = 'git clone https://github.com/%s.git %s' % (name, projectPath)
# 	cwd = os.getcwd()
# 	os.chdir(projectPath)
# 	#result = os.system(cmd)
# 	os.system('git shortlog -s -n>log.txt')
# 	os.chdir(cwd)
# 	#if result != 0:
# 		#return False
# 	#return True
#
# #for name in repos:
# 	#gitClone(name)

=======

import logic.Team1902.projectInfo as p

@route('/hello.py.html')
def projectInfo():
	info = p.getProjectInfo()
	#将info返回给页面
	return response(projectInfo=info)
import ssl
import requests
import os
import json
>>>>>>> b8e10d4c97fbd59d633fdb323d73bd7fe222955d


@route('/hello.py.html')
def projectInfo():
<<<<<<< HEAD
=======
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
>>>>>>> b8e10d4c97fbd59d633fdb323d73bd7fe222955d

	# #info = P.getProjectInfo() <?pythonfor repoName,info in projectInfo.items():?>
	# infoShow  = [
  	# 	{'genre': 'apache/logging-log4j2', 'sold': Q.getstars()[0] },
  	# 	{'genre': 'ReactiveX/RxJava', 'sold': Q.getstars()[1]  },
  	# 	{'genre': 'apache/cassandra', 'sold': Q.getstars()[2]  },
  	# 	{'genre': 'apache/camel', 'sold': Q.getstars()[3]  },
  	# 	{'genre': 'apache/hive', 'sold': Q.getstars()[4]  },
	# 	{'genre': 'apache/commons-lang', 'sold': Q.getstars()[5] },
	# 	{'genre': 'average', 'sold': Q.getstars()[6] },
	# 	{'genre': 'variance/10000', 'sold': Q.getstars()[7]/10000 },
	# 	{'genre': 'median', 'sold': Q.getstars()[8] },
	# 	{'genre': 'quartile', 'sold': Q.getstars()[9] }
	# ]
	#
	# infoShow1 = [
	# 	{'genre': 'apache/logging-log4j2', 'sold': R.getwatchers()[0]},
	# 	{'genre': 'ReactiveX/RxJava', 'sold': R.getwatchers()[1]},
	# 	{'genre': 'apache/cassandra', 'sold': R.getwatchers()[2]},
	# 	{'genre': 'apache/camel', 'sold': R.getwatchers()[3]},
	# 	{'genre': 'apache/hive', 'sold': R.getwatchers()[4]},
	# 	{'genre': 'apache/commons-lang', 'sold': R.getwatchers()[5]},
	# 	{'genre': 'average', 'sold': R.getwatchers()[6]},
	# 	{'genre': 'variance/1000', 'sold': R.getwatchers()[7]/1000},
	# 	{'genre': 'median', 'sold': R.getwatchers()[8]},
	# 	{'genre': 'quartile', 'sold': R.getwatchers()[9]}
	# ]
	#
	# infoShow2 = [
	# 	{'genre': 'apache/logging-log4j2', 'sold': S.getdaydiffers()[0]},
	# 	{'genre': 'ReactiveX/RxJava', 'sold': S.getdaydiffers()[1]},
	# 	{'genre': 'apache/cassandra', 'sold': S.getdaydiffers()[2]},
	# 	{'genre': 'apache/camel', 'sold': S.getdaydiffers()[3]},
	# 	{'genre': 'apache/hive', 'sold': S.getdaydiffers()[4]},
	# 	{'genre': 'apache/commons-lang', 'sold': S.getdaydiffers()[5]},
	# 	{'genre': 'average', 'sold': S.getdaydiffers()[6]},
	# 	{'genre': 'variance/100', 'sold': S.getdaydiffers()[7]/100},
	# 	{'genre': 'median', 'sold': S.getdaydiffers()[8]},
	# 	{'genre': 'quartile', 'sold': S.getdaydiffers()[9]}
	# ]
	#
	# contributors = [69,239,279,544,194,127]
	# infoShow3 = [
	# 	{'genre': 'apache/logging-log4j2', 'sold': 69},
	# 	{'genre': 'ReactiveX/RxJava', 'sold': 239},
	# 	{'genre': 'apache/cassandra', 'sold': 279},
	# 	{'genre': 'apache/camel', 'sold': 544},
	# 	{'genre': 'apache/hive', 'sold': 194},
	# 	{'genre': 'apache/commons-lang', 'sold':127},
	# 	{'genre': 'average', 'sold': int(np.mean(contributors))},
	# 	{'genre': 'variance/100', 'sold': int(np.var(contributors))/ 100},
	# 	{'genre': 'median', 'sold': int(np.percentile(contributors, 50)) },
	# 	{'genre': 'quartile', 'sold': int(np.percentile(contributors, 25))}
	# ]
	#
	# releases = [224,67,243,150,54,87]
	# infoShow4 = [
	# 	{'genre': 'apache/logging-log4j2', 'sold': 224},
	# 	{'genre': 'ReactiveX/RxJava', 'sold': 67},
	# 	{'genre': 'apache/cassandra', 'sold': 243},
	# 	{'genre': 'apache/camel', 'sold': 150},
	# 	{'genre': 'apache/hive', 'sold': 54},
	# 	{'genre': 'apache/commons-lang', 'sold': 87},
	# 	{'genre': 'average', 'sold': int(np.mean(releases))},
	# 	{'genre': 'variance/100', 'sold': int(np.var(releases)) / 100},
	# 	{'genre': 'median', 'sold': int(np.percentile(releases, 50))},
	# 	{'genre': 'quartile', 'sold': int(np.percentile(releases, 25))}
	# ]
	#
	# commits = [5600,10757,24819,40590,13882,5592]
	# infoShow5 = [
	# 	{'genre': 'apache/logging-log4j2', 'sold': 5600},
	# 	{'genre': 'ReactiveX/RxJava', 'sold': 10757},
	# 	{'genre': 'apache/cassandra', 'sold': 24819},
	# 	{'genre': 'apache/camel', 'sold': 40590},
	# 	{'genre': 'apache/hive', 'sold': 13882},
	# 	{'genre': 'apache/commons-lang', 'sold': 5592},
	# 	{'genre': 'average', 'sold': int(np.mean(commits))},
	# 	{'genre': 'variance/10000', 'sold': int(np.var(commits)) / 10000},
	# 	{'genre': 'median', 'sold': int(np.percentile(commits, 50))},
	# 	{'genre': 'quartile', 'sold': int(np.percentile(commits, 25))}
	# ]

<<<<<<< HEAD
	info = T.getprofile()
	info1=[]
	info2=[]
	info3=[]
	info4=[]
	info5=[]
	for i in range(20):						#运行时间
		info1 = info1+[
			{'genre':info[6][i],'sold':info[1][i]}
		]
	for i in range(20):						#调用次数
		info2 = info2+[
			{'genre':info[6][i],'sold':info[2][i]}
		]
	for i in range(20):						#运行时间占比
		info3 = info3+[
			{'genre':info[6][i],'sold':info[3][i]}
		]
	for i in range(20):						#时间占比Top
		info4 = info4+[
			{'genre':info[6][i],'sold':info[4][i]}
		]
	for i in range(20):						#调用次数Top
		info5 = info5+[
			{'genre':info[6][i],'sold':info[5][i]}
		]
	#将info返回给页面
	return response(infoShow = infoShow,infoShow1 = infoShow1,
					infoShow2 = infoShow2,infoShow3 = infoShow3,
					infoShow4 = infoShow4,infoShow5 = infoShow5,
					info1 = info1,info2=info2,info3=info3,
					info4=info4,info5=info5,info6=info[0])
=======

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
>>>>>>> b8e10d4c97fbd59d633fdb323d73bd7fe222955d
