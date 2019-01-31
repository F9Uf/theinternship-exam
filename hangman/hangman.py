# -------------- import ----------------#
import os, platform, re
from time import sleep
from random import randint
# ---------- class of game ------------ #
class hangman(object):
    def __init__(self):
        self.word = ''
        self.hint = ''
        self.score = 0
        self.isOver = False
        self.categories = ['animal', 'fruit', 'football-player'] # <== if you add new category, you shold add file name here
        self.catSelect = ''
    
    def reGame(self):
        self.word = ''
        self.hint = ''
        self.score = 0
        self.isOver = False
        self.catSelect = ''

    def reScreen(self):
        # check os to run command to reScreen for each os
        if platform.system() == 'Windows':
            os.system('cls') 
        else:
            os.system('clear')
        # print UI Title
        print('#######################################')
        print('#            Hangman Game             #')
        print('#######################################\n')

    def gameOver(self):
        self.isOver = True

    def gameLoop(self):

        while not self.isOver:
            self.reScreen()
            # loop for show all category
            print('Select number of category')

            for catIndex in range(len(self.categories)):
                print(f'\t- [{catIndex}] {self.categories[catIndex]}')
            print('\t- [99] Exit')

            # handle input from user
            try:
                userSelect = int(input('\nYour choice is: '))

                if len(self.categories) > userSelect >= 0:
                    # if correct input
                    self.catSelect = self.categories[userSelect]
                    self.gameControl()
                    
                elif userSelect == 99:
                    # if user want to exit
                    print('Thank you for play :)')
                    self.gameOver()
                else:
                    # if it isn't correct input
                    print('Please enter correct input!!')
                    sleep(1)
            except ValueError:
                print('Your input is Invalid!!')
                self.gameOver()

        print('End Program..')

    def gameControl(self):
    
        self.getWord()
        self.getHangman()
        
        wrongCount = 0
        wrongLimit = 6
        wrongWord = []
        isWin = False
        hideWord = list(re.sub(u'[a-zA-Z]', '_', self.word))

        while wrongCount<wrongLimit and not isWin:
            self.reScreen()
            print(f'Category: {self.catSelect}')
            print(f'Hint: {self.hint}')
            print(f'Wrong Words: {wrongWord}')
            print(*self.human[wrongCount], sep='\n')

            if ''.join(hideWord) == self.word and wrongCount<=wrongLimit: # if win
                isWin = True
            elif wrongCount<wrongLimit:
                print('\n\t' + ' '.join(hideWord))
                userGuess = input('\nGuess a Character > ')

                if len(userGuess) == 1 and userGuess.lower() in self.word.lower():
                    # if it's one char and in key word
                    for w in range(len(self.word)):
                        if self.word[w].lower() == userGuess.lower():
                            hideWord[w] = self.word[w] 
                elif len(userGuess) == 1:
                    # if it's one char and not match
                    wrongWord.append(userGuess)
                    wrongCount += 1
            
        self.score = 0 if 100 - (wrongCount * 16) <= 0 else 100 - (wrongCount * 16.67)
        if isWin:
            self.reScreen()
            print(f'\nYou\'re win. This word is {self.word}')
        else:
            self.reScreen()
            print(f'\nOhh! You lose. This word is {self.word}. You can try agin:(')

        print(f'Your Score is {self.score}/100')

        if input('\nDo you want to play again? [y/n] ').lower() == 'y':
            print('Waiting for new game...')
            sleep(1)
        else:
            self.gameOver()
            print('Waiting for end game...')
            sleep(1)

    def getWord(self):
        try:
            with open(f'./category/{self.catSelect}.txt') as file:
                # trim \n and white space
                data = list(map(lambda x: x.strip(), file.readlines())) 
                # random word
                self.word , self.hint = data[randint(0, len(data))].split('|')
        except IOError:
            print('Read file error!')
            self.gameOver()
    
    def getHangman(self):
        self.human = [
            [
                '\t---------',
                '\t|       |',
                '\t|        ',
                '\t|        ',
                '\t|        ',
                '\t|_________'
            ],
            [
                '\t---------',
                '\t|       |',
                '\t|      ( )',
                '\t|         ',
                '\t|         ',
                '\t|_________'
            ],
            [
                '\t---------',
                '\t|       |',
                '\t|      ( )',
                '\t|       | ',
                '\t|         ',
                '\t|_________'
            ],
            [
                '\t---------',
                '\t|       |',
                '\t|      ( )',
                '\t|      /| ',
                '\t|          ',
                '\t|_________'
            ],
            [
                '\t---------',
                '\t|       |',
                '\t|      ( )',
                '\t|      /|\\',
                '\t|         ',
                '\t|_________'
            ],
            [
                '\t---------',
                '\t|       |',
                '\t|      ( )',
                '\t|      /|\\',
                '\t|      /  ',
                '\t|_________'
            ],
            [
                '\t---------',
                '\t|       |',
                '\t|      ( )',
                '\t|      /|\\',
                '\t|      / \\',
                '\t|_________'
            ]
        ]


if __name__ == "__main__":
    game = hangman()
    game.gameLoop()