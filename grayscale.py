import image
img = image.Image('Tele.gif')
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,1000)   # setDelay(1, 2000) will speed up a lot                      # img.setDelay(delay, number of pixels between delay)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        gray_value = int((p.getRed() + p.getGreen() + p.getBlue())/3)

        newred = gray_value
        newgreen = gray_value
        newblue =  gray_value

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()
