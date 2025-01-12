from facade.system_facade import SystemFacade

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            print("\n=== Register ===")
            SystemFacade.register()
        elif choice == '2':
            print("\n=== Login ===")
            SystemFacade.login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()