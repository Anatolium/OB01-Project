from datetime import datetime


class Task:
    def __init__(self, description, deadline):
        self.number = 0
        self.description = description
        self.deadline = deadline
        self.is_done = False


# Класс для управления задачами
class TaskManager:
    def __init__(self):
        self.tasks = []

    # Функция добавления задачи
    def add_task(self):
        description = input('    Введите текст новой задачи: ')
        deadline = input('    Введите срок в формате dd-mm-yyyy: ')
        try:
            date_obj = datetime.strptime(deadline, "%d-%m-%Y")
        except ValueError:
            print("---- Ошибка ввода даты. Задача не добавлена ----")
            return None
        if date_obj < datetime.now():
            print("---- Этот день уже прошёл. Задача не добавлена ----")
            return
        self.tasks.append(Task(description, deadline))
        print(f"**** Задача '{description}' успешно добавлена ****")

    # Вспомогательная функция добавления задачи
    def add_demo_task(self, description, due_date):
        self.tasks.append(Task(description, due_date))

    # Функция удаления задачи
    def del_task(self):
        input_str = input("    Введите номер задачи для удаления: ")
        try:
            input_number = int(input_str)
        except:
            print(f"---- Ошибка ввода номера задачи {input_str} ----")
        else:
            for index, task in enumerate(self.tasks):
                if task.number == input_number:
                    print(f"**** Задача '{task.description}' успешно удалена ****")
                    self.tasks.pop(index)
                    return
            print(f"---- Задачи с номером {input_number} нет в списке----")

    # Функция изменения статуса задачи
    def set_task_done(self):
        input_str = input("    Введите номер задачи для изменения статуса: ")
        try:
            input_number = int(input_str)
        except:
            print(f"---- Ошибка ввода номера задачи {input_str} ----")
            return

        for task in self.tasks:
            if task.number == input_number:
                task.is_done = False if task.is_done else True
                return
        print(f"---- Задачи с номером {input_str} нет в списке----")


    # Функция печати списка текущих задач
    def get_current_tasks(self):
        print("\nТекущие задачи:")
        if len(self.tasks) == 0:
            print("Нет текущих задач.")
            return False
        sorted_task_list = sorted(self.tasks, key=lambda x: x.number)
        for index, task in enumerate(sorted_task_list, 1):
            description = task.description.ljust(30)[:30]
            deadline = task.deadline.ljust(20)[:20]
            status = "Выполнена" if task.is_done else ""
            print(f"{index}. {description}Срок: {deadline}{status}")
        return True

    # Функция пересчёта номеров задач по сроку выполнения
    def renumber_task_list(self):
        sorted_task_list = sorted(self.tasks, key=lambda x: x.deadline)
        for index, task in enumerate(sorted_task_list, 1):
            task.number = index


task_manager = TaskManager()

task_manager.add_demo_task("Починить лампу", "04-04-2024")
task_manager.add_demo_task("Оплатить интернет", "01-04-2024")
task_manager.add_demo_task("Внести платёж по кредиту", "08-04-2024")
task_manager.add_demo_task("Купить продукты", "05-04-2024")
task_manager.add_demo_task("Записаться на медосмотр", "10-04-2024")

task_manager.renumber_task_list()

while True:
    if task_manager.get_current_tasks():
        choice = input(
            '\n1 – Добавить задачу\n2 – Изменить статус\n3 – Удалить задачу\nДр.клавиша – выход\nВведите пункт: ')
    else:
        choice = input('\n1 – Добавить задачу\nДр.клавиша – выход\nВведите пункт: ')
        if not choice == "1":
            break

    match choice:
        case "1":
            task_manager.add_task()
            task_manager.renumber_task_list()
        case "2":
            task_manager.set_task_done()
        case "3":
            task_manager.del_task()
            task_manager.renumber_task_list()
        case _:
            break
