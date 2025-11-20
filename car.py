from typing import List

class Car:
    """Один автомобиль."""
    def __init__(self, make: str, model: str, year: int):
        self.make  = make   # производитель, например "Toyota"
        self.model = model  # модель, например "Corolla"
        self.year  = year   # год выпуска

    def __repr__(self) -> str:
        return f"<Car {self.year} {self.make} {self.model}>"

    def to_dict(self) -> dict:
        """Удобно для сериализации (JSON, CSV и т.п.)."""
        return {"make": self.make, "model": self.model, "year": self.year}

    @staticmethod
    def from_dict(data: dict) -> "Car":
        """Создать объект из словаря."""
        return Car(make=data["make"], model=data["model"], year=data["year"])



class CarCollection:
    """Контейнер для множества объектов Car."""
    def __init__(self, cars: List[Car] | None = None):
        self.cars: List[Car] = cars if cars is not None else []

    # ---------- CRUD ----------
    def add(self, car: Car) -> None:
        """Добавить новый автомобиль."""
        self.cars.append(car)

    def remove(self, car: Car) -> None:
        """Удалить автомобиль (если он есть)."""
        try:
            self.cars.remove(car)
        except ValueError:
            pass  # не найден – ничего не делаем

    def find(self, make: str = "", model: str = "", year: int | None = None) -> List[Car]:
        """Вернуть все машины, подходящие под указанные критерии."""
        result = self.cars
        if make:
            result = [c for c in result if c.make.lower() == make.lower()]
        if model:
            result = [c for c in result if c.model.lower() == model.lower()]
        if year is not None:
            result = [c for c in result if c.year == year]
        return result

    # ---------- представление ----------
    def __len__(self) -> int:
        return len(self.cars)

    def __iter__(self):
        return iter(self.cars)

    def __repr__(self) -> str:
        return f"<CarCollection {len(self)} cars>"

    # ---------- сериализация ----------
    def to_json(self, path: str) -> None:
        """Сохранить список в JSON‑файл."""
        import json
        data = [c.to_dict() for c in self.cars]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @classmethod
    def from_json(cls, path: str) -> "CarCollection":
        """Загрузить список из JSON‑файла."""
        import json
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
        cars = [Car.from_dict(item) for item in raw]
        return cls(cars)