import image

img = image.Image("GoldenGate.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        gray_value = (p.getRed() + p.getGreen() + p.getBlue())/3
        if gray_value < 128:
                newred = 0
                newgreen = 0
                newblue =  0
        else:
            newred = 255
            newgreen = 255
            newblue =  255

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)


img.draw(win)
win.exitonclick()

