
import re
import json

with open("animals.json") as f:
    animals = json.load(f)

animals = sorted(animals)


def binary_search(list, item):  # Binary_search algorithm
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return guess

# Three-letter animal word game


sign_attempts_list = []
score_list = []
attempts_list = []
game_word_attempts_list = []
repeat_animal_list = []


def start_game():
    g = 0
    word = ''
    sign_attempts = 0
    attempts = 0
    score = 0

    game_on = True
    while (word != 'y') and (game_on == True):
        sign_attempts += 1
        sign_attempts_list.append(sign_attempts)

        if len(sign_attempts_list) == 4:
            print('You have only 2 more attempts to enter a valid response!')
        if len(sign_attempts_list) == 6:
            print('All 5 chances to start game have been exhausted')
            break

        print("This is a word game. Do you want to play?")
        word = input("Please enter Y for Yes or N for No ")
        word = word.lower()
        if word == 'n':
            print("See you some other time!")
            break

        for j in word:
            if j == 'y':
                name = input("Please enter your name to begin the game ")
                print('Welcome {} to this word game'.format(name))

                while len(attempts_list) < 11:
                    if len(attempts_list) == 10:
                        print('End of tenth attempt.The game has ended.')
                        print('You had a SCORE of ' + str(len(score_list)) + ' out of 10 attempts')
                        game_on = False
                        break

                    game_word = input('Please enter a three-letter word. Only animal names count! ')

                    if game_word == '':
                        attempts += 1
                        attempts_list.append(attempts)
                        print("You did not enter anything!")
                    else:
                        if re.search(game_word, '[0123456789]'):
                            attempts += 1
                            attempts_list.append(attempts)
                            if len(attempts_list) == 10:
                                print("Sorry, numbers are not allowed")
                            else:
                                if len(attempts_list) < 10:
                                    print("Not really! Please don't enter a number. It's a three-letter word game!")
                                    continue

                    # if not type(game_word) is str:
                    # raise TypeError("Please enter alphabets only!")
                    binary_search(animals, game_word)

                    # Checking to see if length of entered word is greater than null and equal to 3
                    if len(game_word) > 0 and len(game_word) != 3:
                        attempts += 1
                        attempts_list.append(attempts)
                        if len(attempts_list) < 10:
                            print('Enter a three-letter animal word!')

                        # Only three attempts are allowed to enter a three-letter word
                        g += 1
                        game_word_attempts_list.append(g)
                        if len(game_word_attempts_list) == 3:
                            print('A valid three-letter word is required.')
                            continue

                    # Checking to see if entered word is in animals
                    if (game_word in animals) and len(game_word) == 3:
                        attempts += 1
                        attempts_list.append(attempts)
                        repeat_animal_list.append(game_word)
                        if repeat_animal_list.count(game_word) > 1:  # If a word has been entered more than once
                            print('You have already received a score for this word.')

                        else:  # If entered is a three-letter word and in animals list
                            score += 1
                            score_list.append(score)
                            print('Great! You got it right!')

                    else:
                        if game_word not in animals and (len(game_word) == 3):
                            print("Oh no! That's wrong!")
            else:
                print('Please enter a valid response.')


if __name__ == '__main__':
    start_game()

