class User:

    def __init__(self, first_name, last_name, age, sex, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.email = email

    def describe_user(self):
        #summary of user info
        user = [self.first_name, self.last_name, self.age, self.sex, self.email]
        for x in user:
            print(x)

    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello {full_name}!\n")

user_1 = User('Lauren', 'Harms', 26, 'F', 'loh1996@msn.com')
user_1.describe_user()
user_1.greet_user()

user_2 = User('Amy', 'Jones', 225, 'F', 'waters@msn.com')
user_2.describe_user()
user_2.greet_user()

user_3 = User('Sarah', 'Williams', 21, 'F', 'willims@yahoo.com')
user_3.describe_user()
user_3.greet_user()