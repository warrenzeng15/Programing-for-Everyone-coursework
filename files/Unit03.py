## Each segment of code is commented using " ''' " before and after the code. This is because there are some infinite loops present. Remove ''' around the parts that you'd like to run.

#0.1.	Write a program that prompts for input of a username and password and then displays an appropriate message, depending on whether these match.
#       Use a dictionary to hold the usernames and associated passwords.  
'''
passwords = {'asdf':'1234', 'zxcv':'4321'}
username = input('Enter username: ')
password = input('Enter password: ')
if password == passwords[username]:
    print('You are logged in.')
else:
    print('Bad password.')
'''

#0.2.	Write a program that builds a word-line concordance for Pride and Prejudice and tests it using one or more look-ups included in the program code.
#       Use split as a rough method for breaking lines into word.
'''
concordance = {}
with open('pap.txt') as book:
    linenum = 1
    for line in book:
        for word in line.split():
            if word in concordance:
                concordance[word].append(linenum)
            else:
                concordance[word] = [linenum]
        linenum += 1
print('Test: ', concordance['he'])


'''

#0.3.	Revise the concordance program to allow a user to interactively look up as many words as desired.
'''
concordance = {}
with open('pap.txt') as book:
    linenum = 1
    for line in book:
        for word in line.split():
            if word in concordance:
                concordance[word].append(linenum)
            else:
                concordance[word] = [linenum]
        linenum += 1

while True:
    word = input('Enter word: ')
    if word in concordance:
        print('Word found on lines:', concordance[word])
    else:
        print('Word not found')
'''


#0.4.	Revise the concordance program to use a more sophisticated method of breaking lines into words:
#       convert uppercase letters to lowercase and replace non-alphabetic characters with spaces before using split.

'''
alphabet = 'abcdefghijklmnopqrstuvwxyz'

concordance = {}
with open('pap.txt') as book:
    linenum = 1
    for line in book:
        cleanline = ''
        for character in line.lower():
            if character in alphabet:
                cleanline += character
            else:
                cleanline += ' '
        for word in cleanline.split():
            if word in concordance:
                concordance[word].append(linenum)
            else:
                concordance[word] = [linenum]
        linenum += 1

while True:
    word = input('Enter word: ')
    if word in concordance:
        print('Word found on lines:', concordance[word])
    else:
        print('Word not found')
'''



#0.5.	Revise the concordance program by moving the text clean-up code into a function
#       and then calling that function before the application of split.

'''
def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleanline = ''
    for character in line.lower():
        if character in alphabet:
            cleanline += character
        else:
            cleanline += ' '
    return cleanline

concordance = {}
with open('pap.txt') as book:
    linenum = 1
    for line in book:
        for word in cleanedup(line).split():
            if word in concordance:
                concordance[word].append(linenum)
            else:
                concordance[word] = [linenum]
        linenum += 1

while True:
    word = input('Enter word: ')
    if word in concordance:
        print('Word found on lines:', concordance[word])
    else:
        print('Word not found')

'''


#1.	Reuse the cleanedup function in a program that finds the longest word used in Pride and Prejudice.
#       Note that if you use split without cleanedup, your program will find ‘inconveniences--cheerfulness’, which is long, but not a single word.

'''
def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleanline = ''
    for character in line.lower():
        if character in alphabet:
            cleanline += character
        else:
            cleanline += ' '
    return cleanline

with open('pap.txt') as book:
    maxlength = 0
    for line in book:
        for word in cleanedup(line).split():
            length = len(word)
            if length > maxlength:
                maxlength = length
                finalword = word
    print(finalword)

'''


#2.	Write a program that learns vocabulary in a language other than English.
#       It asks the user for words in English, gives the translation if it has seen the word before and, if not, asks the user to enter it.

'''
dictionary = {}

while True:
    english = input('Enter english word: ')
    if english in dictionary:
        print(english, '=', dictionary[english])
    else:
        trans = input('Enter translation: ')
        dictionary[english] = trans
    print()

'''

#3.	Write a program that compiles information on the number of occurrences of each word used in Pride and Prejudice.
#       After the information is compiled, the user should be able to quickly find out how many times any particular words are used.

'''
def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleanline = ''
    for character in line.lower():
        if character in alphabet:
            cleanline += character
        else:
            cleanline += ' '
    return cleanline

occurrences = {}
with open('pap.txt') as book:
    maxlength = 0
    for line in book:
        for word in cleanedup(line).split():
            if word in occurrences:
                occurrences[word] += 1
            else:
                occurrences[word] = 1
while True:
    word = input('Enter word: ')
    if word in occurrences:
        print(word, 'was used', occurrences[word], 'times.')
    else:
        print('Word was not found')
'''

#4.	Write a program that prints the name Fred 100 times, one time per line.
'''
count = 1
while True:
    if count <= 100:
        print(count, 'Fred')
        count += 1

'''
    
#5.	Write a program that repeatedly gets a group of numbers from the user and displays the average.
#       Define and use a function called average that takes in a list of numbers and returns the average.  
'''
def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total/len(numbers)

while True:
    text = input('Enter numbers: ')
    usernumbers = []
    for word in text.split():
        usernumbers.append(int(word))
    print('Average: ', average(usernumbers))


'''

#6.	Write a function called lengths that takes in a list of strings and returns a list of the lengths of the strings.  If we pass it ['Ed', 'Ted', 'Fred', 'Jennifer'], it will return [2, 3, 4, 8].
#Use this function, along with the average function from the previous program and the cleanedup function, to write a program that accepts sentences from the user and reports the average length of the words in the sentence.

#Other than the function definitions, your program should contain only the following code:
#while True:
#    line = input('Enter a sentence: ')
#    words = cleanedup(line).split()
#    print('Average word length:', average(lengths(words)))


'''
def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleanline = ''
    for character in line.lower():
        if character in alphabet:
            cleanline += character
        else:
            cleanline += ' '
    return cleanline

def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total/len(numbers)

def lengths(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths
        

while True:
    line = input('Enter a sentence: ')
    words = cleanedup(line).split()
    print('Average word length:', average(lengths(words)))
    
'''









