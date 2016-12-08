# -*-coding:utf-8 -*-
class NList():
    def __init__(self,*args):
        self.__list=[arg for arg in args ]
        self.index=0
    def __len__(self):
        return len(self.__list)

    def __getitem__(self, item):
        if 0<=item<len(self.__list):
            return  self.__list[item]
        else:
            raise IndexError('index out of range')

    def __setitem__(self, key, value):
        if 0<=key<len(self.__list):
            self.__list[key]=value
        else:
            raise IndexError('index out of range')
    def __delitem__(self, key):
        del self.__list[key]

    def __str__(self):
        return str(self.__list)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.index += 1        # 此处有技巧 先 +1 后返回值
            return self.__list[self.index-1]
        except IndexError:                # 此处改变异常类型 便于将IndexError 转换为StopIteration
            raise StopIteration()         #可以是利用迭代的时候被for循环捕捉处理



