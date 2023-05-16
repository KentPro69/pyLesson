from abc import ABC, abstractmethod

prices = {
    "ticketprice": 60,
    "vip_ticketprice":90,
    "guest_omahind": 40,
    "tulumaks":1.2
}

database = {}
database["totalGuests"] = 0
database["normalGuests"] = 0
database["VIPguests"] = 0

class Person(ABC):

    def __init__(self, name:str, age:int, ticketType= None):

        self.name = name
        self.age = age
        if age < 18:
            raise ValueError("Oled liiga noor, et siseneda")
        self.ticketType = ticketType
        database["totalGuests"] +=1

    def showTicket(self):
        if(self.ticketType == None):
            return print("Mul ei ole piletit")
        else:
            return print("Mul on " +self.ticketType + " pilet")

class vipGuest(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.ticketType = "VIP"

        database["VIPguests"] +=1


class normalGuest(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.ticketType = "tavaline"
        database["normalGuests"] +=1


Guest1 = normalGuest("Joonas",18)
Guest1.showTicket()
Guest2 = vipGuest("Toomas",23)
Guest3 = vipGuest("Joe Biden",54)

print(database)

tulu = (database["normalGuests"]*prices["ticketprice"]+database["VIPguests"]*prices[
    "vip_ticketprice"])*prices["tulumaks"]
kulu = (database["normalGuests"]*prices["guest_omahind"]+database["VIPguests"]*prices["guest_omahind"])

print("Kogu tulu: €"+str(tulu))

print("Kogu kasum: €"+str(tulu-kulu))
