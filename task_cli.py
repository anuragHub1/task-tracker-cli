import sys
import json
import os 
from datetime import datetime

FILE_NAME="tasks.json"

def load_task():
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

