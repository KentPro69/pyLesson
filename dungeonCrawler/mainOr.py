from helperFunctions import binaryInput
from animations import play, morningAni, fightAni, fireballAni
from random import randint, choice
from time import sleep
import os
def clear(): return os.system('cls')


heroData = {
    "name": input("What will be your hero's name?: "),
    "health": 100,
    "XP": 0,
    "inventory": {  # there is no need to store spellbook or fireball ability in herodata
        "Super potion": 0
    },
}

currentDay = 1


def reset():
    global heroData
    global currentDay
    currentDay = 1
    heroData = {
        "name": input("What will be your hero's name?: "),
        "health": 100,
        "XP": 0,
        "inventory": {
            "Super potion": 0
        },
    }


def healthCheck():  # check whether game should be  over
    global heroData
    global currentDay

    if int(heroData["health"]) > 100:
        heroData["health"] = 100

    if heroData["health"] <= 0:
        clear()
        print("You have died!💀")
        input("Press ENTER to play again...")
        reset()
        playGame()
    elif currentDay == 10 and heroData["XP"] <= 0:
        clear()
        print("You were a coward and gained no XP, you lost the game!🙃")
        input("Press ENTER to play again...")
        reset()
        playGame()
    elif currentDay == 10:
        clear()
        print("YOU SURVIVED FOR 10 DAYS!!!😀😀😀😀")
        input("Press ENTER to play again...")
        reset()
        clear()
        playGame()


def morningNews():  # used to show player stats every morning
    global heroData
    global currentDay
    print("Current health: "+str(heroData["health"])+"❤️")
    print("Current XP: "+str(heroData["XP"])+"⬆️")
    # for i in range(len(heroData["inventory"])):
    #     if heroData["inventory"][i]
    print("💼 Your inventory 💼")
    uniqueItems = 0

    for key, value in heroData["inventory"].items():
        if value != 0 or value != False:
            print(" • "+str(key)+": "+str(value))
            uniqueItems += 1
    if uniqueItems == 0:
        print("   [Your inventory is currently empty😕]")
    elif heroData["inventory"]["Super potion"] <= 1:
        consume = binaryInput("Would you like to consume a super potion?")
        if consume == True:
            heroData["health"] = 100
            heroData["inventory"]["Super potion"] -= 1
            print("Health restored! (100❤️)")


def unknownPotion_lootdrop():
    global heroData
    global currentDay
    chance = randint(1, 100)
    if chance <= 60:
        print("You found an unknown potion🧪")
        if binaryInput("Would you like to drink it?") == True:
            if currentDay < 5:
                difference = randint(-20, 20)
            else:
                difference = randint(0, 20)

            print(str(difference)+"💔")

            heroData["health"] = int(heroData["health"]+difference)

        else:
            print("You threw the potion away!")

    healthCheck()


def superPotion_lootdrop():
    global heroData
    global currentDay
    if currentDay >= 5:
        chance = randint(1, 100)
        if chance <= 15:
            print("======")
            print("The goblin dropped a super potion🧪")
            print("You put it in you backpack!")
            print("======")
            heroData["inventory"]["Super potion"] += 1


def fight():
    global heroData
    global currentDay

    if currentDay < 5:
        play(fightAni)
    else:
        play(fireballAni)

    damage = randint(10, 30)
    XPgain = randint(10, 30)
    if currentDay >= 5:
        damage = 0
    heroData["health"] -= damage
    heroData["XP"] += XPgain
    superPotion_lootdrop()
    print("You lost "+str(damage)+"💔.")
    print("You gained " + str(XPgain) + "XP⬆️")

    healthCheck()


def playGame():
    global heroData
    global currentDay
    play(morningAni)
    for currentDay in range(1, 11, 1):
        if currentDay == 5:
            print("======")
            print("You have found a spellbook!📕")
            print("Now you possess the skills to cast a 🔥fireball🔥 - now you won't be damaged, when fighting goblins")
            print(
                "You are also 🧠smart🧠 now, ergo you can't be poisoned by unknown potions")
            print(
                "You now also have a 15% chance to get a 🧪super potion🧪 from goblin fights!")
            print("======")
            input("Press ENTER to continue...")
            clear()

        print("Good morning "+heroData["name"] +
              "! Day number ======> " + str(currentDay)+" <====== begins!")
        morningNews()

        fightGoblins = binaryInput("Would you like to fight some goblins?👺")
        if fightGoblins == True:
            fight()
        else:
            unknownPotion_lootdrop()
        input("Press ENTER to continue...")
        clear()
        print("Sleeping😴...")
        sleep(3)
        clear()
        healthCheck()


playGame()
