import string
import random

characters=list(string.ascii_letters+string.digits+"!@#$%^&*()")

def generateRandomPassword():
    # take length of pasword from user
    length=int(input("Enter the length of the passoword:_"))

    # suffle the characters taken above
    random.shuffle(characters)

    # pick random characters from the list and put into array
    password=[]
    for i in range(length):
        password.append(random.choice(characters))

    # shuffle the result password again 
    random.shuffle(password)

    print("".join(password))
    

generateRandomPassword()