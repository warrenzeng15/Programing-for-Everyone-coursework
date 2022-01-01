## Each segment of code is commented using " ''' " before and after the code. This is because there are some infinite loops present. Remove ''' around the parts that you'd like to run.


#1.  Write a program that prints the name Fred 100 times, one time per line.
#    Do not use for or while.  Instead, create a function called printFred that takes in a number and prints Fred that number of times.
#    The function operates by displaying the name Fred once and then calling itself with the next smaller number, if that number is at least one.
#    The call printFred(100) should do what we want.
'''
def printFred(times):
    print(times, 'Fred')
    if times-1 > 0:
        printFred(times-1)

printFred(100)

'''

#2. Write a program that lists all files in the current directory that contain the string 'random'.
'''
import os

def contains(filename, pattern):
    with open(filename) as file:
        for line in file:
            if pattern in line:
                return True
    return False        

for filename in os.listdir('.'):
    if contains(filename, 'random'):
        print(filename, 'contains random')
'''

#3. Write a program that reports the total number of files in the current directory and any subdirectories, subsubdirectories and so on.
'''
import os
def counter(path):
    count = 0
    for filename in os.listdir(path):
        newpath = os.path.join(path, filename)
        if os.path.isdir(newpath):
            count += counter(newpath)
        else:
            count += 1
    return count

print(counter('.'))

'''

#4. Write a program that solves the word-scramble puzzles produced by Program 2 in Unit 4.
#   The user enters a scrambled string of letters and the program responds by displaying all words in Pride and Prejudice that can be formed by rearranging these letters.
'''
import my

def alphabetize(s):
    letters = list(s)
    letters.sort()
    return my.rejoin(letters)


unscramble = {}

with open('pap.txt') as book:
    for line in book:
        for word in my.cleanedup(line).split():
            key = alphabetize(word)
            if key in unscramble:
                if word not in unscramble[key]:
                    unscramble[key].append(word)
            else:
                unscramble[key] = [word]
                        
puzzle = input('Puzzle: ')
key = alphabetize(puzzle)
if key in unscramble:
    print(unscramble[key])
else:
    print('No answer found')

'''

#5. Write a program to find the five most common words in Pride and Prejudice ending with ‘ing’.  
'''
import my

counts = {}

with open('pap.txt') as book:
    for line in book:
        for word in my.cleanedup(line).split():
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
ingWords = []

for word in counts:
    if word[-3:] == 'ing':
        ingWords.append([counts[word],word])

ingWords.sort()
print(ingWords[-5:])
'''

#6  Write a program to choose a random five-card hand from a standard deck and then report if it is a one-pair hand, a two-pair hand, a three-of-a-kind hand, a full house, or a four-of-a-kind hand.

'''
import cards

def evaluate(hand):
    fvCounts = {}
    for card in hand:
        fv = cards.faceValueOf(card)
        if fv in fvCounts:
            fvCounts[fv] += 1
        else:
            fvCounts[fv] = 1
    justCounts =[]
    for fv in fvCounts:
        justCounts.append(fvCounts[fv])
    justCounts.sort()
    if justCounts == [1,1,1,2]:
        return 'one pair'
    if justCounts == [1,2,2]:
        return 'two pair'
    if justCounts == [1,1,3]:
        return 'three of a kind'
    if justCounts == [2,3]:
        return 'full house'
    if justCounts ==[1,4]:
        return 'four of a kind'
    return 'high card'

hand = cards.shuffledDeck()[:5]
print(hand)
print(evaluate(hand))

'''
