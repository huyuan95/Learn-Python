'''a class for administrator'''

import user

class Privileges():
    def __init__(self,priv):
        self.privileges = priv

    def show_privileges(self):
        for priv in self.privileges:
            print(priv)


class Admin(user.User):
    def __init__(self,f_name, l_name, priv, l_attempts=0):
        super().__init__(f_name, l_name, l_attempts)
        self.privileges=Privileges(priv)

    def show_privileges(self):
        print('Privileges for admin is:')
        self.privileges.show_privileges()


if __name__ == "__main__":
    admin=Admin("Vincent","Hu",["can add post", "can delete post", "can ban \
                                                                   users"])
    admin.show_privileges()
