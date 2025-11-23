from Task import Task
from pathlib import Path
import json

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

    def exit(self):
        lst_dict = [i.to_dict() for i in self.tasks]
        x = self.file_path
        with open(f'{x}', 'a', encoding='utf-8') as file:
            json.dump(lst_dict, file, ensure_ascii=False, indent=4)
        print(f"Сохранено в «{self.file_path}».")


    def __str__(self):
        if not self.tasks:
            return "Список задач пуст"
        else:
            all_in = ""
            for i in self.tasks:
                all_in+= f"задача: {i.title}, is_done: {i.is_done}\n"
            print("aa", all_in)
            return all_in



