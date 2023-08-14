from task import Task
from task_manager import TaskManager

def print_menu():
    print("\nTask Manager Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def main():
    task_manager = TaskManager()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date (DD-MM-YYYY): ")
            task_manager.do_add_task(title, description, due_date)

        elif choice == "2":
            task_manager.do_view_task()

        elif choice == "3":
            title = input("Enter task title to update: ")
            print("Choose attribute to update:")
            print("1. Title")
            print("2. Description")
            print("3. Due Date")
            print("4. Status")
            attr_choice = input("Enter attribute choice: ")
            new_val = input("Enter new value: ")

            attributes = ["Title", "Description", "Due_date", "Status"]
            if attr_choice in ["1", "2", "3", "4"]:
                attribute = attributes[int(attr_choice) - 1]
                task_manager.do_update_task(title, attribute, new_val)
            else:
                print("Invalid attribute choice")

        elif choice == "4":
            title = input("Enter task title to delete: ")
            task_manager.do_delete_task(title)

        elif choice == "5":
            print("Exiting Task Manager...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
