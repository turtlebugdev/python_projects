####Hangman####

import random
hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# word_list = ["aardvark", "baboon", "camel","apple", "mama", "absolute"]
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
chosen_word = random.choice(word_list)
display = []
for letter in chosen_word:
    display.append("_")

print(logo)
print(f"\nWelcome to Hangman\n\nTarget word is: {display}\n")
print(hangmanpics[0])
blank_cnt = display.count("_")
lives = 6
wrongs = 0
guessed = []
while blank_cnt>0 and lives>0:
    guess = input("\nGuess a letter: ").lower()
    ind_cnt = 0
    for letter in chosen_word:
        if guess == letter:
            display[ind_cnt] = guess
        ind_cnt += 1
    new_blank_cnt = display.count("_")
    if new_blank_cnt == blank_cnt:
        lives -= 1
        wrongs += 1
        guessed.append(guess)
    else:
        blank_cnt = new_blank_cnt
    print(f"\nTarget word is: {display}\n")
    print(f"Incorrect guesses: {guessed}")
    print(hangmanpics[wrongs])
if blank_cnt == 0:
    print("\nYou WON!!! Congrats!")
else:
    print(f"\nYou LOST!!! He's dead, Jim...\nThe word was {chosen_word}")
