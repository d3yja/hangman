playagain = True
from hangmanart import *
while playagain:
    guessed = []
    win = False
    dash_display = []
    split_word = []
    max = len(word_list)-1
    import random 
    word = random.randint(0,max)
    h1 = word
    word = word_list[word]
    def dashes(word):
        dashno = len(word)
        for i in range(dashno): # making a list which will act like a display
            dash_display.append("_")
    def wordsplit(word): # splitting the word into a list to make comparing easier
        for i in range(len(word)):
            split_word.append(word[i])
        return split_word
    dashes(word)
    wordsplit(word)
    print(logo)
    print("          ")
    print(dash_display)
    print(stages[0])
    for i in range(6): # 6 mistakes and you lose
        correct = True
        while correct: # as long as correct choice is made, i doesnt increase
            if "_" in dash_display:
                guess = input("Guess a letter: ").lower()
                while (guess in guessed) or len(guess)>1:
                   if guess in guessed:
                        print("This has already been guessed")
                        guess = input("Guess a letter: ").lower()
                   else:
                       print("Can not enter more than one letter at a time")
                       guess = input("Guess a letter: ").lower()
                guessed.append(guess)
                if guess not in split_word:
                    print("Wrong")
                    print(stages[i+1])
                    while i <5:
                        print("Here's a hint!") # Hints to make guessing possible (Made hint list from chatgpt)
                        print(hint[h1][i-1])
                        break
                    correct = False
                    break
                else:
                    for x in range(len(split_word)): # searching for position of letter and adding it to the display
                        temp = split_word[x]
                        if guess == temp:
                            dash_display[x] = guess
                print(dash_display)
                print(stages[i])
            else:
                win = True
                correct = False
                break
    if win:
        print("You win")
    else:
        print("You lost!")
    print(f"The word was {word}")
    print("Dou you want to play again?")
    print("Press 1 to play again and Press 2 to exit")
    choice = int(input("Your choice: "))
    while choice<1 or choice>2:
        print("Invalid choice")
        choice = int(input("Your choice: "))
    if choice == 2:
        print("Goodbye!")
        playagain = False
        break
    else:
        print("New game starting......")
