import random
import string
import json

def generate_password(length=12, include_symbols=True):
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def load_passwords(filename="passwords.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist

def save_passwords(passwords, filename="passwords.json"):
    with open(filename, "w") as f:
        json.dump(passwords, f, indent=4)  # Use indent for pretty printing

def manage_passwords():
    passwords = load_passwords()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Add Password")
        print("2. Change Password")
        print("3. Delete Password")
        print("4. View Passwords") # Added viewing functionality
        print("5. Check Password Strength") # Added password strength checker
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            site = input("Enter website/service name: ")
            length = int(input("Enter password length (default 12): ") or 12)  # Allow default
            include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
            new_password = generate_password(length, include_symbols)
            passwords[site] = new_password
            print(f"Password for {site} generated and saved.")

        elif choice == "2":
            site = input("Enter website/service to change password: ")
            if site in passwords:
                 length = int(input("Enter new password length (default 12): ") or 12)
                 include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
                 new_password = generate_password(length, include_symbols)
                 passwords[site] = new_password
                 print(f"Password for {site} changed and saved.")
            else:
                print(f"No password found for {site}.")

        elif choice == "3":
            site = input("Enter website/service to delete password: ")
            if site in passwords:
                del passwords[site]
                print(f"Password for {site} deleted.")
            else:
                print(f"No password found for {site}.")
        elif choice == "4": # View Passwords
            if passwords:
                for site, password in passwords.items():
                    print(f"{site}: {password}") # Display site and password
            else:
                print("No passwords saved yet.")
        elif choice == "5": # Check Password Strength
            site = input("Enter website/service to change password: ")
            if site in passwords:
                password = passwords[site]
                upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
                lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
                special = any([1 if c in string.punctuation else 0 for c in password])
                digits = any([1 if c in string.digits else 0 for c in password])
                characters = [upper_case, lower_case, special, digits]
                length = len(password)
                score = 0
                with open('common.txt', 'r') as f:
                 common = f.read().splitlines()
                if password in common:
                    print("Password was found in a common list. Score: 0/7")
                    continue
                if length < 8:
                    score += 1
                if length < 12:
                    score += 1
                if length < 17:
                    score += 1
                if length > 20:
                    score += 1
                print(f"Password length is {str(length)}, adding {str(score)} points!")     
                if sum(characters) > 1:
                    score += 1
                if sum(characters) > 2:
                    score += 1
                if sum(characters) > 3:
                    score += 1
                print(f"Password contains {str(sum(characters))} different character types, adding {str(sum(characters) - 1)} points!")           
                if score < 4:
                    print(f"The password is quite weak! Score: {str(score)}/7")
                elif score == 4:
                    print(f"The password is okay! Score: {str(score)}/7")
                elif score > 4 and score < 6:
                    print(f"The password pretty good! Score: {str(score)}/7") 
                elif score > 6:
                    print(f"The password is very strong! Score: {str(score)}/7")
                else:
                    print(f"No password found for {site}.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

    save_passwords(passwords)
    print("Passwords saved and exiting.")

if __name__ == "__main__":
    manage_passwords()