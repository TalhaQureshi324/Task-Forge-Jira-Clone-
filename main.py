# # main.py

# from menu import login_user, signup_user, dashboard

# def main_menu():
#     while True:
#         print("\n Welcome to JIRA Clone Console")
#         print("1. Login")
#         print("2. Sign Up")
#         print("0. Exit")

#         choice = input("Select option: ")
#         if choice == '1':
#             email = input("Email: ")
#             password = input("Password: ")
#             role = login_user(email, password)
#             if role:
#                 dashboard(email, role)
#             else:
#                 print(" Invalid login.")
#         elif choice == '2':
#             signup_user()
#         elif choice == '0':
#             print(" Exiting...")
#             break
#         else:
#             print(" Invalid choice.")

# if __name__ == "__main__":
#     try:
#         main_menu()
#     except Exception as e:
#         print(f" Unexpected Error: {e}")
#         input("Press Enter to exit...")
