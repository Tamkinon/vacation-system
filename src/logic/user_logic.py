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

    def add_vacation(self, vacation_id,vacation_title, start_date, end_date, price, total_likes, img_url, country):
        
        query = """
            INSERT INTO `vacation_system`.`vacations` 
            (vacation_id, vacation_title, start_date, end_date, price, total_likes, img_url, country)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        params = (vacation_id, vacation_title, start_date, end_date, price, total_likes, img_url, country)
        try:
            result = self.dal.insert(query, params)
            return True
        except Exception as err:
            print(f"Error adding vacation: {err}")
            return False    
    
    def edit_vacation(self, vacation_id, vacation_title, start_date, end_date, price, img_url, country):
        
        query = """
            UPDATE `vacation_system`.`vacations` 
            SET vacation_title = %s, start_date = %s, end_date = %s, price = %s, img_url = %s, country = %s 
            WHERE vacation_id = %s
        """
        params = (vacation_title, start_date, end_date, price, img_url, country, vacation_id)
    
        try:
            result = self.dal.update(query, params)
            return True
        except Exception as err:
            print(f"Error editing vacation: {err}")
            return False

    def delete_vacation(self, vacation_id):
       
        query = """
            DELETE FROM `vacation_system`.`vacations` 
            WHERE vacation_id = %s
        """
        params = (vacation_id)

        try:
            result = self.dal.delete(query, params)
            return True
        except Exception as err:
            print(f"Error deleting vacation: {err}")
            return False

      
if __name__ == "__main__":
    try:
       print("good")
    except Exception as err:
        print(f"Error: {err}")
