from Task import Task
from pathlib import Path

FILE_PATH = Path("tasks.json")
class TaskManager():
    def __init__(self, file_path: Path = FILE_PATH):
        self.tasks: list[Task] = []
        self.file_path = file_path


    def add_task(self, title):
        self.title =  title
        if self.title not in self.tasks:
            self.tasks.append(Task(title))
        else:
            return False



    def __str__(self):
        return f"{self.tasks}"

