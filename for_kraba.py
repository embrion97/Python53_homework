import json
from pathlib import Path

FILE_PATH = Path("tasks.json")


# -------------------------------------------------
# 1️⃣ Класс задачи
# -------------------------------------------------
class Task:
    """Одна задача."""
    def __init__(self, title: str, is_done: bool = False):
        self.title = title
        self.is_done = is_done          # False → «Не выполнено», True → «Выполнено»

    def mark_done(self) -> None:
        """Пометить задачу как выполненную."""
        self.is_done = True

    def status(self) -> str:
        """Читаемое представление статуса."""
        return "Выполнено" if self.is_done else "Не выполнено"

    def to_dict(self) -> dict:
        """Сериализация в словарь (для JSON)."""
        return {"title": self.title, "is_done": self.is_done}

    @staticmethod
    def from_dict(data: dict) -> "Task":
        """Создать объект Task из словаря."""
        return Task(title=data["title"], is_done=data["is_done"])


# -------------------------------------------------
# 2️⃣ Класс‑контейнер задач
# -------------------------------------------------
class TaskManager:
    """Управление списком задач, хранение/загрузка из JSON."""
    def __init__(self, file_path: Path = FILE_PATH):
        self.file_path = file_path
        self.tasks: list[Task] = []
        self.load_from_file()                     # попытка загрузить существующий файл

    # ---------- CRUD ----------
    def add_task(self, title: str) -> bool:
        """Добавить задачу, если её ещё нет. Возвращает True / False."""
        if any(t.title == title for t in self.tasks):
            return False
        self.tasks.append(Task(title))
        return True

    def mark_task_done(self, title: str) -> bool:
        """Пометить задачу как выполненную. Возвращает True / False."""
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                return True
        return False

    def show_tasks(self) -> None:
        """Вывести список задач с их статусами."""
        if not self.tasks:
            print("Список задач пуст.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.title} — {task.status()}")

    # ---------- persistence ----------
    def save_to_file(self) -> None:
        """Сохранить текущий список в JSON‑файл."""
        data = [t.to_dict() for t in self.tasks]
        self.file_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2)
        )
        print(f"Сохранено в «{self.file_path}».")

    def load_from_file(self) -> None:
        """Загрузить список из JSON‑файла (если файл существует)."""
        if not self.file_path.is_file():
            return  # файл ещё не создан – оставляем пустой список
        try:
            raw = json.loads(self.file_path.read_text())
            self.tasks = [Task.from_dict(item) for item in raw]
        except (json.JSONDecodeError, KeyError):
            print("Ошибка чтения файла – начат пустой список.")
            self.tasks = []


    # ---------- представление ----------
    def __str__(self) -> str:
        """Удобный вывод списка задач в виде строки."""
        return "\n".join(
            f"{i + 1}. {t.title} — {t.status()}" for i, t in enumerate(self.tasks)
        )