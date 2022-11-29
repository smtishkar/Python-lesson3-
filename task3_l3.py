# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


list = [1.1, 1.2, 3.1, 5, 10.01]
new_list = [round(list[i] % 1,4) for i in range(len(list))] 
max = 0
min = 1

for i in range(len(new_list)-1):
    if max < new_list [i]:
        max = new_list [i]


for i in range(len(new_list)):
    if min > new_list [i] and new_list [i] !=0:
        min = new_list [i]


dif = max - min 
print(round(dif,4))



