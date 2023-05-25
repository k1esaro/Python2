n=int(input('Введите число N: '))
list=[]
k=0
while 2**k<n:
    list.append(int(2**k))
    k+=1
print(list)
