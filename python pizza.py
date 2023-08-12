print('welcome please make your selections')
size= input('what size pizza do you want? \n S = small, M = medium and L = large \n ').upper()
add_peperoni = input('do you want peperoni \n Y OR N \n ').upper()
extra_cheese = input('do you want extra cheese\n Y OR NO\n  ').upper()

price = 0
if size == 'S':
    price += 15
elif size == 'M':
    price += 20
elif size == 'L':
    price += 25
else:
    print('select a valid option')

if size == 'S' and add_peperoni == 'Y':
    price +=2
elif size == 'M' or size == 'L' and add_peperoni == 'Y' :
    price +=3

if extra_cheese == 'Y':
    price += 1
message = f'your total bill for this purchase is ${price} \n thanks for your patronage'
print(message)