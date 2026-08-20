
# show menu
# load tasks
# save tasks into file
# Add a task
# View tasks
# Delete a task
# Mark task as completed
# Exit



complete = " [Complete]"
file_name =  "tasks.txt"
def menu():
    print("\n=== To-Do List Manager ===")
    print("1.View tasks")
    print("2. Add a task")
    print("3.Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")

def load_task():
    try:
        with open(file_name, "r") as file:
            if task:
                for num,task in enumerate(file_name , start= 1):
                    print(f"{num}:{task}")
            else:
                print('No tasks available to show.')
    except FileNotFoundError:
        print("This file name does't exist.")
    
def save_task(tasks):
    try:
        with open(file_name, "a") as file:
            for num, task in enumerate(tasks, start= 1):
                file.write(f"{num}: {task}")
                print("Task saved succesfully.")
    except:
        print("Failed to save.")

def view_tasks(tasks):
    load_task()
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
        save_task(tasks)
    else:
        print("Task can not be empty")
def mark_task(tasks):
    view_tasks()
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
    tasks = load_task()
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




