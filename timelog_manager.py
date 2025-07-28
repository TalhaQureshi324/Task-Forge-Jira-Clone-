from file_io import append_to_file, read_file_lines
from helpers import generate_unique_id, get_current_timestamp

def log_time(issue_id, user_email, hours, description):
    log_id = generate_unique_id()
    line = f"{log_id}|{issue_id}|{user_email}|{hours}|{description}|{get_current_timestamp()}"
    append_to_file("timelogs.txt", line)
    print("Time log added.")

def view_timelogs(issue_id):
    lines = read_file_lines("timelogs.txt")
    for line in lines:
        parts = line.strip().split("|")
        if parts[1] == issue_id:
            print(f"User: {parts[2]}, Hours: {parts[3]}, Desc: {parts[4]}, Timestamp: {parts[5]}")