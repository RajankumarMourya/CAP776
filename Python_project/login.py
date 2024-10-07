import csv
from utils import Utils
from login_attempts import LoginAttempts

class Login:

    CSV_FILE_PATH = 'regno.csv'

    @staticmethod
    def login_user():
        email = input("Enter your email: ").strip()
        
        # Validate email immediately
        if not Utils.validate_email(email):
            print("Invalid email format. Please enter a valid email (e.g., user@example.com).")
            return False
        
        password = input("Enter your password: ").strip()
        if not Utils.validate_password(password):
            print("Invalid password format.")
            return False

        # Check login attempts limit
        if not LoginAttempts.can_attempt_login():
            print("Too many failed login attempts. Please try again later.")
            return False

        # Read stored credentials
        with open(Login.CSV_FILE_PATH, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['email'] == email:
                    if Utils.check_password(row['hashed_password'].encode('utf-8'), password):
                        print(f"Login successful! Welcome {email}.")
                        LoginAttempts.reset_attempts()  # Reset failed attempts
                        return True
                    else:
                        print("Invalid password.")
                        LoginAttempts.increment_attempts()
                        return False

        print("Email not found.")
        LoginAttempts.increment_attempts()
        return False
