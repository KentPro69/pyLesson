from abc import ABC, abstractmethod

prices = {
    "ticketprice": 85,
    "VIP_coefficient": 159/85,
    "normal_coefficient": 1,
    "taxes_coefficient": 1.2
}

database = {}
database["VIP_ticketHolders"] = 0
database["normal_ticketHolders"] = 0
database["totalGuests"] = 0
database["guests"] = []


class Person(ABC):
    @abstractmethod
    def __init__(self, name: str, age: int, ticketType=None):

        self.__gender = "female"
        self.name = name
        self.age = age
        if age < 18:
            raise ValueError("You must be 18 or older")
        self.ticketType = ticketType

        global database
        personObj = {}
        self.personObj = personObj
        personObj["name"] = self.name
        personObj["age"] = self.age
        database["guests"].append(personObj)
        database["totalGuests"] += 1

    # @abstractmethod

    def showTicket(self):
        if (self.ticketType == None):
            return print("I have no ticket")
        else:
            return print("I have a " + self.ticketType + " ticket")

    def getGender(self):
        return print(self.__gender)


class VIP_ticketholder(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.ticketType = "VIP"

        self.personObj["ticketType"] = self.ticketType
        database["VIP_ticketHolders"] += 1


class ticketHolder(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.ticketType = "Normal"

        self.personObj["ticketType"] = self.ticketType
        database["normal_ticketHolders"] += 1


guest1 = VIP_ticketholder("Joe Biden", 22)
guest2 = ticketHolder("Barack Obama", 19)
guest3 = VIP_ticketholder("Tom Cruise", 51)

""" guest0.showTicket() """
""" guest1.showTicket()
guest2.showTicket()


guest1.getGender()
print(guest1.name)
guest1.name = "Michael Jackson"
print(guest1.name)
guest1.__gender = "male"
guest1.getGender()

print(guest1) """

print("==========")

print(database)


def getAverageAge():
    sum = 0
    totalGuests = database["totalGuests"]
    for i in range(totalGuests):
        sum += database["guests"][i]["age"]
    avgAge = sum/totalGuests
    return round(avgAge)


print(getAverageAge())
print("Total revenue: €" + str(round(database["VIP_ticketHolders"]
      * prices["VIP_coefficient"]*prices["ticketprice"]*prices["taxes_coefficient"]+database["normal_ticketHolders"]
      * prices["normal_coefficient"]*prices["ticketprice"]*prices["taxes_coefficient"], 2)))

""" 
class Animal:
    def __init__(self, name):
        self.name = nameW

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
"""
