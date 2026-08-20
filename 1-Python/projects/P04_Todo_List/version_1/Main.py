
# show menu
# Add a task
# View tasks
# Delete a task
# Mark task as completed
# Exit

tasks = ["cooking", "reading"]
complete = " [Complete]"

def menu():
    print("=== To-Do List Manager ===")
    print("1.View tasks")
    print("2. Add a task")
    print("3.Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")




def view_tasks(tasks):
    if not tasks:
        print("There are no tasks yet.")
    else:
        print("-"*20)
        for num, task in enumerate(tasks, start= 1):
            print(f"{num}.{task}")
        print("-"*20)


def  add_task(tasks):
    task = input("Enter a task: ")
    if task:
        tasks.append(task)
        print(f"{task}. Added successfully")
    else:
        print("Task can not be empty")
def mark_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number: ")) -1
        if 0 <= task_number <= len(tasks):
            if complete in tasks[task_number]:
                print("This task already completed.")
            else: 
                tasks[task_number] = tasks[task_number] + complete
                print("marked successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid task number")

    
def delete_task(tasks):
    if not tasks:
        print("No tasks available")
        return
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number: ")) -1
        if 0 <= task_number < len(tasks):
            tasks.pop(task_number)
            print("Task deleted succesfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        menu()
        choice = input("Enter your Choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye. Thanks for using this todo-list manager.")
            break
        else:
            print("Invalid choice.")
    

main()




