# -*- coding:utf-8 -*-
'''
    解决数学上的不同颜色球抽取的组合问题
'''
def color_ball(color_1,color_2,color_3,take_num):
    '''
    :param color_1: 第一个参数是第一种颜色的元组或是列表例如（‘红’，2）[‘red’，2]
    :param color_2: 第二个参数是第二种颜色的元组或是列表例如（‘蓝’，3）[‘blue’，3]
    :param color_3: 第三个参数是第三种颜色的元组或是列表例如（‘绿’，4）[‘green’，4]
    :param take_num: 一次抽取个数
    :return: 返回的是所有可能的组合
    '''
    if isinstance(color_1,(tuple,list)) and isinstance(color_1,(tuple,list)) and isinstance(color_1,(tuple,list)):
        if isinstance(take_num,int):
            color_1_num=color_1[1]
            color_2_num = color_2[1]
            color_3_num = color_3[1]

            color_1_color=color_1[0]
            color_2_color = color_2[0]
            color_3_color = color_3[0]

            if take_num > color_1_num + color_2_num + color_3_num or take_num <=0:
                raise  ValueError('输入的一次抽取球个数不合法')

            count =0

            for num_1 in range(color_1_num+1):
                for num_2 in range(color_2_num+1):
                    for num_3 in range(color_3_num+1):
                        if num_1+ num_2 + num_3 == take_num:
                            count+=1
                            print color_1_color * num_1,color_2_color * num_2,color_3_color*num_3
            return count
        else:
            raise  ValueError('第四个参数应该为整数')
    else:
        raise TypeError('前三个参数应该为元组或者是列表')

count=color_ball(('红',4),('黑',4),('绿',4),3)
print  count
