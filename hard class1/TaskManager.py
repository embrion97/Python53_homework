from Task import Task
from pathlib import Path

FILE_PATH = Path("tasks.json")
class TaskManager():
    def __init__(self, file_path: Path = FILE_PATH):
        self.tasks: list[Task] = []
        self.file_path = file_path

    def error(self):
        print("Такая задача уже существует")


    def add_task(self, title):
        self.title =  title
        for i in self.tasks:
            if i.title == self.title:
                 return self.error()
        else:
            self.tasks.append(Task(title))
            print(f"Задача {title} добавлена")

    def remove(self, title_user):
        for i in self.tasks:
            if i.title == title_user:
                self.tasks.remove(i)

        return False


    def done(self, tittle: str):
        for i in self.tasks:
            if (i.title == tittle) and (i.is_done == "Не выполнено"):
                i.mark_done()
                print("Успешно")
                return True
            elif i.title == tittle:
                print("Задача уже выполнена")
                return True
        return False


    def __str__(self):
        if not self.tasks:
            return "Список задач пуст"
        else:
            all_in = ""
            for i in self.tasks:
                all_in+= f"задача: {i.title}, is_done: {i.is_done}\n"
            print("aa", all_in)
            return all_in



