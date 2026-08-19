# To-Do list manager
# Add a task
# View tasks
# Delete a task
# Mark task as completed


tasks = ["reading", "cooking"]
COMPLETE = " (Complete)"
def menu():
    print("=== To-Do List manager ===")
    print("1.View tasks")
    print("2.Add a task")
    print("3.Mark task as completed")
    print("4.Delete a task")
    print("5.Exit")

def view_tasks(tasks):
    if not tasks:
        print("There are nmo tasks yet.")
    else:
        for num, task in enumerate(tasks, start= 1):
            print(f"{num}:{task}")

def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append[task]

    print("Task added succesfully.")
   

def mark_task(tasks):
    try:
        task_number = int(input("Enter the task number: ")) -1 
        if 0 <= task_number < len(tasks):
            if COMPLETE is tasks[task_number]:
                print("This tasks already marked as a complete.")
            else: 
                tasks[task_number] = tasks[task_number] - COMPLETE
                print("Marked succesfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a Invalid number.")
def delete_task(tasks):
    pass

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thanks for using this task manager. bye")
            break

main()