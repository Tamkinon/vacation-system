import sys
import os
from tabulate import tabulate

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from logic.user_logic import UserLogic
from logic.vacation_logic import VacationLogic
from logic.like_logic import LikeLogic
from facade.user_facade import UserFacade

class SystemFacade:
    def __init__(self):
        self.user_logic = UserLogic()
        self.vacation_logic = VacationLogic()
        self.like_logic = LikeLogic()
        self.user_facade = UserFacade()

    def register(self):
        """Register a new account."""
        return self.user_facade.add_user()

    def login(self):
        """Login to an existing account."""
        return self.user_facade.login()

    def logout(self):
        """Logout the current user."""
        self.user_facade.logout()


    def view_all_vacations(self):
        """View all available vacations in a tabular format."""
        
        vacations = self.vacation_logic.get_all_vacations()
        
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
            for vacation in vacations
        ]
        
        # Define table headers
        headers = [
            "ID", "Title", "Start Date", "End Date", 
            "Price", "Total Likes", "Image URL", "Country"
        ]
        
        # Print the table
        print(tabulate(table_data, headers=headers, tablefmt="grid"))


    def edit_vacation(self):
        vacation_id = input("Enter the ID of the vacation you want to edit: ").strip()
        if not vacation_id.isdigit():
            print("Invalid ID! Please enter a numeric value.")
            return
        vacation_id = int(vacation_id)
        print("\nAvailable fields to update: vacation_title, price, start_date, end_date")
        print("Enter the fields you want to update and their new values (leave blank to stop).")
        updates = {}
        while True:
            field = input("\nEnter the field to update (or press Enter to finish): ").strip()
            if not field:
                break
            if field not in ["vacation_title", "price", "start_date", "end_date"]:
                print(f"Invalid field: {field}. Please choose a valid field.")
                continue
            value = input(f"Enter the new value for {field}: ").strip()
            if field == "price" and value.replace('.', '', 1).isdigit():
                value = float(value)
            updates[field] = value
        if updates:
            success = self.vacation_logic.edit_vacation(vacation_id, **updates)
            if success:
                print(f"Vacation ID {vacation_id} updated successfully!")
            else:
                print(f"Failed to update vacation ID {vacation_id}.")
        else:
            print("No updates provided. Exiting.")

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
