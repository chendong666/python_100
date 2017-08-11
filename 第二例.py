# -*- coding:utf-8 -*-
# python_version:2.7.13
'''企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？'''

# 方法一
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

x = int(raw_input("净利润："))

if x <= 100000:
    bonus = x * 0.1
    print u"奖金:", bonus, u"元"
elif 100001 < x <= 200000:
    bonus = 10000 + (x - 100000) * 0.075
    print u"奖金:", bonus, u"元"
elif 200001 < x <= 400000:
    bonus = 10000 + 7500 + (x - 200000) * 0.05
    print u"奖金:", bonus, u"元"
elif 400001 < x <= 600000:
    bonus = 10000 + 7500 + 10000 + (x - 400000) * 0.03
    print u"奖金:", bonus, u"元"
elif 600001 < x <= 1000000:
    bonus = 10000 + 7500 + 10000 + 6000 + (x - 600000) * 0.015
    print u"奖金:", bonus, u"元"
elif 600001 < x <= 1000000:
    bonus = 10000 + 7500 + 10000 + 6000 + 6000 + (x - 600000) * 0.01
    print u"奖金:", bonus, u"元"

# 方法二
i = int(raw_input('净利润:\n'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for idx in range(0, 6):
    if i > arr[idx]:
        r += (i - arr[idx]) * rat[idx]
        i = arr[idx]
print u'总奖金：', r

# 方法三
i = int(raw_input('净利润:'))
I = [1000000, 600000, 400000, 200000, 100000, 0]
r = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
for j in range(len(I)):
    if i > I[j]:
        b = [0, 0, 0, 0, 0, 0]
        b[j] = i - I[j]
        for k in range(j, len(I)):
            b[k] = I[k]
        bonus = sum(map(lambda (i1, i2): i1 * i2, zip(b, r)))
        break
print '奖金:', bonus
# 方法四
value = int(raw_input('please input profit: '))
list1 = [1000000, 600000, 400000, 200000, 100000, 0]
list2 = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
list3 = [400000, 200000, 200000, 100000, 100000]
for i in range(6):
    if value > list1[i]:
        v1 = (value - list1[i]) * list2[i]
        print v1
        list2_new = list2[i + 1:6]
        list3_new = list3[i:5]
        v2 = sum(map(lambda (x, y): x * y, zip(list2_new, list3_new)))
        print v2
        print v1 + v2
        break
