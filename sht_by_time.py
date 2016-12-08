# -*- coding:utf-8 -*-

import tkinter as tk
import datetime
import os
import threading

class Ntimer():
    def __init__(self,time):
        self.start=datetime.datetime.now()  #获取开始时间
        self.end=self.start+datetime.timedelta(minutes=time)  #获取结束时间

    def getTime(self):
        while True:
            self.now=datetime.datetime.now()  #获取当前时间
            if self.end < self.now:        #如果当前时间大于结束时间则退出循环
                break
        return True

window=tk.Tk()
window.title('shutdown')
window.geometry('160x110')

entry=tk.Entry(window,width=100,show=None)
entry.pack()

def shut():
    try:
        time = int(entry.get())
        ntimer = Ntimer(int(time))
        if ntimer.getTime():
            os.system('shutdown -s -t 0')
    except RuntimeError as reason:
        print('运行时出现错误 %s'% reason)

def shutdown():
    try:
        t=threading.Thread(target=shut,name='shut')
        t.start()
    except RuntimeError as reason:
        print('运行时出现错误 %s'% reason)

button_shut=tk.Button(window,width=10,height=2,bg='red',text='定时关机',command=shutdown)
button_shut.pack(side = 'left')

def quit():
    try:
        os._exit(0)
    except RuntimeError as reason:
        print('无法结束进程 %s'%reason)

button_quit=tk.Button(window,width=10,height=2,bg='blue',text='退出关机',command=quit)
button_quit.pack(side = 'right')

window.mainloop()