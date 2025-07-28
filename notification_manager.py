from file_io import append_to_file, read_file_lines
from helpers import generate_unique_id, get_current_timestamp

def send_notification(user_email, message):
    notification_id = generate_unique_id()
    line = f"{notification_id}|{user_email}|{message}|{get_current_timestamp()}"
    append_to_file("notifications.txt", line)

def view_notifications(user_email):
    lines = read_file_lines("notifications.txt")
    for line in lines:
        parts = line.strip().split("|")
        if parts[1] == user_email:
            print(f"Message: {parts[2]}, Sent: {parts[3]}")