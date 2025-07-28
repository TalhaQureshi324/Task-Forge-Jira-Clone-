from file_io import read_file_lines, write_file_line
from utils import log_activity

def user_exists(email):
    users = read_file_lines('users.txt')
    return any(email == u.split(',')[0] for u in users)

def login_user(email, password):
    try:
        with open("users.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue  # skip bad lines
                u_email, u_pass, role = parts
                if u_email == email and u_pass == password:
                    return role
    except FileNotFoundError:
        print("User database not found.")
    return None


def signup_user():
    print("\n🔐 Sign Up")
    email = input("Email: ")
    password = input("Password: ")
    role = input("Role (e.g., admin, user): ")

    try:
        with open("users.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 1 and parts[0] == email:
                    print("A user with this email already exists.")
                    return
    except FileNotFoundError:
        pass  

    with open("users.txt", "a") as f:
        f.write(f"{email},{password},{role}\n")

    print("Signup successful! You can now login.")


def view_all_users():
    users = read_file_lines('users.txt')
    for u in users:
        print(u)
