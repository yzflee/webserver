#-*- coding: utf-8 -*-

import pstats
import pprint


def getTimes():
    p = pstats.Stats('F:\webserver/data/profile/TriFusion_00e5c44d5a_0.prof')  #读入数据
    p.strip_dirs()
    stats = p.stats     #获取性能数据的对象 其中stats是个字典类型
    #pprint.pprint(stats)
    Times = []
    print(len(stats))       #1）函数个数
    for i, j in stats.items():
        #print(i,j)
        aj = {'genre':i[0],'sold': j[3]}
        Times.append(aj)
    return Times
