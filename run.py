# macro shit

import pyautogui
import os
import sys
from pynput import mouse
from pynput import keyboard
import time
from PIL import Image
import cv2
import math
import gdk
import gi
import time
gi.require_version("Gdk", "3.0")
from gi.repository import Gdk, GdkPixbuf

blackClr = (0, 0, 0)
whiteClr = (163, 162, 165)

topLeft, topRight, bottomLeft, bottomRight = [], [], [], []

blckDiff1, blckDiff2 = 0, 0

lastClr = []

listener, listener2 = 0, 0

pyautogui.PAUSE = 0.3

def setClr(colour):
    r = colour[0]
    g = colour[1]
    b = colour[2]
    pyautogui.moveTo(884, 930)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(str(r))
    pyautogui.moveTo(965, 930)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(str(g))
    pyautogui.moveTo(1043, 930)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(str(b))
    pyautogui.press("Return")
    lastClr = [r, g, b]

def loadBg(type):
    pyautogui.moveTo(1885, 940)
    pyautogui.click()
    time.sleep(0.5) 
    if type == 0:
        pyautogui.moveTo(830, 360)
        pyautogui.click()
    elif type == 1:
        pyautogui.moveTo(1100, 360)
        pyautogui.click()
    else:
        pyautogui.click()
        return print("invalid type!")
    time.sleep(0.5)
    pyautogui.moveTo(830, 630)
    pyautogui.click()
    time.sleep(5)

def setBgClr(colour):
    setClr(colour)
    cX = topLeft[0]
    cY = topLeft[1]
    for count in range(1, 32):
        for count2 in range(1, 24):
            pyautogui.moveTo(cX, cY)
            pyautogui.click()
            cX += blckDiff1[0]
        cX = topLeft[0]
        cY += blckDiff1[1]

# focus on rbxl
# pyautogui.moveTo(pyautogui.size()[0]/2, pyautogui.size()[1]/2)
# pyautogui.click()

# setBgClr(blackClr)
# setBgClr(whiteClr)

def takeScr(filename):
    w = Gdk.get_default_root_window()
    sz = w.get_geometry()[2:4]
    #print "The size of the window is %d x %d" % sz
    pb = Gdk.pixbuf_get_from_window(w, 0, 0, sz[0], sz[1])
    if (pb != None):
        pb.savev("./rendered/"+filename+".png","png", [], [])
        print("Screenshotted as "+filename+".png.")
    else:
        print("Unable to get the screenshot.")

def analyseFrame(fileName):
    filePath = "./ffmpegd/"+fileName
    img = Image.open(filePath, "r")
    pixels = list(img.getdata())
    highPixels = 0
    for pixel in pixels:
        if pixel > 127:
            highPixels += 1
    bgtype = 1
    if highPixels > (len(pixels)/2):
        bgtype = 0
    print(bgtype)
    return pixels, bgtype

def renderFrame(frameNum):
    startTime = time.time()
    fileName = str(frameNum)+".jpg"
    pixels, bgType = analyseFrame(fileName)
    loadBg(bgType)
    count = 0
    #pyautogui.press("5")
    if bgType == 0:
        if lastClr != [0, 0, 0]:
            setClr((0, 0, 0))
    else:
        if lastClr != [163, 162, 165]:
            setClr((163, 162, 165))
    print(len(pixels))
    for pixel in pixels:
        if pixel > 127:
            clr = 1
        else:
            clr = 0
        if bgType == clr:
            moveX = count % 32
            moveY = math.floor(count/32)
            print(count/32)
            cX = topLeft[0]+((moveX*blckDiff1[0]))
            cY = topLeft[1]+((moveY)*blckDiff1[1])
            pyautogui.moveTo(cX, cY)
            pyautogui.click()
        count += 1
    elapsed = time.time() - startTime
    print("Rendered in "+str(math.ceil(elapsed))+" seconds!")
    return pixels

def start():
    print("Playing project.mp4...")
    pyautogui.moveTo(1115, 1005) # move to paintbrush ingame
    pyautogui.click()
    
    #loop through frames, set to 1690 for testing

    count = 0
    dir = "./ffmpegd/"
    files = os.listdir(dir)
    lastPixls = []
    while count < len(files):
        cPixels, bgType = analyseFrame(str(count)+".jpg")
        if cPixels != lastPixls:
            renderFrame(count)
        takeScr(str(count))

        lastPixls = cPixels
        count += 1

    os._exit(0)













































def on_press(key):
    if key == keyboard.Key.esc:
        exit(0)

print("click on top left")
clix = 0
def on_click(x, y, button, pressed):
    global clix
    global topLeft
    global topRight
    global bottomLeft
    global bottomRight
    global blckDiff1
    global blckDiff2
    if button == mouse.Button.left:
        if clix == 0:
            topLeft = (x, y)
            print("click on top right")
        elif clix == 2:
            topRight = (x, y)
            print("click on bottom left")
        elif clix == 4:
            bottomLeft = (x, y)
            print("click on bottom right")
        elif clix == 6:
            bottomRight = (x, y)
            print(topLeft)
            print(topRight)
            print(bottomLeft)
            print(bottomRight)
            blckDiff1 = (
                -(
                    ( ((topLeft[0] - topRight[0])/32) + ((bottomLeft[0] - bottomRight[0])/32) )/2
                ),
                -(
                    ( ((topLeft[1] - bottomLeft[1])/24) + ((topRight[1] - bottomRight[1])/24) )/2
                )
            )
            #blckDiff2 = ((bottomLeft[0] - bottomRight[0]), (bottomLeft[1] - bottomRight[1]))
            start()
    clix += 1

#listener2 = keyboard.Listener(on_press=on_press)
#listener = mouse.Listener(on_click=on_click)
#listener.start()
#listener.join()
#listener2.start()
#listener2.join()

with mouse.Listener(on_click=on_click) as listener:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
