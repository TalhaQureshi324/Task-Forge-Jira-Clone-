import os
import time
from user import login_user, signup_user
from project import create_project, assign_user_to_project, view_all_projects
from issue import create_issue, update_issue_status, list_issues_by_project, search_issues
from sprint import create_sprint, view_sprints
from epic import create_epic, view_epics
from timelog import add_time_log, view_time_logs
from watcher import add_watcher, view_watchers
from notification import add_notification, view_notifications
from subtask import create_subtask, view_subtasks
from helpers import generate_unique_id, get_current_timestamp, log_activity
from utils import log_activity
from comment import add_comment, view_comments
from issue import show_progress, view_overdue_issues, update_issue_priority, add_priority_to_issue
#from colorama import init, Fore, Back, Style
from colorama import Back, Fore, Style, init
# Initialize colorama
init(autoreset=False)

if os.name == 'nt':
    os.system('color B5')

DARK_BLUE = "\033[34m"
BLACK = "\033[30m"
RESET = "\033[0m"
BOLD = "\033[1m"

TASKFORGE_BANNER = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_start_screen():
    clear()
    if os.path.exists("start.txt"):
        with open("start.txt", "r") as file:
            for line in file:
                if "WELCOME TO" in line:
                    print(f"{DARK_BLUE}{BOLD}{line.rstrip()}{RESET}")
                elif "Initializing" in line:
                    print(f"{Fore.CYAN}{line.rstrip()}{Style.RESET_ALL}")
                else:
                    print(f"{line.rstrip()}")
                time.sleep(0.03)
    else:
        print(f"{DARK_BLUE}Launching Task Forge...{RESET}")
    time.sleep(1.5)
    clear()

def load_taskforge_banner():
    global TASKFORGE_BANNER
    if os.path.exists("taskforge.txt"):
        with open("taskforge.txt", "r") as file:
            for line in file:
                if "Task Forge Console" in line:
                    TASKFORGE_BANNER.append(f"{DARK_BLUE}{BOLD}{line.rstrip()}{RESET}")
                elif "A JIRA-Inspired" in line:
                    TASKFORGE_BANNER.append(f"{Fore.CYAN}{line.rstrip()}{Style.RESET_ALL}")
                else:
                    TASKFORGE_BANNER.append(f"{line.rstrip()}")
    else:
        TASKFORGE_BANNER = [f"{BLACK}Task Forge Console - JIRA Clone{RESET}"]
                 
               
                    
               
def print_taskforge_banner():
    for line in TASKFORGE_BANNER:
        print(line)
    print("-" * 80)

def main_menu():
    clear()
    print_taskforge_banner()

    print("\n📌 Welcome to JIRA Clone Console")
    print("1. Login")
    print("2. Sign Up")
    print("0. Exit")

    choice = input("Select option: ")
    if choice == '1':
        email = input("Email: ")
        password = input("Password: ")
        if login_user(email, password):
            role = login_user(email, password)
            dashboard(email, role)
        else:
            print("Invalid login.")
    elif choice == '2':
        signup_user()
    elif choice == '0':
        exit()
    else:
        print("Invalid choice.")

def dashboard(email, role):
    while True:
        clear()
        print_taskforge_banner()
        print(f"\nWelcome, {email} [{role}]")
        print("\n🛠️ Main Dashboard")
        print("1. Create Project")
        print("2. Assign User to Project")
        print("3. View All Projects")
        print("4. Create Issue")
        print("5. Update Issue Status")
        print("6. View Issues by Project")
        print("7. Create Sprint")
        print("8. View Sprints")
        print("9. Create Epic")
        print("10. View Epics")
        print("11. Add Time Log")
        print("12. View Time Logs")
        print("13. Add Watcher")
        print("14. View Watchers")
        print("15. Add Notification")
        print("16. View Notifications")
        print("17. Create Subtask")
        print("18. View Subtasks")
        print("19. Add Comment to Issue")
        print("20. View Comments on Issue")
        print("21. Add Priority to Issue")
        print("22. Update Issue Priority")
        print("23. Search Issues")
        print("24. View Progress Report")
        print("25. View Overdue Issues")
        print("0. Logout")

        choice = input("Choose option: ")

        if choice == '1':
            pname = input("Project name: ")
            create_project(pname, email)
        elif choice == '2':
            pname = input("Project name: ")
            uemail = input("User email to assign: ")
            assign_user_to_project(pname, uemail)
        elif choice == '3':
            view_all_projects()
        elif choice == '4':
            pname = input("Project name: ")
            title = input("Issue title: ")
            desc = input("Description: ")
            assignee = input("Assign to: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            priority = input("Priority (High/Medium/Low): ")
            create_issue(pname, title, desc, assignee, due_date, priority)
        elif choice == '5':
            iid = input("Issue ID: ")
            new_status = input("New Status: ") 
            update_issue_status(iid, new_status)
        elif choice == '6':
            pname = input("Project name: ")
            list_issues_by_project(pname)
        elif choice == '7':
            pname = input("Project name: ")
            sprint_name = input("Sprint name: ")
            create_sprint(pname, sprint_name)
        elif choice == '8':
            view_sprints()
        elif choice == '9':
            pname = input("Project name: ")
            epic_title = input("Epic title: ")
            create_epic(pname, epic_title)
        elif choice == '10':
            view_epics()
        elif choice == '11':
            iid = input("Issue ID: ")
            hours = input("Hours logged: ")
            add_time_log(email, iid, hours)
        elif choice == '12':
            view_time_logs(email)
        elif choice == '13':
            iid = input("Issue ID: ")
            add_watcher(email, iid)
        elif choice == '14':
            view_watchers()
        elif choice == '15':
            msg = input("Notification message: ")
            add_notification(email, msg)
        elif choice == '16':
            view_notifications(email)
        elif choice == '17':
            iid = input("Parent Issue ID: ")
            title = input("Subtask title: ")
            create_subtask(iid, title)
        elif choice == '18':
            view_subtasks()
        elif choice == '19':
            iid = input("Issue ID: ")
            text = input("Comment: ")
            add_comment(iid, email, text)
        elif choice == '20':
            iid = input("Issue ID: ")
            view_comments(iid)
        elif choice == "21":
            issue_id = input("Enter Issue ID: ")
            priority = input("Enter priority (High/Medium/Low): ")
            add_priority_to_issue(issue_id, priority)
        elif choice == "22":
            issue_id = input("Enter Issue ID to update priority: ")
            new_priority = input("Enter new priority (High/Medium/Low): ")
            update_issue_priority(issue_id, new_priority)
        elif choice == '23':
            s = input("Status (or leave blank): ")
            a = input("Assignee email (or leave blank): ")
            s = s if s else None
            a = a if a else None
            search_issues(s, a)
        elif choice == '24':
            pname = input("Project name (or leave blank for all): ")
            pname = pname if pname else None
            show_progress(pname)
        elif choice == '25':
            view_overdue_issues()
        elif choice == '0':
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    show_start_screen()
    load_taskforge_banner()
    while True:
        main_menu()
