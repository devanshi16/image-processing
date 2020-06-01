import image

img = image.Image("noisyman.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
n = 2
img1 = image.EmptyImage(img.getWidth()*2, img.getHeight()*2)
win1 = image.ImageWin(img.getWidth()*2, img.getHeight()*2)
img2 = image.EmptyImage(img.getWidth()*2, img.getHeight()*2)
win2 = image.ImageWin(img.getWidth()*2, img.getHeight()*2)
try:
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            
            img1.setPixel(col*n,row*n, p)
            img1.setPixel(col*n,row*n+1, p)
            img1.setPixel(col*n+1,row*n, p)
            img1.setPixel(col*n+1,row*n+1, p)
except:
    pass

try:
    for row in range(1,img1.getHeight() - 1):
        for col in range(1,img1.getWidth() - 1):
                p1 = img1.getPixel(col - 1, row - 1) 
                p2 = img1.getPixel(col - 1, row )
                p3 = img1.getPixel(col - 1, row + 1)
                p4 = img1.getPixel(col , row - 1)
                p5 = img1.getPixel(col , row + 1)
                p6 = img1.getPixel(col + 1, row - 1)
                p7 = img1.getPixel(col + 1, row )
                p8 = img1.getPixel(col + 1, row + 1)

                newred = (p1.getRed() + p2.getRed() + p3.getRed() + p4.getRed() + p5.getRed() + p6.getRed() + p7.getRed() + p8.getRed())/8
                newgreen = (p1.getGreen() + p2.getGreen() + p3.getGreen() + p4.getGreen() + p5.getGreen() + p6.getGreen() + p7.getGreen() + p8.getGreen())/8
                newblue =  (p1.getBlue() + p2.getBlue() + p3.getBlue() + p4.getBlue() + p5.getBlue() + p6.getBlue() + p7.getBlue() + p8.getBlue())/8

                newpixel = image.Pixel(newred, newgreen, newblue)
                img2.setPixel(col,row, newpixel)
except:
    pass
img2.draw(win2)
win.exitonclick()