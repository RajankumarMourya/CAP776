import csv
from utils import Utils

class ForgotPassword:

    CSV_FILE_PATH = 'regno.csv'

    @staticmethod
    def reset_password():
        email = input("Enter your registered email: ").strip()

        # Validate email
        if not Utils.validate_email(email):
            print("Invalid email format.")
            return False

        # Read stored credentials
        users = []
        with open(ForgotPassword.CSV_FILE_PATH, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                users.append(row)

        # Find the user
        user = next((user for user in users if user['email'] == email), None)
        if not user:
            print("Email not found.")
            return False

        # Verify security question
        answer = input("What is your favorite color? (security question): ").strip()
        if answer == user['security_question']:
            new_password = input("Enter your new password: ").strip()
            if not Utils.validate_password(new_password):
                print("Password must be at least 8 characters long, with one uppercase letter, one lowercase letter, one digit, and one special character.")
                return False

            # Update the password
            user['hashed_password'] = Utils.hash_password(new_password).decode('utf-8')
            with open(ForgotPassword.CSV_FILE_PATH, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['email', 'hashed_password', 'security_question'])
                writer.writeheader()
                writer.writerows(users)

            print("Password reset successfully.")
            return True
        else:
            print("Security question answer is incorrect.")
            return False
