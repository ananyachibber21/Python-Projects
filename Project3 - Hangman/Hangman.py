import random

print("--------------- Welcome to the Hangman Game ---------------")

def hang():
    word = random.choice(["apple", "batman", "chamaleon", "denmark", "elephant", "foolish", "graph", "happiness", "indigo",
        "juggle", "kashmir", "laugh", "magnets", "netcraft", "opaque", "parrot", "return"])
    letters = "abcdefghijklmnopqrstuvwxyz"
    guessmade = ""
    trial = 10
    while(len(word)>0):
        main = ""
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word:" , main)
        guess = input()

        if guess in letters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            trial = trial - 1
            if trial == 9:
                print("9 turns left")
                print("  --------  ")
            if trial == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if trial == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if trial == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if trial == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if trial == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if trial == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if trial == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if trial == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if trial == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break
        
name = input("Enter your name: ")
print("Hello ", name, "Let's start...")
print("Try to guess the word in less than 10 attemps.")
hang()
print()