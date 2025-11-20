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

def new_file():
    with open("hello.txt", "r", encoding="utf-8") as file:
        x = file.read()

    with open(f"hello_copy.txt", "w", encoding="utf-8") as myfile:
        myfile.write(x)

new_file()

vocabular = ('ой', "уй")
text = "ой как хорошо уй буй"
def seach(vocabular, text):
    for i in vocabular:
        for match in re.finditer(i, text):
            text = text[:match.start()] + text[match.start(-1):]
    print(text)

seach(vocabular, text)












