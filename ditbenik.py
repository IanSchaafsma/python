#main program

#Naam Invoer
print("Hello You!, ik ben Ian")

name1 = input("Wat is je naam? ") 
print("Hallo " + name1)

#Tijd
import datetime

time = datetime.datetime.now() 
print("Het is nu:")
print(time)

while True:
    print( name1 + " Tijd voor wat vragen. ")
    vraag1 = input("Waar woon ik? A = Alkmaar B = Schagen C = Winkel ")

    if vraag1 == 'A':
        print("Nee man")
            
    elif vraag1 == 'B':
        print("Bijna")
        
    elif vraag1 == 'C':
        print("Lekker bezig")

    else: break

    vraag2 = input("Wat voor opleiding heb ik hiervoor gedaan? A = MVI B = HBR = PIE ")

    if vraag2 == 'A':
        print("Perfecto")
    elif vraag2 == 'B':
        print("Ben geen chef kok")
        
    elif vraag2 == 'C':
        print("Nope")
         
    else: break 

    vraag3 = input("Wat is mijn favoriete fast food keten? A = Burger King B = Mcdonalds C = KFC ")

    if vraag3 == 'A':
        print("Nee")
        
    elif vraag3 == 'B':
        print("Lekker")

    elif vraag3 == 'C':
        print("Nope")

    else: break
      


while True:
    #restart
    print( name1 + " wil jij dit nog een keer doen? ")
    restart = input("Y/N ")

    if restart == 'Y':
        break
    elif restart == 'N':
        print("Bedankt voor het meedoen.")
        break

    else: print("type Y of N ")