# Part 1


#1
def Nchar(user_input):
    length = len(user_input)
    print('Your name is', length, 'characters long.')
    return length

#2
def Lchar(user_input, length):
    print('The last character is :', user_input[length - 1])

#3
def findE(user_input): # Return 0 if e is not found
    for i in range(len(user_input)):
        if user_input[i] == 'e':
            print()
            print(f'The first \'e\' is at position {i + 1}.')
            break

#4
def Nwords(user_input):
    count = 1
    for i in range(len(user_input)):
        if user_input[i] == ' ':
            count += 1
    print('Your name has', count, 'words.')
#5
def Fword(user_input):
    for i in range(len(user_input)):
        if user_input[i] == ' ':
            print(f'Your first name is {user_input[0:i]}.')
            break

#6
def Nvowels(user_input):
    count = 0
    for i in range(len(user_input)):
        if user_input[i] == 'A':
            count += 1
        elif user_input[i] == 'a':
            count += 1
        elif user_input[i] == 'E':
            count += 1
        elif user_input[i] == 'e':
            count += 1
        elif user_input[i] == 'I':
            count += 1
        elif user_input[i] == 'i':
            count += 1
        elif user_input[i] == 'O':
            count += 1
        elif user_input[i] == 'o':
            count += 1
        elif user_input[i] == 'U':
            count += 1
        elif user_input[i] == 'u':
            count += 1
    print('Your name contains', count, 'vowels.')

#7
def Cap_vowels(user_input):
    New_user = ''
    New_user = user_input.lower()
    New_user = New_user.replace('a','A')
    New_user = New_user.replace('e', 'E')
    New_user = New_user.replace('i', 'I')
    New_user = New_user.replace('o', 'O')
    New_user = New_user.replace('u', 'U')
    print('Your name with uppercase vowels is:', New_user)

#8
def center(user_input):
    user_input = user_input.center(50, '~')
    user_input = user_input.center(70, '+')
    print(user_input)

#9
def split(user_input):
    x = len(user_input)
    y = x // 2
    z = 70 - x
    a = x - y
    user1 = user_input[0:y]
    user2 = ''
    for i in range(z):
        user2 += '*'
    user3 = user_input[a - 1:]
    print(user1 + user2 + user3)

#John Jacob Jingleheimer Schmidt

user_input = input('Please enter your name: ')
print()

#1
length = Nchar(user_input)
print()

#2
Lchar(user_input, length)

#3
findE(user_input)
print()

#4
Nwords(user_input)
print()

#5
Fword(user_input)
print()

#6
Nvowels(user_input)
print()

#7
Cap_vowels(user_input)
print()

#8
center(user_input)
print()

#9
split(user_input)


print()
# Part 2

#A
def mirror(speech):
    reverse = speech.replace(speech[0:], speech[::-1])
    combined = speech + reverse
    print(combined)

#B
def remove(speech):
    speech = speech.replace('E', '')
    speech = speech.replace('e', '')
    print(speech)

#C
def char_num(speech):
    count = 0
    for i in range(len(speech)):
        if speech[i].isalpha():
            count += 1
    x = count
    count = 0
    for i in range(len(speech)):
        if speech[i] == 'e':
            count += 1
    z = (count / x) * 100
    z = round(z, 1)
    print(f'Your text contains {x} alphabetic characters, of which {count} ({z}%) are \'e\'.')

#D
def char_num_mod(speech, user_char):
    count = 0
    for i in range(len(speech)):
        if speech[i].isalpha():
            count += 1
    x = count
    count = 0
    for i in range(len(speech)):
        if speech[i] == user_char:
            count += 1
    z = (count / x) * 100
    z = round(z, 1)
    print(f'Your text contains {x} alphabetic characters, of which {count} ({z}%) are \'{user_char}\'.')

#E
def no_e(user_word):
    e = ''
    for i in range(len(user_word)):
        if user_word[i] == 'e':
            e = False
    if e != False:
        return True

#F
def no_e_mod(user_word, user_char):
    x = ''
    for i in range(len(user_word)):
        if user_word[i] == user_char:
            x = False
    if x != False:
        return True

#G
def speech_no_e(speech):
    first = False
    y = ''
    for i in range(len(speech)):
        if (speech[i] == ' ' or speech[i] == '.') and first == False:
            count = 0
            x = speech[0:i]
            test = True
            for j in range(len(x)):
                if x[j] == 'e':
                    test = False
            if test == True and x[1:].isalpha():
                y += x
            first = True
        elif (speech[i] == ' ' or speech[i] == '.') and first == True:
            x = speech[z:i]
            test = True
            for k in range(len(x)):
                if x[k] == 'e':
                    test = False
            if test == True and x[1:].isalpha():
                y += x
                count += 1
        if speech[i] == ' ':
            z = i
    print(y[1:])
    print()
    print('There are', count, 'words with no \'e\'.')

#H
def avoids(user_word, string_letters):
    x = True
    for i in range(len(string_letters)):
        for j in range(len(user_word)):
            if user_word[j] == string_letters[i]:
                x = False
                return False
    if x == True:
        return True

