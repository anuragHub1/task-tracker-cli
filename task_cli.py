import sys
import json
import os 
from datetime import datetime

FILE_NAME="tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME,'w') as f:
            json.dump([],f)
    with open(FILE_NAME,'r') as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f, indent=4)

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def add_task(description):
    tasks = load_tasks()
    task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task['id']})")

def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully!")
            return
    print("Task not found!")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print("Task not found!")
        return
    save_tasks(new_tasks)
    print(f"Task {task_id} deleted successfully!")

def mark_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}.")
            return
    print("Task not found!")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [t for t in tasks if t["status"] == filter_status]
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"{task['id']}. [{task['status']}] {task['description']}")


def show_help():
    print("""
Usage:
  python task-cli.py add "Task description"
  python task-cli.py update <id> "New description"
  python task-cli.py delete <id>
  python task-cli.py mark-in-progress <id>
  python task-cli.py mark-done <id>
  python task-cli.py list [todo|in-progress|done]
""")
    
def main():
    
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]
    tasks = load_tasks()

    if command == "add":
        if len(sys.argv) < 3:
            print("Missing task description.")
        else:
            add_task(sys.argv[2])

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: task-cli update <id> 'new description'")
        else:
            update_task(int(sys.argv[2]), sys.argv[3])

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: task-cli delete <id>")
        else:
            delete_task(int(sys.argv[2]))

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-in-progress <id>")
        else:
            mark_status(int(sys.argv[2]), "in-progress")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-done <id>")
        else:
            mark_status(int(sys.argv[2]), "done")

    elif command == "list":
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()

    else:
        show_help()

if __name__ == "__main__":
    main()