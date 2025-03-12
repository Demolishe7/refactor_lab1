class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def delete_task(self, index):
        try:
            self.tasks.pop(index)
        except IndexError:
            print("Ошибка: неверный индекс задачи.")

    def mark_task_completed(self, index):
        try:
            self.tasks[index].completed = True
        except IndexError:
            print("Ошибка: неверный индекс задачи.")

    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")


def get_user_choice():
    print("\nМеню:")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Отметить задачу как выполненную")
    print("5. Выйти")
    return input("Выберите действие: ")


def main():
    task_manager = TaskManager()

    while True:
        choice = get_user_choice()

        if choice == "1":
            task_manager.show_tasks()
        elif choice == "2":
            task = input("Введите задачу: ")
            task_manager.add_task(task)
        elif choice == "3":
            try:
                index = int(input("Введите номер задачи для удаления: ")) - 1
                task_manager.delete_task(index)
            except ValueError:
                print("Ошибка: введите число.")
        elif choice == "4":
            try:
                index = int(input("Введите номер задачи для отметки как выполненной: ")) - 1
                task_manager.mark_task_completed(index)
            except ValueError:
                print("Ошибка: введите число.")
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()