# -*- coding:utf-8 -*-
L = list(range(1,10))
def x2(n):
	return n * 2
it = map(x2,L)
print('result x2',list(it))

def char2num(c):
	return int(c)

def realNum(x , y):
	return x * 10 + y

from functools import reduce
result = reduce(realNum , map(char2num,['9','8','7','6','5','4','3','2','1']))
print('result is',result)


def jishu():
	n = 1
	while True:
		n = n + 2
		yield n

def mod0(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = jishu()
	while True:
		n = next(it)
		yield n
		it = filter(mod0(n),it)

for n in primes():
	if n > 1000:
		break
	else:
		print(n)


L = [('A',22),('B',10),('C',33)]
def byName(x):
	return x[0]

def byScore(x):
	return x[1]


print('byName',sorted(L,key=byName))
print('byScore',sorted(L,key=byScore))

import time
def log(func):
	def wrapper(*args,**kw):
		print('call ',func.__name__)
		return func(*args,**kw)
	return wrapper


@log
def now():
	print(time.time())

now()

def log(txt):
	def decorator(func):
		def wrapper(*args,**kw):
			print(txt,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator

@log('call')
def now2():
	print(time.time())

now2()


