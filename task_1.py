# Enhanced To-Do List Application

import datetime

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View All Tasks")
    print("2. Add a New Task")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Search Tasks")
    print("6. View Tasks by Category")
    print("7. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']} | Priority: {task['priority']} | Due: {task['due_date']} | Category: {task['category']}")

def add_task(tasks):
    title = input("\nEnter the task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return
    priority = input("Enter task priority (High/Medium/Low): ").strip().capitalize()
    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority. Defaulting to 'Medium'.")
        priority = "Medium"
    due_date = input("Enter the due date (YYYY-MM-DD): ").strip()
    try:
        datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Defaulting to 'No Deadline'.")
        due_date = "No Deadline"
    category = input("Enter task category (e.g., Work, Personal, Study): ").strip().capitalize()
    if not category:
        category = "Uncategorized"
    task = {"title": title, "priority": priority, "due_date": due_date, "category": category}
    tasks.append(task)
    print("Task added successfully!")

def update_task(tasks):
    if not tasks:
        print("\nYour to-do list is empty! Nothing to update.")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            task = tasks[task_num - 1]
            print("\nUpdating Task:", task['title'])
            new_title = input("Enter new title (leave blank to keep current): ").strip()
            new_priority = input("Enter new priority (High/Medium/Low, leave blank to keep current): ").strip().capitalize()
            new_due_date = input("Enter new due date (YYYY-MM-DD, leave blank to keep current): ").strip()
            new_category = input("Enter new category (leave blank to keep current): ").strip().capitalize()

            if new_title:
                task['title'] = new_title
            if new_priority in ["High", "Medium", "Low"]:
                task['priority'] = new_priority
            if new_due_date:
                try:
                    datetime.datetime.strptime(new_due_date, "%Y-%m-%d")
                    task['due_date'] = new_due_date
                except ValueError:
                    print("Invalid date format. Keeping current due date.")
            if new_category:
                task['category'] = new_category

            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    if not tasks:
        print("\nYour to-do list is empty! Nothing to delete.")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['title']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def search_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty! Nothing to search.")
        return
    query = input("\nEnter a keyword to search: ").strip().lower()
    results = [task for task in tasks if query in task['title'].lower() or query in task['category'].lower()]
    if results:
        print("\nSearch Results:")
        for i, task in enumerate(results, 1):
            print(f"{i}. {task['title']} | Priority: {task['priority']} | Due: {task['due_date']} | Category: {task['category']}")
    else:
        print("No tasks matched your search.")

def view_by_category(tasks):
    if not tasks:
        print("\nYour to-do list is empty! No categories to display.")
        return
    categories = set(task['category'] for task in tasks)
    print("\nAvailable Categories:", ", ".join(categories))
    category = input("Enter the category to view tasks: ").strip().capitalize()
    filtered_tasks = [task for task in tasks if task['category'] == category]
    if filtered_tasks:
        print(f"\nTasks in Category '{category}':")
        for i, task in enumerate(filtered_tasks, 1):
            print(f"{i}. {task['title']} | Priority: {task['priority']} | Due: {task['due_date']}")
    else:
        print(f"No tasks found in category '{category}'.")

def main():
    tasks = []
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice (1-7): "))
            if choice == 1:
                view_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                update_task(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                search_tasks(tasks)
            elif choice == 6:
                view_by_category(tasks)
            elif choice == 7:
                print("Exiting the To-Do List application. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
