import random

# 0 - ножницы
# 1 - камень
# 2 - бумага

while True:

    bot  = random.randint(0,2)
    user = int(input("Введите число от 0 до 2, где 0 - ножницы, 1 - камень, 2 - бумага"))
    if user == 0 or 1 or 2:
        if bot == 0 and user == 0:
            print("Ничья")
        elif bot == 0 and user == 1:
            print("Вы выиграли")
        elif bot == 0 and user == 2:
            print("ВЫ проиграли")
        elif bot == 1 and user == 0:
            print("Вы проиграли")
        elif bot == 1 and user == 1:
            print("Ничья")
        elif bot == 1 and user == 2:
            print("Вы выиграли")
        elif bot == 2 and user == 0:
            print("Вы выиграли")
        elif bot == 2 and user == 1:
            print("Вы проиграли")
        elif bot == 2 and user == 2:
            print("Ничья")
    else:
        print("Введен неверный формат")
    play_now = 0
    while play_now != 1 and play_now != 2:
        play_now = int(input("Играть снова: 1 - ДА, 2 - НЕТ"))
    if play_now == 2:
        break
print("Конец")


