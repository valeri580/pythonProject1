# Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения
# и статус (выполнено/не выполнено). Реализуй функцию для добавления
# задач, отметки выполненных задач и вывода списка текущих
# (не выполненных) задач.

class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, date, period_of_execution, status='не выполнена'):
        new_task = {
            'description': description,
            'date': date,
            'period': period_of_execution,
            'status': status
        }
        self.tasks.append(new_task)
        print(f"Задача добавлена успешно: {description}")

    def close_task(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = "выполнена"
                print(f"Задача выполнена: {description}")
                return
        print(f"Задача не найдена: {description}")

    def show_pending_tasks(self):
        print("\nТекущие задачи:")
        pending = [task for task in self.tasks if task['status'] == 'не выполнена']

        if not pending:
            print("Нет невыполненных задач!")
            return

        for task in pending:
            print(f"- {task['description']} (Создана: {task['date']}, срок в днях: {task['period']})")

