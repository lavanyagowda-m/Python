

tasks = ["yoga","healthy breakfast","shopping"]

def display_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_tasks():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_tasks():
     task=input("enter the task:")
     if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed")
     else:
         print(f"Task '{task}'not found")
        

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_tasks()
        elif choice == '3':
             remove_tasks()
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
