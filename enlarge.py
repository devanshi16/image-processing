import image

img = image.Image("GoldenGate.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
n = 2
imgn = image.EmptyImage(img.getWidth()*n, img.getHeight()*n)
win1 = image.ImageWin(img.getWidth()*n, img.getHeight()*n)
try:
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            
            imgn.setPixel(col*n,row*n, p)
            imgn.setPixel(col*n,row*n+1, p)
            imgn.setPixel(col*n+1,row*n, p)
            imgn.setPixel(col*n+1,row*n+1, p)
except:
    pass

imgn.draw(win1)
win.exitonclick()