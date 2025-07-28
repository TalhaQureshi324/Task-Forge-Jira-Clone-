from file_io import append_to_file, read_file_lines
from helpers import generate_unique_id, get_current_timestamp, log_activity

def create_sprint(project_name, sprint_name):
    # Generating unique sprint ID
    sprint_id = generate_unique_id()
    sprint_data = f"{sprint_id}|{project_name}|{sprint_name}"
    append_to_file("sprints.txt", sprint_data)
    log_activity(f"Sprint created: {sprint_name} under project {project_name}")

def view_sprints():
    sprints = read_file_lines("sprints.txt")
    for sprint in sprints:
        print(sprint)
