# -*- coding:UTF-8 -*-
def cal_bonus():
    i = int(input("净利润"))
    arr = [1000000,600000,400000,200000,100000,0]
    rat = [0.01,0.015,0.03,0.05,0.075,0.1]
    b = 0
    for idx in range(0,6):
        if i>arr[idx]:
            b += (i-arr[idx])*rat[idx]
            print((i-arr[idx])*rat[idx])
            i = arr[idx]
    print(b)

cal_bonus()

