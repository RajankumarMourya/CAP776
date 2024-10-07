import csv
from utils import Utils

class Register:

    CSV_FILE_PATH = 'regno.csv'

    @staticmethod
    def register_user():
        email = input("Enter your email: ").strip()
        
        # Validate email immediately
        if not Utils.validate_email(email):
            print("Invalid email format. Please enter a valid email (e.g., user@example.com).")
            return

        password = input("Enter your password: ").strip()
        if not Utils.validate_password(password):
            print("Invalid password format. Ensure it has at least 8 characters, one uppercase letter, one lowercase letter, one digit, and one special character.")
            return

        security_question = input("What is your favorite color? (security question): ").strip()
        hashed_password = Utils.hash_password(password)
        
        # Store credentials in CSV file
        with open(Register.CSV_FILE_PATH, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['email', 'hashed_password', 'security_question'])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow({'email': email, 'hashed_password': hashed_password.decode('utf-8'), 'security_question': security_question})
        
        print(f"User {email} registered successfully!")
