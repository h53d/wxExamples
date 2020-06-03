#!/usr/bin/env python3

import time
import random

# 随机生成一个口算题及其正确结果的函数
def genOneExercise():
	opt = random.randint(0, 1)  # 在0和1中随机取一个值
	if opt == 1:	# 如果随机得到的是 1，我们就生成加法口算题
		a = random.randint(1, 99)	# 注意这里是 99
		b = random.randint(1, 100-a)	# 这是保证百以内加法的地方
		result = a + b
		return a, opt, b, result
	else:			# 如果随机得到的是 0，我们就生成减法口算题
		a = random.randint(1, 100)
		b = random.randint(1, 100)
		if a > b:
			result = a - b
			return a, opt, b, result
		else:
			result = b - a	# 这里是避免出现减数不够的地方
			return b, opt, a, result

# 做口算练习， 做的题目个数通过函数参数指定
def doExercises(times):
	random.seed(time.time())	# 随机系统的种子

	errorList = []
	i = 0
	while i < times:
		try:
			x, op, y, res = genOneExercise()
			if op == 1:
				tip = str(x) + ' + ' + str(y) + ' = '
			else:
				tip = str(x) + ' - ' + str(y) + ' = '

			num = input(tip)
			if num.isdigit():
				ret = int(num)
				if ret != res:		# 口算错了时才记录
					record = (x, op, y, res, ret)	# 信息组织成元组结构
					errorList.append( record )
				i = i + 1
			else:
				print("请输入整数")
		except Exception as e:
				print("出现异常:", e)

	return errorList

# 打印口算结果
def printErrors(errors):
	if len(errors) > 0:
		print("口算错误的题目:")
		for error in errors:
			a, op, b, result, yourInput = error
			if op == 1:
				tip = str(a) + ' + ' + str(b) + ' = ' + str(result) + ", 你的错误答案:" + str(yourInput)
			else:
				tip = str(a) + ' - ' + str(b) + ' = ' + str(result) + ", 你的错误答案:" + str(yourInput)
			print(tip)
	else:
		print("恭喜你全部答对!")



# 本文件执行时的入口 - 运行时从这里开始
if __name__ == '__main__':
	errors = doExercises(4)		# 做练习
	printErrors(errors)		# 打印练习结果
