import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from logic.user_logic import UserLogic
from logic.vacation_logic import VacationLogic
from logic.like_logic import LikeLogic

class SystemFacade:
    def __init__(self):
        self.user_logic = UserLogic()
        self.vacation_logic = VacationLogic()
        self.like_logic = LikeLogic()
        self.current_user = None 

    def register(self):
        """Register a new account."""
        firstname = input("Enter first name: ").strip()
        lastname = input("Enter last name: ").strip()
        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()
        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ").strip()
        role = input("Enter role (1 - User / 2 - Admin): ").strip()

        self.current_user = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "password": password,
            "date_of_birth": date_of_birth,
            "role": int(role)
        }

        signin = self.user_logic.check_valid_signup(self.current_user['email'])
        if signin: 
            print(f"Registration successful! Your user ID is {self.current_user['id']}.")
        else:
            print("Registration failed. Please try again.")

    def login(self):
        """Login to an existing account."""
        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()

        login = self.user_logic.check_valid_login(email, password)
        if login:
            self.current_user = {
                "user_id": self.current_user['user_id'], 
                "firstname": self.current_user['firstname'],
                "lastname": self.current_user['lastname'],
                "email": self.current_user['email'],
                "role": self.current_user['role']
            }
            print(f"Welcome, {self.current_user['firstname']}! Your user ID is {self.current_user['user_id']}.")
        else:
            print("Login failed. Check your credentials.")

    def logout(self):
        """Logout the current user."""
        if self.current_user:
            print(f"Goodbye, {self.current_user['firstname']} (ID: {self.current_user['user_id']})!")
            self.current_user = None
        else:
            print("No user is currently logged in.")

    def view_all_vacations(self):
        """View all available vacations."""
        
        vacations = self.vacation_logic.get_all_vacations()
        for vacation in vacations:
            print(
                f"ID: {vacation['vacation_id']}, "
                f"Title: {vacation['vacation_title']}, "
                f"Start date: {vacation['start_date']}, "
                f"End date: {vacation['end_date']}, "
                f"Price: ${vacation['price']}, "
                f"Total likes: {vacation['total_likes']}, "
                f"Image: {vacation['img_url']}, "
                f"Country: {vacation['country']}"
            )

    def like_vacation(self):
        """Like a vacation."""
        if not self.current_user:
            print("You must be logged in to like a vacation.")
            return

        vacation_title = input("Enter the title of the vacation to like: ").strip()
        result = self.like_logic.add_like(self.current_user["user_id"], vacation_title)
        if result:
            print("Vacation liked successfully!")
        else:
            print("Failed to like vacation. You may have already liked it.")

    def unlike_vacation(self):
        """Unlike a vacation."""
        if not self.current_user:
            print("You must be logged in to unlike a vacation.")
            return

        vacation_title = input("Enter the title of the vacation to unlike: ").strip()
        result = self.like_logic.delete_like(self.current_user["user_id"], vacation_title)
        if result:
            print("Vacation unliked successfully!")
        else:
            print("Failed to unlike vacation.")

    def view_liked_vacations(self):
        """View vacations liked by the current user."""
        if not self.current_user:
            print("You must be logged in to view your liked vacations.")
            return

        liked_vacations = self.like_logic.get_all_likes(self.current_user["user_id"])
        for vacation in liked_vacations:
            print(
                f"ID: {vacation['vacation_id']}, "
                f"Title: {vacation['vacation_title']}, "
                f"Start date: {vacation['start_date']}, "
                f"End date: {vacation['end_date']}, "
                f"Price: ${vacation['price']}, "
                f"Total likes: {vacation['total_likes']}, "
                f"Image: {vacation['img_url']}, "
                f"Country: {vacation['country']}"
            )


if __name__ == "__main__":
    facade = SystemFacade()

    while True:
        print("\nOptions:")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. View All Vacations")
        print("5. Like a Vacation")
        print("6. Unlike a Vacation")
        print("7. View Liked Vacations")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            facade.register()
        elif choice == "2":
            facade.login()
        elif choice == "3":
            facade.logout()
        elif choice == "4":
            facade.view_all_vacations()
        elif choice == "5":
            facade.like_vacation()
        elif choice == "6":
            facade.unlike_vacation()
        elif choice == "7":
            facade.view_liked_vacations()
        elif choice == "8":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
