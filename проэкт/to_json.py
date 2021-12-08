import json
from data import *


def convertToJSON():
    with open("price.json", "w") as write_file:
        json.dump(nounlist, write_file)


def convertInJSON():
    with open("dovidnuk.json", "w") as write_file:
        json.dump(nounlist2, write_file)
