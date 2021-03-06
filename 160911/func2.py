#装饰器


#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
#函数对象有一个__name__属性，可以拿到函数的名字：
def now():
	print('201628211')

print(now.__name__)

#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。本质上，decorator 就是一个返回函数的高阶函数。
def log(func):
	def wrapper(*args,**kw):
		print('call %s():'% func.__name__)
		return func(*args,**kw)
	return wrapper
#观察上面的 log，因为它是一个 decorator，所以接受一个函数作为参数，
#并返回一个函数。我们要借助 Python 的@语法，把 decorator 置于函数的定义处：

@log
def now():
	print('201628211')

print(now())
#调用 now()函数，不仅会运行 now()函数本身，还会在运行 now()函数前打印一行日志：
#把@log 放到 now()函数的定义处，相当于执行了语句：now = log(now)
