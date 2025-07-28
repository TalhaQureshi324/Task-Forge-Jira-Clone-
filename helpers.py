import uuid
from datetime import datetime

def generate_unique_id():
    return str(uuid.uuid4())

# def generate_unique_id():
#     """
#     Prompts the user for an ID type (prefix) and generates a unique ID by scanning
#     the appropriate file. Assumes ID is the first item per line, separated by comma.
#     """
#     prefix = input("Enter ID type (e.g., ISSUE, USER, PROJECT): ").strip().upper()

#     file_map = {
#         "ISSUE": "issues.txt",
#         "USER": "users.txt",
#         "PROJECT": "projects.txt",
#         "SPRINT": "sprints.txt",
#         "EPIC": "epics.txt",
#         "TIMELOG": "timelogs.txt",
#         "SUBTASK": "subtasks.txt",
#         "NOTIF": "notifications.txt",
#         "WATCHER": "watchers.txt"
#     }

#     filename = file_map.get(prefix)
#     if not filename:
#         print("❌ Invalid prefix or unsupported type.")
#         return None

#     last_id = 0
#     try:
#         with open(filename, 'r') as f:
#             for line in f:
#                 if line.strip():
#                     parts = line.strip().split(",")
#                     if parts[0].startswith(prefix):
#                         num_part = parts[0].replace(f"{prefix}-", "")
#                         if num_part.isdigit():
#                             last_id = max(last_id, int(num_part))
#     except FileNotFoundError:
#         pass

#     next_id = last_id + 1
#     return f"{prefix}-{next_id:03d}"


def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_activity(message):
    timestamp = get_current_timestamp()
    with open("activity_log.txt", "a") as f:
        f.write(f"{timestamp} - {message}\n")
