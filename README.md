# Task Tracker CLI

A simple command-line tool to manage tasks using Python. Tasks are saved in a JSON file, and you can add, update, delete, or mark them as done/in-progress.

## Features
- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as in-progress or done
- List tasks with optional filtering by status

## Requirements
- Python 3.8+

## Usage
```bash
# Add a task
python task_cli.py add "Working on project"

# Update a task
python task_cli.py update 1 "Adding some features in other API project"

# Delete a task
python task_cli.py delete 1

# Mark a task as in-progress
python task_cli.py mark-in-progress 1

# Mark a task as done
python task_cli.py mark-done 1

# List all tasks or filter by status
python task_cli.py list
python task_cli.py list done
