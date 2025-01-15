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
            # Fetch vacation_id based on vacation_title
            vacation_query = """
            SELECT vacation_id FROM vacation_system.vacations WHERE vacation_title = %s
            """
            vacation = self.dal.get_one(vacation_query, (vacation_title,))
            
            if not vacation:
                print("Vacation not found.")
                return False

            vacation_id = vacation["vacation_id"]

            # Check if user already liked the vacation
            like_check_query = """
            SELECT 1 FROM vacation_system.likes WHERE user_id = %s AND vacation_id = %s
            """
            like_exists = self.dal.get_scalar(like_check_query, (user_id, vacation_id))

            if like_exists:
                print("User has already liked this vacation.")
                return False

            # Add like to the likes table and increment total_likes
            like_query = """
            INSERT INTO vacation_system.likes (user_id, vacation_id) VALUES (%s, %s)
            """
            update_likes_query = """
            UPDATE vacation_system.vacations 
            SET total_likes = total_likes + 1 
            WHERE vacation_id = %s
            """
            
            self.dal.insert(like_query, (user_id, vacation_id))
            self.dal.update(update_likes_query, (vacation_id,))
            print("👍")
            return True

        except Exception as e:
            print(f"Error adding like: {e}")
            return False

    def delete_like(self, user_id, vacation_title):
        """
        Removes a like for a vacation by a user. Updates the total_likes column in the vacations table.
        """
        try:
            # Fetch vacation_id based on vacation_title
            vacation_query = """
            SELECT vacation_id FROM vacation_system.vacations WHERE vacation_title = %s
            """
            vacation = self.dal.get_one(vacation_query, (vacation_title,))
            
            if not vacation:
                print("Vacation not found.")
                return False

            vacation_id = vacation["vacation_id"]

            # Check if user already liked the vacation
            like_check_query = """
            SELECT 1 FROM vacation_system.likes WHERE user_id = %s AND vacation_id = %s
            """
            like_exists = self.dal.get_scalar(like_check_query, (user_id, vacation_id))

            if not like_exists:
                print("User has not liked this vacation yet.")
                return False

            # Remove like from the likes table and decrement total_likes
            unlike_query = """
            DELETE FROM vacation_system.likes WHERE user_id = %s AND vacation_id = %s
            """
            update_likes_query = """
            UPDATE vacation_system.vacations 
            SET total_likes = total_likes - 1 
            WHERE vacation_id = %s
            """

            self.dal.delete(unlike_query, (user_id, vacation_id))
            self.dal.update(update_likes_query, (vacation_id,))
            return True

        except Exception as e:
            print(f"Error deleting like: {e}")
            return False
        
    def has_user_liked_any_vacations(self, user_id):
        try:
            # Query to check if the user has liked any vacation
            query_any = """
            SELECT COUNT(*) AS count
            FROM vacation_system.likes
            WHERE user_id = %s
            """
            result_any = self.dal.get_scalar(query_any, (user_id,))
            has_liked_any = result_any and result_any["count"] > 0

            return has_liked_any

            
        except Exception as e:
            print(f"Error checking like status: {e}")
            return False, False
    
    def has_user_liked_specific_vacation(self, user_id, vacation_title):
            # Query to check if the user has liked the specific vacation
            query_specific = """
            SELECT COUNT(*) AS count
            FROM vacation_system.likes l
            JOIN vacation_system.vacations v ON l.vacation_id = v.vacation_id
            WHERE l.user_id = %s AND v.vacation_title = %s
            """
            result_specific = self.dal.get_scalar(query_specific, (user_id, vacation_title))
            has_liked_specific = result_specific and result_specific["count"] > 0

            return has_liked_specific


if __name__ == "__main__":
    try:
        user_id = 1
        vacation_title = "Paris"

        with LikeLogic() as like_logic:
            # Test get_all_likes
            print("Testing get_all_likes:")
            likes = like_logic.get_all_likes(user_id)
            if likes:
                for like in likes:
                    print(f"Vacation ID: {like['vacation_id']}, Title: {like['vacation_title']}")
            else:
                print("No likes found for the user.")

            # Test add_like
            print("\nTesting add_like:")
            added = like_logic.add_like(user_id, vacation_title)
            if added:
                print(f"Successfully added a like for vacation '{vacation_title}'.")
            else:
                print(f"Failed to add a like for vacation '{vacation_title}'.")

            # Test delete_like
            print("\nTesting delete_like:")
            deleted = like_logic.delete_like(user_id, vacation_title)
            if deleted:
                print(f"Successfully deleted a like for vacation '{vacation_title}'.")
            else:
                print(f"Failed to delete a like for vacation '{vacation_title}'.")

    except Exception as err:
        print(f"Error: {err}")

