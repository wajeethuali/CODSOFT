# Initialize an empty list to store tasks
codsoft_task1_todolist = []

# Function to display the menu options
def display_menu():
    print("\n--- To-Do List For Planning a Vacation Trip  ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")

# Function to add a task
def add_task():
    task = input("Enter the task: ")
    codsoft_task1_todolist.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")




# Function to view tasks
def view_codsoft_task1_todolist():
    if not codsoft_task1_todolist:
        print("No tasks in the list.")
        return
    print("\n--- Your Tasks ---")
    for i, item in enumerate(codsoft_task1_todolist):
        status = "Done" if item["completed"] else "Pending"
        print(f"{i + 1}. {item['task']} [{status}]")

# Function to mark a task as done
def mark_task_as_done():
    view_codsoft_task1_todolist()
    if not codsoft_task1_todolist:
        return
    try:
        task_num = int(input("Enter the number of the task to mark as done: ")) - 1
        if 0 <= task_num < len(codsoft_task1_todolist):
            codsoft_task1_todolist[task_num]["completed"] = True
            print(f"Task '{codsoft_task1_todolist[task_num]['task']}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to remove a task
def remove_task():
    view_codsoft_task1_todolist()
    if not codsoft_task1_todolist:
        return
    try:
        task_num = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_num < len(codsoft_task1_todolist):
            removed_task = codsoft_task1_todolist.pop(task_num)
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_codsoft_task1_todolist()
    elif choice == '3':
        mark_task_as_done()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")