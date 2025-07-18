import csv
import os

def main():
    choice = input("Add Task | Update Task | All Tasks | Completed Tasks | In Progress Tasks | Todo Tasks | Delete Tasks:   ").strip().lower()
    if choice == "add task":
        add_task()
    elif choice == "update task":
        update_task()
    elif choice == "all tasks":
        all_tasks()
    elif choice == "completed tasks":
        completed_tasks()
    elif choice == "in progress tasks":
        in_progress_tasks()
    elif choice == "todo tasks":
        todo_tasks()
    elif choice == "delete tasks":
        delete_tasks()
    else:
        print("Invalid Action")


def add_task():
    
    new_task = input("Task name: ").strip().lower()
    new_task_description = input("Enter a description: ").strip().lower()
    new_task_status = input("In progress | Todo | Completed: ").strip().lower()

    file_empty = not os.path.exists("task.csv") or os.stat("task.csv").st_size == 0

    with open('task.csv', 'a', newline='') as csvfile:
        fieldnames = ['task_name','description','status']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

        if file_empty:
            writer.writeheader()
        writer.writerow({'task_name': new_task, 'description': new_task_description, 'status': new_task_status})

def update_task():
    task_number = int(input("Input task # of the task you want to edit: ").strip().lower())
    task_part = input("name | description | status ").strip().lower()
    new_value = input(f" Enter new value for {task_part}: ")
    
    with open('task.csv','r',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        tasks = list(reader)

        index = task_number -1
        if 0<= index < len(tasks):
            if task_part == "name":
                tasks[index]['task_name'] = new_value
            elif task_part == "description":
                tasks[index]['description'] = new_value
            elif task_part == 'status':
                tasks[index]['status'] = new_value
            else:
                print("Invalid input")
                return
        else:
            print("Task not Found")
            return
        with open('task.csv', 'w', newline = '') as csvfile:
            fieldnames = ['task_name','description','status']
            writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(tasks)         

def all_tasks():
    with open('task.csv','r',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        tasks = list(reader)
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task_name']} - {task['description']} ({task['status']})")
def completed_tasks():
    with open('task.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        tasks = list(reader)
        found = False
        for i, task in enumerate(tasks, start=1):
            if task['status'].strip().lower() == "completed":
                print(f"{i}. {task['task_name']} - {task['description']} ({task['status']})")
                found = True
        if not found:
            print("No completed tasks found")

def in_progress_tasks():
    with open('task.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        tasks = list(reader)
        found = False
        for i, task in enumerate(tasks, start=1):
            if task['status'].strip().lower() == "in progress":
                print(f"{i}. {task['task_name']} - {task['description']} ({task['status']})")
                found = True
        if not found:
            print("No in progress tasks found")
def todo_tasks():
    with open('task.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        tasks = list(reader)
        found = False
        for i, task in enumerate(tasks, start=1):
            if task['status'].strip().lower() == "todo":
                print(f"{i}. {task['task_name']} - {task['description']} ({task['status']})")
                found = True
        if not found:
            print("No todo tasks found")
def delete_tasks():
    task_number = int(input("Input task # of the task you want to delete: "))

    
    with open('task.csv','r',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        tasks = list(reader)

        index = task_number -1
        if 0<= index < len(tasks):
           del tasks[index] 
        else:
            print("Task not Found")
            return
        with open('task.csv', 'w', newline = '') as csvfile:
            fieldnames = ['task_name','description','status']
            writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(tasks)
    
if __name__ == "__main__":
    main()