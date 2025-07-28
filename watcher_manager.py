from file_io import append_to_file, read_file_lines

def add_watcher(issue_id, user_email):
    line = f"{issue_id}|{user_email}"
    append_to_file("watchers.txt", line)
    print("Watcher added.")

def list_watchers(issue_id):
    lines = read_file_lines("watchers.txt")
    for line in lines:
        parts = line.strip().split("|")
        if parts[0] == issue_id:
            print(f"Watcher: {parts[1]}")