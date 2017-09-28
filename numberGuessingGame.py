#Greg Phillips
#9/28/17
#numberGuessingGame.py

from random import randint 
 
num1 = randint(1,100)
i = 1 
while True:
    
    num = int(input("Guess a number between 1 and 100: "))
    if num>num1:
        print("too high")
    if num<num1:
        print("too low")
    if num == num1:
        break
    i += 1
print("You got it in", i, "tries")
     
