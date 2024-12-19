class user_logic:

    def add_vacation(self, vacation_id,vacation_title, start_date, end_date, price, total_likes, img_url, country):

        query = """
            INSERT INTO `vacation_system`.`vacations` 
            (vacation_id, vacation_title, start_date, end_date, price, total_likes, img_url, country)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (vacation_id, vacation_title, start_date, end_date, price, total_likes, img_url, country)
        return query, values

    def edit_vacation(self, vacation_id, vacation_title, start_date, end_date, price, img_url, country):
        query = """
            UPDATE `vacation_system`.`vacations` 
            SET vacation_title = %s, start_date = %s, end_date = %s, price = %s, img_url = %s, country = %s 
            WHERE vacation_id = %s
        """
        values = (vacation_title, start_date, end_date, price, img_url, country, vacation_id)
        return query, values

    def delete_vacation(self, vacation_id):

        delete_likes_query = """
            DELETE FROM `vacation_system`.`likes` 
            WHERE vacation_id = %s
        """

        delete_vacation_query = """
            DELETE FROM `vacation_system`.`vacations` 
            WHERE vacation_id = %s
        """
        values = (vacation_id)
        return delete_likes_query, delete_vacation_query, values    
