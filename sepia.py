import image
img = image.Image("GoldenGate.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        newred = int(p.getRed() * 0.393 + p.getGreen() * 0.769 + p.getBlue() * 0.189)
        newgreen = int(p.getRed() * 0.349 + p.getGreen() * 0.686 + p.getBlue() * 0.168)
        newblue =  int(p.getRed() * 0.272 + p.getGreen() * 0.534 + p.getBlue() * 0.131)

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)
img.draw(win)
win.exitonclick()

