# WarPaint
# Aaron Li
# TO DO:
# Tool Preview
# Fullscreen support
from pygame import *
from math import *
from random import *
from tkinter import filedialog, Tk
startTime = time.get_ticks()
root = Tk()
root.withdraw()
mixer.init()
font.init()
init()
screen = display.set_mode((1280, 720))
#Load required loading display fonts
loadFont = font.SysFont("Lucida Console", 11)
loaded = loadFont.render("0%", False, (255, 255, 255))
screen.blit(loaded, (1, 5))
display.flip()
running = True
# Text
helpLines = [["Pen", "Line", "Free"],
             ["Eraser", "Trash", ""],
             ["Shapes", "Ellipse", "Rectangle"],
             ["Paint", "Spray Can", "Bucket"],
             ["Pick & Mix", "Eyedropper", "Mixer"],
             ["Ink", "Text", "Stamps"],
             ["Files", "Save", "Load"]]

windowLines = ["Wake up, Tenno...",
               "Marines Inbound.",
               "Stay away from the fire.",
               "Now I am the Lotus.",
               "Now I am the mother.",
               "WarPaint"]
# Sounds
drumIn = mixer.Sound("music/drumOpen.ogg")
musicCollection = ["music/WFCombatMusic.ogg",
                   "music/WFCombatMusic2.ogg",
                   "music/WFCorpusTheme.ogg",
                   "music/WFCorpusTheme2.ogg",
                   "music/WFGrineerTheme.ogg",
                   "music/WFOrokinTheme.ogg",
                   "music/WFDrums.ogg",
                   "music/WFStalkerTheme.ogg"]
# Warframe music is generated based on context, the music doesn't have official names.
songNames = [["Generic", "Combat"],
             ["Grineer", "Calm"],
             ["Corpus", "Combat"],
             ["Corpus", "Calm"],
             ["Grineer", "Propoganda"],
             ["Orokin", "Calm"],
             ["Tenno", "Drums"],
             ["Stalker", "Theme"]]
print("Loaded", len(musicCollection), "songs")


def nextSong():
    global musicEnds
    global musicCollection
    if musicEnds < len(musicCollection) - 1:
        musicEnds += 1
    else:
        musicEnds = 0
    mixer.music.load(musicCollection[musicEnds])
    mixer.music.play()
    print(" ".join(songNames[musicEnds]))


def lastSong():
    global musicEnds
    global musicCollection
    if musicEnds > -len(musicCollection):
        musicEnds -= 1
    else:
        musicEnds = 7
    mixer.music.load(musicCollection[musicEnds])
    mixer.music.play()
    print(" ".join(songNames[musicEnds]))


mixer.music.set_volume(1)
# Colours
white = (255, 255, 255)
black = (0, 0, 0)
cyan = (0, 150, 150)
red = (255, 0, 0)
dumfingColour = (68, 117, 109)  # Colours produced by converting "Dumfing" into hexadecimal
dumfingColour2 = (102, 105, 110)
darkGrey = (120, 120, 120)
grey = (150, 150, 150)
# Rects
canvas = Rect(10, 120, 1049, 590)
colourPalette = Rect(1142, 10, 128, 128)
pencil = Rect(10, 15, 32, 32)
ruler = Rect(15, 42, 21, 21)
eraser = Rect(34, 15, 32, 32)
freehand = Rect(15, 64, 21, 21)
trash = Rect(39, 42, 21, 21)
compass = Rect(60, 15, 32, 32)
circle = Rect(62, 42, 21, 21)
rectangle = Rect(62, 64, 21, 21)
bucket = Rect(85, 15, 32, 32)
spray = Rect(86, 42, 21, 21)
undo = Rect(10, 96, 47, 16)
redo = Rect(146, 96, 47, 16)
eyeDropTool = Rect(106, 15, 32, 32)
eyeDrop = Rect(110, 42, 21, 21)
MortAndPest = Rect(110, 64, 21, 21)
mixerOptions = Rect(222, 10, 200, 103)
mixColourBox1 = Rect(264, 22, 30, 30)
mixColourBox2 = Rect(264, 68, 30, 30)
setColour1Box = Rect(396, 39, 10, 20)
setColour2Box = Rect(396, 61, 10, 20)
ink = Rect(130, 15, 32, 32)
textMod = Rect(134, 42, 21, 21)
stampTools = Rect(222, 10, 302, 104)
stampBox = Rect(224, 12, 298, 100)
stampRectangle = Rect(134, 64, 21, 21)
corpusBox = Rect(228, 252, 268, 400)
tennoBox = Rect(506, 252, 268, 400)
grineerBox = Rect(784, 252, 268, 400)
vanillaTennoBox = Rect(506, 252, 124, 400)
orokinVoidBox = Rect(640, 252, 124, 400)
bucketBox = Rect(86, 64, 21, 21)
folderBox = Rect(160, 17, 32, 32)
saveBox = Rect(166, 42, 21, 21)
loadBox = Rect(166, 64, 21, 21)
openMusicSettings = Rect(1260, 459, 20, 100)
musicSettings = Rect(1080, 459, 200, 100)
closeMusicSettings = Rect(1080, 459, 20, 100)
volumeSlider = Rect(1180, 469, 30, 20)
lastSongRect = Rect(1140, 529, 40, 20)
nextSongRect = Rect(1210, 529, 40, 20)
openToolPreview = Rect(1260,579,20,100)
previewSettings = Rect(1080,579,200,99)
closePreviewSettings = Rect(1080,579,20,100)
# WarframeSticker rectangles
topBox = Rect(226, 13, 520, 2)
emberStamp = Rect(226, 17, 96, 96)
excalStamp = Rect(325, 17, 96, 96)
frostStamp = Rect(424, 17, 96, 96)
lokiStamp = Rect(226, 116, 96, 96)
magStamp = Rect(325, 116, 96, 96)
novaStamp = Rect(424, 116, 96, 96)
rhinoStamp = Rect(226, 214, 96, 96)
trinityStamp = Rect(325, 214, 96, 96)
voltStamp = Rect(424, 214, 96, 96)
bottomBox = Rect(226, 312, 520, 2)
# 25%
screen.fill((0, 0, 0))
loaded = loadFont.render("25%", False, (255, 255, 255))
screen.blit(loaded, (1, 5))
display.flip()
# Colours for box 1
useColour1Box1 = Rect(232, 25, 10, 20)
useColour2Box1 = Rect(244, 25, 10, 20)
# Colours for box 2
useColour1Box2 = Rect(232, 75, 10, 20)
useColour2Box2 = Rect(244, 75, 10, 20)
mixedColourBox = Rect(358, 45, 30, 30)
mixBG = Rect(260, 18, 132, 84)
# Surfaces
canvaSurface = screen.subsurface(canvas)
toolDisplaySurface= screen.subsurface(previewSettings)
alphaSurface = Surface((1280, 720))
# Images
logo = image.load("img/warframeLogo.png")
palette = image.load("img/color-pickerS.png")
backgroundSelection = [["backgrounds/corpus1.png", "backgrounds/corpus2.png", "backgrounds/corpus3.png"]
    , ["backgrounds/grineer1.png", "backgrounds/grineer2.png", "backgrounds/grineer3.png"]
    , ["backgrounds/tenno1.png", "backgrounds/tenno2.png", "backgrounds/tenno3.png"]
    , ["backgrounds/void1.png", "backgrounds/void2.png", "backgrounds/void3.png"]]
