import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)

from src.utils.dal import DAL

class VacationLogic:
    def __init__(self):
        self.dal = DAL()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()

    def get_all_vacations(self):
        '''returns: list of vacation dictionaries'''
        '''empty list if no vacations in the database'''

        query = "SELECT * from vacation_system.vacations"
        result = self.dal.get_table(query)
        return result if result is not None else []

    def add_vacation(self, vacation_title, start_date, end_date, country, price, img_url):
        try:
            query = """
            INSERT INTO vacation_system.vacations 
            (vacation_title, start_date, end_date, price, total_likes, img_url, country)
            VALUES 
            (%s, %s, %s, %s, 0, %s, (SELECT country_id FROM vacation_system.countries WHERE country_name LIKE %s))
            """
            params = (vacation_title, start_date,
                    end_date,  price, img_url, f"%{country}%",)
            self.dal.insert(query, params)
            return True

        except Exception as err:
            print(f"Error adding vacation: {err}")
            return False

    def edit_vacation(self, id, **kwargs):
        if not kwargs:
            return False

        clause = ", ".join([f"{k} = %s" for k in kwargs.keys()])

        params = tuple(kwargs.values()) + (id,)
        query = f"UPDATE vacation_system.vacations SET {clause} WHERE vacation_id = %s"

        try:
            self.dal.update(query, params)
            return True
        except Exception as e:
            print(f"Error updating vacation: Vacation not found!")
            return False

    def del_vacation(self, id):
        try:
            delete_likes_query = "DELETE FROM vacation_system.likes WHERE vacation_id = %s"
            self.dal.delete(delete_likes_query, (id,))

            delete_vacation_query = "DELETE FROM vacation_system.vacations WHERE vacation_id = %s"
            self.dal.delete(delete_vacation_query, (id,))

            print("Vacation and associated likes deleted successfully!")
            return True
        except Exception as err:
            print(f"Error deleting vacation: {err}")
            return False


if __name__ == "__main__":
    try:
        with VacationLogic() as vacation_logic:
            # Test get_all_vacations
            print("Testing get_all_vacations:")
            vacations = vacation_logic.get_all_vacations()
            if vacations:
                print("Vacations retrieved successfully:")
                for vacation in vacations:
                    print(vacation)
            else:
                print("No vacations found in the database.")

            # Test add_vacation
            print("\nTesting add_vacation:")
            vacation_title = "Summer Paradise"
            start_date = "2025-06-15"
            end_date = "2025-06-25"
            country = "Greece"
            price = 1200.50
            img_url = "http://example.com/summer_paradise.jpg"
            added = vacation_logic.add_vacation(vacation_title, start_date, end_date, country, price, img_url)
            if added:
                print(f"Vacation '{vacation_title}' added successfully.")
            else:
                print(f"Failed to add vacation '{vacation_title}'.")

            # Test edit_vacation
            print("\nTesting edit_vacation:")
            vacation_id_to_edit = 1  # Replace with an existing vacation ID for a meaningful test
            updated_data = {
                "price": 1000.75,
                "vacation_title": "Updated Paradise",
            }
            edited = vacation_logic.edit_vacation(vacation_id_to_edit, **updated_data)
            if edited:
                print(f"Vacation with ID {vacation_id_to_edit} updated successfully.")
            else:
                print(f"Failed to update vacation with ID {vacation_id_to_edit}.")

            # Test del_vacation
            print("\nTesting del_vacation:")
            vacation_id_to_delete = 1  # Replace with an existing vacation ID for a meaningful test
            deleted = vacation_logic.del_vacation(vacation_id_to_delete)
            if deleted:
                print(f"Vacation with ID {vacation_id_to_delete} deleted successfully.")
            else:
                print(f"Failed to delete vacation with ID {vacation_id_to_delete}.")

    except Exception as err:
        print(f"Error: {err}")
