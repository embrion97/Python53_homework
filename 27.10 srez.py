import random

#1
numbers = []

#for i in range(0, 4):
#    value = float(input(f"Введите число {i}: "))
#    numbers.append(value)

#minimum = min(numbers)
#print("Наименьшее число:", minimum)

#2
chislo = -3
while True:
    if chislo < -25:
        break
    print(chislo)
    chislo = chislo -3


#3
n = int(input("Введите сторону квадрата: "))
for i in range(n):
    print(" " * i, end="")
    for _ in range(n - i):
        print("*", end=" ")
    print()


#4
total = 0
count = 0
while True:
    x = float(input("Введите число: "))
    if x == 0:
        break
    total += x
    count += 1

if count == 0:
    print("Чисел не введено.")
else:
    avg = total / count
    print("Среднее арифметическое:", avg)

#5
first  = int(input("Первая граница диапазона: "))
second = int(input("Вторая граница диапазона: "))
if first > second:
    first,second = second,first
numbers = [random.randint(first, second) for _ in range(10)]
print("Список:", numbers)


#6 Продолжение 5 задачи
min_x = 0
for i in range(1, len(numbers)):
    if numbers[i] < numbers[min_x]:
        min_x = i
print(min_x)


#7
def copy_list(source, copy_sourse):
    for item in source:
        copy_sourse.append(item)
    print(source)
    print(copy_sourse)

x = [3, 5,1, 7, 11, "a"]
b = []
copy_list(x, b)

#8
def insert_ilement(lst, n, value):
    if n < 0:
        i = max(len(lst) + n, 0)
    n = min(n, len(lst))
    new_lst = lst[:i] + [value] + lst[i:]
    return new_lst

#9
def create_list(n, a, b):
    lst1 = list(range(a, b + 1))
    result = []
    for i in range(n):
        result.append(lst1[i % len(lst1)])
    return result

xx = create_list(15, 2, 25)
print("Задание 9 первая функция: ", xx)

def remove_value(ls: list, value):
    while value in ls:
        ls.remove(value)
    return ls

ls2 = [1, 7, 15, 76, "ab", 68, 15]

new_ls = remove_value(ls2, 15)
print("Новый список: ", new_ls)


