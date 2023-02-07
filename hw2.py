# # Задача 2.
# # Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# # Пример
# # 5
# # 1 2 3 4 5
# # 6
# # -> 5


n=int(input('Введите количество элементов в массиве N:'))
while n<=0  :
     n=int(input('Введите число большее 0 :' ))
my_list=[]
for i in range(n):
     num=int(input(f'Введите {i+1} элемент массива :'))
     my_list.append(num)
x=float(input('Введите число X:'))

my_list_1=[]
for i in range(n): 
    b=abs(my_list[i]-x) 
    my_list_1.append(b) 
min=my_list_1[0] 
index=0
for i in range(1,len(my_list_1)): 
    if my_list_1[i]<=min: 
        min=my_list_1[i] 
        index=i   
print(f'Ближайший элемент массива {my_list} к числу {x} элемент {my_list[index]}')