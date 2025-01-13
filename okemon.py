#Ana Milosevic
#11/20/24
#Pokemon Evolution

#Initalize
import random
pokemon_level = 0
pokemon_name = "Bulbasaur"
day = 1
#Functions
def draw_venusaur():
    print("""
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟥🟨🟨⬛🟥🟨🟨🟥⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟨🟥🟥🟥⬛⬛⬛🟥🟥🟨🟨🟥⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟥🟥🟥⬛⬛🟨🟨🟨⬛⬛⬛⬛🟥🟥⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟥⬛⬛🟥🟥⬛⬛🟨🟨⬛🟥🟨⬛⬛⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟥🟨🟨🟥🟥🟥🟥⬛🟥🟥🟥🟥🟥⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟩⬛🟥🟥🟥🟥🟥🟥🟥🟥⬛🟨🟨🟥🟥🟥⬛⬜⬜
⬜⬜⬜⬜⬛⬜⬛⬛⬛⬛⬛🟥🟥🟥🟥🟥🟥⬛🟥🟥🟥🟥🟥⬛⬛⬜⬜
⬜⬜⬜⬛🟦⬛⬛🟩⬛🟩🟩⬛⬛⬛🟥🟥🟥⬛⬛⬛⬛⬛⬛🟩⬛⬛⬜
⬜⬜⬜⬛🟦🟦⬛⬛⬛🟩⬛⬛🟩🟩⬛⬛⬛🟩⬛🟩🟩🟩⬛⬛🟩🟩⬛
⬜⬜⬜⬛🟦🟦🟦🟦🟦⬛⬛⬛⬛🟩🟩⬛🟩⬛⬛🟩⬛🟩🟩⬛🟩⬛⬛
⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛🟦⬛⬛🟩⬛🟩⬛🟩⬛
⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦⬛⬛🟩⬛🟩⬛
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟥🟥⬛🟦⬛🟦🟦🟦⬛⬛⬛⬜
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟥🟥⬛🟦🟦🟦⬛🟦🟦🌫️⬛⬜⬜
⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦⬛🟦⬛🟦⬛🟦🌫️⬛⬜⬜⬜
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛🟥⬜🟦🟦🟦🟦🟦🟦🟦⬛⬜⬛⬛⬜⬜⬜⬜
⬜⬛⬛🟦🟦🟦🟦🟦⬛⬜⬜🟦🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟦🟦🟦🟦⬜⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬛⬜🟦⬜⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜""")
def draw_bulbasaur():
    print("""
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟩🟩🟩⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛⬜⬜
⬜⬜⬜⬛⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜
⬜⬜⬛🟦⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬜⬛🟦🟦🟦⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬜⬛🟦🟦🟦🟦🟦⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟩🟩🟩🟩🟩🟩⬛⬜
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟩🟩🟩⬛⬛⬛⬛⬜
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦⬛⬛⬛🟦🟦🟦⬛⬜
⬛🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦⬜⬛⬜
⬛🟦🟦🟦🟦🟦⬛🟥⬜⬜🟦🟦⬛🟦🟦⬛⬛⬛⬜⬜
⬜⬛🟦🟦🟦🟦⬛🟥⬜🟦🟦⬛🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜🟦⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜""")
def draw_ivysaur():
    print("""
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟥⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🏻🏻⬛🟥⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛🏻🏻🏻⬛🟥⬛🏽🏽⬛⬜⬜⬜
⬜⬜⬜⬛⬜⬛🏽🏽⬛🏻🏻⬛🟥🟥⬛⬛⬛🟩⬛⬜⬜
⬜⬜⬛🟦⬛🟩🟩⬛⬛⬛🏻🟥🟥⬛🟩🟩🟩⬛⬛⬜⬜
⬜⬜⬛🟦🟦⬛⬛🟩🟩🏽⬛⬛⬛⬛⬛⬛⬛🟩🟩⬛⬜
⬜⬜⬛🟦🏽🟦🟦⬛⬛⬛🟩🟩⬛🟩🟩🟩⬛⬛⬛⬛⬜
⬜⬛🟦🟦🏽🏽🟦🟦🟦🟦⬛⬛⬛🟩🟩⬛🟩🟩⬛🟩⬛
⬜⬛🟦🟦🟦🟦🟦🟦🏽🟦🟦🟦🟦⬛🟩⬛🟩⬛🟩⬛⬛
⬛⬛🟦🟦🟦🏽🏽🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛⬛🟩🟩⬛
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🏽🟦⬛⬛⬛⬜
⬛🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦🟦🏽🟦🌫️⬛⬜
⬛🟦🟦🟦🟦🟦⬛🟥⬜🟦🟦🟦🟦🟦⬛🟦⬛⬛⬛⬜⬜
⬜⬛🟦🟦🟦⬛🟥🟥⬜🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬜🟦⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜""")
def train():
    global pokemon_level
    pokemon_level = pokemon_level + 1
def win_battle():
    global pokemon_level
    pokemon_level = pokemon_level + 2
def rest():
    if pokemon_level < 3:
        draw_bulbasaur()
    if pokemon_level > 2 and pokemon_level < 6:
        draw_ivysaur()
    else:
        draw_venusaur()
def day_time():
    global day
    day = day + 1
def evolve():
    if pokemon_level < 3:
        print("You are still not ready to evolve yet, keep playing to evolve!")
    if pokemon_level > 2 and pokemon_level < 6:
        print("Yay! You evolved! Goodbye Bulbasaur, you're new name is Ivysaur!")
    if pokemon_level > 5:
        print("Yay! You've evolved once again! Goodbye Ivysaur, you're new name is Venusaur!")

#main
print("Welcome to Pokemon Evolution Simulator")
while True:
    print("What would you like to do with your pokemon today? Day: " + str(day)) #While loop this so the player keeps playing
    day_time()
    print("""1. Train
2. Gym Battle
3. Rest (Display Info)
4. End""")
    activity = int(input("Enter activity:"))
    if activity == 1:
        train()
        print("Your level was " + str(pokemon_level - 1) + " , after training your level is now " + str(pokemon_level) + "!")
        evolve()
    if activity == 2:
        print("You are now going into battle, your current level is " + str(pokemon_level))
        battle = random.randint(1,2)
        if battle == 1:
            print("Oh no! You lost the fight! Sorry, but your level stays " + str(pokemon_level))
            evolve()
        if battle == 2:
            win_battle()
            print("Yay! You won the battle against your enemy! Great job! Your level is now " + str(pokemon_level) + "!")
            evolve()
    if activity == 3:
        rest()
    if activity == 4:
        break
