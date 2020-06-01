import image
img = image.Image('Tele.gif')
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,1000)   # setDelay(1, 2000) will speed up a lot   

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        gray_value = int((p.getRed() + p.getGreen() + p.getBlue())/3)
        newpixel = image.Pixel(gray_value, gray_value, gray_value)

        img.setPixel(col, row, newpixel)
img.draw(win)
win.exitonclick()