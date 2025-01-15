
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)

from src.utils.dal import DAL


class CountryLogic:
    def __init__(self):
        self.dal = DAL()
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()

    def get_all_countries(self):
        """
        Retrieve all countries from the database.
        Returns a list of dictionaries, each representing a country.
        """
        query = "SELECT country_id, country_name FROM vacation_system.countries"
        try:
            result = self.dal.get_table(query)
            return result if result else []
        except Exception as e:
            print(f"Error retrieving countries: {e}")
            return []

    def check_if_country_exist(self, country_name):
        """
        Check if a country exists in the database by its name.
        Returns True if the country exists, False otherwise.
        """
        query = "SELECT COUNT(*) AS count FROM vacation_system.countries WHERE country_name = %s"
        params = (country_name,)
        try:
            result = self.dal.get_scalar(query, params)
            return result["count"] > 0 if result else False
        except Exception as e:
            print(f"Error checking country existence: {e}")
            return False


if __name__ == "__main__":
    try:
        with CountryLogic() as country_logic:
            countries = country_logic.get_all_countries()
            for country in countries:
                print("----------------------")
                print(country)
            country_name = "Canada"
            print(f"{country_name} in countries table? -> {country_logic.check_if_country_exist(country_name)}")
    except Exception as err:
        print(f"Error: {err}")
