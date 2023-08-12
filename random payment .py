#random payer for purchase
import random
names = input('please fill in the names of all on table with a coma (,) and space.\n')
namesplit = names.split(',')
num_names = len(namesplit)
random_chioce = random.randint(0,num_names-1)
paying_today = namesplit[random_chioce]
print(f'{paying_today},would be paying this bill')

# list_of_names = namesplit
# print(list_of_names)
# random_name = random.choice(list_of_names)
#print(f'{random_name},will be paying the bill for everyone \n thank you!!')
