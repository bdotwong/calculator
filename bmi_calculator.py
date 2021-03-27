#get user height, weight, gender, age
#calculate BMI

height = int(input('What is your height in inches? \n'))
weight = int(input('What is your weight in lbs? \n'))
BMI = (weight*703)/(height*height)

if BMI <= 18.5:
    print('Your BMI is', BMI, 'which is underweight')
elif BMI > 18.5 and BMI < 25:
    print('Your BMI is', BMI, 'which is normal')
elif BMI > 25 and BMI < 30:
    print('Your BMI is', BMI, 'which is overweight')
elif BMI > 30:
    print('Your BMI is', BMI, 'which is obese')

    

    


    
print('Your BMI is', + BMI)
             
