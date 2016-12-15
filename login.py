# -*-coding:utf-8 -*-

import tkinter as tk
import pickle

#创建一个window窗口，并设置其属性
window=tk.Tk()
window.title('蜥蜴登录界面')
window.geometry('260x350')

#添加一块画布
canvas=tk.Canvas(window,height=160,width=300)
image_file=tk.PhotoImage(file='newt.gif') #设置图片的文件
canvas.create_image(0,0,anchor='nw',image=image_file) #利用画布创建图片，设置图片的位置
canvas.pack(side='top')

#设置一个str变量存储用户名输入的值，并为其赋值，使得用户名输入框有默认提示
var_usr_name=tk.StringVar()
var_usr_name.set('empty@newt.com.cn')

#创建一个str变量存储密码输入框的值
var_usr_pwd=tk.StringVar()

#创建用户名输入框和密码输入框
entry_usr_name=tk.Entry(window,width=20,textvariable=var_usr_name)
entry_usr_psw=tk.Entry(window,width=20,textvariable=var_usr_pwd,show='*')
entry_usr_name.place(x=95,y=200)
entry_usr_psw.place(x=95,y=260)

#创建两个label用于提示用户输入
label_usr_name=tk.Label(window,text='注册账号：',width=9)
label_warning=tk.Label(window,width=30,fg='red')
label_usr_psw=tk.Label(window,text='注册密码：',width=9)
label_usr_name.place(x=20,y=200)
label_warning.place(x=30,y=230)
label_usr_psw.place(x=20,y=260)

#注册按钮点击后调用的方法
def sign():
    '''
        该方法创建另一个弹出窗口用于新用户的注册。
    '''
#创建弹出窗口
    toplever=tk.Toplevel(window,height=300,width=500)
    toplever.title('用户注册')

#创建新的三个变量便于存储用户输入的信息
    var_usr_name_new = tk.StringVar()
    var_usr_pwd_new=tk.StringVar()
    var_usr_pwd_comfirm=tk.StringVar()
#设置用户名的示例
    var_usr_name_new.set('empty@newt.com.cn')

#创建三个输入框用户接受用户的输入信息
    entry_usr_name_new = tk.Entry(toplever,width=30, textvariable=var_usr_name_new)
    entry_usr_psw = tk.Entry(toplever,width=30, textvariable=var_usr_pwd_new, show='*')
    entry_usr_psw_comfirm = tk.Entry(toplever, width=30, textvariable=var_usr_pwd_comfirm, show='*')
    entry_usr_name_new.place(x=180, y=60)
    entry_usr_psw.place(x=180, y=120)
    entry_usr_psw_comfirm.place(x=180,y=180)

#三个label用于提示用户输入信息，其中一个警示标签在用户输入错误的信息是提示用户纠正
    label_usr_name_new = tk.Label(toplever, text='注册账号：', width=9)
    label_warning_new = tk.Label(toplever, width=30, fg='red')
    label_usr_psw_new = tk.Label(toplever, text='注册密码：', width=9)
    label_usr_psw_comfirm=tk.Label(toplever, text='确认密码：', width=9)
    label_usr_name_new.place(x=50, y=60)
    label_warning_new.place(x=150, y=90)
    label_usr_psw_new.place(x=50, y=120)
    label_usr_psw_comfirm.place(x=50,y=180)

#内部方法
    def sign_new():
        '''
            该内部方法是一系列对用户信息的判断，符合注册条件的用户将被注册
        '''
        #设置三个变量获取并存储输入框的信息
        new_name=entry_usr_name_new.get()
        new_pwd=entry_usr_psw.get()
        new_pwd_comfirm=entry_usr_psw_comfirm.get()

        with open('usr.pic','rb') as f_r:   #打开数据库
            usr_info=pickle.load(f_r)  #读取数据库
            if new_name == 'empty@newt.com.cn':
                #判断用户是否输入新的用户名
                label_warning_new.config(text='你还没有输入用户名')
            elif new_pwd == '' or new_pwd_comfirm == '':
                #判断两次密码是否存在没有输入的情况
                label_warning_new.config(text='两次密码不能为空')
            elif new_name in usr_info:
                #判断注册的新用户是否已在数据库中存在
                label_warning_new.config(text='该用户已被注册')
            elif len(new_pwd_comfirm)<8 or len(new_pwd)<8:
                #判断用户设置的密码的安全等级是否过低
                label_warning_new.config(text='您的密码过于简单，应不少于8位')
            elif new_pwd_comfirm!=new_pwd:
                #判断两次输入的密码是否一致
                label_warning_new.config(text='两次密码不一致')
            else:
                with open('usr.pic','wb') as f_w:
                    usr_info[new_name]=new_pwd_comfirm  #新用户的信息添加数据库中保存
                    pickle.dump(usr_info,f_w)
                    label_warning_new.config(text='注册成功')
    def quit():
        '''
        退出本程序
        '''
        window.destroy()
#创建不想注册则退出按钮和注册按钮
    button_sign_new = tk.Button(toplever, text='注册', bg='CornflowerBlue', width=8,command=sign_new)
    button_quit_new = tk.Button(toplever, text='退出', bg='CornflowerBlue', width=8,command=quit)
    button_quit_new.place(x=100, y=240)
    button_sign_new.place(x=320, y=240)
#在点击登录按钮后调用
def login():
    '''
        用于判断用户的登录信息是否正确
    '''
    #打开数据库
    with open('usr.pic','rb')as f:
        dict_usr_login=pickle.load(f)  #读取数据库中的用户信息
        if entry_usr_name.get() not in dict_usr_login:
            #判断用户是否已经注册，未注册则提示
            label_warning.config(text='该用户还没有注册，请注册！')
        elif dict_usr_login[entry_usr_name.get()]==entry_usr_psw.get():
            #判断用户名的密码是否与数据库中的密码一致
            label_warning.config(text='登录成功！')
        else:
            #密码错误提示
            label_warning.config(text='密码错误！')

#创建登录和注册按钮
button_sign=tk.Button(window,text='注册',bg='CornflowerBlue',width=8,command=sign)
button_login=tk.Button(window,text='登录',bg='CornflowerBlue',width=8,command=login)
button_login.place(x=40,y=300)
button_sign.place(x=180,y=300)

#开启主循环
window.mainloop()