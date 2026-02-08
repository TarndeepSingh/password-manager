"""
MyPass Entry Point
-----------------
CLI-based interface for interacting with the password manager.
"""

from app.password_manager import PasswordManager
from app.storage import StorageHandler
from app.security import SecurityUtils
from app.exceptions import PasswordManagerError


def main():
    storage = StorageHandler("data/data.json")
    manager = PasswordManager(storage)

    while True:
        print("\n--- MyPass Password Manager ---")
        print("1. Add Credential")
        print("2. Find Credential")
        print("3. Generate Password")
        print("4. Exit")

        choice = input("Select an option: ").strip()

        try:
            if choice == "1":
                website = input("Website: ")
                email = input("Email/Username: ")
                password = input("Password: ")
                manager.add_credential(website, email, password)
                print("✅ Credential saved successfully.")

            elif choice == "2":
                website = input("Website: ")
                credential = manager.find_credential(website)
                print(f"Email: {credential['email']}")
                print(f"Password: {credential['password']}")

            elif choice == "3":
                length = int(input("Password length: "))
                print("Generated Password:",
                      SecurityUtils.generate_password(length))

            elif choice == "4":
                print("Goodbye 👋")
                break

            else:
                print("Invalid option. Try again.")

        except PasswordManagerError as error:
            print(f"❌ Error: {error}")
        except ValueError as error:
            print(f"❌ Invalid input: {error}")


if __name__ == "__main__":
    main()
