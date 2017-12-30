'''a class for normal user'''

class User():
    def __init__(self, f_name, l_name, l_attempts=0):
        self.first_name = f_name
        self.last_name = l_name
        self.login_attempts=l_attempts

    def describe_user(self):
        print("Name of the user is %s %s." % (self.first_name, self.last_name))
        print("%s %s has loginned %d times." % (self.first_name,
                                                self.last_name,
                                                self.login_attempts))

    def greet_user(self):
        print("Hello, %s %s." % (self.first_name, self.last_name))

    def increment_login_attempt(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

if __name__== "__main__":
    user1=User("Tom","Kruis")
    print(user1.first_name,user1.last_name)
    user1.describe_user()
    user1.greet_user()
    user1.increment_login_attempt()
    user1.increment_login_attempt()
    user1.describe_user()
    user1.reset_login_attempts()
    user1.describe_user()
