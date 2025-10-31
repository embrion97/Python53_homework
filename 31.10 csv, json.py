import json
import csv
from pathlib import Path
from typing import List, Dict

DATA_FILE = Path("employees.json")

def load_data() -> List[Dict]:
    if DATA_FILE.exists():
        with DATA_FILE.open(encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(employees: List[Dict]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(employees, f, ensure_ascii=False)

def print_table(employees: List[Dict]) -> None:
    if not employees:
        print("Список пуст.")
        return

    headers = ["Фамилия", "Имя", "Отчество", "Кабинет", "Телефон", "Должность"]
    col_widths = [max(len(str(row[h.lower()])) for row in employees) for h in headers]
    col_widths = [max(w, len(h)) for w, h in zip(col_widths, headers)]

    row_fmt = " | ".join(f"{{:<{w}}}" for w in col_widths)

    print(row_fmt.format(*headers))
    print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))

    for emp in employees:
        print(
            row_fmt.format(
                emp["surname"],
                emp["name"],
                emp["patronymic"],
                emp["room"],
                emp["phone"],
                emp["position"],
            )
        )

def add_employee(employees: List[Dict]) -> None:
    emp = {
        "surname": input("Фамилия: ").strip(),
        "name": input("Имя: ").strip(),
        "patronymic": input("Отчество: ").strip(),
        "room": input("Номер кабинета: ").strip(),
        "phone": input("Номер телефона: ").strip(),
        "position": input("Должность: ").strip(),
    }
    employees.append(emp)
    print("Сотрудник добавлен.")


def delete_employee(employees: List[Dict]) -> None:
    surname = input("Введите фамилию сотрудника для удаления: ").strip()
    for i, emp in enumerate(employees):
        if emp["surname"].lower() == surname.lower():
            del employees[i]
            print("Сотрудник удалён.")
            return
    print("Сотрудник не найден.")


def edit_employee(employees: List[Dict]) -> None:
    surname = input("Введите фамилию сотрудника для изменения: ").strip()
    for emp in employees:
        if emp["surname"].lower() == surname.lower():
            print("Новые данные (оставьте пустым, чтобы оставить без изменения):")
            for key in ["surname", "name", "patronymic", "room", "phone", "position"]:
                new_val = input(f"{key.capitalize()} [{emp[key]}]: ").strip()
                if new_val:
                    emp[key] = new_val
            print("Данные обновлены.")
            return
    print("Сотрудник не найден.")


def list_by_room(employees: List[Dict]) -> None:
    room = input("Введите номер кабинета: ").strip()
    filtered = [e for e in employees if e["room"] == room]
    print_table(filtered)


def sort_by_surname(employees: List[Dict]) -> None:
    employees.sort(key=lambda e: e["surname"].lower())
    print("Список отсортирован по фамилии.")


def find_by_surname(employees: List[Dict]) -> None:
    surname = input("Введите фамилию для поиска: ").strip()
    found = [e for e in employees if e["surname"].lower() == surname.lower()]
    print_table(found)

def export_to_csv(employees: List[Dict]) -> None:
    csv_file = Path("employees.csv")
    with csv_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["surname", "name", "patronymic", "room", "phone", "position"]
        )
        for e in employees:
            writer.writerow(
                [
                    e["surname"],
                    e["name"],
                    e["patronymic"],
                    e["room"],
                    e["phone"],
                    e["position"],
                ]
            )
    print(f"Экспортировано в {csv_file}")


def import_from_csv(employees: List[Dict]) -> None:
    csv_file = Path("employees.csv")
    if not csv_file.exists():
        print("CSV‑файл не найден.")
        return

    with csv_file.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            employees.append(
                {
                    "surname": row["surname"],
                    "name": row["name"],
                    "patronymic": row["patronymic"],
                    "room": row["room"],
                    "phone": row["phone"],
                    "position": row["position"],
                }
            )
    print(f"Импортировано из {csv_file}")

#1  Показать всех
#2  Добавить сотрудника
#3  Удалить сотрудника
#4  Изменить данные сотрудника
#5  Показать сотрудников в кабинете
#6  Сортировать по фамилии
#7  Найти по фамилии
#8  Экспорт в CSV
#9  Импорт из CSV
#0  Выход
#Выберите пункт:


employees = load_data()
while True:
        choice = input("введи цифру").strip()
        if choice == "1":
            print_table(employees)
        elif choice == "2":
            add_employee(employees)
        elif choice == "3":
            delete_employee(employees)
        elif choice == "4":
            edit_employee(employees)
        elif choice == "5":
            list_by_room(employees)
        elif choice == "6":
            sort_by_surname(employees)
        elif choice == "7":
            find_by_surname(employees)
        elif choice == "8":
            export_to_csv(employees)
        elif choice == "9":
            import_from_csv(employees)
        elif choice == "0":
            save_data(employees)
            print("Данные сохранены. До свидания!")
            break