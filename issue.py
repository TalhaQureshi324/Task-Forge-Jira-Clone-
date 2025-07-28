from file_io import write_file_line, read_file_lines
from utils import generate_unique_id, log_activity
from datetime import datetime
import uuid

# def create_issue(project_name, title, description, assignee):
#     issue_id = generate_unique_id()
#     status = "To Do"
#     line = f"{issue_id},{project_name},{title},{description},{status},{assignee}"
#     write_file_line('issues.txt', line)
#     log_activity(f"Issue created: {issue_id} for {project_name}")
#     print("Issue created with ID:", issue_id)

def create_issue(project, title, desc, assignee, due_date, priority):
    issue_id = str(uuid.uuid4())
    status = "open"
    line = f"{issue_id},{project},{title},{desc},{assignee},{priority},{status},{due_date}"
    write_file_line("issues.txt", line)
    print(f"✅ Issue created with ID: {issue_id}")



def view_overdue_issues():
    today = datetime.today().date()
    issues = read_file_lines("issues.txt")
    print("\n⚠️ Overdue Issues:")
    for line in issues:
        parts = line.strip().split(",")
        if len(parts) < 8:
            continue
        issue_id, proj, title, desc, assign, status, priority, due = parts
        try:
            due_date = datetime.strptime(due, "%Y-%m-%d").date()
            if due_date < today and status.lower() != "closed":
                print(f"{issue_id}: {title} (Due: {due_date})")
        except ValueError:
            continue  


def update_issue_status(issue_id, new_status):
    issues = read_file_lines('issues.txt')
    updated_issues = []
    found = False
    for issue in issues:
        parts = issue.split(',')
        if parts[0] == issue_id:
            parts[4] = new_status
            found = True
        updated_issues.append(','.join(parts))
    if found:
        write_file_line('issues.txt', '\n'.join(updated_issues))
        log_activity(f"Issue {issue_id} updated to {new_status}")

def list_issues_for_user(user_email):
    issues = read_file_lines('issues.txt')
    for i in issues:
        if user_email in i:
            print(i)

def list_issues_by_project(project_name):
    issues = read_file_lines('issues.txt')
    for i in issues:
        if project_name in i:
            print(i)

def search_issues(status=None, assignee=None, priority=None):
    issues = read_file_lines("issues.txt")
    print("\n🔎 Search Results:")
    for line in issues:
        parts = line.strip().split(",")
        if len(parts) < 6:
            continue
        issue_id, proj, title, desc, assign, stat = parts[:6]
        match = (
            (status is None or stat == status) and
            (assignee is None or assign == assignee)
        )
        if match:
            print(f"{issue_id}: {title} (Assigned: {assign}, Status: {stat})")



def show_progress(project_name=None):
    issues = read_file_lines("issues.txt")
    open_count = 0
    closed_count = 0
    for line in issues:
        parts = line.strip().split(",")
        if len(parts) < 6:
            continue
        _, proj, _, _, _, status = parts[:6]
        if project_name is None or proj == project_name:
            if status.lower() == "closed":
                closed_count += 1
            else:
                open_count += 1
    print(f"\n📊 Progress Report for {project_name or 'All Projects'}")
    print(f"Open: {open_count}, Closed: {closed_count}")
    

def add_priority_to_issue(issue_id, priority):
    issues = read_file_lines("issues.txt")
    updated = []
    found = False

    for line in issues:
        parts = line.strip().split(",")
        if parts[0] == issue_id:
            found = True
            if len(parts) == 7:
                parts.insert(5, priority) 
            elif len(parts) == 8:
                parts[5] = priority  
        updated.append(','.join(parts))

    if found:
        with open("issues.txt", "w") as f:
            for line in updated:
                f.write(line + "\n")
        print(f"✅ Priority '{priority}' added to issue {issue_id}")
    else:
        print("❌ Issue ID not found.")


def update_issue_priority(issue_id, new_priority):
    add_priority_to_issue(issue_id, new_priority)  
