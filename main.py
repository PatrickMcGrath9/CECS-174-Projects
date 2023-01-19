correctL = True
correctV = False

user_input1 = input('Enter the customer\'s code: ')
if user_input1 != 'r' and user_input1 != 'R' and user_input1 != 'c' and user_input1 != 'C' and user_input1 != 'i' and user_input1 != 'I':
    correctL = False
    print('Error. You did not use a correct letter.')


elif correctL == True:
    user_input2 = int(input('Enter the customer\'s beginning meter reading: '))
    user_input3 = int(input('The customer\'s ending meter reading: '))

min = 0
max = 999999999

amountbilled1 = 0

gallonsofwater = 0

priceofgallons1 = .0005
priceofgallons2 = .00025

if user_input1 == 'r' or user_input1 == 'R':
    if user_input2 < user_input3 and user_input2 >= min and user_input2 <= max and user_input3 >= min and user_input3 <= max:
        gallonsofwater = (user_input3 - user_input2) / 10
        amountbilled1 = 5 + (priceofgallons1 * gallonsofwater)
        correctV = True
    elif user_input3 < user_input2 and user_input2 >= min and user_input2 <= max and user_input3 >= min and user_input3 <= max:
        gallonsofwater = ((1000000000 - user_input2) + user_input3) / 10
        amountbilled1 = 5 + (priceofgallons1 * gallonsofwater)
        correctV = True

elif user_input1 == 'c' or user_input1 == 'C':
    if user_input2 < user_input3 and user_input2 >= min and user_input2 <= max and user_input3 >= min and user_input3 <= max:
        gallonsofwater = (user_input3 - user_input2) / 10
        amountbilled1 = 1000
        correctV = True
        if gallonsofwater > 4000000:
            amountbilled1 = amountbilled1 + (priceofgallons2 * gallonsofwater)
    elif user_input3 < user_input2 and user_input2 >= min and user_input2 <= max and user_input3 >= min and user_input3 <= max:
        gallonsofwater = ((1000000000 - user_input2) + user_input3) / 10
        amountbilled1 = 1000
        correctV = True
        if gallonsofwater > 4000000:
            amountbilled1 = amountbilled1 + (priceofgallons2 * gallonsofwater)

elif user_input1 == 'i' or user_input1 == 'I':
    if user_input2 < user_input3 and user_input2 >= min and user_input2 <= max and user_input3 >= min and user_input3 <= max:
        gallonsofwater = (user_input3 - user_input2) / 10
        correctV = True
        if gallonsofwater < 4000000:
            amountbilled1 = 1000
            amountbilled1 = amountbilled1 + (priceofgallons2 * gallonsofwater)
        elif gallonsofwater > 4000000 and gallonsofwater < 10000000:
            amountbilled1 = 2000
        elif gallonsofwater > 10000000:
            amountbilled1 = 2000 + (priceofgallons2 * gallonsofwater)
    elif user_input3 < user_input2 and user_input2 >= min and user_input2 <= max and user_input3 >= min and user_input3 <= max:
        gallonsofwater = ((1000000000 - user_input2) + user_input3) / 10
        correctV = True
        if gallonsofwater < 4000000:
            amountbilled1 = 1000
        elif gallonsofwater > 4000000 and gallonsofwater < 10000000:
            amountbilled1 = 2000
        elif gallonsofwater > 10000000:
            amountbilled1 = 2000 + (priceofgallons2 * gallonsofwater)

if correctV == True:
    print()
    print('Customer code:', user_input1)

    user_input2 = '{:0>9}'.format(user_input2)
    print('Beginning meter reading:', user_input2)

    user_input3 = '{:0>9}'.format(user_input3)
    print('Ending meter reading:   ', user_input3)

    print('Gallons of water used:', gallonsofwater)

    print('Amount billed: $', end = '')
    print('{:.2f}'.format(amountbilled1))

else:
    print('Values out of range.')
