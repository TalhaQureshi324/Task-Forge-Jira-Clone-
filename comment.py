from file_io import write_file_line, read_file_lines
from utils import get_current_timestamp
import uuid


def add_comment_to_issue(issue_id, commenter, comment):
    timestamp = get_current_timestamp()
    write_file_line('comments.txt', f"{issue_id},{commenter},{comment},{timestamp}")
    print("Comment added.")

def view_comments_for_issue(issue_id):
    comments = read_file_lines('comments.txt')
    for c in comments:
        if c.startswith(issue_id):
            print(c)

def add_comment(issue_id, author_email, comment_text):
    comment_id = str(uuid.uuid4())
    line = f"{comment_id},{issue_id},{author_email},{comment_text}"
    write_file_line("comments.txt", line)
    print("✅ Comment added.")

def view_comments(issue_id):
    comments = read_file_lines("comments.txt")
    print(f"\n💬 Comments for Issue {issue_id}:")
    for line in comments:
        cid, iid, author, text = line.strip().split(",", 3)
        if iid == issue_id:
            print(f"- {author}: {text}")