# 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


#Первый способ при помощи метода:

# number = int(input('Введите число: '))
# a = bin(number)[2:]
# print(a)


#Второй способ
number = int(input('Введите число: '))
list = []

while number > 0:           # переводим в двричную сисему
    res = number % 2
    number = number // 2
    list.append(res)


# print (list)
list.reverse()              
# print (list)

for i in range(len(list)):
    print (list[i], end='' )    