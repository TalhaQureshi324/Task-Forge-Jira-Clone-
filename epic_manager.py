import os
from file_io import append_to_file, read_file_lines
from helpers import generate_unique_id, get_current_timestamp

def create_epic(project_name, title, description):
    epic_id = generate_unique_id()
    line = f"{epic_id}|{project_name}|{title}|{description}|{get_current_timestamp()}"
    append_to_file("epics.txt", line)
    print("Epic created successfully.")

def list_epics(project_name):
    lines = read_file_lines("epics.txt")
    for line in lines:
        parts = line.strip().split("|")
        if parts[1] == project_name:
            print(f"ID: {parts[0]}, Title: {parts[2]}, Description: {parts[3]}")