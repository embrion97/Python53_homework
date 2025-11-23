from Task import Task
from TaskManager import TaskManager

command = f"add - добавить задачу\ndel - удалить задачу\nlist - список активных хадач\ndone - изменить статус задачи"
first = TaskManager()
while True:
    x = input(command)
    if x == "add":
        first.add_task(input("Введи наименование новой задачи"))
    elif x == "del":
        del_task = input("введи название задачи которую хочешь удалить")
        if first.remove(del_task) == False:
            print("Такой задачи не существует")


    elif x == "list":
        print(first)
    elif x == "done":
        tittle = input("Какую задачу изменить")
        if first.done(tittle):
            pass
        else:
            print("Такой задачи не существует")
    elif x == "exit":
        first.exit()
        break



if __name__ == '__main__':
    pass