import cv2
import os
import numpy
import glob
from PIL import Image

size = (1920, 1080)

img_array = []
count = 0
dir = './rendered/'
files = os.listdir(dir)
while count < len(files):
    filename = dir+str(count)+".png"
    img = cv2.imread(filename)
    img_array.append(img)
    print(count)
    count += 1
 
 
out = cv2.VideoWriter(filename='project.mp4', fourcc=cv2.VideoWriter_fourcc(*'mp4v'), frameSize=size, fps=30)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