#I
def uses_only(user_word, string_letters):
    count = 0
    for i in range(len(user_word)):
        for j in range(len(string_letters)):
            if user_word[i] == string_letters[j]:
                count += 1
    x = len(user_word)
    if count == x:
        return True

    elif count != x:
        return False

#J
def uses_all(user_word, string_letters):
    count = 0
    for i in range(len(string_letters)):
        for j in range(len(user_word)):
            if user_word[j] == string_letters[i]:
                count += 1
                break
    x = len(string_letters)
    if count == x:
        return True

    elif count != x:
        return False

#K
def is_abecedarian(user_word):
    count = 0
    letters = 0
    alphabetical_order = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(user_word)):
        for j in range(len(alphabetical_order)):
            if user_word[i] == alphabetical_order[j]:
                if count >= 1:
                    if x <= j:
                        letters += 1
                x = j
                count += 1
    if letters + 1 == len(user_word):
        return True

    else:
        return False

#L
def find(speech, user_char):
    print(speech.find(user_char))

#M
def find_mod(speech, user_char, index):
    print(speech.find(user_char, index))

#N
def is_sorted(speech):
    sorted_speech = sorted(speech.split())
    speech = speech.split()
    if sorted_speech == speech:
        return True
    else:
        return False

#O
def is_anagram(user_word, user_word2):
    test = True
    if len(user_word) != len(user_word2):
        test = False
    count = 0
    for i in range(len(user_word)):
        for j in range(len(user_word2)):
            if user_word[i] == user_word2[j]:
                count += 1
                break
    if count == len(user_word) and test != False:
        return True
    else:
        return False

#P
def has_duplicates(user_word):
    x = user_word
    count = 0
    for i in range(len(user_word)):
        for j in range(len(x)):
            if user_word[i] == x[j]:
                count += 1
    if count > len(user_word):
                return True


#Q
def remove_duplicates(user_word):
    x = ''
    for i in user_word:
        if i not in x:
            x = x + i
    return x



#For functions A,B,C,D,G,L,M,N
speech = '''We observe today not a victory of party but a celebration of 
freedom symbolizing an end as well as a beginning signifying renewal as 
well as change. For I have sworn before you and Almighty God the same 
solemn oath our forbears prescribed nearly a century and three-quarters ago.'''

#For functions D,F,L,M
user_char = input('Enter a letter: ')

#For functions E,F,H,I,J,K,O,P,Q
user_word = input('Enter a word: ')

#For functions O
user_word2 = input('Enter a word: ')

#For functions H,I,J
string_letters = input('Enter a string of letters: ')

#For function M
index = int(input('Enter a number for the start of the index to find your character: '))

#A
print()
print('Function A, Original and reversed string')
print()
mirror(speech)
print()

#B
print('Function B, removes e and E from the string')
print()
remove(speech)
print()

#C
print('Function C, counts letters and checks how many are e')
print()
char_num(speech)
print()

#D
print('Function D, counts letters and checks how many are user_char')
print()
char_num_mod(speech, user_char)
print()

#E
print('Function E, returns true if the word doesn\'t have e')
print()
no_E = no_e(user_word)
print(no_E)
print()

#F
print('Function F, returns true if the word doesn\'t have user_char')
print()
no_E_mod = no_e_mod(user_word, user_char)
print(no_E_mod)
print()

#G
print('Function G, prints words that have no e and the percent of words without it')
print()
speech_no_e(speech)
print()

#H
print('Function H, checks if user_word doesn\'t use string_letters')
print()
Avoids = avoids(user_word, string_letters)
print(Avoids)
print()

#I
print('Function I, checks if user_word only uses letters from string_letters')
print()
Uses_only = uses_only(user_word, string_letters)
print(Uses_only)
print()

#J
print('Function J, checks if user_word has all letters in string_letters')
print()
Uses_all = uses_all(user_word, string_letters)
print(Uses_all)
print()

#K
print('Function K, checks if user_word has the letters in alphabetical order')
print()
is_Abecedarian = is_abecedarian(user_word)
print(is_Abecedarian)
print()

#L
print('Function L, character index of user_char')
print()
find(speech, user_char)
print()

#M
print('Function M, character index of user_char with starting point index')
print()
find_mod(speech, user_char, index)
print()

#N
print('Function N, returns true or false depending on if a string is sorted in ascending order')
print()
is_Sorted = is_sorted(speech)
print(is_Sorted)
print()

#O
print('Function O, returns true or false if two strings are anagrams')
print()
is_Anagram = is_anagram(user_word, user_word2)
print(is_Anagram)
print()

#P
print('Function P, returns true if a letter is repeated in user_word')
print()
has_Duplicates = has_duplicates(user_word)
print(has_Duplicates)
print()

#Q
print('Function Q, returns a new string without duplicate letters from user_word')
print()
remove_Duplicates = remove_duplicates(user_word)
print(remove_Duplicates)
print()
