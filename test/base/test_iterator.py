#测试迭代

info = {'name':'dotmoon','age':18,'city':'HZ'}
for k in info:
	print(k)
for v in info.values():
	print(v)
for k , v in info.items():
	print(k,v)

L = [0x000f,0x00f0,0x0f00,0xf000]
for k , v in enumerate(L):
	print(k , '%x' % v)

#列表生成式
jishu = [x for x in range(1,10) if x % 2 == 1]
print('jishu',jishu)
oushu = [x for x in range(1,10) if x % 2 == 0]
print('oushu',oushu)
hunhe = [x * y for x in jishu for y in oushu]
print('hunhe',hunhe)

#生成器
g = (x for x in range(1,10))
print(g)
print('print values in g')
for v in g:
	print(v)

from collections import Iterator,Iterable
# print('isintance(g,Iterator)',isintance(g,Iterator))
# print('isintance(g,Iterable)',isintance(g,Iterable))