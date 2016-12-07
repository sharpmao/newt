#   -*- coding:utf-8 -*-
'''
   对列表插入操作的实现
'''
class myList(object):
    '''
        自己实现的list类
    '''
    __list=[]

    def __init__(self,*value):
        self.__list.extend(value)

    def __str__(self):
       return  str(self.__list)

    def myInsert(self,index,value):
        '''
        :function   利用切片方法实现list的insert()方法
        :param  index: give a index
        :param  value: the value you want to insert
        example:    mylist.myInsert(2,7)
        '''
        if index < 0 or index > len(self.__list):
            raise IndexError('index out of list')
        else:
            list_in_1 = self.__list[:index]
            list_in_2 = self.__list[index:]
            list_in_1.append(value)
            list_in_1.extend(list_in_2)
            self.__list = list_in_1
