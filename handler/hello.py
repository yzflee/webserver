#-*- coding: utf-8 -*-
from app import route, response, redirect, config

import logic.Team1902.projectInfo as P
import logic.Team1902.branches as Q
import logic.Team1902.commits as C
@route('/hello.py.html')
def projectInfo(cookie):

	info = [P.getProjectInfo(),Q.getbranches(),C.getcommits()]
	infoShow  = [
  	{ 'genre': 'Sports', 'sold': 275 },
  	{ 'genre': 'Strategy', 'sold': 115 },
  	{ 'genre': 'Action', 'sold': 120 },
  	{ 'genre': 'Shooter', 'sold': 350 },
  	{ 'genre': 'Other', 'sold': 150 }
	]


	#将info返回给页面
	return response(projectInfo=info,infoShow = infoShow)