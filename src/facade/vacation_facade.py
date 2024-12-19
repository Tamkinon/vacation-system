from datetime import date, datetime
from logic.vacation_logic import VacationLogic
# from logic.countries_logic import CountryLogic

class VacationFacade:
    def __init__(self):
        self.params = []
        self.now = date.today()
        self.logic = VacationLogic()
        # self.country_logic = CountryLogic()

    def add_vacation(self):
        self.get_title()
        self.get_start_date()
        self.get_end_date()
        self.get_price()
        self.get_img_url()
        self.get_country_name()

        return self.logic.add_vacation(*self.params)
        
    def get_title(self):
        while True:
            title = input("Enter title: ")
            if not title.isalpha():
                print("title must be alphabetic")
            elif len(title) < 5:
                print("title must be longer then 5 letters")
            else:
                self.params.append(title)
                print("Title added!")
                break
    
    def get_start_date(self):
        while True:
            try:
                year = int(input("Enter year: "))
                month = int(input("Enter year: "))
                day = int(input("Enter year: "))

                date_input = input("Enter date(YYYY-MM-DD): ")
                start_date = date.s

            except ValueError
