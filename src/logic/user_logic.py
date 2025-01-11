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

    def add_user(self, first_name, last_name, email, password, date_of_birth):
        try:
            query = """
                    INSERT INTO vacation_system.users 
                    (first_name, last_name, email, password, date_of_birth, role)
                    VALUES 
                    (%s, %s, %s, %s, %s, 2)
                    """
            params = (first_name, last_name,
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
        query = "SELECT * FROM users WHERE email = %s"
        params = (email,)
        result = self.dal.get_table(query, params)
        return result if result is not None else []
  
      
if __name__ == "__main__":
    try:
        with UserLogic() as user_logic:
            email1 = "will.thomas@example.com"
            print(f"can {email1} signup? -> {user_logic.check_valid_signup(email1)}")
    
            email2 = "alice.smith@example.com"
            password = "password123"
            print(f"can email: {email2} | password: {password} login? -> {user_logic.check_valid_login(email2, password)}")
    except Exception as err:
        print(f"Error: {err}")
