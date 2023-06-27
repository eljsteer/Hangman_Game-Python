#Hangman Game

## PseudoCode
## STEPS ##

# 1. Computer picks out random word
# 2. Computer counts # of letters in word and draws lines.
# 3. Computer draws Gallows and guesses remaining.
# 4. User types letter to guess letter in word
# 5. Computer reads input and checks it against word for match.
# 6. If letter in word.
# write letter in word where it is placed
# else draw next piece on hangman and countdown guesses remaining.

#________________________________________________________________________
# --> Phase 1 <-- #

import random
import Hangman_stages

word_list = ["aardvark", "baboon", "camel"]

end_of_game = False
incorrect_guess_round = 0
letters_guessed = []
chosen_word = random.choice(word_list)
list_chosen_word = list(chosen_word)
word_length = len(chosen_word)

# Setting Word to # of blank lines
display_word = []
for _ in range(word_length):
    display_word += "_"

print("WELCOME TO PYTHON HANGMAN!\n")
print(f"The word is {word_length} letters long \n")
print(*display_word)

while not end_of_game:
    if display_word == list_chosen_word:
        print("\n ***_You Win_***")
        end_of_game = True
        break
    elif incorrect_guess_round == len(Hangman_stages.stages)-1:
        end_of_game = True
    else:
        user_guess = (input("\nPlease guess a letter between a - z:  ")).lower()
        if user_guess in letters_guessed:
            print(f'You have already guessed: "{user_guess}" before, please guess another letter')
            continue
        else:
            letters_guessed.append(user_guess)
            if user_guess in list_chosen_word:
                for position in range(word_length):
                    letter = chosen_word[position]
                    if user_guess == letter:
                        display_word[position] = letter
                print(*display_word)
            else:
                incorrect_guess_round += 1
                print(Hangman_stages.stages[incorrect_guess_round])
                print(f"\nIncorrect Guess, {user_guess} is not in this word")
            
else:
    print(f'\n***GAME OVER YOU LOSE***\n\n The word is: "{chosen_word}"')