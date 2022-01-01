## Each segment of code is commented using " ''' " before and after the code. This is because there are some infinite loops present. Remove ''' around the parts that you'd like to run.


#1. Write a program that prints the name Fred 100 times, one time per line.
'''
for number in range(100):
    print(number, 'Fred')
'''

#2 part 1  (refer to unit04.doc)
'''
import random
def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def wordlist(filename):
    words = []
    with open(filename) as book:
        for line in book:
            for word in cleanedup(line).split():
                if word not in words:
                        words.append(word)
    return words
'''

#2 part 2
'''
def rejoin(characters):
    word = ''
    for character in characters:
        word += character
    return word

def scramble(word):
    mixed = list(word)
    random.shuffle(mixed)
    return rejoin(mixed)
'''

#2 part 3
'''
words = wordlist('pap.txt')

while True:
    word = random.choice(words)
    mixed = scramble(word)
    print('Letters: ', mixed)
    guess = input('Guess the original word: ')
    if guess == word:
        print('Right!')
    else:
        print('Wrong.The right answer is: ', word)
'''

#3 Modify the program so that it gives the user a three-letter puzzle to start and then adjusts the number of letters up by one every time a correct answer is given and down by one for every wrong answer.
'''
import random
def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def wordlists(filename):
    words = {}
    with open(filename) as book:
        for line in book:
            for word in cleanedup(line).split():
                length = len(word)
                if length in words:
                    words[length].append(word)
                else:
                    words[length] = [word]
    return words

def rejoin(characters):
    word = ''
    for character in characters:
        word += character
    return word

def scramble(word):
    mixed = list(word)
    random.shuffle(mixed)
    return rejoin(mixed)

words = wordlists('pap.txt')


level = 3

while True:
    word = random.choice(words[level])
    mixed = scramble(word)
    print('Letters: ', mixed)
    guess = input('Guess the original word: ')
    if guess == word:
        print('Right!')
        level += 1
    else:
        print('Wrong.The right answer is: ', word)
        level -= 1

'''

#4.	Write a program that randomly chooses a hand of five cards from a standard deck of playing cards and displays it for the user to see.
#       Use a function that returns a shuffled deck, ready for dealing.
'''
import random

faceValues = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']

suits = ['clubs', 'diamonds', 'hearts', 'spades']

def shuffledDeck():
    deck = []
    for faceValue in faceValues:
        for suit in suits:
            deck.append(faceValue + ' of ' + suit)
    random.shuffle(deck)
    return deck
'''

#5. Modify the previous program so that, in addition to displaying a five-card hand, it reports the number of aces and the number of clubs in the hand.
#   Use one function to determine the face value, given a string like 'queen of diamonds', and another one to determine the suit.
'''
def faceValueOf(card):
    return card.split()[0]

def suitOf(card):
    return card.split()[2]

d = shuffledDeck()
numberOfAces = 0
numberOfClubs = 0
for number in range(5):
    card = d[number]
    print(card)
    if faceValueOf(card) == 'ace':
        numberOfAces += 1
    if suitOf(card) == 'clubs':
        numberOfClubs += 1

print('Number of aces: ', numberOfAces)
print('Number of clubs: ', numberOfClubs)

'''    

#6. Collect the card-related functions you have written into a module called cards.py and rewrite the previous program so that it begins by importing this module.
'''
import cards

d = cards.shuffledDeck()
numberOfAces = 0
numberOfClubs = 0
for number in range(5):
    card = d[number]
    print(card)
    if cards.faceValueOf(card) == 'ace':
        numberOfAces += 1
    if cards.suitOf(card) == 'clubs':
        numberOfClubs += 1

print('Number of aces: ', numberOfAces)
print('Number of clubs: ', numberOfClubs)

'''














