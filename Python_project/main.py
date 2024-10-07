from login import Login
from register import Register
from forgot_password import ForgotPassword
from Api import Api


def main():
    api = Api()  # Create an Api object to fetch sunrise and sunset data
    logged_in = False  # Track if the user is logged in

    while True:
        if not logged_in:
            print("\n1. Register")
            print("2. Login")
            print("3. Forgot Password")
            print("4. Exit")
            
            choice = input("Choose an option: ").strip()

            if choice == '1':
                Register.register_user()
            elif choice == '2':
                if Login.login_user():  # Assuming login_user() returns True on successful login
                    logged_in = True
                    print("\nLogin successful! Now you can check sunrise and sunset times.")
                else:
                    print("Login failed.")
            elif choice == '3':
                ForgotPassword.reset_password()
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please try again.")
        else:
            print("\n1. Get Sunrise and Sunset Times")
            print("2. Exit")
            
            choice = input("Choose an option: ").strip()

            if choice == '1':
                city = input("Enter the city to get sunrise and sunset times: ").strip()
                api.sunrise_sunset(city)  # Updated method name to sunrise_sunset
            elif choice == '2':
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
