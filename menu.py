from user import login_user, signup_user
from project import create_project, assign_user_to_project, view_all_projects
from issue import create_issue, update_issue_status, list_issues_by_project
from sprint import create_sprint, view_sprints
from epic import create_epic, view_epics
from timelog import add_time_log, view_time_logs
from watcher import add_watcher, view_watchers
from notification import add_notification, view_notifications
from subtask import create_subtask, view_subtasks
from helpers import generate_unique_id, get_current_timestamp, log_activity
from utils import log_activity

def main_menu():

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
    print(f"\nWelcome, {email} [{role}]")
    while True:
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
            create_issue(pname, title, desc, assignee)
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
        elif choice == '0':
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    while True:
        main_menu()
