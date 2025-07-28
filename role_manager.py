from file_io import append_to_file, read_file_lines

def set_user_role(user_email, role):
    line = f"{user_email}|{role}"
    append_to_file("roles.txt", line)
    print("Role set.")

def get_user_role(user_email):
    lines = read_file_lines("roles.txt")
    for line in lines:
        parts = line.strip().split("|")
        if parts[0] == user_email:
            return parts[1]
    return "user"