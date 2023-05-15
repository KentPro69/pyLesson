from random import randint
#from main import *


def binaryInput(question):  # used for (y/n) questions
    answer = input(" ==> "+question + " (any/n) ")
    if answer.lower() == "n":
        return False
    else:
        return True
