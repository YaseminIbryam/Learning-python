to_do_list = []


def add_new_task():
    task_description = input("Enter the task description: ")
    completed_status = False
    task = [task_description, completed_status]
    to_do_list.append(task)
    print(f"Task {task_description} added successfully")


def view_all_tasks():
    for task in to_do_list:
        print(f"Index - {to_do_list.index(task)}, Description - {task[0]}, Completed status - {task[1]}")


def mark_a_task_as_completed():
    view_all_tasks()
    completed_task_index = int(input("Enter the index of the completed task: "))
    to_do_list[completed_task_index][1] = True


def quit_program():
    print("Goodbye!")
    exit()


while True:
    print("Main Menu")
    print("Select what to do.\n1.Add new task\n2.Mark task as completed\n3.View all tasks\n4.Quit the program")
    while True:
        task_number = input("Enter the number: ")
        if task_number not in ["1", "2", "3", "4"]:
            print("Enter a valid number!")
        else:
            break
    match task_number:
        case "1":
            add_new_task()
        case "2":
            mark_a_task_as_completed()
        case "3":
            view_all_tasks()
        case "4":
            quit_program()