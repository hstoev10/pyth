tasks = []

def display_tasks():
    if not tasks:
        print("Няма текущи задачи.")
        return

    print("Текущи задачи:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def add_task():
    new_task = input("Въведете нова задача: ")
    tasks.append(new_task)
    print(f"Задачата '{new_task}' беше добавена успешно.")

def edit_task():
    display_tasks()
    try:
        index = int(input("Изберете индекс на задача за промяна: ")) - 1
        if 0 <= index < len(tasks):
            new_title = input("Въведете ново заглавие за задачата: ")
            tasks[index] = new_title
            print(f"Задачата с индекс {index + 1} беше успешно променена на '{new_title}'.")
        else:
            print("Невалиден индекс.")
    except ValueError:
        print("Моля, въведете валиден индекс.")

def swap_tasks():
    display_tasks()
    try:
        index1 = int(input("Изберете индекс на първата задача за размяна: ")) - 1
        index2 = int(input("Изберете индекс на втората задача за размяна: ")) - 1

        if 0 <= index1 < len(tasks) and 0 <= index2 < len(tasks):
            tasks[index1], tasks[index2] = tasks[index2], tasks[index1]
            print(f"Задачите с индекси {index1 + 1} и {index2 + 1} бяха успешно разменени.")
        else:
            print("Невалиден индекс.")
    except ValueError:
        print("Моля, въведете валиден индекс.")

def delete_task():
    display_tasks()
    task_to_delete = input("Въведете заглавие или индекс на задача за изтриване: ")

    for task in tasks:
        if task_to_delete.lower() in task.lower() or task_to_delete.isdigit() and int(task_to_delete) == tasks.index(task) + 1:
            tasks.remove(task)
            print(f"Задачата '{task}' беше успешно изтрита.")
            return

    print(f"Задача с заглавие '{task_to_delete}' не беше намерена.")

while True:
    print("\nИзберете действие:")
    print("1. Добавяне на задача")
    print("2. Преглеждане на задачи")
    print("3. Промяна на заглавие на задача")
    print("4. Пренареждане на две задачи по индекс")
    print("5. Изтриване на задача")
    print("6. Изход")

    choice = input("Ваш избор: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        edit_task()
    elif choice == "4":
        swap_tasks()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("Довиждане!")
        break
    else:
        print("Невалиден избор. Моля, опитайте отново.")
