#!/usr/bin/env python3

def findNarcissisticNumber():
  i = 100
  while i <= 999:
    low = i % 10          # 用取余的方法得到个位数
    mid = int(i/10) % 10  # 取十位数， 注意除以10后的取整
    hight = int(i /100)   # 取百位数，同样注意除法后的取整
    sum = low * low * low + mid * mid * mid + hight * hight * hight # 关键算法
    if i == sum : # 判断是否为水仙花数
      print("找到一个水仙花数:", i)
    i = i + 1

if  __name__ == "__main__":
  findNarcissisticNumber()