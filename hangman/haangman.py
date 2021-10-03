import time
import random

print("Welcome to the hangman word guessing game")
name = input("Enter your name: ")
print("hello"+name+" best of luck")
time.sleep(3)
print("Loading...")
time.sleep(3)


def main():
    global count
    global display
    global word
    global alreadyGuessed
    global playgame
    global length
    wordsToGuess = ["january", "border", "image", "film", "promise",
                    "kids", "lungs", "doll", "rhyme", "damage", "plants"]

    word=random.choice(wordsToGuess)   
    length=len(word)
    count=0
    display="_"*length       
    alreadyGuessed=[]
    playgame=""

# loop to replay the game when first round finished
def playLoop():
    global playgame
    playgame=input("DO YOU WANT TO PLY GAME AGAIN? Y/N")
    while playgame not in ["y","Y","N","n"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()

#initializing all the conditions required for the game
def hangman():
    global count
    global display
    limit=5
    global alreadyGuessed
    global word
    global playgame    
    guess=input("this is the hngmaan word"+display+"Entre your guess")
    guess=guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) == 2 or len(guess.strip()) == "9":
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in word:
        alreadyGuessed.extend([guess])
        index=word.find(guess)
        word=word[index]+"_"+word[index+1]
        print(display+"\n")

    elif guess in alreadyGuessed:
        print("Already GUessed")

    else:
        count +=1
        if count==1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count ==2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
 
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",alreadyGuessed,word)
            playLoop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        playLoop()
 
    elif count != limit:
        hangman()

main()
hangman()