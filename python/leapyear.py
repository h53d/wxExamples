#!/usr/bin/env python3

def leapYear(year):
	isLeapYear = False
	y = int(year)
	if y % 4 == 0:
		if y % 100 == 0:
			if y % 400 == 0:
				isLeapYear = True
			else:
				isLeapYear = False
		else:
			isLeapYear = True
	else:
		isLeapYear = False
	return isLeapYear



if __name__ == '__main__':
	year = input('请输入年份整数：') # 获得输入的数据是字符串类型，把它存在变量 year 里
	if True == leapYear(year):
		print(year + '是闰年')
	else:
		print(year + '不是闰年.')
