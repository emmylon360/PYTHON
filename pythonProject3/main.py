from game_date import data
import random
from art import logo,vs
print(logo)
score = 0
print(score)
game_should_continue = True

info_2 = random.choice(data)

while game_should_continue:
    def format_data(account):
        '''takes account data and returns printable data'''
        account_name= account['name']
        account_discription = account ['description']
        account_country = account ['country']
        return f'{account_name}, a {account_discription}, from {account_country}'

    info = info_2
    info_2 = random.choice(data)
    if info == info_2:
        info_2 = random.choice(data)

    print(f'compare {format_data(info)}\n {vs} \n{format_data(info_2)}')

    guess = input('who has more followers? type A or B:  ').lower()
    info_followers = info['follower_count']
    info_2folowers = info_2['follower_count']

    answer = ''
    if info_followers > info_2folowers :
        answer = 'a'
    elif info_2folowers >info_followers:
        answer = 'b'
    if guess == answer:
        score += 1
        print(f'your score is {score}')
        print('you win')
    else:
        print(f'you lose, final score {score}')
        game_should_continue = False