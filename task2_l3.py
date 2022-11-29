# 2'. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний
#  элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 
# В скобках пример, как это работает!!!


from random import randint

initial_list_len = 8
sum = 0
list = [randint (0,10) for i in range (initial_list_len)]
new_list = []
mul = 0 
if initial_list_len % 2 == 0:
    len_list = int(initial_list_len/2)
else:
    len_list =int(initial_list_len/2)+1

# print(len_list)
print(list)


for i in range (len_list):
    mul = list[i] * list [(i+1)*-1]
    new_list.append(mul)
    print (mul, list [i], list [(i+1)*-1])

print(new_list)