import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)

from src.utils.dal import DAL

class UserLogic:
    def __init__(self):
        self.dal = DAL()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()

    def add_user(self, firstname, lastname, email, password, date_of_birth):
        try:
            query = """
                    INSERT INTO vacation_system.users 
                    (firstname, lastname, email, password, date_of_birth, role)
                    VALUES 
                    (%s, %s, %s, %s, %s, 2)
                    """
            params = (firstname, lastname,
                        email,  password, date_of_birth,)
            self.dal.insert(query, params)
            return True
        except Exception as err:
                print(f"Error adding user: {err}")
                return False

    def check_valid_signup(self, email):
        query = "SELECT COUNT(*) AS count FROM vacation_system.users WHERE email = %s"
        params = (email,)
        try:
            result = self.dal.get_scalar(query, params)
            return result["count"] == 0 if result else True
        except Exception as e:
            print(f"Error validating signup: {e}")
            return False

    def check_valid_login(self, email, password):
        query = "SELECT COUNT(*) AS count FROM vacation_system.users WHERE email = %s AND password = %s"
        params = (email, password,)
        try:
            result = self.dal.get_scalar(query, params)
            return result["count"] > 0 if result else False
        except Exception as e:
            print(f"Error validating login: {e}")
            return False
        
    def get_user_by_email(self, email):
        query = "SELECT * FROM vacation_system.users WHERE email = %s"
        params = (email,)
        result = self.dal.get_scalar(query, params)
        return result if result is not None else {}
  

if __name__ == "__main__":
    try:
        # Test user data
        test_firstname = "John"
        test_lastname = "Doe"
        test_email = "johndoe@example.com"
        test_password = "password123"
        test_dob = "1990-01-01"  # Example date of birth

        with UserLogic() as user_logic:
            # Test add_user
            print("Testing add_user:")
            added = user_logic.add_user(test_firstname, test_lastname, test_email, test_password, test_dob)
            if added:
                print(f"User {test_firstname} {test_lastname} added successfully.")
            else:
                print(f"Failed to add user {test_firstname} {test_lastname}.")

            # Test check_valid_signup
            print("\nTesting check_valid_signup:")
            is_valid_signup = user_logic.check_valid_signup(test_email)
            if is_valid_signup:
                print(f"Email '{test_email}' is available for signup.")
            else:
                print(f"Email '{test_email}' is already in use.")

            # Test check_valid_login
            print("\nTesting check_valid_login:")
            is_valid_login = user_logic.check_valid_login(test_email, test_password)
            if is_valid_login:
                print(f"Login successful for email '{test_email}'.")
            else:
                print(f"Invalid login credentials for email '{test_email}'.")

            # Test get_user_by_email
            print("\nTesting get_user_by_email:")
            user = user_logic.get_user_by_email(test_email)
            if user:
                print(f"User details for email '{test_email}': {user}")
            else:
                print(f"No user found with email '{test_email}'.")

    except Exception as err:
        print(f"Error: {err}")