logo = transform.smoothscale(logo, (461, 153))
penTool = image.load("img/pencil.png")
rulerModifier = image.load("img/rulerShort.png")
eraserTool = image.load("img/eraser.png")
handModifier = image.load("img/freehand.png")
trashModifier = image.load("img/trash.png")
measure = image.load("img/compass.png")
circleModifier = image.load("img/circle.png")
rectangleModifier = image.load("img/rectangle.png")
paintBucket = image.load("img/bucket.png")
sprayModifier = image.load("img/spray.png")
windowIcon = image.load("img/windowIcon.png")
undoButton = image.load("img/undo.png")
redoButton = transform.flip(undoButton, True, False)
eyeDropToolIcon = image.load("img/eyedrop.png")
eyeDropModifier = image.load("img/eyedropMod.png")
pestle = image.load("img/MandP.png")
useColour1 = image.load("img/colour1.png")
useColour2 = image.load("img/colour2.png")
setColour1 = image.load("img/setColour1.png")
setColour2 = image.load("img/setColour2.png")
inkTool = image.load("img/ink.png")
textModifier = image.load("img/text.png")
stampModifier = image.load("img/stamp.png")
bucketModifier = image.load("img/bucketMod.png")
grineer = image.load("img/grineer.jpg")
corpus = image.load("img/corpus.jpg")
tenno = image.load("img/tenno.jpg")
grineer = transform.smoothscale(grineer, (268, 400))
corpus = transform.smoothscale(corpus, (268, 400))
tenno = transform.smoothscale(tenno, (268, 400))
flipFilter = image.load("img/flipFilter.png")
folder = image.load("img/folder.png")
save = image.load("img/save.png")
load = image.load("img/load.png")
openArrow = image.load("img/soundArrow.png")
openArrowHover = image.load("img/soundArrowHover.png")
closeArrow = transform.flip(openArrow, True, False)
closeArrowHover = transform.flip(openArrowHover, True, False)
leftArrow = image.load("img/leftArrow.png")
rightArrow = transform.flip(leftArrow, True, False)
cursor = image.load("img/cursor.png")
#cursor = transform.smoothscale(cursor,(32,32))
# 50%
screen.fill((0, 0, 0))
loaded = loadFont.render("50%", False, (255, 255, 255))
screen.blit(loaded, (1, 5))
display.flip()
# Stamps - rest of stamps loaded later
excalibur = image.load("wfStickers/Excalibur.png")
excaliburPrime = image.load("wfStickers/ExcaliburPrime.png")
# Fonts
helpFont = font.Font("fonts/sansation/sansation.ttf", 20)
modFont = font.Font("fonts/sansation/sansationLight.ttf", 15)
descFont = font.Font("fonts/sansation/sansationLight.ttf", 12)
typeFont = font.Font("fonts/sansation/sansationLight.ttf", 25)
# Other
tool = "linePen"
colour = dumfingColour
colour2 = dumfingColour2
size = 5
mx, my = 0, 0
bucketList = []
omx, omy = mx, my
redoBuffer = []
undoBuffer = []
colourMix1, colourMix2 = white, white
mixerTool = "mixcolour1"
invertColour = (255 - colour[0], 255 - colour[1], 255 - colour[2])
invertColour2 = (255, colour[0], 255 - colour[1], 255 - colour[2])
allowUnRe = True
typing = False
message = []
textColour = colour
scrollUp = False
scrollDown = False
scrollBar = 0
prime = False
canScrollUp = False
canScrollDown = False
choosing = True
lineMx, lineMy = 0, 0
sticker = "ember"
pickedTenno = False
factionChosen = False
canPickTenno = False
currentHover = "none"
musicEnd = 15
mixer.music.set_endevent(musicEnd)
musicEnds = -1
soundSettingsOpened = False
volume = 0
canChangeSong = True
flipSc = True
bg = image.load(backgroundSelection[0][0])
toolPreviewOpened=False
previewScale=0
toolSurfaceDisplayOld=toolDisplaySurface.copy()
exampleWord="Hello World"
blitText=False
# 75%
screen.fill((0, 0, 0))
loaded = loadFont.render("75%", False, (255, 255, 255))
screen.blit(loaded, (1, 5))
display.flip()
# Window makeup
display.set_icon(windowIcon)
display.set_caption(choice(windowLines))


# Canvas Interactions
# Pens (Line and free)
def penDraw(surface, startX, startY, endX, endY, colourIn, thickness):
    global oldScreenCap
    xLeg, yLeg = endX - startX, endY - startY
    penHypot = hypot(xLeg, yLeg)
    if penHypot == 0:
        penHypot = 1
    xRatio, yRatio = xLeg / penHypot, yLeg / penHypot
    for i in range(0, int(penHypot)):
        draw.circle(surface, colourIn, (int(startX + (xRatio * i)), int(startY + (yRatio * i))), max(thickness, 0))
        # Ellipse


