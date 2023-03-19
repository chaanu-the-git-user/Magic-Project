import pickle
#making the class for users
class user:
    def __init__(self, password, username):
        self.password = password
        self.username = username
    def change_password(password):
        self.password = password
mainpass = str(input('Enter Your Password: '))
mainusern = str(input('Enter Your Username: '))
mainuser = str(user(mainpass, mainusern))
# serializing the data to remember the user
usaf = mainusern + '.pkl'
with open(usaf, 'wb') as mainfil:
    pickle.dump(mainuser, mainfil)
with open('user.py', 'w') as thisfile:
    thisfile.write("""mainuser = open('user.pkl', 'rb')
    mainuser1  = mainuser.read()
    mainuserpassword, mainuserusername = manuser1.split
    givenpassword = input('Enter The Password ')
    if mainuserpassword == givenpassword:
        print('hello!')
    else:
        print('you intruter!')""")