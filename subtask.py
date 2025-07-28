from file_io import append_to_file, read_file_lines
from helpers import generate_unique_id, get_current_timestamp, log_activity

def create_subtask(issue_id, subtask_title):
    subtask_id = generate_unique_id()
    subtask_data = f"{subtask_id}|{issue_id}|{subtask_title}"
    append_to_file("subtasks.txt", subtask_data)
    log_activity(f"Subtask created: {subtask_title} under issue {issue_id}")

def view_subtasks():
    subtasks = read_file_lines("subtasks.txt")
    for subtask in subtasks:
        print(subtask)
