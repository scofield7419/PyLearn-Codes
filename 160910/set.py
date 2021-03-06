#set
#set 和 dict 类似，也是一组 key 的集合，但不存储 value。由于 key 不能重复，所以，在 set 中，没有重复的 key。
#要创建一个 set，需要提供一个 list 作为输入集合：
#重复元素在 set 中自动被过滤
#同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证 set 内部“不会有重复元素”。
s  = set([1,2,3,8,9,2,3,7,4,5])
print(s)

s.add(34)
print(s)

#set 可以看成数学意义上的无序和无重复元素的集合，因此，两个 set 可以做数学意义上的交集、并集等操作：

s1 = set([1,2,3])
s2 = set([1,2,5,4])
print(s1&s2)
print(s1|s2)


#str 是不变对象，而 list 是可变对象。
#比如str，对 str 进行操作：
a = 'abc'
a.replace('a', 'A')
print(a)

a = 'abcd'
b = a.replace('d', 'D')
print(b)
print(a)
