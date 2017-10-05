#Greg Phillips
#9/27/17
#satfb.py

from ggame import * 

red = Color(0xcc0000,1)
blue = Color(0x000099,1)
white = Color(0xffffff,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #(pixels thick,color)

redRectangle = RectangleAsset(100,20,blackOutline,red) #(width,height,outline,fill)
whiteRectangle = RectangleAsset(100,20,blackOutline,white) #(width,height,outline,fill)
blueRectangle = RectangleAsset(100,20,blackOutline,blue) #(width,height,outline,fill)
text = TextAsset("SATURDAYS", fill=white, style="bold 8pt Times")
text2 = TextAsset("ARE_FOR", fill=blue, style="bold 8pt Times")
text3 = TextAsset("THE_BOYS", fill=white, style="bold 8pt Times")

for j in range(7):
    for i in range(7):
        Sprite(redRectangle, (0 + 150*i, 0 + 75*j))
        Sprite(whiteRectangle, (0 + 150*i,20 + 75*j))
        Sprite(blueRectangle, (0 + 150*i,40 + 75*j))
        Sprite(text, (20 + 150*i,7 + 75*j))
        Sprite(text2, (23 + 150*i,27 + 75*j))
        Sprite(text3, (20 + 150*i,47 + 75*j))
App().run()
