import random

going = True
day = 1
hunger = 0
thirst = 0
happiness = 50
boredom = 5
strength = 0
proceed = None
state = "Unidentified Mineral"
stats = {"state": state, "hunger": hunger, "thirst": thirst, "happiness": happiness}

print("-----Welcome to the Pet Rock Simulator!-----")
tutorial = input("Would you like to view the tutorial? (y/n)")
if tutorial == "y":
    print("")

name = input("What would you like to name your pet rock?")
if name == "":
    print("Indecisive, huh. The rock decides to name itself Reginald.")
    name = "Reginald"
else:
    print(f"Very fitting name for your rock, {name} seems to like it.")

while going:
    for x in stats:
        if stats[x] < 0:
            stats[x] = 0
    print(f"----- Day {day} -----")
    print(stats)
    option = input(f"What would you and you pet rock like to do? \n 1: Pet {name} \n 2: Excercise {name} \n 3: Feed {name} \n 4: Play a game with your pet rock \n 5: Water the rock")
    if option == "1":
        print(f"{name} is very happy, it enjoyed being pet.")
        happiness += 1
        boredom -= 2
    elif option == "2":
        print(f"The rock and you lift weights.")
        if random.randint(1,3) == 1:
            print(f"{name} fails a bench press pr and is annoyed")
            happiness -= 1
            thirst += 1
        elif random.randint(1,3) == 2:
            print(f"{name} is proud of itself for having a good workout.")
            happiness += 1
            thirst += 1
            strength += 2
        elif random.randint(1,3) == 3:
            print(f"{name} hit a new bench press PR and is very excited!.")
            print("Rock became stronger.")
            happiness += 3
            thirst += 2
            strength += 5
    elif option == "3":
        print("")
    elif option == "4":
        print("")
    elif option == "5":
        print(f"You pour some water on {name}. It is now dripping wet.")
        if thirst <= 0:
            print(f"{name} was not thirsty and is now annoyed that it is covered in water.")
            happiness -= 10
        elif thirst > 6:
            print(f"Thank you! I was so thirsty!  -{name}")
            thirst += 4
        elif thirst > 3:
            print(f"Thank you for water!  -{name}")
            thirst -= 3
    else:
        print(f"{name} is confused, and doesn't do anything.")

    if strength > 4 and proceed == None:
        print("The rock loses a good amount of weight, and realizes what it is.")
        proceed = input("What do you say to the rock? \n 1: Congradulations! \n 2: Proceed.")
        if proceed == "2":
            stats["state"] = "Wolframite"

    day = day + 1
    hunger = hunger + 1
    thirst = thirst + 1
    boredom = boredom + 1
