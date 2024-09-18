# print("welcome to the game")
# height = int(input("what is your height in cm?"))

# if height > 120:
#     print("you can ride the rollercoster!")
    
# else:
#         print("sorry you have to grow taller before you can ride")
        
        
height = float(input("what is your height in m?\n"))
weight = float(input("what is your weight in kg?\n"))

bmi = weight / (height * height)

if bmi > 25:
    print(f"your bmi is {bmi}, you are overweight")
elif bmi < 18.5:
    print(f"your bmi is {bmi}, you are underweight")
    
else:
    print(f"your bmi is {bmi}, you are good")
    

    