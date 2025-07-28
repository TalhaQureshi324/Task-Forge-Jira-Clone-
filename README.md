# Task Forge - JIRA Clone (Console-Based Project in Python)

Task Forge is a comprehensive console-based project management system inspired by JIRA. Designed and developed in Python, this project allows users to manage projects, issues, sprints, epics, subtasks, time logs, watchers, roles, and notifications using text-based file storage.

## 💻 Technologies Used
- Python 3.x
- Text File-Based Storage (no database)
- Visual Studio Community Edition (for development)

## 📁 Project Structure & File Explanations

### Core Python Files

- **main.py**: Entry point of the program. Handles splash screen and initialization.
- **menu.py**: Displays user menus, routes user interactions to appropriate modules.

### Project & Issue Management

- **project.py / projects.txt**: Handles project creation and storage.
- **issue.py / issues.txt**: Manages individual issues (tasks, bugs, etc.).
- **subtask.py / subtasks.txt**: Handles subtasks under issues.
- **epic.py / epics.txt**: Organizes issues into larger bodies of work (epics).
- **sprint.py / sprints.txt**: Manages sprint creation and issue assignments.

### User & Role Management

- **user.py / users.txt**: Manages user information and credentials.
- **role_manager.py**: Handles role-based access and permissions.

### Time Logging

- **timelog.py / time_logs.txt**: Logs user time spent on issues.
- **timelog_manager.py**: Facilitates time logging operations and validations.

### Watchers & Notifications

- **watcher.py / watchers.txt**: Enables users to watch issues for updates.
- **watcher_manager.py**: Manages adding/removing watchers and listing them.
- **notification.py / notifications.txt**: Sends notifications when issues are updated.
- **notification_manager.py**: Controls notification logic and broadcasting.

### Epic & Sprint Management

- **epic_manager.py**: Epic creation, editing, and management functions.
- **sprint_manager.py**: Sprint assignment, completion, and status checks.

### Subtask Management

- **subtask_manager.py**: Create, update, assign and delete subtasks.

### Utilities

- **utils.py**: Utility functions shared across modules.
- **helpers.py**: Helper functions like validations and date parsing.
- **file_io.py**: Abstracted file I/O operations to simplify text-based data handling.

### Activity Logging

- **activity_log.txt**: Logs actions such as creation, assignment, updates, deletions.

### ASCII Art Screens

- **start.txt**: ASCII splash screen shown on launch.
- **taskforge.txt**: Branded display of Task Forge name.

## 🧪 Supporting Files

- **Task_forge__JIRA_Clone__Python_Project.pyproj**: Visual Studio project file.
- **Task_forge__JIRA_Clone__Python_Project.spec**: PyInstaller build specification file.

## 🧑‍💻 How to Run

1. Clone the repository:
```bash
git clone https://github.com/TalhaQureshi324/Task-Forge-Jira-Clone-
cd Task-Forge-Jira-Clone-
```

2. Open the project in Visual Studio Community Edition.

3. Run `main.py` to start the console app.

## 🎯 Features Summary

- Project & issue tracking
- Subtasks and Epics
- Sprint planning and progress tracking
- User, role, and access management
- Time logging and overdue detection
- Watchers and notifications
- Persistent data storage in `.txt` files
- Interactive ASCII splash screen

---

## 📣 Follow Me

Please follow me on GitHub for more awesome open-source projects and tools:

**GitHub**: [https://github.com/TalhaQureshi324/](https://github.com/TalhaQureshi324/)

If you'd like to clone this repository:
**Repo Link**: [https://github.com/TalhaQureshi324/Task-Forge-Jira-Clone-](https://github.com/TalhaQureshi324/Task-Forge-Jira-Clone-)
