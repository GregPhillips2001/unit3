#Greg Phillips
#10/5/17
#dotsDemo.py - making some dots

from ggame import *

red = Color(0xff0000,1)

dot = CircleAsset(20,LineStyle(1,red),red)

for j in range(10): #Prints the row 10 times
    for i in range(20):  #Prints one row of dots
        Sprite(dot,(20 + 40*i,20 + 40*j))
App().run()
