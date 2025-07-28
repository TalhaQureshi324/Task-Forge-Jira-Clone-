import uuid
from datetime import datetime
from file_io import write_file_line

def generate_unique_id():
    return str(uuid.uuid4())

def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_activity(activity):
    write_file_line('activity_log.txt', f"{get_current_timestamp()} - {activity}")
