from file_io import read_file_lines, write_file_line
from utils import log_activity

def create_project(project_name, created_by):
    write_file_line('projects.txt', f"{project_name},{created_by}")
    log_activity(f"Project created: {project_name} by {created_by}")

def assign_user_to_project(project_name, user_email):
    write_file_line('projects.txt', f"{project_name},{user_email}")
    log_activity(f"{user_email} assigned to project {project_name}")

def view_projects_for_user(user_email):
    projects = read_file_lines('projects.txt')
    for project in projects:
        name, email = project.split(',')
        if email == user_email:
            print(f"Project: {name}")

def view_all_projects():
    projects = read_file_lines('projects.txt')
    for p in projects:
        print(p)
