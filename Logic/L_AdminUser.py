# Here we will be stored logic of admin users.
from L_User import User
from SFI import Data


# This class inherit the abstracts methods for handle admin user, also We extend the init.
class Admin(User):
    def __init__(self, name, password):
        super().__init__(name, password)

    # Here this method is created to create an admin user, the data is stored in a dict and inserted in data users.
    def create_user(self):
        try:
            self.password = int(self.password)
        except:
            print("Password must be numbers")
            exit()

        self.name = self.name.lower()
        self.password = str(self.password)

        newuser = {
            'name': self.name,
            'password': self.password,
            'role': 'admin'
        }

        Data.users.append(newuser)
        return Data.users

    # Here this method is created to delete user, if method validateUser is true,
    # It iterated through the data users and once it finds the user, Ut removes them from list of dict.
    def delete_user(self):
        self.name = self.name.lower()

        if not self.validate_user():
            print('Error')
            exit()
        for i in Data.users:
            if i['name'] == self.name and i['password'] == self.password:
                Data.users.remove(i)
        return Data.users

    # Here this method os created to validate amd wanted a user,
    # the name's inserted are compared with the data of the users,
    # if They are found, They will return True, else return False.
    def validate_user(self):
        self.name = self.name.lower()

        for i in Data.users:
            if i['name'] == self.name and i['password'] == self.password:
                return True
        return False


test = Admin(input('Name '), input('Password '))
