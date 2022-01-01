## Each segment of code is commented using " ''' " before and after the code. This is because there are some infinite loops present. Remove ''' around the parts that you'd like to run.

#1. Write and test a function called lengths that takes in a list of strings and returns a list of the lengths of the strings.  If we pass it ['Ed', 'Ted', 'Fred', 'Jennifer'], it will return [2, 3, 4, 8].
#   Your function should use a list comprehension.

'''
def length(strings):
    return [len(s) for s in strings]


names = ['Ed', 'Ted', 'Fred', 'Jennifer']
print(length(names))
'''

#2. Write a program to add Pride and Prejudice to the shelve object that holds Huckleberry Finn.
'''
import shelve

with open('pap.txt') as book:
    lines = book.readlines()

shelf = shelve.open('books')
shelf['Pride and Prejudice'] = lines 
shelf.close()

'''

#3. Use the shelved versions of Pride and Prejudice and Huckleberry Finn to see which of the two novels uses longer words on average.
'''
import my, shelve

def averageWordLength(title):
    shelf = shelve.open('books')
    lines = shelf[title]
    shelf.close()

    number = 0
    totalLength = 0

    for line in lines:
        for word in my.cleanedup(line).split():
            number += 1
            totalLength += len(word)
    return totalLength/number

for title in ['Pride and Prejudice', 'Huckleberry Finn']:
        print(title, averageWordLength(title))
'''

#4.	Use the shelved version of the Consumer Price Index data to find the largest percentage increase in prices ever recorded over the summer months—that is, from May to September—and the year in which it occurred.
#       Your program should use a function to compute the percentage increase.  If a value increases from begin to end, the percentage increase is given by the formula: 100*(end/begin-1)
'''
import shelve

def pctIncrease(begin, end):
    return 100*(end/begin-1)

shelf = shelve.open('cpi')
cpi = shelf['cpi']
shelf.close()

maxIncrease = 0
for year in range(1913,2009):
    increase = pctIncrease(cpi[year][5], cpi[year][9])
    if increase > maxIncrease:
        maxIncrease = increase
        maxYear = year

print(maxYear, maxIncrease)

'''

#5. The web page file http://time.is/New_York contains the current time in New York. Use a web browser to see how the file is meant to look when displayed.
#   Then write a program to read the page, extract the current time and print it.
'''
import urllib.request

url = 'http://time.is/New_York'
book = urllib.request.urlopen(url)
lines = book.readlines()
book.close()

for lines in lines:
    line = line.decode()
    if 'Make New York time default' in line:
        print(line[98:106])
'''

#6. Write a function f that takes in a number x and returns 17.7/(4x2-12x+13).
#   Then write a program that asks the user for two floating point numbers, checks the value of f at 100 evenly spaced points between these two numbers and reports the highest value found.
#   Use the built-in function max, which takes in a list of values and returns the highest.
'''
def f(x):
    return 17.7/(4*x**2-12*x+13)

def xValues(begin, end, number):
    step = (end-begin)/(number-1)
    return [begin+n*step for n in range(number)]

begin = float(input('Enter beginning number: '))
end = float(input('Enter ending number: '))
print(max([f(x) for x in xValues(begin, end,100)]))
'''
