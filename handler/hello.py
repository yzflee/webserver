#-*- coding: utf-8 -*-
from app import route, response, redirect, config

import logic.Team1902.projectInfo as P
import logic.Team1902.branches as Q
@route('/hello.py.html')
def projectInfo(cookies):

	info = {
		P.getProjectInfo(),
		Q.getbranches()
	}
	#将info返回给页面
	return response(projectInfo=info)

