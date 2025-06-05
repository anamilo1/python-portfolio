#Ana Milosevic
# 01/31/25
#Slot Machine
#Init
symbols = ["♣" , "♢" , "7" , "♡" , "♠"] #5 symbols
import random
import time
credit = 100
#Functions
#Main
#1. Introduction
print("Hello! Welcome to the slot machine!")
print("You start with 100 credits, each spin costs 1 credit")
while True:
    #2. Ask the player , spin or quit
    ans = input("Would you like to spin or quit?")
    #3. Randomly pull 3 items from your list
    #Make sure you store these in a VARIABLE!
    if ans == "spin":
        if credit < 1:
            print("Unfortunatly you do not have enough credits to keep playing.")
        if credit > 0:
            credit -= 1
            slot1 = random.choice(symbols)
            slot2 = random.choice(symbols)
            slot3 = random.choice(symbols)
            slot4 = random.choice(symbols)
            slot5 = random.choice(symbols)
            print("You now have " + str(credit) + " credits left")
            #4. Display 3 images
            print("spinning...")
            time.sleep(2)
            print(slot1 + " " + slot2 + " " + slot3)
    elif ans == "quit":
        break
    #5. Determine the outcome (say u win/ u loose/ jackpot)(IF/ ELSE)
    if slot1 == "7" and slot2 == "7" and slot3 == "7" and slot4 == "7" and slot5 == "7":
        credit *= 100
        print("Congradulations! You got a jackpot! You now have " + str(credit) + " credits")
    elif slot1 == slot2 and slot2 == slot3 and slot3 == slot4 and slot4 == slot5
        credit *= 10
        print("Congradulations! You won! You now have " + str(credit) + " credits")
    elif slot1 == slot2 or slot1 == slot3 or slot1 == slot4 or slot1 == slot5 or slot2 == slot3 or slot2 == slot4 or slot2 == slot5 or slot3 = slot4 or slot3 = slot5 or slot4 = slot5
        credit *=2
        print("Congradulations! You got doubles! You how have " + str(credit) + " credits")
    else:
        print("Sorry, You lost. You still have " + str(credit) + " credits left")
if credit == 0:
    print("Sorry, You cannot play with 0 credit")
    quit()

#Part 2:
    #Credit system
    #Add more symbols
#1. Start the player with 100 (choice) credits
#2. Every spin costs 1 (choice) credit
#3. Jackpot =x100 reward (choice)
#4. 3 of a kind = x10 reward (choice)
#4b. 2 of a kind = x2 reward (choice)
#5. loss = nothing
#6. Display their credits considently
#7. Do not let them play with 0 credit
