from array import *
import time

while True:
    factory = ["auto"]
    distribution = []
    shop = []

    print("fabriek:", factory )
    popped_from_factory = factory.pop(0)
    distribution.append(popped_from_factory)
    time.sleep(1)
    print("Fabriek:", factory)

    time.sleep(1)

    print("distribution:", distribution )
    popped_from_distribution = distribution.pop(0)
    shop.append(popped_from_distribution)
    time.sleep(1)
    print("distribution:", distribution)

    time.sleep(1)

    print("shop:", shop )
    popped_fromshop = shop.pop(0)
    time.sleep(1)
    print("shop:", shop)


    start = input('Wil je opnieuw beginnen JA/NEE ')
    if start == 'JA'.strip().lower():
        print("We beginnen opnieuw!")
        
    elif start == 'NEE'.strip().lower():
        print("doei!")
        break
    else: 
        print("Dat is een ongeldig antwoord.")
        break

        