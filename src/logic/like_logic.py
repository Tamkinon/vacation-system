import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)


from src.utils.dal import DAL


class LikeLogic:
    def __init__(self):
        self.dal = DAL()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()

    def get_all_likes(self, user_id):
        query = """SELECT v.* from vacation_system.vacations v, vacation_system.likes l
                   WHERE v.vacation_id = l.vacation_id AND l.user_id = %s"""
        params = (user_id,)
        result = self.dal.get_table(query, params)
        return result if result is not None else []

    def add_like(self, user_id, vacation_title):
        try:

        # First check if the like already exists
            check_query = """
            SELECT COUNT(*) as count 
            FROM vacation_system.likes l
            JOIN vacation_system.vacations v ON l.vacation_id = v.vacation_id
            WHERE l.user_id = %s AND v.vacation_title LIKE %s
            """
            check_params = (user_id, f"%{vacation_title}%")
            result = self.dal.get_scalar(check_query, check_params)
            
            if result['count'] > 0:
                print("You have already liked this vacation!")
                return False
            
        # If no existing like, proceed with adding the like
            query = """INSERT INTO vacation_system.likes 
            (user_id, vacation_id)
            VALUES (%s, (SELECT vacation_id FROM vacation_system.vacations WHERE vacation_title LIKE %s))
            """
            params = (user_id, f"%{vacation_title}%")
            self.dal.insert(query, params)
            return True
        
        except Exception as err:
            print(f"Error adding like: {err}")
            return False

    def delete_like(self, user_id, vacation_title):
        try:
            # First check if the like exists
            check_query = """
            SELECT COUNT(*) as count 
            FROM vacation_system.likes l
            JOIN vacation_system.vacations v ON l.vacation_id = v.vacation_id
            WHERE l.user_id = %s AND v.vacation_title LIKE %s
            """
            check_params = (user_id, f"%{vacation_title}%")
            result = self.dal.get_scalar(check_query, check_params)
            
            if result['count'] == 0:
                print("You haven't liked this vacation!")
                return False
                
            # If like exists, proceed with deletion
            delete_query = """
            DELETE l FROM vacation_system.likes l
            JOIN vacation_system.vacations v ON l.vacation_id = v.vacation_id
            WHERE l.user_id = %s AND v.vacation_title LIKE %s
            """
            delete_params = (user_id, f"%{vacation_title}%")
            self.dal.delete(delete_query, delete_params)
            print("Like removed successfully!")
            return True
            
        except Exception as err:
            print(f"Error removing like: {err}")
            return False


if __name__ == "__main__":
    try:
        with LikeLogic() as like_logic:
            likes = like_logic.get_all_likes(1)
            for like in likes:
                print("----------------------")
                print(like)
    except Exception as err:
        print(f"Error: {err}")
