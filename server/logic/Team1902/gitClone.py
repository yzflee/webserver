def gitClone(clone1):
	projectPath = os.path.abspath('data/gitRepo/%s' % (clone1))
	not os.path.isdir(projectPath) and os.makedirs(projectPath)
	cmd='git clone http://github.com/%s.git %s' % (clone1,projectPath)
	cwd=os.getcwd()#记录当前目录
	os.chdir(projectPath)#跳转到需要保存代码库的路径
	result = os.system(cmd)#执行shell命令
	os.chdir(cwd)#跳转回当前目录
	if result!=0:
		return False
	return True