protein = 4
carb = 4
fat = 9
alcohol = 7


weight = int(input('What is your weight in lbs? \n'))
height = int(input('What is your height in inches? \n'))
age = int(input('How old are you? \n'))

BMR = (655 + 4.35 * weight) + (4.7 * height) - (4.7 * age)

#activity level
##none = 1.2
##light = 1.375
##moderate = 1.55
##heavy = 1.725
level = input('What is your activity level?\n none \n light \n modertate \n heavy \n').lower()

if level == 'none':
    BMR = round(1.2 * BMR)
elif level == 'light':
    BMR == round(1.375 * BMR)
elif level == 'moderate':
    BMR = round(1.375 * BMR)
elif level == 'heavy':
    BMR = round(1.725 * BMR)
    
#BMR = (655 + 4.35 * weight) + (4.7 * height) - (4.7 * age)

print('Your BMR is', + BMR)
while True:
    protein_percentage = int(input('What percentage of protein would you like? \n'))
    carb_percentage = int(input('What percentage of carbohydrates would you like? \n'))
    fat_percentage = int(input('What percentage of fat would you like? \n'))

    percentage = protein_percentage + carb_percentage + fat_percentage

    if percentage == 100:
        print('NICE')
        break
    elif percentage > 100:
        print('Your percentage is over 100')
    else:
        print('Your percentage is under 100')


