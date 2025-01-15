import sys
import os
from tabulate import tabulate

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

import re
from datetime import datetime, date
from logic.country_logic import CountryLogic
from logic.vacation_logic import VacationLogic

class VacationFacade:
    def __init__(self):
        self.params = []
        self.now = date.today()
        self.logic = VacationLogic()
        self.country_logic = CountryLogic()

    def add_vacation(self):
        self.get_title()
        self.get_start_date()
        self.get_end_date()
        self.get_countries_name()
        self.get_price()
        self.get_image()
        

        return self.logic.add_vacation(*self.params)

    def get_title(self):
        while True:
            title = input("Enter title: ").strip()
            if not title.replace(" ", "").isalpha():
                print("Title must contain only letters and spaces")
            elif len(title) < 5:
                print("Title must be at least 5 characters long")
            else:
                self.params.append(title)
                print("Title added")
                break

    def get_countries_name(self):
        while True:
            country_name = input("Enter country name: ").lower()
            if self.country_logic.check_if_country_exist(country_name):
                print("Country added to vacation info!")
                self.params.append(country_name)
                break
            else:
                print(
                    "Country does not exist in database, here is a list of all countries:")
                countries = self.country_logic.get_all_countries()
                print(" | ".join(country["country_name"]
                      for country in countries))

    def get_start_date(self):

        while True:
            try:
                date_str = input("Enter start date (YYYY-MM-DD): ")
                start_date = datetime.strptime(date_str, "%Y-%m-%d").date()

                if start_date < self.now:
                    print("Start date cannot be in the past")
                    continue

                self.params.append(start_date)
                print("Start date added")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD")

    def get_end_date(self):

        while True:
            try:
                date_str = input("Enter end date (YYYY-MM-DD): ")
                end_date = datetime.strptime(date_str, "%Y-%m-%d").date()

                if end_date < self.now:
                    print("End date cannot be in the past")
                    continue

                if end_date <= self.params[-1]:  
                    print("End date must be after start date")
                    continue

                self.params.append(end_date)
                print("End date added")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD")

    def get_price(self):
        while True:
            try:
                price = float(input("Enter price: "))
                if not 1000 <= price <= 10000:
                    print("Price must be between 1000 and 10000")
                else:
                    self.params.append(price)
                    print("Price added")
                    break
            except ValueError:
                print("Price must be a number!")

    def get_image(self):
        while True:
            image_url = input(
                "Enter image URL (optional, press Enter to skip): ").strip()
            if not image_url:
                self.params.append(None)
                print("No image URL selected")
                break

            # Basic URL validation with regular expression
            url_pattern = r'^https?:\/\/[^\s\/$.?#].[^\s]*$'
            if not re.match(url_pattern, image_url):
                print("Invalid URL format!")
                continue

            self.params.append(image_url)
            print("Image URL added")
            break

    def view_all_vacations(self):
        """View all available vacations in a tabular format."""
        
        vacations = self.logic.get_all_vacations()
        
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
            success = self.logic.edit_vacation(vacation_id, **updates)
            if success:
                print(f"Vacation ID {vacation_id} updated successfully!")
            else:
                print(f"Failed to update vacation ID {vacation_id}.")
        else:
            print("No updates provided. Exiting.")
    
    def del_vacation(self):
        vacation_id = input("Enter the ID of the vacation you want to delete: ").strip()
        if not vacation_id.isdigit():
            print("Invalid ID! Please enter a numeric value.")
            return
        vacation_id = int(vacation_id)
        success = self.logic.del_vacation(vacation_id)
        if success:
            print(f"Vacation ID {vacation_id} deleted successfully!")
        else:
            print(f"Failed to delete vacation ID {vacation_id}.")



if __name__ == "__main__":

    vacation = VacationFacade()

    result = vacation.add_vacation()

    print("\nBooking Results:")
    print("---------------")
    print(f"Vacation title: {vacation.params[0]}")
    print(f"Start date: {vacation.params[1]}")
    print(f"End date: {vacation.params[2]}")
    print(f"Country: {vacation.params[3]}")
    print(f"Price: ${vacation.params[4]}")
    print(f"Image URL: {vacation.params[5]}")