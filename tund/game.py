from random import randint, choice

class Hero:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.inventory = {
            "Potion":0,
            "Sword": False
        }



    def showHealth(self):
        print("Mul on "+ str(self.health) +"❤")

hero_name = input("Mis nimi sul on?")
heroObject = Hero(hero_name)

day = 1

def reset():
    day = 1
    heroObject = Hero(hero_name)

def healthCheck():
    if heroObject.health <= 0:
        reset()
    else:
        pass

def kysimus(kysimuseText):
    vastus = input(kysimuseText)
    if vastus.lower() == "no":
        return False
    elif vastus.lower()=="yes":
        return True

def game():
    for day in range(1,10):
        if day == 11:
            print("Tubli, sa voitsid!")
        print("Algab päev nr."+str(day))

        if day == 1:
            print("Hommikust " + heroObject.name)
        else:
            print("Sinu joogid:"+str(heroObject.inventory["Potion"]))
            heroObject.showHealth()

            if heroObject.inventory["Potion"] != 0:
                wannaDrink = kysimus("Kas sa soovid juua oma jooki?")
                if wannaDrink == True:
                    heroObject.inventory["Potion"] -=1
                    suvalineNumber = randint(10, 20)
                    heroObject.health += suvalineNumber
                    print("Sa said juurde "+suvalineNumber+"❤")
                    if heroObject.health > 100:
                        heroObject.health = 100



        voitlus = kysimus("Kas tahad koletistega voidelda?")

        if voitlus == True:
            print("voitled!😈")

            if heroObject.inventory["Sword"] == True:
                suvalineNumber = 0
            else:
                suvalineNumber = randint(-20, -10)

            print("Kaotasid "+ str(suvalineNumber) + "❤, kuna sa võitlesid koletisega")
            heroObject.health += suvalineNumber

            chestChance = randint(0,100)
            if chestChance <= 30:
                print("Sa leidsid kirstu!")
                wannaOpen = kysimus("Kas sa soovid seda avada?")
                if wannaOpen == True:
                    swordChance = randint(0,100)
                    if swordChance <= 10 and heroObject.inventory["Sword"] == False:
                        print("Sa leidsid mõõga!🗡")
                        heroObject.inventory["Sword"] = True
                    else:
                        print("Sa leidsid joogi!")
                        heroObject.inventory["Potion"] += 1
                else:
                    print("Viskasid kirstu minema")

        else:

            randomNumber = randint(0,100)
            if randomNumber >= 50:
                heroObject.inventory["Potion"] += 1
                print("Leidsid joogi!")


        soovidMagada = kysimus("Kas soovid magada?")
        if soovidMagada == True:
            print("head und!")
        else:
            suvalineNumber = randint(-10, 0)
            print("Kaotasid "+ str(suvalineNumber) + "❤, kuna sa ei maganud")

            heroObject.health += suvalineNumber





game()