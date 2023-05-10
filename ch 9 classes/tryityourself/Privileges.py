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

class Privileges:

    def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print("The following are Admin privileges:")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):

    def __init__(self, first_name, last_name, age, sex, email ):
        super().__init__(first_name, last_name, age, sex, email)
        self.privileges_admin = Privileges()


my_admin = Admin('Lauren', 'Harms', 26, 'F', 'loh1996@msn.com')
my_admin.privileges_admin.show_privileges()