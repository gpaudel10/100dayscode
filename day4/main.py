#rock,paper, sissors


import random

rock = '''
    dhunga
'''

paper = '''
    pana   
'''

scissors = '''
    kaichi
'''
my_list = [rock, paper, scissors]
num = int(input("what do you choose? type 0 for rock, type 1 for paper and 2 for scissors"))

print(f"you choose {num} !!")

random_choose = random.randint(0, 2)
print(f'computer choose {random_choose} which is ')
print(my_list[random_choose])

if num >= 3 or num < 0 :
    print("invalid number you lose !")
    
elif num == 0 and random_choose == 2:
    print("you win")
    
elif random_choose == 0 and num == 2:
    print("you lose !")

elif random_choose > num:
    print("you lose !")

elif num > random_choose:
    print("you win !")

elif num == random_choose:
    print("its draw")


