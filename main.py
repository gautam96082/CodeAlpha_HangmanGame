

import random
from words import words
from hangman_art import hangman_art
import string



def get_valid_word(words):
    word = random.choice(words)  
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  

    attempts_left = 7

    while len(word_letters) > 0 and attempts_left > 0:
      
        print('You have', attempts_left, 'attempts left and you have used these letters:', ' '.join(sorted(used_letters)))


        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(hangman_art[attempts_left])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                attempts_left -= 1  
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

  
    if attempts_left == 0:
        print(hangman_art[attempts_left])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()