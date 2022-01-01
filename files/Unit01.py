'''
0.1.	Write a program that produces the following output:
Hello Fred
Hello Ted
Hello Ed
'''

students = ['Fred', 'Ted', 'Ed']
for student in students:
    print('Hello', student)


'''
0.2.	Write a program that produces the following output:
ham on rye
ham on whole wheat
ham on a roll
pastrami on rye
pastrami on whole wheat
pastrami on a roll
roast beef on rye
roast beef on whole wheat
roast beef on a roll
chicken on rye
chicken on whole wheat
chicken on a roll

'''

meats = ['ham','pastrami','roast beef','chicken']
breads = ['rye','whole wheat','roll']
for meat in meats:
    for bread in breads:
        print(meat, 'on', bread)

'''
1.	Write a program that prints the letters in the alphabet, one per line.
'''

for letter in 'abcdefghijklmnopqrstuvwxyz':
    print(letter)

'''
2.	The word ‘substantiate’ contains the word ‘ant’.
Write a program that reports which of the following words is contained in
‘substantiate’: ‘ate’, ‘state’, ‘a’, ‘substantiate’, ‘it’, ‘tan’.
The output should look like this:

ate is a substring of substantiate
a is a substring of substantiate
substantiate is a substring of substantiate
tan is a substring of substantiate
'''
    
substrings = ['ate','state','a','substantiate','it','tan']
word = 'substantiate'
for substring in substrings:
    if substring in word:
        print(substring, 'is a substring of', word)


'''
3.	Write a program that prints the name Fred 100 times, one time per line.
Your program should be reasonably short and should not include a list containing more than ten items
or a string containing more than ten characters.

'''

tenDashes = '----------'
for y in tenDashes:
    for x in tenDashes:
        print('Fred')



'''
4.	Write a program that counts down from 10 to 1
'''
numbers = [10,9,8,7,6,5,4,3,2,1]
for number in numbers:
    print(number)


'''
5.	Write a program that tells us which vowels are used in each of the following words: ‘apple’, ‘banana’, ‘peach’, ‘grapefruit’.
The output should look like this:

Vowels in apple
a
e
Vowels in banana
a
Vowels in peach
a
e
Vowels in grapefruit
a
e
i
u
'''

vowels = 'aeiou'
words = ['apple', 'banana', 'peach', 'grapefruit']
for word in words:
    print('Vowels in', word)
    for vowel in vowels:
        if vowel in word:
            print(vowel)

       
































