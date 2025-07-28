from file_io import append_to_file, read_file_lines
from helpers import generate_unique_id, get_current_timestamp, log_activity

def add_notification(user_email, message):
    notification_data = f"{user_email}|{message}|{get_current_timestamp()}"
    append_to_file("notifications.txt", notification_data)
    log_activity(f"Notification added for {user_email}: {message}")

def view_notifications(user_email):
    notifications = read_file_lines("notifications.txt")
    for notification in notifications:
        if user_email in notification:
            print(notification)
