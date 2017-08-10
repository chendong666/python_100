# -*- coding:utf-8 -*-
# python_version : 2.7.13

# 有四个数字：1、2、3、4，能组成多少个相互不同且不含重复数字的三位数，各是多少？

import time

a = time.time()
for bai in range(1, 5):
    for shi in range(1, 5):
        for ge in range(1, 5):
            if (bai != shi) and (shi != ge) and (bai != ge):
                print bai, shi, ge
b = time.time()

for bai in range(1, 5):
    for shi in range(1, 5):
        if bai != shi:
            for ge in range(1, 5):
                if shi != ge != bai:
                    print bai, shi, ge
c = time.time()

for bai in range(1, 5):
    for shi in range(1, 5):
        if bai != shi:
            for ge in range(1, 5):
                if shi != ge != bai:
                    print bai * 100 + shi * 10 + ge
d = time.time()

i = b - a
j = c - b
k = d - c
print cmp(i, j)
print cmp(j, k)
print cmp(i, k)
