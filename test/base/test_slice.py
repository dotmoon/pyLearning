#切片
L = [1 , 2 ,3 ,4]
print('第二第三个元素',L[1:3])
print('末尾3个元素',L[-3:])
L1 = list(range(1,100))
print('奇数',L1[::2])

L2 = L1[:]
L2.append(101)
print('L2 == L1',L2 == L1)
print('id(L2)',id(L2))
print('id(L1)',id(L1))
print('L1',L1)
print('L2',L2)

text = 'this is a text!'
print(text[0:9])
print(text[1::2])