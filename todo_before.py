tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    else:
        print("Ошибка: неверный индекс задачи")

def mark_task_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
    else:
        print("Ошибка: неверный индекс задачи")

def show_tasks():
    if not tasks:
        print("Список задач пуст")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "✗"
            print(f"{i + 1}. [{status}] {task['task']}")

def main():
    while True:
        print("\nМеню:")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Отметить задачу как выполненную")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Введите задачу: ")
            add_task(task)
        elif choice == "3":
            index = int(input("Введите номер задачи для удаления: ")) - 1
            delete_task(index)
        elif choice == "4":
            index = int(input("Введите номер задачи для отметки как выполненной: ")) - 1
            mark_task_done(index)
        elif choice == "5":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()