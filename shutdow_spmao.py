# -*- coding:utf-8 -*-
'''
   author :       sharpmao
   version :      1.0
   function　:    shutdown your computer by time
   
'''
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
# 创建window
window=tk.Tk()
window.title('shutdown')
window.geometry('160x300')

# 创建一个标签提示用户选择定时关机时间
label=tk.Label(window,text='请选择定时关机时间')
label.pack()

#创建一个listbox 并为其设置选项值
var_1=tk.StringVar()
var_1.set([5,10,15,20,30,40,60,120,150,180])
listbox=tk.Listbox(window,listvariable=var_1)
listbox.pack()

# 创建一个标签提示用户输入自定义的定时关机时间
label=tk.Label(window,text='请输入自定义关机时间')
label.pack()

#创建一个输入框，便于获取用户输入的定时关机时间
entry=tk.Entry(window,width=100,show=None)
entry.pack()

def shut():
    '''
        实现对输入框用户输入时间和列表选项时间的获取，之后执行关机程序
    '''
    try:
        try:
            time = int(entry.get())                     # 获取输入框中用户输入的自定义关机时间
            if time==None:              #若用户没有自定义时间则获取选项时间
                time=int(listbox.get(listbox.curselection()))           # 若选项时间也没有则捕获其抛出的异常
        except Exception:
           return          #处理列表选项抛出的异常，终止关机按钮的操作
        ntimer = Ntimer(int(time))             #创建计时器对象，并初始化其定时时间
        if ntimer.getTime():
            os.system('shutdown -s -t 0')    #定时器时间达到则执行关机
    except RuntimeError as reason:
        print('运行时出现错误 %s'% reason)      #若无法正常关机则会抛出运行时异常

def shutdown():
    '''
        该方法在关机按钮点击时被调用，功能是创建新的线程处理等待用户输入以及等待关机时刻的到来
    '''
    try:
        t=threading.Thread(target=shut,name='shut')
        t.start()                                  #若无法正常开启新的线程则会抛出运行时异常
    except RuntimeError as reason:
        print('运行时出现错误 %s'% reason)

#创建一个关机按钮，功能是当用户点击是执行定时关机，若用户没有选择关机时间且没有输入自定义的关机时间则直接返回
button_shut=tk.Button(window,width=10,height=2,bg='red',text='定时关机',command=shutdown)
button_shut.pack(side = 'left')

def quit():
    '''
         调用os模块的_exit(0)方法退出该程序进程
    '''
    try:
        os._exit(0)
    except RuntimeError as reason:
        print('无法结束进程 %s'%reason)

#创建一个退出该程序的按钮，该按钮直接杀死该程序进程
button_quit=tk.Button(window,width=10,height=2,bg='blue',text='退出关机',command=quit)
button_quit.pack(side = 'right')

#开启主循环
window.mainloop()
