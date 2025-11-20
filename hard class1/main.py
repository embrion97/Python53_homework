from Task import Task
from TaskManager import TaskManager

first = TaskManager()
while True:

    first.add_task(input("Введи"))
    print(first)


if __name__ == '__main__':
    pass