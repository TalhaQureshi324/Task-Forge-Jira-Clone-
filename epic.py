from file_io import append_to_file, read_file_lines
from helpers import generate_unique_id, get_current_timestamp, log_activity

def create_epic(project_name, epic_title):
    # Generating unique epic ID (you can change this logic as per your need)
    epic_id = generate_unique_id()
    epic_data = f"{epic_id}|{project_name}|{epic_title}"
    append_to_file("epics.txt", epic_data)
    log_activity(f"Epic created: {epic_title} under project {project_name}")

def view_epics():
    epics = read_file_lines("epics.txt")
    for epic in epics:
        print(epic)
