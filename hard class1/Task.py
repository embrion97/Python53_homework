class Task:
    def __init__(self, title, is_done = "Не выполнено"):
        self.title = title
        self.is_done = is_done

    def mark_done(self):
        self.is_done = "Выполнено"

    def compliet(self):
        return self.is_done


def to_dict(self) -> dict:
    return {"title": self.title, "is_done": self.is_done}




