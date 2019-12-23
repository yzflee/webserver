#-*- coding: utf-8 -*-

import pstats
import pprint

profile = ['F:\webserver/data/profile/TriFusion_0b9a801551_',
           'F:\webserver/data/profile/TriFusion_0c6bf1ac1e_',
           'F:\webserver/data/profile/TriFusion_0f6400cc09_',
           'F:\webserver/data/profile/TriFusion_00e5c44d5a_',
           'F:\webserver/data/profile/TriFusion_1b5e66ad58_']

def getprofile():
    p = pstats.Stats('F:\webserver/data/profile/TriFusion_0c6bf1ac1e_0.prof')  #读入数据
    p1 = pstats.Stats('F:\webserver/data/profile/TriFusion_0c6bf1ac1e_1.prof')
    p2 = pstats.Stats('F:\webserver/data/profile/TriFusion_0c6bf1ac1e_2.prof')
    p3 = pstats.Stats('F:\webserver/data/profile/TriFusion_0c6bf1ac1e_3.prof')
    p4 = pstats.Stats('F:\webserver/data/profile/TriFusion_0c6bf1ac1e_4.prof')
    #p.strip_dirs()
    #p.strip_dirs().sort_stats('time')
    stats = p.stats     #获取性能数据的对象 其中stats是个字典类型
    stats1 = p1.stats
    stats2 = p2.stats
    stats3 = p3.stats
    stats4 = p4.stats
    #p.print_stats()
    #pprint.pprint(stats)   #格式化输出

    King = []

    functions = []
    Times = []              #2)
    Times1 = []
    Times2 = []
    Times3 = []
    Times4 = []
    Times5 = []
    Diaoci = []             #3)
    Diaoci1 = []
    Diaoci2 = []
    Diaoci3 = []
    Diaoci4 = []
    Diaoci5 = []
    Timeszhanbi = []          #4)
    TopTimes_func = []          #5)
    TopTimes = []
    TopDiaoci_func = []         #6)
    TopDiaoci = []

    alltime = 0
    #print(len(stats))       #1）函数个数
    for i, j in stats.items():
        #print(i,j)
        functions.append(i[2])
        Times1.append(j[3])
        Diaoci1.append(j[0])
    for i, j in stats1.items():
        #print(i,j)
        Times2.append(j[3])
        Diaoci2.append(j[0])
    for i, j in stats2.items():
        #print(i,j)
        Times3.append(j[3])
        Diaoci3.append(j[0])
    for i, j in stats3.items():
        #print(i,j)
        Times4.append(j[3])
        Diaoci4.append(j[0])
    for i, j in stats4.items():
        #print(i,j)
        Times5.append(j[3])
        Diaoci5.append(j[0])
    for i in range(20):
        Times.append((Times1[i]+Times2[i]+Times3[i]+Times4[i]+Times5[i])/5)
        Diaoci.append((Diaoci1[i]+Diaoci2[i]+Diaoci3[i]+Diaoci4[i]+Diaoci5[i])/5)

    for m in Times:
        alltime = m + alltime
    for n in Times:
        Timeszhanbi.append(n/alltime)

    functions1 = functions.copy()
    functions2 = functions.copy()
    Timeszhanbi1 =Timeszhanbi.copy()
    Diaoci11 = Diaoci.copy()
    for i in range(20):
        TopTimes.append(max(Timeszhanbi1))
        TopTimes_func.append(functions1[Timeszhanbi1.index(max(Timeszhanbi1))])
        del functions1[Timeszhanbi1.index(max(Timeszhanbi1))]
        del Timeszhanbi1[Timeszhanbi1.index(max(Timeszhanbi1))]
        TopDiaoci.append(max(Diaoci11))
        TopDiaoci_func.append(functions2[Diaoci11.index(max(Diaoci11))])
        del functions2[Diaoci11.index(max(Diaoci11))]
        del Diaoci1[Diaoci11.index(max(Diaoci11))]
    King.append(len(stats))
    King.append(Times)
    King.append(Diaoci)
    King.append(Timeszhanbi)
    King.append(TopTimes)
    King.append(TopDiaoci)
    King.append(functions)
    return King
getprofile()

