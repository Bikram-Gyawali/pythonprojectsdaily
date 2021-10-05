import random
import string

# characters to generate random password from
alphabets=list(string.ascii_letters)
digits=list(string.digits)
specialCharacters=list("!@#$%^&*()")
characters=list(string.ascii_letters+string.digits+"!@#$%^&*()")


def generateRandomPassword():
    # take length of password from user
    print("hello world")
    length=int(input("Enter password length:_"))

    # number of each items take input from user
    alphabetsCount=int(input("Enter alphabets count in password:_"))
    digitsCounts=int(input("Enter the digits count in password "))
    specialCharactersCount=int(input("Enter the specal char count in pssword"))

    charactersCount=alphabetsCount+digitsCounts+specialCharactersCount

    # check the total length
    if charactersCount>length:
        print("Characters total count is more than pw length")
        return


    # initialize the pasword
    password=[]

    for i in range(alphabetsCount):
        password.append(random.choice(alphabets))

    # picking random digits
    for i in range(digitsCounts):
        password.append(random.choice(digits))

    for i in range(specialCharactersCount):
        password.append(random.choice(specialCharactersCount))

    
    # if total character count is less than the password length add random numbers to make it equal
        if charactersCount<length:
            random.shuffle(characters)
            for i in range(length-charactersCount):
                password.append(random.choice(characters))

        # again suffling the resultant password
        random.shuffle(password)

        # converting the list to string and printing the list
        print("".join(password))




# calling the function
generateRandomPassword()