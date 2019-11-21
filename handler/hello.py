#-*- coding: utf-8 -*-
from app import route, response, redirect, config
import os

import logic.Team1902.projectInfo as P
import logic.Team1902.stars as Q
import logic.Team1902.watchers as R
import logic.Team1902.differdate as S

@route('/hello.py.html')
def projectInfo():

	info = [P.getProjectInfo()]
	infoShow  = [
  	{ 'genre': 'apache/logging-log4j2', 'sold': Q.getstars()[0] },
  	{ 'genre': 'ReactiveX/RxJava', 'sold': Q.getstars()[1]  },
  	{ 'genre': 'apache/cassandra', 'sold': Q.getstars()[2]  },
  	{ 'genre': 'apache/camel', 'sold': Q.getstars()[3]  },
  	{ 'genre': 'apache/hive', 'sold': Q.getstars()[4]  },
	{'genre': 'apache/commons-lang', 'sold': Q.getstars()[5] },
	{'genre': 'average', 'sold': Q.getstars()[6] },
	{'genre': 'variance/10000', 'sold': Q.getstars()[7]/10000 },
	{'genre': 'median', 'sold': Q.getstars()[8] },
	{'genre': 'quartile', 'sold': Q.getstars()[9] }
	]

	infoShow1 = [
		{'genre': 'apache/logging-log4j2', 'sold': R.getwatchers()[0]},
		{'genre': 'ReactiveX/RxJava', 'sold': R.getwatchers()[1]},
		{'genre': 'apache/cassandra', 'sold': R.getwatchers()[2]},
		{'genre': 'apache/camel', 'sold': R.getwatchers()[3]},
		{'genre': 'apache/hive', 'sold': R.getwatchers()[4]},
		{'genre': 'apache/commons-lang', 'sold': R.getwatchers()[5]},
		{'genre': 'average', 'sold': R.getwatchers()[6]},
		{'genre': 'variance/10000', 'sold': R.getwatchers()[7]/10000},
		{'genre': 'median', 'sold': R.getwatchers()[8]},
		{'genre': 'quartile', 'sold': R.getwatchers()[9]}
	]

	infoShow2 = [
		{'genre': 'apache/logging-log4j2', 'sold': S.getdaydiffers()[0]},
		{'genre': 'ReactiveX/RxJava', 'sold': S.getdaydiffers()[1]},
		{'genre': 'apache/cassandra', 'sold': S.getdaydiffers()[2]},
		{'genre': 'apache/camel', 'sold': S.getdaydiffers()[3]},
		{'genre': 'apache/hive', 'sold': S.getdaydiffers()[4]},
		{'genre': 'apache/commons-lang', 'sold': S.getdaydiffers()[5]},
		{'genre': 'average', 'sold': S.getdaydiffers()[6]},
		{'genre': 'variance/10000', 'sold': S.getdaydiffers()[7]/10000},
		{'genre': 'median', 'sold': S.getdaydiffers()[8]},
		{'genre': 'quartile', 'sold': S.getdaydiffers()[9]}
	]

	#将info返回给页面
	return response(projectInfo=info,infoShow = infoShow,infoShow1 = infoShow1,infoShow2 = infoShow2)

def gitClone(name):
	projectPath = os.path.abspath('data/gitRepo/%s'%(name))
	not os.path.isdir(projectPath) and os.makedirs(projectPath)
	cmd = 'git clone https://github.com/%s.git %s'% (name,projectPath)
	cwd = os.getcwd()
	os.chdir(projectPath)
	result = os.system(cmd)
	os.system('git shortlog -s -n>%slog.txt' % name)
	os.chdir(cwd)
	if result !=0:
		return False
	return True

gitClone('apache/logging-log4j2')