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
            (%s, %s, %s, %s, 0, %s, (SELECT id FROM vacations_mysql.countries WHERE country_name LIKE %s))
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
        query = f"UPDATE vacation_system.vacations SET {clause} WHERE id = %s"

        try:
            self.dal.update(query, params)
            return True
        except Exception as e:
            print(f"Error updating vacation: Vacation not found!")
            return False

    def del_vacation(self, id):
        query = "DELETE FROM vacation_system.vacations WHERE id = %s"
        params = (id,)
        try:
            result = self.dal.delete(query, params)
            return True
        except Exception as err:
            print(f"Error deleting vacation: {err}")
            return False


if __name__ == "__main__":
    try:
        with VacationLogic() as vacation_logic:
            vacations = vacation_logic.get_all_vacations()
            for vacation in vacations:
                print("----------------------")
                print(vacation)
    except Exception as err:
        print(f"Error: {err}")