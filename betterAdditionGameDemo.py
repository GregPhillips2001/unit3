#Greg Phillips
#10/4/17
#betterAdditionGame.py - ask addition problems until user gets 5

from random import randint

numCorrect = 0
while numCorrect < 5:
    num1 = randint(-10,10)
    num2 = randint(-10,10)
    question = "what is " + str(num1) + "+" +str(num2) + "?"
    answer = int(input(question))
    if num1 + num2 == answer:
        print("Correct")
        numCorrect += 1
    else:
        print("The answer was", num1 + num2)

