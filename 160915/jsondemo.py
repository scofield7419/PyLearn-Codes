#json

#JSON 类型 Python 类型
#{} dict
#[] list
#"string" str
#1234.56 int 或 float
#true/false True/False
#null None

# dumps()
import json
d = dict(name='scott',age=23,score = 88)
str = json.dumps(d)
print(str)


#load()
#把 JSON 反序列化为 Python 对象
print(json.loads(str))


#定制序列化class
#dumps()的可选参数可以让我们来定制 JSON 序列化
#我们只需要为 Student 专门写一个转换函数，再把函数传进去即可：
class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score

s = Student('scofield',23,99)

def stud2dict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}

#Student 实例首先被 student2dict()函数转换成 dict，然后再被顺利序列化为 JSON：
print(json.dumps(s,default = stud2dict))


#把任意 class 的实例变为 dict：
print(json.dumps(s,default=lambda obj:obj.__dict__))
#通常 class 的实例都有一个__dict__属性，它就是一个 dict，用来存储实例变量。


#反序列化
def dict2student(d):
	return Student(d['name'], d['age'], d['score'])

json_st = str
print(json.loads(json_st,object_hook = dict2student))




