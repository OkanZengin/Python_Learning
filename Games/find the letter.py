import string
import random
string.ascii_letters

while True:
    letter = random.choice(string.ascii_letters)
    rslt = str.upper(letter)
    gss = input("guess the letter ")
    syc = 1
    while True:
        if syc == 30:
            print("you couldn't find the letter, sorry")
            break
        if str.upper(gss)==rslt:
            print(f"congratulations you found the letter only {syc} tries")
            break
        elif gss!=rslt:
            gss=input("you guessed wrong, try again ")
            syc+=1
    if input("type 'bye' to quit ").lower()=="bye":
        break
input("press enter to exit")