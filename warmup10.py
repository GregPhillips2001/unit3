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

Sprite(redRectangle)
Sprite(whiteRectangle, (0,20))
Sprite(blueRectangle, (0,40))
Sprite(text, (20,7))
Sprite(text2, (23,27))
Sprite(text3, (20,47))
App().run()
