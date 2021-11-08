class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email

class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoggedIn=False
        self.currentUser={}
        #load users from .json file
        self.loadUser()

    def loadUser(self):
        pass
    def register(self,user:User):
        self.users.append(user)
        print("user is created")

    def login(self):
        pass
    def savetoFile(self):
        pass

repository=UserRepository()

while True:
     print("Menü".center(50,'*'))
     secim=input('1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nYour choice: ')
     if secim=='5':
        break

     else:
         if secim == '1':
             username = input('username: ')
             password = input('password: ')
             email = input('email: ')
             user = User(username, password, email)
             repository.register(user)
             print(repository.users)
             
         elif secim == '2':
             pass
         elif secim == '3':
             pass
         elif secim == '4':
             pass
         else:
             print("Wrong Choice")