import os
from file_io import append_to_file, read_file_lines
from helpers import generate_unique_id, get_current_timestamp

def create_sprint(project_name, sprint_name, start_date, end_date):
    sprint_id = generate_unique_id()
    line = f"{sprint_id}|{project_name}|{sprint_name}|{start_date}|{end_date}|{get_current_timestamp()}"
    append_to_file("sprints.txt", line)
    print("Sprint created successfully.")

def list_sprints(project_name):
    lines = read_file_lines("sprints.txt")
    for line in lines:
        parts = line.strip().split("|")
        if parts[1] == project_name:
            print(f"ID: {parts[0]}, Name: {parts[2]}, Start: {parts[3]}, End: {parts[4]}")