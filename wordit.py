#nltk.download('wordnet')
#nltk.download('words')
#nltk.download('omw-1.4')

import random
import nltk
from nltk.corpus import words
from nltk.corpus import wordnet
from termcolor import colored

def get_random_word(file):
    with open(file, 'r') as file:
        words = file.read().splitlines()
        return random.choice(words)
    
def print_colored_alphabet(green, yellow, red):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',\
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in alphabet:
        if letter in green:
            letter_colored(letter, 'green')
        elif letter in yellow:
            letter_colored(letter, 'yellow')
        elif letter in red:
            letter_colored(letter, 'red')
        else:    
            print(letter, end=' ')
            
def letter_colored(letter, color, whitespace=True):
    end = ' '
    if not whitespace:
        end = ''
    print(colored(letter, color), end=end)

#nltk.data.path.append('/work/words')
#wordlist = words.words()
#five_letters = set(filter(lambda x: len(x) == 5, wordlist))

again = 'y'

while again == 'y':
    green = []
    yellow = []
    red = []
    word = get_random_word('words.txt').lower()
    #word = random.choice(five_letters).lower()
    count = 0
    print('Type a 5-letter word and press enter: ')
    
    while count <= 6:
        guess = input().lower()
        
        if len(guess) != 5:
            print('You must type a word with 5 letters.')
            continue
            
        if not wordnet.synsets(guess):
            print('This is not a valid word.')
            continue
        else:
            count += 1
            print(f'{count}: ', end='')

        for i in range(5):
            if guess[i] == word[i]:
                if guess[i] not in green or guess.count(guess[i]) > 1:
                    green.append(guess[i])
                elif guess[i] in green and guess.count(guess[i]) == 1:
                    if guess[i] in yellow:
                        yellow.remove(guess[i])
                        print('removed letter from yellowlist')
                letter_colored(guess[i], 'green', whitespace=False)
            elif guess[i] in word:
                if guess[i] not in yellow:
                    yellow.append(guess[i])
                letter_colored(guess[i], 'yellow', whitespace=False)
            else:
                red.append(guess[i])
                letter_colored(guess[i], 'red', whitespace=False)
        '''print()    
        print('after for loop:')
        print(f'greenlist: {green}')
        print(f'yellowlist: {yellow}')'''
                    
        print('\n')   
        if guess == word:
            print(f'Yay! You needed {count} attempts.')  
            print(colored('**********', 'green'))
            break
        elif count == 6:
            print('Bad luck. No more attempts left.')
            print(f'The word is {word}')
            print(colored('----------', 'red'))
            break
        else:
            print_colored_alphabet(green, yellow, red)
        print('\n')   

    again = input('Type "y" to play again. Press any other key to quit.\n')

