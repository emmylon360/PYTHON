print('love calculator ')
name = input('what is your full name without space in between? \n').lower()
lovers_name = input('what is the name of your lover without space in between? \n').lower()
both_names = name+lovers_name
t = both_names.count('t')
r = both_names.count('r')
u = both_names.count('u')
e = both_names.count('e')

true = t+r+u+e

l = both_names.count('l')
o = both_names.count('o')
v = both_names.count('v')
e = both_names.count('e')

love = l+o+v+e

love_score = int(str(true)+str(love))
if love_score <10 or love_score > 90 :
    print(f'your score is {love_score} you go together like coke and mentos')
elif love_score >= 40 and love_score <= 50 :
    print(f'your score is {love_score}you are alright together')
else :
    print(f'your score is {love_score}')