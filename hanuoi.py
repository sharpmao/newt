# -*- coding:utf-8 -*-

def hanuoi(n,x,y,z):
    if n==1:
        print x,'--->',z
    else:
        # 将n-1个盘子从x移动到y上
        hanuoi(n-1,x,z,y)
        print x,'--->',z
        #将n-1个盘子从y上移动到z
        hanuoi(n-1,y,x,z)

hanuoi(4,'X','Y','Z')




