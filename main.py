print('Welcome to the vending machine change maker program')
print('Change maker initialized.')

n = 25
d = 25
q = 25
o = 0
f = 0

print()
print('Stock contains:')

if n < 100 and n >= 10:
    print('{:>5}'.format(n), 'nickels')
else:
    print('{:>4}'.format(n), 'nickels')

if d < 100 and d >= 10:
    print('{:>5}'.format(d), 'dimes')
else:
    print('{:>4}'.format(d), 'dimes')

if q < 100 and q >= 10:
    print('{:>5}'.format(q), 'quarters')
else:
    print('{:>4}'.format(q), 'quarters')

if o < 100 and o >= 10:
    print('{:>5}'.format(o), 'ones')
else:
    print('{:>4}'.format(o), 'ones')

if f < 100 and f >= 10:
    print('{:>5}'.format(f), 'fives')
else:
    print('{:>4}'.format(f), 'fives')

Price = 0
payment = 0
deposit = 0
dollars = 0
cents = 0
qowed = 0
dowed = 0
nowed = 0
absPrice = 0
total = 0


print()
Price = input('Enter the purchase price (xx.xx) or \'q\' to quit: ')
while Price != 'q' or Price == 0:
    Price = float(Price)
    hunPrice = Price * 100
    if hunPrice % 5 != 0 or hunPrice < 0:
        print('Illegal price: Must be a non-negative multiple of 5 cents.\n')
        Price = input('Enter the purchase price (xx.xx) or \'q\' to quit: ')
        continue

    else:
        print()
        print('Menu for deposits:')
        print('{:>1}'.format(''), '\'n\' - deposit a nickel')
        print('{:>1}'.format(''), '\'d\' - deposit a dime')
        print('{:>1}'.format(''), '\'q\' - deposit a quarter')
        print('{:>1}'.format(''), '\'o\' - deposit a one dollar bill')
        print('{:>1}'.format(''), '\'f\' - deposit a five dollar bill')
        print('{:>1}'.format(''), '\'c\' - cancel the purchase\n')

        while Price > 0 and deposit != 'c':
            dollars = Price // 1
            cents = (Price % 1) * 100
            if Price >= 1:
                print('Payment due:', round(dollars), 'dollar(s) and', round(cents), 'cents')
            else:
                print('Payment due:', round(cents), 'cents')
            deposit = input('Indicate your deposit: ')
            if deposit == 'n':
                Price -= 0.05
                n += 1
                payment += 0.05
            elif deposit == 'd':
                Price -= 0.10
                d += 1
                payment += 0.10
            elif deposit == 'q':
                Price -= 0.25
                q += 1
                payment += 0.25
            elif deposit == 'o':
                Price -= 1
                o += 1
                payment += 1
            elif deposit == 'f':
                Price -= 5
                f += 1
                payment += 5
            elif deposit == 'c':
                print()
                print('Please take the change below.')
                if payment == 0:
                    print('  No change due.')
                if round(payment,3) >= 0.25:
                    qowed = (payment * 100) // 25
                    if q < qowed:
                        qowed = q
                payment -= (qowed * 0.25)
                q -= qowed

                if round(payment,3) >= 0.10:
                    dowed = (payment * 100) // 10
                    if d < dowed:
                        dowed = d
                payment -= (dowed * 0.10)
                d -= dowed

                if round(payment,3) >= 0.05:
                    nowed = (payment * 100) // 5
                    if n < nowed:
                        nowed = n
                payment -= (nowed * 0.05)
                n -= nowed
                dollars = payment // 1
                cents = (payment % 1) * 100

                if qowed != 0:
                    print('  ', int(qowed), 'quarters')
                if dowed != 0:
                    print('  ', int(dowed), 'dimes')
                if nowed != 0:
                    print('  ', int(nowed), 'nickels')
                if round(payment) > 0:
                    print('Machine is out of change.')
                    print('See store manager for remaining refund.')
                    if payment >= 1:
                        print('Amount due is :', round(dollars), 'dollars and', round(cents), 'cents')
                    elif payment < 1 and absPrice > 0:
                        print('Amount due is :', round(cents), 'cents')
                print()
            else:
                print('Illegal selection:', deposit)





        if round(Price,3) == 0 and deposit != 'c':
            print()
            print('Please take the change below')
            print('  No change due.')
            print()
        elif Price < 0 and deposit != 'c':
            print()
            print('Please take the change below')
            absPrice = abs(Price)
            if absPrice >= 0.25:
                qowed = (absPrice * 100) // 25
                if q < qowed:
                    qowed = q
            absPrice -= (qowed * 0.25)
            q -= qowed

            if absPrice >= 0.10:
                dowed = (absPrice * 100) // 10
                if d < dowed:
                    dowed = d
            absPrice -= (dowed * 0.10)
            d -= dowed

            if absPrice >= 0.05:
                nowed = (absPrice * 100) // 5
                if n < nowed:
                    nowed = n
            absPrice -= (nowed * 0.05)
            n -= nowed
            dollars = absPrice // 1
            cents = (absPrice % 1) * 100
            if qowed != 0:
                print('  ', int(qowed), 'quarters')
            if dowed != 0:
                print('  ', int(dowed), 'dimes')
            if nowed != 0:
                print('  ', int(nowed), 'nickels')
            if round(absPrice, 2) > 0:
                print('Machine is out of change.')
                print('See store manager for remaining refund.')
                if absPrice >= 1:
                    print('Amount due is :', round(dollars), 'dollars and', round(cents), 'cents')
                if absPrice < 1 and absPrice > 0:
                    print('Amount due is :', round(cents), 'cents')
            print()

    print('Stock contains:')

    if n < 100 and n >= 10:
        print('{:>5}'.format(int(n)), 'nickels')
    else:
        print('{:>4}'.format(int(n)), 'nickels')

    if d < 100 and d >= 10:
        print('{:>5}'.format(int(d)), 'dimes')
    else:
        print('{:>4}'.format(int(d)), 'dimes')

    if q < 100 and q >= 10:
        print('{:>5}'.format(int(q)), 'quarters')
    else:
        print('{:>4}'.format(int(q)), 'quarters')

    if o < 100 and o >= 10:
        print('{:>5}'.format(int(o)), 'ones')
    else:
        print('{:>4}'.format(int(o)), 'ones')

    if f < 100 and f >= 10:
        print('{:>5}'.format(int(f)), 'fives\n')
    else:
        print('{:>4}'.format(int(f)), 'fives\n')

    Price = input('Enter the purchase price (xx.xx) or \'q\' to quit: ')
    payment = 0
    deposit = 0
    qowed = 0
    dowed = 0
    nowed = 0
if Price == 'q':
    total = n * 5
    total = total + (d * 10)
    total = total + (q * 25)
    total = total + (o * 100)
    total = total + (f * 500)
    dollars = total // 100
    cents = (total % 100)
    print()
    print('Total :', int(dollars), 'dollars and', int(cents), 'cents')