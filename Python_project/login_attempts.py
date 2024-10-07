class LoginAttempts:

    MAX_ATTEMPTS = 5
    attempts = 0

    @staticmethod
    def increment_attempts():
        LoginAttempts.attempts += 1
        remaining_attempts = LoginAttempts.MAX_ATTEMPTS - LoginAttempts.attempts
        if remaining_attempts > 0:
            print(f"Invalid login. You have {remaining_attempts} attempt(s) left.")
        else:
            print(f"Too many failed attempts. You have exceeded the limit of {LoginAttempts.MAX_ATTEMPTS} attempts.")
    
    @staticmethod
    def reset_attempts():
        LoginAttempts.attempts = 0

    @staticmethod
    def can_attempt_login():
        return LoginAttempts.attempts < LoginAttempts.MAX_ATTEMPTS
