
# 🚀 Task Forge - JIRA Clone (Console-Based Project in Python)

**Task Forge** is a feature-rich, console-based project management system inspired by Atlassian JIRA. Built using Python, this system supports the full workflow of project planning, issue tracking, sprint management, and more — all backed by simple `.txt` file-based storage, making it lightweight and easy to run anywhere.

---

## 💻 Technologies Used

- 🐍 Python 3.x
- 📄 Plain Text File Storage (No database needed)
- 🧰 Visual Studio Community Edition (Development IDE)

---

## 📁 Project Structure & File Explanations

### 🧠 Core Program Logic

- `main.py` — 🔰 Entry point, displays welcome screen and initializes the program.
- `menu.py` — 📜 Handles navigation and user menu logic.

---

### 📦 Project & Issue Management

- `project.py` / `projects.txt` — 🏗️ Create and manage projects.
- `issue.py` / `issues.txt` — 🐞 Create, update, delete and track issues (bugs, features).
- `subtask.py` / `subtasks.txt` — 🪜 Manage breakdown of tasks (subtasks).
- `epic.py` / `epics.txt` — 🧩 Organize multiple issues under larger epics.
- `sprint.py` / `sprints.txt` — 🏃‍♂️ Plan and manage agile sprints.

---

### 👥 User & Role Management

- `user.py` / `users.txt` — 👤 User creation and basic user data management.
- `role_manager.py` — 🛡️ Role-based permissions (admin, dev, tester etc).

---

### ⏱️ Time Logging & Reporting

- `timelog.py` / `time_logs.txt` — ⏰ Log time spent by users on tasks.
- `timelog_manager.py` — 📊 View and manage time entries.

---

### 👀 Watchers & 🔔 Notifications

- `watcher.py` / `watchers.txt` — 👁️ Add users as watchers on issues.
- `watcher_manager.py` — 🔄 Handle add/remove watchers.
- `notification.py` / `notifications.txt` — 📬 Notify users on changes.
- `notification_manager.py` — 💡 Manages dispatch of notifications.

---

### 🧩 Epic & Sprint Managers

- `epic_manager.py` — 🧠 Manage epics and group issues logically.
- `sprint_manager.py` — ⏳ Manage sprint planning and updates.

---

### 🧱 Subtask Manager

- `subtask_manager.py` — 🧮 Full CRUD for subtasks (create, update, assign, delete).

---

### 🔧 Utility & I/O Helpers

- `utils.py` — 🧰 Shared utility functions.
- `helpers.py` — 🛠️ Data validations, date/time helpers.
- `file_io.py` — 📂 Simplifies reading/writing to `.txt` files.

---

### 📜 Activity & Logging

- `activity_log.txt` — 📝 Records all major user/system actions for tracking.
- `start.txt` — ✨ ASCII splash screen on startup.
- `taskforge.txt` — 🧱 ASCII banner/logo for branding.

---

### ⚙️ Project & Build Metadata

- `.pyproj` — Visual Studio Python project file.
- `.spec` — PyInstaller configuration for generating an executable.

---

## ✅ Key Features

- 🔧 Create/manage projects, issues, and subtasks
- 🧱 Define epics and organize tasks
- 🏃‍♂️ Sprint planning and execution
- ⏱️ Time logs and productivity tracking
- 👥 Role-based access for users
- 👁️ Watchers and change notifications
- 📬 Custom notification system
- 📂 File-based persistent storage
- 🎨 Console-based UI with ASCII graphics

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/TalhaQureshi324/Task-Forge-Jira-Clone-
cd Task-Forge-Jira-Clone-
```

### 2. Run the App
- Open the project in **Visual Studio Community Edition**
- Run `main.py` to launch the Task Forge interface

> ⚠️ Make sure Python 3.x is installed and configured properly.

---

## 🧪 Coming Soon / Future Plans

- Web-based UI using Flask or Django
- User authentication with login/logout
- Export reports to CSV
- GitHub integration for developer tasks

---

## 📣 Follow Me

If you like this project and want to support or stay updated with future releases:

🔗 **GitHub**: [https://github.com/TalhaQureshi324/](https://github.com/TalhaQureshi324/)

📂 **Repo**: [https://github.com/TalhaQureshi324/Task-Forge-Jira-Clone-](https://github.com/TalhaQureshi324/Task-Forge-Jira-Clone-)

👉 _Please give the repo a star ⭐ and follow me for more Python and Dev projects._

---
