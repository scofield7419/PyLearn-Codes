#slice切片：截取list的片段

L = ['micheal','scott','bob','jack']
print(L[0:3])

print(L[:2])

print(L[1:2])

#倒数切片
print(L[-3:-1])


#
print((1,2,3,4,5,6,7,8,9,0)[2:5])

P = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
#前 10 个数，每两个取一个：
print(P[:10:2])
#所有数，每 5 个取一个：
print(P[::5])


#字符串'xxx'也可以看成是一种 list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('SCOFIELD'[2:4])
print('kjaefkejnfeafe'[::3])
