import image
import math
img = image.Image("noisyman.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
imgn = image.EmptyImage(img.getWidth(), img.getHeight())
win1 = image.ImageWin(img.getWidth(), img.getHeight())

for row in range(1,img.getHeight() - 1):
    for col in range(1,img.getWidth() - 1):

                p1 = img.getPixel(col - 1, row - 1) 
                p2 = img.getPixel(col - 1, row )
                p3 = img.getPixel(col - 1, row + 1)
                p4 = img.getPixel(col , row - 1)
                p5 = img.getPixel(col , row + 1)
                p9 = img.getPixel(col , row )
                p6 = img.getPixel(col + 1, row - 1)
                p7 = img.getPixel(col + 1, row )
                p8 = img.getPixel(col + 1, row + 1)

                newred = int((p1.getRed() + p2.getRed() + p3.getRed() + p4.getRed() + p5.getRed() + p6.getRed() + p7.getRed() + p8.getRed() + p9.getRed())/9)
                newgreen = int((p1.getGreen() + p2.getGreen() + p3.getGreen() + p4.getGreen() + p5.getGreen() + p6.getGreen() + p7.getGreen() + p8.getGreen() + p9.getGreen())/9)
                newblue =  int((p1.getBlue() + p2.getBlue() + p3.getBlue() + p4.getBlue() + p5.getBlue() + p6.getBlue() + p7.getBlue() + p8.getBlue() + p9.getBlue())/9)

                newpixel = image.Pixel(newred, newgreen, newblue)
                imgn.setPixel(col,row, newpixel)

imgn.draw(win1)
win.exitonclick()