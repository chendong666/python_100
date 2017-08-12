# -*- coding:utf-8 -*-
# python_version : 2.7.13

# 有四个数字：1、2、3、4，能组成多少个相互不同且不含重复数字的三位数，各是多少？

# 第一种方法
i = 0
for bai in range(1, 5):
    for shi in range(1, 5):
        for ge in range(1, 5):
            if (bai != shi) and (shi != ge) and (bai != ge):
                print bai, shi, ge
                i += 1
print u'共', i, u'个'

# 第二种方法
i = 0
for bai in range(1, 5):
    for shi in range(1, 5):
        if bai != shi:
            for ge in range(1, 5):
                if shi != ge != bai:
                    print bai, shi, ge
                    i += 1
print u'共', i, u'个'

# 第三种方法
# 列表生成式
list_num = [1, 2, 3, 4]

list2 = [i * 100 + j * 10 + k
         for i in list_num
         for j in list_num
         for k in list_num
         if (j != i and k != j and k != i)]

print (list2)
print u'共', len(list2), u'个'

# 第四种方法
# 通过检查所有可能的数字的百十个位是否相等来剔除不符合要求的
line = []
for i in range(111, 444):
    a = i % 10
    b = (i % 100) / 10
    c = (i % 1000) / 100
    if a != b and b != c and a != c and 0 < a < 5 and 0 < b < 5 and 0 < c < 5:
        print (i)
        line.append(i)
print('the total is :', len(line))

# 第五种方法
# 用集合去重然后判断集合长度来筛选
import pprint

# 使用此模块打印数据结构比较整齐

list_num = ['1', '2', '3', '4']
list_result = []
for i in list_num:
    for j in list_num:
        for k in list_num:
            if len(set(i + j + k)) == 3:
                list_result += [int(i + j + k)]
print("能组成%d个互不相同且无重复数字的三位数: " % len(list_result))
pprint.pprint(list_result)

# 第六种方法
# 调用自带的该模块和函数
from itertools import permutations

for i in permutations([1, 2, 3, 4], 3):
    print i

# 将结果转化为数字
for i in permutations([1, 2, 3, 4], 3):
    k = ''
    for j in range(0, len(i)):
        k = k + str(i[j])
    print (int(k))

# 第七种方法 按位运算
# 从 00 01 10  到  11 10 01
for num in range(6, 58):
    a = num >> 4 & 3
    b = num >> 2 & 3
    c = num & 3
    if (a ^ b) and (b ^ c) and (c ^ a):
        print a + 1, b + 1, c + 1
