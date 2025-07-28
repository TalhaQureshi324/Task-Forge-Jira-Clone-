from file_io import append_to_file, read_file_lines
from helpers import generate_unique_id, get_current_timestamp, log_activity

def add_watcher(user_email, issue_id):
    watcher_data = f"{user_email}|{issue_id}"
    append_to_file("watchers.txt", watcher_data)
    log_activity(f"Watcher added: {user_email} is now watching issue {issue_id}")

def view_watchers():
    watchers = read_file_lines("watchers.txt")
    for watcher in watchers:
        print(watcher)
