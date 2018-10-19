#测试默认参数、可变参数和关键字参数
def foo(p=[]):
	p.append('end')
	return p

L = [1,2,3,4]
L2 = foo(L)
print('L',L)
print('L2',L2)
print('L == L2',L==L2)


def my_sum(*p):
	psum = 0 
	for i in p:
		psum = psum + i
	return psum

print('my_sum 1-5',my_sum(1,2,3,4,5))
L = [1,2,3,4,5,6]
print('my_sum L',my_sum(*L))

def printInfo(**kw):
	print('printInfo')
	for k,v in kw.items():
		print(k+":"+str(v))

printInfo(name='dotmoon',age=22,country='China')
info = {'name':'小明','age':15,'country':'China'}
printInfo(**info)

def printMainInfo(*,name,city):
	print('printMainInfo')
	print('name',name)
	print('city',city)

printMainInfo(name='Lily',city='SH')
# printMainInfo(name='GG',age=18)

def testParams(name,age,*args,country,city):
	print('testParams')
	print('name:'+name)
	print('age:'+str(age))
	print(args)
	print(country)
	print(city)

testParams('Jimmy',19,173,55,country='China',city='NC')



