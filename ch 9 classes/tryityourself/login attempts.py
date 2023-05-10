class User:

    def __init__(self, first_name, last_name, age, sex, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        #summary of user info
        user = [self.first_name, self.last_name, self.age, self.sex, self.email]
        for x in user:
            print(x)

    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello {full_name}!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        if self.login_attempts == 5:
            reset = self.login_attempts = 0

user_1 = User('Lauren', 'Harms', 26, 'F', 'loh1996@msn.com')
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)


