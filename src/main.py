from facade.system_facade import SystemFacade
def userMenu():
    print("\n--- User Features ---")
    print("1. View all vacations")
    print("2. Like vacation")
    print("3. unlike vacation")
    print("4. View your liked vacations")
    print("5. Exit")

def AdminMenu():
    print("\n--- Admin Features ---")
    print("1. View all vacations")
    print("2. Add new vacations")
    print("3. Edit existing vacations")
    print("4. Delete vacations")
    print("5. Exit")


def main():
    sf = SystemFacade()
    flag = True
    while flag:
        print("\n--- Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            print("\n=== Register ===")
            sf.register()
            flag = False
        elif choice == '2':
            print("\n=== Login ===")
            sf.login()
            flag = False
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    while True:
        if sf.current_user['role'] == 2:
            userMenu()
            choice = int(input("Choose an option (1-5): "))
            if choice == 1:
                sf.view_all_vacations()
            elif choice == 2:
                vacation_title = input("Enter a vacation title you would like: ")
                sf.like_logic.add_like(sf.current_user['user_id'],vacation_title)
            elif choice == 3:
                vacation_title = input("Enter a vacation title you would like: ")
                sf.like_logic.delete_like(sf.current_user['user_id'],vacation_title)
            elif choice == 4:
                sf.view_liked_vacations()
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please enter a command between 1 and 5.")

        elif sf.current_user['role'] == 1: 
            AdminMenu()  
            choice = int(input("Choose an option (1-5): "))
            if choice == 1:
                sf.view_all_vacations()
            if choice == 2:
                vacation_title = input("Enter vacation title: ")
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                country = input("Enter country: ")
                price = float(input("Enter price: "))
                img_url = input("Enter image URL: ")
                sf.vacation_logic.add_vacation(vacation_title, start_date, end_date, country, price, img_url)
            elif choice == 3:
                vacation_id = input("Enter vacation id: ")
                sf.vacation_logic.edit_vacation(vacation_id)
            elif choice == 4:
                vacation_id = input("Enter vacation id: ")
                sf.vacation_logic.del_vacation(vacation_id)
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please enter a command between 1 and 5.")




     
if __name__ == "__main__":
    main()