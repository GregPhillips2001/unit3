#Greg Phillips
#10/5/17
#dotsDemo.py - making some dots

from ggame import *

red = Color(0xff0000,1)

dot = CircleAsset(20,LineStyle(1,red),red)

for j in range(30):
    for i in range(20):
        Sprite(dot,(20 + 51*i,20 + 51*j))
App().run()
