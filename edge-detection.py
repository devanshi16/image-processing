import image
import math
img = image.Image("noisyman.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img1 = image.EmptyImage(img.getWidth(), img.getHeight())
win1 = image.ImageWin(img.getWidth(), img.getHeight())
gx = [1,0,-1,2,0,-2,1,0,-1]
gy = [1,2,1,0,0,0,-1,-2,-1]
def kernel(c,r):
    counter = 0
    gtx = 0
    gty = 0
    for b in [-1,0,1]:
        for a in [-1,0,1]:
            p = img.getPixel(c+a,r+b)
            gtx += gx[counter]*p.getGreen()
            gty += gy[counter]*p.getGreen()
            counter += 1
    return math.sqrt(gtx**2 + gty**2)

for r in range(1,img.getHeight()-1):
    for c in range(1,img.getWidth()-1):
        p = img.getPixel(c,r)
        g = int(kernel(c,r))
        p1 = image.Pixel(g,g,g)
        img1.setPixel(c,r,p1)

img1.draw(win1)
win.exitonclick()