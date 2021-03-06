#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

a = abs
print(a(-123))

n1 = 255
n2 = 1024
h = hex(n1)
print(h)
h2 = hex(n2)
print(h2)

#在 Python 中，定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用 return 语句返回。

def fun1(x):
	if x>=23:
		return 'big'
	else:
		return 'small'

print(fun1(21))

#如果想定义一个什么事也不做的空函数，可以用 pass 语句：
def nop():
	pass
#pass 语句什么都不做，那有什么用？实际上 pass 可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个 pass，让代码能运行起来。
#pass 还可以用在其他语句里，比如：
#if age >= 18:
# pass


#对函数参数类型做检查
#添加了参数检查后，如果传入错误的参数类型，函数就可以抛出一个错误：
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return-x

#print(my_abs('asd'))


#函数可以返回多个值吗？答案是肯定的。
#Python 的函数返回多值其实就是返回一个 tuple，但写起来更方便。
import math

def move(x,y ,step ,angle):
	nx = x+step*math.cos(angle)
	ny = y-step*math.sin(angle)
	return nx,ny

x,y = move(100,100,60,math.pi/60)
print(x,y)

r =  move(100,100,60,math.pi/60)
print(r)

#默认参数
#规则：必选参数在前，默认参数在后
def powerful(x ,n =2):
	s = 1;
	while n>0:
		n -= 1
		s *=x
	return s

print(powerful(5))
print(powerful(5,5))

#默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑
def add_end(L = []):
	L.append('END')
	return L

print(add_end([1,2,3]))#正常传参
print(add_end())#默认传参有问题
print(add_end())
print(add_end())

#因为L指向了可变对象。所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=None):
	if L is None:
		L = [ ]
	L.append('END')
	return L

print(add_end())#默认传参正常
print(add_end())
print(add_end())
#为什么要设计 str、None 这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。



#在 Python 函数中，还可以定义可变参数
#方式1：可以把 a，b，c……作为一个 list 或 tuple 传进来
def calc(numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum
#但是调用的时候，需要先组装出一个 list 或 tuple：
print(calc([1,2,3,4]))
print(calc((1,4,25,3)))

 #方式2：利用可变参数，调用函数的方式可以简化.定义可变参数和定义一个 list 或 tuple 参数相比，仅仅在参数前面加了一个*号
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum
print(calc(1,4,2,6))
 #Python允许你在list或tuple前面加一个*号，把 list 或 tuple 的元素变成可变参数传进去
print(calc(*[1,2,45,9]))




#可变参数允许你传入 0 个或任意个参数，这些可变参数在函数调用时自动组装为一个 tuple。而关键字参数允许你传入 0 个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个 dict
def person(name,age,**kw):
	print('name: ',name,' age: ',age,' other: ',kw)
#可以传入任意个数的关键字参数：
person('scott',23,city='hubei')
person('scott',23,city='hubei',job='coder')

extra = {'city':'beijing','job':'coder'}
person('scott',23,city=extra['city'],job=extra['job'])
#**extra 表示把 extra 这个 dict 的所有 key-value 用关键字参数传入到函数的**kw 参数，kw 将获得一个 dict，注意 kw 获得的 dict 是 extra 的一份拷贝，对 kw 的改动不会影响到函数外的 extra。
person('scofield',22,**extra)



#位置参数(普通参数)和命名关键字参数（*）
def person(name,age,*,city='hongkong',job='coder'):
	print(name,age,city,job)
person('scofff',212,city='homy',job='eatter')



#参数组合
#在 Python 中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这 5 种参数都可以组合使用
#但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
def f1(a,b,c=0,*args,**kw):
	print(a,b,c,args,kw)
f1(1,2)
f1(1,2,c=4)
f1(1,3,6,'aw','wad',x=123,y='1232')

def f2(a,b,c=1,*,d,**kw):
	print(a,b,c,d,kw)
args=(1,23,45)
kw={'d':23,'wa':'#'}
f2(*args,**kw)

#要注意定义可变参数和关键字参数的语法：
#*args 是可变参数，args 接收的是一个 tuple；
#**kw 是关键字参数，kw 接收的是一个 dict。

