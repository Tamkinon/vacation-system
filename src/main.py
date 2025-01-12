import os
import time
from facade.system_facade import SystemFacade

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def userMenu():
    print("\n--- User Features ---")
    print("1. View all vacations")
    print("2. Like vacation")
    print("3. Unlike vacation")
    print("4. View your liked vacations")
    print("5. Exit")

def adminMenu():
    print("\n--- Admin Features ---")
    print("1. View all vacations")
    print("2. Add new vacation")
    print("3. Edit existing vacation")
    print("4. Delete vacation")
    print("5. Exit")

def mainMenu():
    print("\n--- Main Menu ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def handleUserActions(sf):
    while True:
        userMenu()
        try:
            choice = int(input("Choose an option (1-5): "))
            clear_screen()
            if choice == 1:
                sf.view_all_vacations()
            elif choice == 2:
                sf.view_all_vacations()
                vacation_title = input("Enter a vacation title you would like to like: ")
                sf.like_logic.add_like(sf.user_facade.current_user['user_id'], vacation_title)
            elif choice == 3:
                sf.view_liked_vacations()
                vacation_title = input("Enter a vacation title you would like to unlike: ")
                sf.like_logic.delete_like(sf.user_facade.current_user['user_id'], vacation_title)
            elif choice == 4:
                sf.view_liked_vacations()
            elif choice == 5:
                clear_screen()
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def handleAdminActions(sf):
    while True:
        adminMenu()
        try:
            choice = int(input("Choose an option (1-5): "))
            clear_screen()
            if choice == 1:
                sf.view_all_vacations()
            elif choice == 2:
                vacation_title = input("Enter vacation title: ")
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                country = input("Enter country: ")
                price = float(input("Enter price: "))
                img_url = input("Enter image URL: ")
                sf.vacation_logic.add_vacation(vacation_title, start_date, end_date, country, price, img_url)
            elif choice == 3:
                vacation_id = input("Enter vacation ID to edit: ")
                sf.vacation_logic.edit_vacation(vacation_id)
            elif choice == 4:
                vacation_id = input("Enter vacation ID to delete: ")
                sf.vacation_logic.del_vacation(vacation_id)
            elif choice == 5:
                clear_screen()
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def moving_boat():
    """Animates a boat moving across the screen."""
    boat_frames = [
        "        ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ",
        "              ___|____|___              ",
        "           __/            \\__           ",
        "       ___/                  \\___       ",
        "   ___/      Goodbye!          \\___    ",
        "   \\______________________________/    ",
        "       ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~     "
    ]

    for i in range(135):  # Move the boat 30 steps
        clear_screen()
        for line in boat_frames:
            print(" " * i + line)  # Add spaces to move the boat to the right
        time.sleep(0.03)  # Pause for animation speed

    print("\nThe boat has sailed away...")

def main():
    sf = SystemFacade()
    while True:
        mainMenu()
        choice = input("Choose a command (1/2/3): ")
        clear_screen()

        if choice == '1':
            print("\n=== Register ===")
            sf.register()
        elif choice == '2':
            print("\n=== Login ===")
            sf.login()

            role = sf.user_facade.current_user['role']
            clear_screen()
            if role == 2:
                handleUserActions(sf)
            elif role == 1:
                handleAdminActions(sf)
        elif choice == '3':
            moving_boat()
            break
        else:
            print("Invalid command. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
