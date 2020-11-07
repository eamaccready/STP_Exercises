# Code from Cory Altoff's self-taught programmer.
# Modified to handle duplicate letters and to print to console a bit neater.
# as well as reporting duplicate guesses and not allowing them.

def hangman(word):
    wrong = 0
    stages = [ "",
               "_________          ",
               "|                  ",
               "|        |         ",
               "|        0         ",
               "|       /|\        ",
               "|       / \        ",
               "|                  "
               ]
    word_letters = list(word)
    board = ["__"] * len(word)
    win = False
    guessed = []
    print("Welcome to Hangman!")
    while wrong < len(stages)-1:
        print("\n")
        msg = "Guess a letter: "
        guess = input(msg)
        if not guess in guessed:
            if guess in word_letters:
                for (i, word) in enumerate(word_letters):
                    if word == guess:
                        board[i]= guess
                        word_letters[i] = '$'
            else:
                wrong +=1
            guessed.append(guess)    
            print((" ".join(board)))
            e = wrong + 1
            print("\n".join(stages[0:e]))
            if "__" not in board:
                print("\nYou win!")
                print(" ".join(board))
                win = True
                break
        else:
            print("You already guessed {}. Pick another letter.".format(guess))
    if not win:
        print("\n".join(stages[0:wrong +1]))
        print("\nYou lose! The word was {}".format(word)) 
                
hangman("kitty")