def circleDraw(surface, startX, startY, endX, endY, colourIn, thickness):
    global oldScreenCap
    screen.blit(oldScreenCap, canvas)
    ellipseRect = Rect(startX, startY, endX - startX, endY - startY)
    ellipseRect.normalize()
    thicknessMod = max(min(min(ellipseRect.height, ellipseRect.width) // 2, thickness), 0)
    draw.ellipse(surface, colourIn, ellipseRect, thicknessMod)
    # Spray Can


def sprayDraw(surface, startX, startY, endX, endY, colourIn, thickness):
    global oldScreenCap
    spRadius = max(3, thickness)
    xLeg, yLeg = endX - startX, endY - startY
    penHypot = hypot(xLeg, yLeg)
    if penHypot == 0:
        penHypot = 1
    xRatio, yRatio = xLeg / penHypot, yLeg / penHypot
    for i in range(0, int(penHypot)):
        for j in range(max(3, thickness // 3)):
            sprayX = randint(0 - spRadius * 4, spRadius * 4)
            sprayY = randint(0 - spRadius * 4, spRadius * 4)
            if hypot(sprayX, sprayY) <= spRadius * 4:
                surface.set_at((int(startX + (xRatio * i)) + sprayX, int(startY + (yRatio * i)) + sprayY), colourIn)


def floodFill(surface,limits, newColour, xIn, yIn):
    colourToChange = surface.get_at((xIn, yIn))
    if colourToChange == newColour:
        return 0
    paintcoords = set()
    paintcoords.add((xIn, yIn))
    while len(paintcoords) > 0:
        x, y = paintcoords.pop()
        if surface.get_at((x, y)) == colourToChange and limits.collidepoint(x, y):
            surface.set_at((x, y), newColour)
            paintcoords.add((x + 1, y))
            paintcoords.add((x - 1, y))
            paintcoords.add((x, y + 1))
            paintcoords.add((x, y - 1))


def redrawBG():
    global bg, logo, screen
    screen.blit(bg, (0, 1))
    screen.blit(logo, (470, 0))


# 100%
screen.fill((0, 0, 0))
loaded = loadFont.render("100%", False, (255, 255, 255))
screen.blit(loaded, (1, 5))
display.flip()
endTime = time.get_ticks()
screen.fill((0, 0, 0))
loaded = loadFont.render("Loaded in " + str(endTime - startTime) + " milliseconds", False, (255, 255, 255))
print("Loaded in",endTime-startTime,"ms")
screen.blit(loaded, (1, 5))
display.flip()
time.wait(1000)
screen.fill((0, 0, 0))
# background choosing
while choosing:
    for e in event.get():
        if e.type == QUIT:
            running = False
            choosing = False
        if e.type == MOUSEBUTTONUP:
            canPickTenno = True
        if e.type == KEYDOWN:
            if e.key == 27:
                running=False
                choosing=False
    screen.fill(black)
    screen.blit(logo, (640 - logo.get_width() // 2, 100))
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    if corpusBox.collidepoint((mx, my)) and not factionChosen:
        screen.blit(corpus, (228, 252 - 10))
        screen.blit(flipFilter, (228, 452 - 10))
        screen.blit(tenno, (506, 252))
        screen.blit(flipFilter, (506, 452))
        screen.blit(grineer, (784, 252))
        screen.blit(flipFilter, (784, 452))
        if mb[0]:
            bg = image.load(backgroundSelection[0][randint(0, 2)])
            choosing = False
            factionChosen = True
            for i in range(255):
                alphaSurface.set_alpha(1)
                alphaSurface.fill((0, 0, 0))
                screen.blit(alphaSurface, (0, 0))
                display.flip()
                time.wait(0)
    elif tennoBox.collidepoint((mx, my)) and not factionChosen:
        screen.blit(corpus, (228, 252))
        screen.blit(flipFilter, (228, 452))
        screen.blit(tenno, (506, 252 - 10))
        screen.blit(flipFilter, (506, 452 - 10))
        screen.blit(grineer, (784, 252))
        screen.blit(flipFilter, (784, 452))
        if mb[0]:
            factionChosen = True
            pickedTenno = True
            for i in range(255):
                alphaSurface.set_alpha(1)
                alphaSurface.fill((0, 0, 0))
                screen.blit(alphaSurface, (0, 0))
                display.flip()
                time.wait(0)
    elif grineerBox.collidepoint((mx, my)) and not factionChosen:
        screen.blit(corpus, (228, 252))
        screen.blit(flipFilter, (228, 452))
        screen.blit(tenno, (506, 252))
        screen.blit(flipFilter, (506, 452))
        screen.blit(grineer, (784, 252 - 10))
        screen.blit(flipFilter, (784, 452 - 10))
        if mb[0]:
            bg = image.load(backgroundSelection[1][randint(0, 2)])
            choosing = False
            factionChosen = True
            canPickTenno = False
            for i in range(255):
                alphaSurface.set_alpha(1)
                alphaSurface.fill((0, 0, 0))
                screen.blit(alphaSurface, (0, 0))
                display.flip()
                time.wait(0)
    elif not factionChosen:
        screen.blit(corpus, (228, 252))
        screen.blit(flipFilter, (228, 452))
        screen.blit(tenno, (506, 252))
        screen.blit(flipFilter, (506, 452))
        screen.blit(grineer, (784, 252))
        screen.blit(flipFilter, (784, 452))
    if factionChosen and pickedTenno and canPickTenno:
        if vanillaTennoBox.collidepoint((mx, my)):
            draw.rect(screen, white, (506, 247, 124, 400))
            draw.rect(screen, white, (640, 257, 124, 400))
            screen.blit(excalibur, (506, 247), (80, 0, 124, 400))
            screen.blit(excaliburPrime, (640, 257), (75, 5, 124, 400))
            screen.blit(flipFilter, (506, 447), (0, 0, 124, 200))
            screen.blit(flipFilter, (640, 457), (0, 0, 124, 200))
            if mb[0]:
                bg = image.load(backgroundSelection[2][randint(0, 2)])
                choosing = False
                prime = False
        elif orokinVoidBox.collidepoint((mx, my)):
            draw.rect(screen, white, (506, 257, 124, 400))
            draw.rect(screen, white, (640, 247, 124, 400))
            screen.blit(excalibur, (506, 257), (80, 0, 124, 400))
            screen.blit(excaliburPrime, (640, 247), (75, 5, 124, 400))
            screen.blit(flipFilter, (506, 457), (0, 0, 124, 200))
            screen.blit(flipFilter, (640, 447), (0, 0, 124, 200))
            if mb[0]:
                bg = image.load(backgroundSelection[3][randint(0, 2)])
                choosing = False
                prime = True
                sticker = "emberPrime"
        else:
            draw.rect(screen, white, (506, 257, 124, 400))
            draw.rect(screen, white, (640, 257, 124, 400))
            screen.blit(excalibur, (506, 257), (80, 0, 124, 400))
            screen.blit(excaliburPrime, (640, 257), (75, 5, 124, 400))
            screen.blit(flipFilter, (506, 457), (0, 0, 124, 200))
            screen.blit(flipFilter, (640, 457), (0, 0, 124, 200))
    reflectionSurf = screen.subsurface((0, 262, 1280, 400))
    reflection = reflectionSurf.copy()
    reflection = transform.flip(reflection, False, True)
    screen.blit(reflection, (0, 652))
    display.flip()
# End background choosing
drumIn.play()
for i in range(255):
    alphaSurface.set_alpha(1)
    alphaSurface.fill((0, 0, 0))
    screen.blit(alphaSurface, (0, 0))
    display.flip()
    time.wait(0)
# Loading prime stamps and non prime stamps
if prime:
    emberPrime = image.load("wfStickers/EmberPrime.png")
    frostPrime = image.load("wfStickers/FrostPrime.png")
    lokiPrime = image.load("wfStickers/LokiPrime.png")
    magPrime = image.load("wfStickers/MagPrime.png")
    novaPrime = image.load("wfStickers/NovaPrime.png")
    rhinoPrime = image.load("wfStickers/RhinoPrime.png")
    trinityPrime = image.load("wfStickers/TrinityPrime.png")
    voltPrime = image.load("wfStickers/VoltPrime.png")
else:
    ember = image.load("wfStickers/Ember.png")
    frost = image.load("wfStickers/Frost.png")
    loki = image.load("wfStickers/Loki.png")
    mag = image.load("wfStickers/Mag.png")
    nova = image.load("wfStickers/Nova.png")
    rhino = image.load("wfStickers/Rhino.png")
    trinity = image.load("wfStickers/Trinity.png")
    volt = image.load("wfStickers/Volt.png")
redrawBG()
canvaSurface.fill(white)
oldScreenCap = canvaSurface.copy()
currentCanvas = canvaSurface.copy()
undoBuffer.append(canvaSurface.copy())
nextSong()
# MAIN CODE
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            # Have to change where canvas is copied, will update when selecting colours. shouldn't
            if e.button != 4 and e.button != 5:
                if canvas.collidepoint(mx, my):
                    lineMx, lineMy = mx, my
                oldScreenCap = canvaSurface.copy()
            if e.button == 4:
                scrollUp = True
            if e.button == 5:
                scrollDown = True
            redrawBG()
        if e.type == MOUSEBUTTONUP:
            if canvaSurface.copy() != undoBuffer[-1] and canvas.collidepoint((mx, my)) and tool != "text" and e.button != 4 and e.button != 5:
                undoBuffer.append(canvaSurface.copy())
                del redoBuffer[0:]
            redrawBG()
            allowUnRe = True
            canChangeSong = True
        if e.type == KEYDOWN:
            if e.key == 27:
                running = False
            if e.key == 13 and typing == True:
                typing = False
                blitText=True
            if e.key == 8 and len(message) > 0:
                del message[-1]
            elif typing == True:
                message.append(e.unicode)
        if e.type == musicEnd:
            nextSong()
            if musicEnds == len(musicCollection):
                musicEnds = 0
    # ███████████████████████████████████████████████████████████████████████████████
    # Draw Canvas and tools
    draw.rect(screen, white, (10, 10, 184, 64))
    screen.blit(currentCanvas, canvas)
    screen.blit(palette, colourPalette)
    screen.blit(penTool, pencil)
    screen.blit(eraserTool,eraser)
    screen.blit(measure, compass)
    screen.blit(paintBucket, bucket)
    screen.blit(undoButton, undo)
    screen.blit(redoButton, redo)
    screen.blit(eyeDropToolIcon, eyeDropTool)
    screen.blit(inkTool, ink)
    screen.blit(folder, folderBox)
    # Help boxes
    draw.rect(screen, white, (1180, 385, 100, 20))
    draw.rect(screen, white, (1180, 407, 100, 20))
    draw.rect(screen, white, (1180, 429, 100, 20))
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    mixer.music.set_endevent(musicEnd)
    # Inverted Colours
    invertColour, invertColour2 = (255 - colour[0], 255 - colour[1], 255 - colour[2]), (
    255 - colour2[0], 255 - colour2[1], 255 - colour2[2])
    # Scrolling
    if scrollUp and tool != "stamp":
        size += 1
    elif scrollDown and tool != "stamp":
        size -= 1
    elif tool == "stamp" and mb == (0, 0, 0):
        canScrollUp = 17 > emberStamp[1] + scrollBar
        canScrollDown = 10 < voltStamp[1] + scrollBar
        if scrollUp and canScrollUp:
            scrollBar = 12
        elif scrollDown and canScrollDown:
            scrollBar = -12
        if ((canScrollUp and scrollUp and scrollBar == 12) or (canScrollDown and scrollDown and scrollBar == -12)):
            topBox = Rect(topBox[0], topBox[1] + scrollBar, 520, 2)
            emberStamp = Rect(emberStamp[0], emberStamp[1] + scrollBar, 96, 96)
            excalStamp = Rect(excalStamp[0], excalStamp[1] + scrollBar, 96, 96)  # Rect(224,12,96,96)
            frostStamp = Rect(frostStamp[0], frostStamp[1] + scrollBar, 96, 96)  # Rect(323,12,96,96)
            lokiStamp = Rect(lokiStamp[0], lokiStamp[1] + scrollBar, 96, 96)  # Rect(422,14,32,32)
            magStamp = Rect(magStamp[0], magStamp[1] + scrollBar, 96, 96)  # Rect(328,14,32,32)
            novaStamp = Rect(novaStamp[0], novaStamp[1] + scrollBar, 96, 96)
            rhinoStamp = Rect(rhinoStamp[0], rhinoStamp[1] + scrollBar, 96, 96)  # Rect(226,48,32,32)
            trinityStamp = Rect(trinityStamp[0], trinityStamp[1] + scrollBar, 96, 96)  # Rect(424,111,96,96)
            voltStamp = Rect(voltStamp[0], voltStamp[1] + scrollBar, 96, 96)  # Rect(294,48,32,32)
            bottomBox = Rect(bottomBox[0], bottomBox[1] + scrollBar, 520, 2)
        scrollBar = 0
    # Tool selection
    if pencil.collidepoint(mx, my):
        screen.blit(penTool, (10, 11))
        if mb[0]:
            tool = "linePen"
    if eraser.collidepoint(mx, my):
        screen.blit(eraserTool, (34, 11))
        if mb[0]:
            tool = "eraser"
    if compass.collidepoint(mx, my):
        screen.blit(measure, (60, 11))
        if mb[0]:
            tool = "circle"
    if bucket.collidepoint(mx, my):
        screen.blit(paintBucket, (85, 11))
        if mb[0]:
            tool = "spray"
    if undo.collidepoint(mx, my):
        draw.rect(screen, darkGrey, undo, 2)
        if mb[0]:
            draw.rect(screen, red, undo, 2)
    if redo.collidepoint(mx, my):
        draw.rect(screen, darkGrey, redo, 2)
        if mb[0]:
            draw.rect(screen, red, redo, 2)
    if eyeDropTool.collidepoint(mx, my):
        screen.blit(eyeDropToolIcon, (106, 11))
        if mb[0]:
            tool = "colourSel"
    if ink.collidepoint(mx, my):
        screen.blit(inkTool, (130, 11))
        if mb[0]:
            tool = "text"
    if folderBox.collidepoint(mx, my):
        screen.blit(folder, (160, 11))
        if mb[0]:
            tool = "files"
    # Tool selected identifier
    if tool == "pen" or tool == "linePen":
        toolName = helpFont.render(helpLines[0][0], True, black)
        if tool == "linePen":
            modifier1 = modFont.render(helpLines[0][1], True, red)
            modifier2 = modFont.render(helpLines[0][2], True, black)
        elif tool == "pen":
            modifier1 = modFont.render(helpLines[0][1], True, black)
            modifier2 = modFont.render(helpLines[0][2], True, red)
        screen.blit(penTool, (10, 11))
    elif tool == "eraser":
        # colour text for eraser is useless, but it's there!
        toolName = helpFont.render(helpLines[1][0], True, black)
        if tool == "eraser":
            modifier1 = modFont.render(helpLines[1][1], True, black)
            modifier2 = modFont.render(helpLines[1][2], True, red)
        elif tool == "trash":
            modifier1 = modFont.render(helpLines[1][1], True, red)
            modifier2 = modFont.render(helpLines[1][2], True, black)
        screen.blit(eraserTool, (34, 11))
    elif tool == "circle" or tool == "rectangle":
        toolName = helpFont.render(helpLines[2][0], True, black)
        if tool == "circle":
            modifier1 = modFont.render(helpLines[2][1], True, red)
            modifier2 = modFont.render(helpLines[2][2], True, black)
        if tool == "rectangle":
            modifier1 = modFont.render(helpLines[2][1], True, black)
            modifier2 = modFont.render(helpLines[2][2], True, red)
        screen.blit(measure, (60, 11))
    elif tool == "spray" or tool == "bucket":
        # Same for paint, but hopefully can change in the future
        toolName = helpFont.render(helpLines[3][0], True, black)
        if tool == "spray":
            modifier1 = modFont.render(helpLines[3][1], True, red)
            modifier2 = modFont.render(helpLines[3][2], True, black)
        elif tool == "bucket":
            modifier1 = modFont.render(helpLines[3][1], True, black)
            modifier2 = modFont.render(helpLines[3][2], True, red)
        screen.blit(paintBucket, (85, 11))
    elif tool == "colourSel" or tool == "mixer":
        toolName = helpFont.render(helpLines[4][0], True, black)
        if tool == "colourSel":
            modifier1 = modFont.render(helpLines[4][1], True, red)
            modifier2 = modFont.render(helpLines[4][2], True, black)
        elif tool == "mixer":
            modifier1 = modFont.render(helpLines[4][1], True, black)
            modifier2 = modFont.render(helpLines[4][2], True, red)
        screen.blit(eyeDropToolIcon, (106, 11))
    elif tool == "text" or tool == "stamp":
        toolName = helpFont.render(helpLines[5][0], True, black)
        if tool == "text":
            modifier1 = modFont.render(helpLines[5][1], True, red)
            modifier2 = modFont.render(helpLines[5][2], True, black)
        elif tool == "stamp":
            modifier1 = modFont.render(helpLines[5][1], True, black)
            modifier2 = modFont.render(helpLines[5][2], True, red)
            screen.blit(inkTool, (130, 11))
    elif tool == "files":
        toolName = helpFont.render(helpLines[6][0], True, black)
        modifier1 = modFont.render(helpLines[6][1], True, black)
        modifier2 = modFont.render(helpLines[6][2], True, black)
        screen.blit(folder, (160, 11))
    screen.blit(toolName, (1181, 383))
    screen.blit(modifier1, (1190, 407))
    screen.blit(modifier2, (1190, 429))
    # "Quiver"
    draw.rect(screen, grey, (10, 32, 184, 64))
    draw.rect(screen, (50, 50, 50), (58, 96, 88, 17))
    thePouch = modFont.render("Armory", True, cyan)
    screen.blit(thePouch, (79, 95))
    ## Mixer UI
    if tool == "mixer":
        draw.rect(screen, darkGrey, mixerOptions)
        draw.rect(screen, (140, 140, 140), mixBG)
        screen.blit(useColour1, (232, 25))
        screen.blit(useColour2, (244, 25))
        screen.blit(useColour1, (232, 75))
        screen.blit(useColour2, (244, 75))
        screen.blit(setColour1, (396, 39))
        screen.blit(setColour2, (396, 61))
        draw.rect(screen, colourMix1, mixColourBox1)
        draw.rect(screen, colourMix2, mixColourBox2)
        draw.line(screen, colourMix1, (296, 35), (321, 59), 5)
        draw.line(screen, colourMix2, (296, 85), (321, 61), 5)
        mixedColour = [(colourMix1[0] + colourMix2[0]) // 2, (colourMix1[1] + colourMix2[1]) // 2,(colourMix1[2] + colourMix2[2]) // 2]
        draw.line(screen, mixedColour, (321, 60), (355, 60), 6)
        draw.rect(screen, mixedColour, mixedColourBox)
    # Modifiers
    # Pen Modifiers
    if tool == "pen" or tool == "linePen":
        screen.blit(rulerModifier, (10, 42))
        screen.blit(handModifier, (10, 64))
        if ruler.collidepoint(mx, my):
            draw.rect(screen, darkGrey, ruler, 2)
            if mb[0]:
                tool = "linePen"
        elif freehand.collidepoint(mx, my):
            draw.rect(screen, darkGrey, freehand, 2)
            if mb[0]:
                tool = "pen"
        if tool == "linePen":
            draw.rect(screen, red, ruler, 2)
        elif tool == "pen":
            draw.rect(screen, red, freehand, 2)
            # Eraser Modifiers
    elif tool == "eraser":
        screen.blit(trashModifier, (34, 42))
        if trash.collidepoint(mx, my):
            draw.rect(screen, darkGrey, trash, 2)
            if mb[0]:
                draw.rect(screen, red, trash, 2)
                canvaSurface.fill(white)
                undoBuffer.append(canvaSurface.copy())
                del redoBuffer[0:]
                # Shape Modifiers
    elif tool == "rectangle" or tool == "circle":
        screen.blit(circleModifier, (58, 42))
        screen.blit(rectangleModifier, (58, 64))
        if circle.collidepoint(mx, my):
            draw.rect(screen, darkGrey, circle, 2)
            if mb[0]:
                tool = "circle"
        elif rectangle.collidepoint(mx, my):
            draw.rect(screen, darkGrey, rectangle, 2)
            if mb[0]:
                tool = "rectangle"
        if tool == "circle":
            draw.rect(screen, red, circle, 2)
        elif tool == "rectangle":
            draw.rect(screen, red, rectangle, 2)
            # Paint Modifiers
    elif tool == "bucket" or tool == "spray":
        screen.blit(sprayModifier, (82, 42))
        screen.blit(bucketModifier, (82, 64))
        if spray.collidepoint(mx, my):
            draw.rect(screen, darkGrey, spray, 2)
            if mb[0]:
                tool = "spray"
        elif bucketBox.collidepoint((mx, my)):
            draw.rect(screen, darkGrey, bucketBox, 2)
            if mb[0]:
                tool = "bucket"
        if tool == "spray":
            draw.rect(screen, red, spray, 2)
        elif tool == "bucket":
            draw.rect(screen, red, bucketBox, 2)
            # Canvas Colour Modifiers
    elif tool == "colourSel" or tool == "mixer":
        screen.blit(eyeDropModifier, (106, 42))
        screen.blit(pestle, (106, 64))
        if eyeDrop.collidepoint(mx, my):
            draw.rect(screen, darkGrey, eyeDrop, 2)
            if mb[0]:
                tool = "colourSel"
        elif MortAndPest.collidepoint(mx, my):
            draw.rect(screen, darkGrey, MortAndPest, 2)
            if mb[0]:
                tool = "mixer"
                mixerTool = "mixcolour1"
        if tool == "colourSel":
            draw.rect(screen, red, eyeDrop, 2)
        elif tool == "mixer":
            draw.rect(screen, red, MortAndPest, 2)
            if mixColourBox1.collidepoint(mx, my):
                draw.rect(screen, darkGrey, mixColourBox1, 2)
                if mb[0]:
                    draw.rect(screen, red, mixColourBox1, 2)
                    mixerTool = "mixcolour1"
            elif mixColourBox2.collidepoint(mx, my):
                draw.rect(screen, darkGrey, mixColourBox2, 2)
                if mb[0]:
                    draw.rect(screen, red, mixColourBox2, 2)
                    mixerTool = "mixcolour2"
            if useColour1Box1.collidepoint(mx, my):
                draw.rect(screen, darkGrey, useColour1Box1, 2)
                if mb[0]:
                    draw.rect(screen, red, useColour1Box1, 2)
                    mixerTool = ""
                    colourMix1 = colour
            elif useColour2Box1.collidepoint(mx, my):
                draw.rect(screen, darkGrey, useColour2Box1, 2)
                if mb[0]:
                    draw.rect(screen, red, useColour2Box1, 2)
                    mixerTool = ""
                    colourMix1 = colour2
            elif useColour1Box2.collidepoint(mx, my):
                draw.rect(screen, darkGrey, useColour1Box2, 2)
                if mb[0]:
                    draw.rect(screen, red, useColour1Box2, 2)
                    mixerTool = ""
                    colourMix2 = colour
            elif useColour2Box2.collidepoint(mx, my):
                draw.rect(screen, darkGrey, useColour2Box2, 2)
                if mb[0]:
                    draw.rect(screen, red, useColour2Box2, 2)
                    mixerTool = ""
                    colourMix2 = colour2
            if setColour1Box.collidepoint(mx, my):
                draw.rect(screen, darkGrey, setColour1Box, 2)
                if mb[0]:
                    draw.rect(screen, red, setColour1Box, 2)
                    colour = mixedColour
            elif setColour2Box.collidepoint(mx, my):
                draw.rect(screen, darkGrey, setColour2Box, 2)
                if mb[0]:
                    draw.rect(screen, red, setColour2Box, 2)
                    colour2 = mixedColour
            if mixerTool == "mixcolour1":
                draw.rect(screen, red, mixColourBox1, 2)
            elif mixerTool == "mixcolour2":
                draw.rect(screen, red, mixColourBox2, 2)
                # Ink Modifiers
    elif tool == "text" or tool == "stamp":
        screen.blit(textModifier, (129, 42))
        screen.blit(stampModifier, (129, 64))
        if textMod.collidepoint((mx, my)):
            draw.rect(screen, darkGrey, textMod, 2)
            if mb[0]:
                draw.rect(screen, red, textMod, 2)
                tool = "text"
        if stampRectangle.collidepoint((mx, my)):
            draw.rect(screen, darkGrey, stampRectangle, 2)
            if mb[0]:
                draw.rect(screen, red, stampRectangle, 2)
                tool = "stamp"
        if tool == "text":
            draw.rect(screen, red, textMod, 2)
        elif tool == "stamp":
            draw.rect(screen, red, stampRectangle, 2)
            # File Modifiers
    elif tool == "files":
        screen.blit(save, (161, 42))
        screen.blit(load, (161, 64))
        if saveBox.collidepoint(mx, my):
            draw.rect(screen, darkGrey, saveBox, 2)
            if mb[0]:
                draw.rect(screen, red, saveBox, 2)
                fname = filedialog.asksaveasfilename(defaultextension=[".png"])
                if len(fname) > 0:
                    image.save(canvaSurface, fname)
        if loadBox.collidepoint(mx, my):
            draw.rect(screen, darkGrey, loadBox, 2)
            if mb[0]:
                draw.rect(screen, red, loadBox, 2)
                fname = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.bmp;*.jpg;*.jpeg")])
                if len(fname) > 0:
                    loadedFile = image.load(fname)
                    loadedFile = transform.smoothscale(loadedFile, (1049, 590))
                    screen.blit(loadedFile, canvas)
    # Canvas interactions
    if mb[0] and canvas.collidepoint(mx, my):
        screen.set_clip(canvas)
        if tool == "linePen":
            screen.blit(oldScreenCap, canvas)
            penDraw(screen, lineMx, lineMy, mx, my, colour, size)
        elif tool == "pen":
            penDraw(screen, omx, omy, mx, my, colour, size)
        elif tool == "eraser":
            penDraw(screen, omx, omy, mx, my, white, size)
        elif tool == "rectangle":
            screen.blit(oldScreenCap, canvas)
            draw.rect(screen, colour, (lineMx, lineMy, mx - lineMx, my - lineMy), max(size, 0))
        elif tool == "circle":
            circleDraw(screen, lineMx, lineMy, mx, my, colour, size)
        elif tool == "spray":
            sprayDraw(screen, mx, my, omx, omy, colour, size)
        elif tool == "bucket":
            floodFill(screen,canvas, colour, mx, my)
        elif tool == "colourSel":
            colour = screen.get_at((mx, my))
        elif tool == "mixer":
            if mixerTool == "mixcolour1":
                colourMix1 = screen.get_at((mx, my))
            elif mixerTool == "mixcolour2":
                colourMix2 = screen.get_at((mx, my))
                # Text
        if tool == "text" and typing == False:
            typing = True
            message = []
            textColour = colour
        screen.set_clip(None)
    elif mb[2] and canvas.collidepoint(mx, my):
        screen.set_clip(canvas)
        if tool == "linePen":
            screen.blit(oldScreenCap, canvas)
            penDraw(screen, lineMx, lineMy, mx, my, colour2, size)
        elif tool == "pen":
            penDraw(screen, omx, omy, mx, my, colour2, size)
        elif tool == "eraser":
            penDraw(screen, omx, omy, mx, my, white, size)
        elif tool == "rectangle":
            screen.blit(oldScreenCap, canvas)
            draw.rect(screen, colour2, (lineMx, lineMy, mx - lineMx, my - lineMy), max(size, 0))
        elif tool == "circle":
            circleDraw(screen, lineMx, lineMy, mx, my, colour2, size)
        elif tool == "spray":
            sprayDraw(screen, mx, my, omx, omy, colour2, size)
        elif tool == "bucket":
            floodFill(screen,canvas, colour2, mx, my)
        elif tool == "colourSel":
            colour2 = screen.get_at((mx, my))
        elif tool == "mixer":
            if mixerTool == "mixcolour1":
                colourMix1 = screen.get_at((mx, my))
            elif mixerTool == "mixcolour2":
                colourMix2 = screen.get_at((mx, my))
                # Text
        if tool == "text" and typing == False:
            typing = True
            message = []
            textColour = colour2
        screen.set_clip(None)
    # Text Tool
    if typing:
        screen.blit(oldScreenCap, canvas)
        draw.line(screen,textColour,(lineMx-2,lineMy+5),(lineMx-2,lineMy+22),2)
        renderedMessage = typeFont.render("".join(message), True, textColour)
        screen.blit(renderedMessage, (lineMx, lineMy))
    if blitText:
        blitText=False
        screen.blit(oldScreenCap, canvas)
        renderedMessage=typeFont.render("".join(message),True,textColour)
        screen.blit(renderedMessage, (lineMx, lineMy))
        undoBuffer.append(canvaSurface.copy())
        del redoBuffer[0:]
    if tool != "text" and typing:
        print("Tool changed while typing")
        typing = False
        screen.blit(oldScreenCap, canvas)
    # StampBox
    if tool == "stamp":
        draw.rect(screen, darkGrey, stampTools)
        draw.rect(screen, grey, stampBox)
        screen.set_clip(stampBox)
        # boxes
        draw.rect(screen, white, topBox)
        draw.rect(screen, darkGrey, emberStamp)
        draw.rect(screen, darkGrey, excalStamp)
        draw.rect(screen, darkGrey, frostStamp)
        draw.rect(screen, darkGrey, lokiStamp)
        draw.rect(screen, darkGrey, magStamp)
        draw.rect(screen, darkGrey, novaStamp)
        draw.rect(screen, darkGrey, rhinoStamp)
        draw.rect(screen, darkGrey, trinityStamp)
        draw.rect(screen, darkGrey, voltStamp)
        draw.rect(screen, white, bottomBox)
        if not prime:
            # Non prime stamps and backgrounds for them
            screen.blit(ember, emberStamp, (80, 8, 96, 96))
            screen.blit(excalibur, excalStamp, (80, 8, 96, 96))
            screen.blit(frost, frostStamp, (86, 10, 96, 96))
            screen.blit(loki, lokiStamp, (86, 8, 96, 96))
            screen.blit(mag, magStamp, (77, 16, 96, 96))
            screen.blit(nova, novaStamp, (80, 15, 96, 96))
            screen.blit(rhino, rhinoStamp, (79, 8, 96, 96))
            screen.blit(trinity, trinityStamp, (61, 8, 96, 96))
            screen.blit(volt, voltStamp, (70, 8, 96, 96))
        else:
            screen.blit(emberPrime, emberStamp, (100, 50, 96, 96))
            screen.blit(excaliburPrime, excalStamp, (80, 20, 96, 96))
            screen.blit(frostPrime, frostStamp, (80, 10, 96, 96))
            screen.blit(lokiPrime, lokiStamp, (86, 8, 96, 96))
            screen.blit(magPrime, magStamp, (77, 16, 96, 96))
            screen.blit(novaPrime, novaStamp, (70, 15, 96, 96))
            screen.blit(rhinoPrime, rhinoStamp, (85, 8, 96, 96))
            screen.blit(trinityPrime, trinityStamp, (80, 8, 96, 96))
            screen.blit(voltPrime, voltStamp, (80, 15, 96, 96))
        if stampBox.collidepoint((mx, my)):
            if emberStamp.collidepoint((mx, my)):
                draw.rect(screen, darkGrey, emberStamp, 2)
                if mb[0]:
                    draw.rect(screen, red, emberStamp, 2)
                    if prime:
                        sticker = "emberPrime"
                    else:
                        sticker = "ember"
            elif excalStamp.collidepoint((mx, my)):
                draw.rect(screen, darkGrey, excalStamp, 2)
                if mb[0]:
                    draw.rect(screen, red, excalStamp, 2)
                    if prime:
                        sticker = "excaliburPrime"
                    else:
                        sticker = "excalibur"
            elif frostStamp.collidepoint((mx, my)):
                draw.rect(screen, darkGrey, frostStamp, 2)
                if mb[0]:
                    draw.rect(screen, red, frostStamp, 2)
                    if prime:
                        sticker = "frostPrime"
                    else:
                        sticker = "frost"
            elif lokiStamp.collidepoint((mx, my)):
                draw.rect(screen, darkGrey, lokiStamp, 2)
                if mb[0]:
                    draw.rect(screen, red, lokiStamp, 2)
                    if prime:
                        sticker = "lokiPrime"
                    else:
                        sticker = "loki"
            elif magStamp.collidepoint((mx, my)):
                draw.rect(screen, darkGrey, magStamp, 2)
                if mb[0]:
                    draw.rect(screen, red, magStamp, 2)
                    if prime:
                        sticker = "magPrime"
                    else:
                        sticker = "mag"
            elif novaStamp.collidepoint((mx, my)):
                draw.rect(screen, darkGrey, novaStamp, 2)
                if mb[0]:
                    draw.rect(screen, red, novaStamp, 2)
                    if prime:
                        sticker = "novaPrime"
                    else:
                        sticker = "nova"
            elif rhinoStamp.collidepoint((mx, my)):
                draw.rect(screen, darkGrey, rhinoStamp, 2)
                if mb[0]:
                    draw.rect(screen, red, rhinoStamp, 2)
                    if prime:
                        sticker = "rhinoPrime"
                    else:
                        sticker = "rhino"
            elif trinityStamp.collidepoint((mx, my)):
                draw.rect(screen, darkGrey, trinityStamp, 2)
                if mb[0]:
                    draw.rect(screen, red, trinityStamp, 2)
                    if prime:
                        sticker = "trinityPrime"
                    else:
                        sticker = "trinity"
            elif voltStamp.collidepoint((mx, my)):
                draw.rect(screen, darkGrey, voltStamp, 2)
                if mb[0]:
                    draw.rect(screen, red, voltStamp, 2)
                    if prime:
                        sticker = "voltPrime"
                    else:
                        sticker = "volt"
        screen.set_clip(None)
        if canvas.collidepoint((mx, my)):
            screen.set_clip(canvas)
            if mb[0]:
                screen.blit(oldScreenCap, canvas)
                screen.blit(eval(sticker),
                            (mx - (eval(sticker).get_width() // 2), my - (eval(sticker).get_height() // 2)))
        screen.set_clip(None)
    ## Undo/Redo
    if mb[0] and allowUnRe:
        if undo.collidepoint(mx, my) and len(undoBuffer) > 1:
            redoBuffer.append(undoBuffer.pop(-1))
            screen.blit(undoBuffer[-1], canvas)
            allowUnRe = False
        if redo.collidepoint(mx, my) and len(redoBuffer) > 0:
            screen.blit(redoBuffer[-1], canvas)
            undoBuffer.append(redoBuffer.pop(-1))
            allowUnRe = False
    # Colour Picker
    draw.rect(screen, colour, (1060, 10, 50, 10))
    draw.rect(screen, colour2, (1060, 30, 50, 10))
    draw.rect(screen, colour, (1112, 10, 20, 10))
    draw.rect(screen, colour2, (1112, 30, 20, 10))
    colour1Text = descFont.render("Colour 1", True, invertColour)
    colour2Text = descFont.render("Colour 2", True, invertColour2)
    screen.blit(colour1Text, (1065, 8))
    screen.blit(colour2Text, (1065, 28))
    if colourPalette.collidepoint(mx, my):
        draw.rect(screen, white, (1142, 10, 128, 128), 1)
        if mb[0]:
            colour = screen.get_at((mx, my))
            draw.rect(screen, colour, (1132, 10, 10, 10))
            draw.rect(screen, colour, (1142, 10, 128, 128), 1)
        elif mb[2]:
            colour2 = screen.get_at((mx, my))
            draw.rect(screen, colour2, (1132, 30, 10, 10))
            draw.rect(screen, colour2, (1142, 10, 128, 128), 1)
    # info display
    draw.rect(screen, white, (1210, 710, 34, 10))
    draw.rect(screen, white, (1246, 710, 34, 10))
    draw.rect(screen, white, (1210, 698, 70, 10))
    xText = descFont.render("x: " + str(mx), True, black)
    yText = descFont.render("y: " + str(my), True, black)
    mouseB = descFont.render("mb: " + str(mb), True, black)
    screen.blit(mouseB, (1211, 696))
    screen.blit(xText, (1211, 708))
    screen.blit(yText, (1247, 708))
    omx, omy = mx, my
    scrollUp, scrollDown = False, False
    currentCanvas = canvaSurface.copy()
    # Volume Bar
    if not soundSettingsOpened:
        draw.rect(screen, (200, 200, 200), openMusicSettings)
        screen.blit(openArrow, openMusicSettings)
        if openMusicSettings.collidepoint(mx, my):
            draw.rect(screen, (100, 100, 100), openMusicSettings)
            screen.blit(openArrowHover, openMusicSettings)
            if mb[0]:
                for i in range(1280, 1079, -1):
                    musicSettings = Rect(i, musicSettings[1], musicSettings[2], musicSettings[3])
                    draw.rect(screen, grey, musicSettings)
                    time.wait(0)
                    display.flip()
                soundSettingsOpened = True
    if soundSettingsOpened:
        draw.rect(screen, grey, musicSettings)
        screen.blit(closeArrow, musicSettings)
        draw.line(screen, black, (1194, 529), (1194, 484), 2)
        draw.rect(screen, (65, 65, 65), volumeSlider)
        if volumeSlider.collidepoint(mx, my):
            if mb[0]:
                volumeSlider = Rect(volumeSlider[0], max(min(my - 15, 529), 469), volumeSlider[2], volumeSlider[3])
                mouse.set_pos((volumeSlider[0] + 15, volumeSlider[1] + 15))
                volume = round(abs(volumeSlider[1] - 529) / 60, 2)
                screen.blit(loadFont.render(str(int(volume * 100)), True, white), (1180, volumeSlider[1] + 5))
                mixer.music.set_volume(volume)
        screen.blit(leftArrow, (1140, 489))
        screen.blit(rightArrow, (1210, 489))
        draw.rect(screen, white, (1102, 480, 65, 20))
        draw.rect(screen, white, (1102, 502, 65, 20))
        songFaction = descFont.render(songNames[musicEnds][0], True, black)
        songStyle = descFont.render(songNames[musicEnds][1], True, black)
        screen.blit(songFaction, (1103, 481))
        screen.blit(songStyle, (1103, 503))
        if lastSongRect.collidepoint(mx, my) and canChangeSong:
            draw.rect(screen, darkGrey, lastSongRect)
            screen.blit(leftArrow, (1140, 489))
            if mb[0]:
                canChangeSong = False
                lastSong()
        if nextSongRect.collidepoint(mx, my) and canChangeSong:
            draw.rect(screen, darkGrey, nextSongRect)
            screen.blit(rightArrow, (1210, 489))
            if mb[0]:
                canChangeSong = False
                nextSong()
        if closeMusicSettings.collidepoint(mx, my):
            draw.rect(screen, (100, 100, 100), closeMusicSettings)
            screen.blit(closeArrowHover, closeMusicSettings)
            if mb[0]:
                redrawBG()
                soundSettingsOpened = False
                flipSc = False
                # Tool Preview Bar
    if not toolPreviewOpened:
        draw.rect(screen,(200,200,200),openToolPreview)
        screen.blit(openArrow,openToolPreview)
        if openToolPreview.collidepoint(mx,my):
            draw.rect(screen,(100,100,100),openToolPreview)
            screen.blit(openArrowHover,openToolPreview)
            if mb[0]:
                for i in range(1280,1079,-1):
                    previewSettings = Rect(i , previewSettings[1], previewSettings[2], previewSettings[3])
                    draw.rect(screen, grey, previewSettings)
                    time.wait(0)
                    display.flip()
                toolPreviewOpened=True
    if toolPreviewOpened:
        draw.rect(screen,white,previewSettings)
        draw.rect(screen,grey,previewSettings,2)
        draw.rect(screen,grey,closePreviewSettings)
        screen.blit(closeArrow,previewSettings)
        screen.set_clip(previewSettings)
        if tool=="pen" or tool == "linePen":
            draw.circle(screen,cyan,(1190,629),max(size,0))
            screen.blit(cursor,(1190,629))
        elif tool=="eraser":
            draw.circle(screen,black,(1190,629),max(size,1),1)
            screen.blit(cursor,(1190,629))
        elif tool=="rectangle":
            draw.rect(screen,cyan,(1150,582,2*int(previewScale),2*int(previewScale)))
            screen.blit(cursor,(1150+2*int(previewScale),582+2*int(previewScale)))
        elif tool=="circle":
            draw.ellipse(screen,cyan,(1150,582,2*int(previewScale),2*int(previewScale)))
            screen.blit(cursor,(1150+2*int(previewScale),582+2*int(previewScale)))
        elif tool=="spray":
            screen.blit(toolSurfaceDisplayOld,(1100,579),(1100,579,180,99))
            sprayDraw(screen,1190,629,1190,629,cyan,size)
            screen.blit(cursor,(1190,629))
            toolSurfaceDisplayOld=screen.copy()
            if previewScale==0:
                toolSurfaceDisplayOld.fill((255,255,255))
        elif tool=="bucket":#Drawing rectangles because it's faster
            draw.line(screen,black,(1190,531),(1190,727))
            if previewScale<10:
                screen.blit(cursor,(1145,629))
            if previewScale==10:
                draw.rect(screen,colour,(1100,580,90,200))
            if previewScale>10 and previewScale<20:
                draw.rect(screen,colour,(1100,580,90,198))
                screen.blit(cursor,(1145+int(9*(previewScale-10)),629))
            if previewScale>20:
                draw.rect(screen,colour,(1100,580,90,198))
                draw.rect(screen,colour2,(1191,580,90,198))
                screen.blit(cursor,(1235,629))
        elif tool=="text":
            if previewScale==0:
                exampleWord=choice(windowLines)
            if int(previewScale)<len(exampleWord):
                exampleText=modFont.render(exampleWord[0:int(previewScale)],True,cyan)
            else:
                exampleText=modFont.render(exampleWord,True,cyan)
            screen.blit(exampleText,(1110,625))
        screen.set_clip(None)
        if closePreviewSettings.collidepoint(mx,my):
            draw.rect(screen,(100,100,100),closePreviewSettings)
            screen.blit(closeArrowHover, closePreviewSettings)
            if mb[0]:
                redrawBG()
                toolPreviewOpened = False
                flipSc = False
    if previewScale>49:#Clock for preview stuff
        previewScale=0
    else:
        previewScale+=0.05
    # ███████████████████████████████████████████████████████████████████████████████████████████
    if flipSc:  # prevents wierd things from appearing when closing sound settings
        display.flip()
    else:
        flipSc = True
quit()
