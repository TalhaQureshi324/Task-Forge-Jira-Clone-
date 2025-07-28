from file_io import append_to_file, read_file_lines
from helpers import generate_unique_id, get_current_timestamp, log_activity

def add_time_log(user_email, issue_id, hours):
    # Generating unique time log ID
    time_log_id = generate_unique_id()
    time_log_data = f"{time_log_id}|{user_email}|{issue_id}|{hours}|{get_current_timestamp()}"
    append_to_file("time_logs.txt", time_log_data)
    log_activity(f"Time log added: {hours} hours for issue {issue_id} by {user_email}")

def view_time_logs(user_email):
    time_logs = read_file_lines("time_logs.txt")
    for log in time_logs:
        if user_email in log:
            print(log)
