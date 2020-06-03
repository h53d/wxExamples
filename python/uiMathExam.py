#!/usr/bin/env python3

import random
import tkinter as tk

# 随机生成一个口算题及其正确结果的函数
def genOneExercise():
	opt = random.randint(0, 1)  # 在0和1中随机取一个值
	if opt == 1:	# 如果随机得到的是 1，我们就生成加法口算题
		a = random.randint(1, 99)	# 注意这里是 99
		b = random.randint(1, 100-a)	# 这是保证百以内加法的地方
		result = a + b
		#return a, opt, b, result
		return " {a} + {b} = ".format(a=a, b=b), result
	else:			# 如果随机得到的是 0，我们就生成减法口算题
		a = random.randint(1, 100)
		b = random.randint(1, 100)
		if a > b:
			result = a - b
			# 和上篇文章里代码比， 此处已把返回数据格式简化
			return " {a} - {b} = ".format(a=a, b=b), result
		else:
			result = b - a	# 这里是避免出现减数不够的地方
			# 和上篇文章里代码比， 此处已把返回数据格式简化
			return " {a} - {b} = ".format(a=b, b=a), result


class MyApp(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.counter = 0
		self.result = None
		self.master = master
		self.pack()
		self.create_widgets()
	
	def create_widgets(self):
		self.tip = tk.StringVar()
		self.tip.set("准备好了？")
		self.question = tk.Label(self, textvariable=self.tip, justify="right")
		self.question.grid(row=0, column=0, sticky=tk.E)
		
		self.input = tk.IntVar()
		self.answer = tk.Entry(self, textvariable=self.input, state="disabled")
		self.answer.bind('<Key-Return>',self.enterConfirm)
		self.answer.grid(row=0, column=1, sticky=tk.W)
		
		self.btnStart = tk.Button(self, text="开始", command=self.clickStart)
		self.btnStart.grid(row=0, column=2, sticky=tk.W)
		
		self.confirm = tk.Button(self, text="确定", fg="red", command=self.clickConfirm)
		self.confirm.grid(row=0, column=2, sticky=tk.W)
		self.confirm.grid_remove()
		
		self.his = tk.StringVar()
		self.his.set("history items")
		self.history = tk.Text(self, bg='green', height=50)
		self.history.grid(row=1, columnspan=3)
		
		self.quit = tk.Button(self, text="退出", fg="red", command=self.master.destroy)
		self.quit.grid(row=3, column=0, columnspan=3)
	
	
	def clickStart(self):
		txt, self.result = genOneExercise()
		self.tip.set(txt)
		self.input.set("")
		
		self.btnStart.grid_remove()
		self.answer['state'] = 'normal'
		self.confirm.grid()
	
	def clickConfirm(self):
		self.counter = self.counter + 1
		v = self.input.get()
		if v == self.result:
			his = "({i}), {q} {a}  对\n".format(i=self.counter, q=self.tip.get(),a=v)
		else:
			his = "({i}), {q} {a}  错\n".format(i=self.counter, q=self.tip.get(),a=v)
		self.history.insert('end', his )
		
		txt, self.result = genOneExercise()
		self.tip.set(txt)
		self.input.set("")
	
	def enterConfirm(self,event):
		self.counter = self.counter + 1
		v = self.input.get()
		if v == self.result:
			his = "({i}), {q} {a}  对\n".format(i=self.counter, q=self.tip.get(),a=v)
		else:
			his = "({i}), {q} {a}  错\n".format(i=self.counter, q=self.tip.get(),a=v)
		self.history.insert('end', his )
		
		txt, self.result = genOneExercise()
		self.input.set("")
		self.tip.set(txt)

if __name__ == "__main__":
	root = tk.Tk()
	app = MyApp(master=root)
	app.master.title("口算程序")
	app.mainloop()
