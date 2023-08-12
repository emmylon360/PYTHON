#LEAP YEAR FINDER!!!
year = int(input('what year will you want to check out to see if it is a leap year,? '))
print(f"{year % 4} \n {year % 100} \n {year % 400}  ")
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0 :
    print(f"{year} is a leap year")
else:
    print(f'{year} is not a leap year try another year')
