import sys
import os
from tabulate import tabulate

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from logic.user_logic import UserLogic
from logic.vacation_logic import VacationLogic
from logic.like_logic import LikeLogic
from facade.user_facade import UserFacade
from facade.vacation_facade import VacationFacade

class SystemFacade:
    def __init__(self):
        self.user_logic = UserLogic()
        self.vacation_logic = VacationLogic()
        self.like_logic = LikeLogic()
        self.user_facade = UserFacade()
        self.vacation_facade = VacationFacade()

    def register(self):
        """Register a new account."""
        return self.user_facade.add_user()

    def login(self):
        """Login to an existing account."""
        return self.user_facade.login()

    def logout(self):
        """Logout the current user."""
        self.user_facade.logout()

    def like_vacation(self):
        """Like a vacation."""
        if not self.user_facade.current_user:
            print("You must be logged in to like a vacation.")
            return

        vacation_title = input("Enter the title of the vacation to like: ").strip()
        result = self.like_logic.add_like(self.user_facade.current_user["user_id"], vacation_title)
        if result:
            print("Vacation liked successfully!")
        else:
            print("Failed to like vacation. You may have already liked it.")

    def unlike_vacation(self):
        """Unlike a vacation."""
        if not self.user_facade.current_user:
            print("You must be logged in to unlike a vacation.")
            return

        vacation_title = input("Enter the title of the vacation to unlike: ").strip()
        result = self.like_logic.delete_like(self.user_facade.current_user["user_id"], vacation_title)
        if result:
            print("Vacation unliked successfully!")
        else:
            print("Failed to unlike vacation.")

    def view_liked_vacations(self):
    
        if not self.user_facade.current_user:
            print("You must be logged in to view your liked vacations.")
            return

        liked_vacations = self.like_logic.get_all_likes(self.user_facade.current_user["user_id"])

        # Check if there are liked vacations
        if not liked_vacations:
            print("You have not liked any vacations yet.")
            return

        # Prepare data for the table
        table_data = [
            [
                vacation['vacation_id'],
                vacation['vacation_title'],
                vacation['start_date'],
                vacation['end_date'],
                f"${vacation['price']}",
                vacation['total_likes'],
                vacation['img_url'],
                vacation['country']
            ]
            for vacation in liked_vacations
        ]

        # Define table headers
        headers = [
            "ID", "Title", "Start Date", "End Date", 
            "Price", "Total Likes", "Image URL", "Country"
        ]

        # Print the table
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    facade = SystemFacade()
    
    # Test 1: Register a new user
    print("\nTesting Register...")
    facade.register() 
    print("Register test passed!\n")

    # Test 2: Login with a user
    print("Testing Login...")
    facade.login()  
    print("Login test passed!\n")

    # Test 3: Like a vacation (user must be logged in)
    print("Testing Like Vacation...")
    facade.user_facade.current_user = {"user_id": 1}  # Simulate logged-in user
    facade.like_vacation()  
    print("Like Vacation test passed!\n")

    # Test 4: Unlike a vacation (user must be logged in)
    print("Testing Unlike Vacation...")
    facade.unlike_vacation()  
    print("Unlike Vacation test passed!\n")

    # Test 5: View liked vacations (user must be logged in)
    print("Testing View Liked Vacations...")
    facade.view_liked_vacations()  
    print("View Liked Vacations test passed!\n")

    # Test 6: Logout
    print("Testing Logout...")
    facade.logout()  
    print("Logout test passed!\n")

    # Test 7: Invalid action (when not logged in)
    print("Testing Like Vacation without being logged in...")
    facade.user_facade.current_user = None 
    facade.like_vacation()  
    print("Invalid Like Vacation test passed!\n")

    print("Exiting system. Goodbye!")