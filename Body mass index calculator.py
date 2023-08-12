#body mass index calculator
print('welcome to BMI calculator')
weight = int(input('please tell me your weight \n'))
height = input('whats your hieght \n')
new_height = float(height) ** 2
bmi = round(weight/new_height)
#print(f'with {bmi} as your bmi')
if bmi < 18.5 :
    print('you are underweight')
elif bmi < 25 :
    print('you have normal weight')
elif bmi <30 :
    print('you are overweight')
elif bmi < 35 :
    print('you are obese')
elif bmi > 35 :
    print('you are clinically obese')


print(f'your body mass index is {bmi}')
