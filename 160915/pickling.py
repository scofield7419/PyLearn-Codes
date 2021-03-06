#序列化
#把变量从内存中变成可存储或传输的过程称之为序列化
#在 Python中叫 pickling，在其他语言中也被称之为 serialization，marshalling，flattening 等等
#反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即 unpickling

import pickle
d = dict(name='scott',age=22,score=80)
s = pickle.dumps(d)#将对象序列化
print(s)
#pickle.dumps()方法把任意对象序列化成一个 bytes，然后，就可以把这
#个 bytes 写入文件。或者用另一个方法 pickle.dump()直接把对象序列化
#后写入一个 file-like Object：

f = open('dump.txt','wb')
pickle.dump(d,f) #
f.close()

