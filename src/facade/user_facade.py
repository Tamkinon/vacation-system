import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

import re
from datetime import datetime, date
from logic.user_logic import UserLogic

class UserFacade:
    def __init__(self):
        self.now = date.today()
        self.logic = UserLogic()
        self.current_user = None

    def add_user(self):
        firstname = self.get_firstname()
        lastname = self.get_lastname()
        email = self.get_email()
        password = self.get_password()
        date_of_birth = self.get_date_of_birth()

        signup = self.logic.check_valid_signup(email)
        if signup:
            result = self.logic.add_user(firstname, lastname, email, password, date_of_birth)
            self.current_user = self.logic.get_user_by_email(email)
            print(f"Registration successful! Your user ID is {self.current_user['user_id']}.")
        else:
            result = False
            print("Email already exists. Please try again.")
        return result
    
    def login(self):
        email = self.get_email()
        password = self.get_password()

        login = self.logic.check_valid_login(email, password)
        if login:
            self.current_user = self.logic.get_user_by_email(email)
            print(f"Welcome, {self.current_user['firstname']}! Your user ID is {self.current_user['user_id']}.")
        else:
            print("Login failed. Check your credentials.")
    
    def logout(self):
        if self.current_user:
            print(f"Goodbye, {self.current_user['firstname']} (ID: {self.user_facade.current_user['user_id']})!")
            self.current_user = None
        else:
            print("No user is currently logged in.")

    def get_firstname(self):
        while True:
            firstname = input("Enter first name: ").strip()
            if not firstname.isalpha():
                print("First name must contain only letters")
            else:
                print("First name added")
                return firstname
    
    def get_lastname(self):
        while True:
            lastname = input("Enter last name: ").strip()
            if not lastname.isalpha():
                print("Last name must contain only letters")
            else:
                print("Last name added")
                return lastname
    
    def get_email(self):
        while True:
            email = input("Enter email: ").strip()

            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, email):
                print("Invalid email format!")
                continue

            return email
    
    def get_password(self):
        while True:
            password = input("Enter password: ").strip()
            if len(password) < 8:
                print("Password must be at least 8 characters long.")
            elif not any(char.isdigit() for char in password):
                print("Password must contain at least one digit.")
            elif not any(char.islower() for char in password):
                print("Password must contain at least one lowercase letter.")
            else:
                return password

    def get_date_of_birth(self):
        while True:
            try:
                date_str = input("Enter date of birth (YYYY-MM-DD): ")
                date_of_birth = datetime.strptime(date_str, "%Y-%m-%d").date()

                if date_of_birth > self.now:
                    print("Date of birth cannot be in the future")
                    continue

                print("Date of birth added")
                return date_of_birth
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD")