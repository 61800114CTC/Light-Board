import board
import board
import displayio
import rgbmatrix
import random
import time
import adafruit_display_text.label
from adafruit_bitmap_font import bitmap_font
from adafruit_matrixportal.matrix import Matrix


# If there was a display before, release it
displayio.release_displays()

# Create RGB matrix object
matrix = Matrix(bit_depth=6)

# Associate RGB Matrix with a Display to use displayio features
display = matrix.display

SCALE = 1

# Show label
font = bitmap_font.load_font("fonts/Arial-12.bdf", displayio.Bitmap)

line1 = adafruit_display_text.label.Label(
    font,
    color=(255,255,255),
    scale=1,
    text="")

line1.x = display.width
line1.x = 0
line1.y = 6

line2 = adafruit_display_text.label.Label(
    font,
    color=(240,240,240),
    scale=1,
    text="")

line2.x = display.width
line2.x = 70
line2.y = 9

line3 = adafruit_display_text.label.Label(
    font,
    color=(0,0,255),
    scale=1,
    text = "")

line3.x = display.width
line3.x = 0
line3.y = 22

line4 = adafruit_display_text.label.Label(
    font,
    color=(255,0,0),
    scale=1,
    text = "")

line4.x = display.width
line4.x = 0
line4.y = 22

# Put each line of text into a Group then show it
#g = displayio.Group()
#g.append(line1)
#display.show(g)
#time.sleep(2)

# Bitmap holds the two dimensional array of pixels, last value is color depth
b1 = displayio.Bitmap(display.width//SCALE, display.height//SCALE, 6)
b2 = displayio.Bitmap(display.width//SCALE, display.height//SCALE, 6)

# Set values directly like (the value is the color from palette)
# b1[23,42] = 2

# Create an X color palette (however many colors you lie)
palette = displayio.Palette(7)
palette[0] = 0X000000
palette[1] = 0XFF0000
palette[2] = 0X00FF00
palette[3] = 0X0000FF
palette[4] = 0XFFFFFF
palette[5] = 0XF8F8FF
palette[6] = 0X00FFFF

tg1 = displayio.TileGrid(b1, pixel_shader=palette)
tg2 = displayio.TileGrid(b2, pixel_shader=palette)
g1 = displayio.Group(scale=SCALE)
g1.append(tg1)
g1.append(line1)
g1.append(line2)
g1.append(line3)
g1.append(line4)
display.show(g1)
g2 = displayio.Group(scale=SCALE)




while True:
    # Not sure if we need to alternate bitmaps or not
    line1.text="Welcome CTC students to"
    line3.text="                                        INST's project show"
    display.show(g1)
    Y = 1
    X = display.width
    while X > len(line1.text)*-18+32:
        line1.x=X
        line3.x=X
        display.show(g1)
        X=X-2
        time.sleep(.1)
        if X % 5 == 0:
            line2.x = X
            line3.x = Y
    X = 2
    line2.x = X
    line3.x = X



    times = 1
    while times > 0:
        line2.text="Connect"
        line3.text="4 by"
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1

    times = 1
    while times > 0:
        line2.text="Scott J"
        line3.text=""
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1


    times = 1
    while times > 0:
        line2.text="BATTLE"
        line3.text="SHIP by"
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1
    # If Line4 stay's add new Line to bottom part.
    times = 1
    while times > 0:
        line2.text="Scott J"
        line4.text="Simon"
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line4.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1


    times = 1
    while times > 0:
        line2.text="Tic-Tac"
        line3.text="Toe by"
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1
 

    times = 1
    while times > 0:
        line2.text="Elliot"
        line3.text="Scott J"
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1

    times = 1
    while times > 0:
        line2.text="Korbin"
        line3.text="Dakota"
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1

    times = 1
    while times > 0:
        line2.text="Owen"
        line3.text=""
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1

    times = 1
    while times > 0:
        line2.text="Black"
        line3.text="Jack by"
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1

    times = 1
    while times > 0:
        line2.text="Jacob"
        line3.text="Joseph"
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1

    times = 1
    while times > 0:
        line2.text="tiffany"
        line3.text="taishaun"
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1

    times = 1
    while times > 0:
        line2.text="2d game"
        line3.text="design:"
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1

    times = 1
    while times > 0:
        line2.text="Ashton"
        line3.text="Aaron"
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1


    times = 1
    while times > 0:
        line2.text="tf2 cnsl"
        line3.text="game by"
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1

    times = 1
    while times > 0:
        line2.text="Caden"
        line3.text=""
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1


    times = 1
    while times > 0:
        line2.text="Interact"
        line3.text="Story"
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1

    times = 1
    while times > 0:
        line2.text="Josh"
        line3.text=""
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1

    times = 1
    while times > 0:
        line2.text="VR Yu-"
        line3.text="Gi-Oh"
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1

    times = 1
    while times > 0:
        line2.text="Quinlan"
        line3.text=""
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1

    times = 1
    while times > 0:
        line2.text="Simon"
        line3.text="Says by"
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1

    times = 1
    while times > 0:
        line2.text="Konnor"
        line3.text=""
        display.show(g1)
        time.sleep(2)
        line2.text=""
        line3.text=""
        display.show(g1)

        time.sleep(1)
        times = times - 1
# html css color.com,

    '''
    # If at a border, change directions, otherwise, change randomly
    if (direction == "right" and x >= display.width -1) or (direction == "left" and x < 1):
        direction = "up" if random.random() > .5 else "down"
    elif (direction == "down" and y >= display.height -1) or (direction == "up" and y < 1):
        direction = "left" if random.random() > .5 else "right"
    elif random.random()< .1:
        if direction == "left" or direction == "right":
            if y == 0:
                direction = "down"
            elif y == display.height-1:
                direction = "up"
            else:
                direction = "up" if random.random() > .5 else "down"
        elif direction == "up" or direction == "down":
            if x == 0:
                direction = "right"
            elif x == display.width - 1:
                direction = "left"
            else:
                direction = "left" if random.random() > .5 else "right"


    if direction == "right":
        x += 1
    elif direction == "left":
        x -= 1
    elif direction == "up":
        y -= 1
    elif direction == "down":
        y += 1

    x = max(0, min(display.width-1,x))
    y = max(0, min(display.height-1,y))
    segments.append({'x': x, 'y': y})

    # Only show the last 30, then start erasing
    if len(segments) > 30:
        b1[segments[0]['x'], segments[0]['y']] = 0
        del segments[0]

    # Check for collision
    if b1[x,y] > 0:
        # Boom
        #palette[0] = 0XFF0000
        time.sleep(.5)
        #palette[0] = 0X000000
        for s in segments:
            b1[s['x'], s['y']] = 0
        segments.clear()
        x,y = 32,16

    else:
        c = random.randint(1,len(palette)-1)
        palette[c] = (random.randint(30,255), random.randint(30,255), random.randint(30,255))
        b1[x,y] = c
        time.sleep(.02)
    '''

