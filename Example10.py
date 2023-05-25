lenght = input("Введите кол-во моенток: ")
lenght = int(lenght)
list = []
while len(list) <lenght:
    list.append(int(input("Введите положение монетки: ")))
i=0
reshka=0
orel=0
while i<len(list)-1:
    if list[i]==1 :
        orel+=1
    else:
        reshka+=1
    i+=1
if orel > reshka:
    print (list , ' Нужно перевернуть -->', orel , 'монеток' )
else:
    print (list , ' Нужно перевернуть -->', reshka , 'монеток' )
