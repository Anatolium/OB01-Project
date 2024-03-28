# Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
from datetime import datetime


class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.is_done = False


# Класс для управления задачами
class TaskManager:
    def __init__(self):
        self.tasks = []

    # Функция добавления задачи
    def add_task(self, description, deadline):
        self.tasks.append(Task(description, deadline))

    # Функция отметки задачи как выполненной
    def mark_as_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.is_done = True
                print(f'Задача "{description}" отмечена как выполненная.')
                break
        else:
            print(f'Задача с описанием "{description}" не найдена.')

    # Функция печати списка текущих задач
    def get_current_tasks(self):
        print("Текущие задачи:")
        current_tasks_num = 0
        for task in self.tasks:
            if not task.is_done:
                current_tasks_num += 1
                print(f'{current_tasks_num}. Описание: {task.description}, Срок: {task.deadline}')
        if not current_tasks_num == 0:
            print("Нет текущих задач.")


task_manager = TaskManager()
task_manager.get_current_tasks()

task_manager.add_task("Починить утюг", "2023-04-20")
task_manager.add_task("Помыть машину", "2023-04-25")
task_manager.add_task("Купить продукты", "2023-04-15")
