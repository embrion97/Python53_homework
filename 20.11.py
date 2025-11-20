import re

def find_slovo(x: str):
    sum = 0
    with open('hello.txt', "r", encoding="utf-8") as myfile:
        a = myfile.read()
        print(a)
        aa = a.split("\n")
        print(aa)
        for i in aa:
            if i == x:
                sum  = sum + 1
    print(sum)


find_slovo('line')








