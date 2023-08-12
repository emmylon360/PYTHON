#presumed days of life remaining if we live up to 90 years
print('\n')
welcome_essage = 'assuming that you wil live up to 90 years this app will tell you how long you have left to the very seconds'
print(welcome_essage)
print('\n')
name = input('i will like to know what is your name? \n')
age = int(input('how old are you \n'))
age_remaining = 90 - age
months_remaining = age_remaining * 12
weeks_remaining = age_remaining * 52
days_remaining = age_remaining * 365
hours_remaining = days_remaining * 60
minutes_remaining = hours_remaining * 60
seconds_remaining = minutes_remaining * 60
serious_me = round(weeks_remaining/ 12)
message = (f'hello dear {name} you have {seconds_remaining} seconds, {minutes_remaining} minutes, {hours_remaining} hours {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months remainig to live,')
print(message)
print(f'if you start to take your life serious and work with the 12 week year you will have {serious_me} years, which is an advantage compared to {age_remaining}years')