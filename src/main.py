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
                sf.vacation_facade.view_all_vacations()
            elif choice == 2:
                sf.vacation_facade.add_vacation()
            elif choice == 3:
                sf.vacation_facade.view_all_vacations()
                sf.vacation_facade.edit_vacation()
            elif choice == 4:
                sf.vacation_facade.view_all_vacations()
                sf.vacation_facade.del_vacation()
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

    for i in range(110):  
        clear_screen()
        for line in boat_frames:
            print(" " * i + line)  
        time.sleep(0.03)

    print("\nThe boat has sailed away...")

def main():
    sf = SystemFacade()
    while True:
        mainMenu()
        choice = input("Choose a command (1/2/3): ")
        clear_screen()

        if choice == '1':
            print("\n=== Register ===")
            if not sf.register():
                continue
        elif choice == '2':
            print("\n=== Login ===")
            if not sf.login():
                continue

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
