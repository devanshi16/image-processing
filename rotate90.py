import image

img = image.Image("GoldenGate.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
#img.setDelay(1,2000)   # setDelay(0) turns off animation
n = image.EmptyImage(img.getHeight(),img.getWidth())
win1 = image.ImageWin(img.getHeight(),img.getWidth())
try:
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            
            n.setPixel(img.getHeight()-1-row, col, p)
except:
    pass

n.draw(win1)
win.exitonclick()