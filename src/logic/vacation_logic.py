class VacationLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_vacation(self):
        query = """
            """
        
        result == self.dal.get_table(query)
        if result:
            for vacation in result:
                print(vacation)
            return result
        else:
            return ValueError("Faild to retrive Vacation")
        
    def add_vacation(self, title, vacation_description,start_date):
        params = ()
