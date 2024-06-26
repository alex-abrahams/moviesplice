import cv2
import argparse
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=False, default='output.mp4', help="output video file")
ap.add_argument("-a", "--all", required=False, default=1, help="all frames if true")
args = vars(ap.parse_args())

root = tk.Tk()
root.withdraw()

frames1 = []
frames2 = []
file_path = filedialog.askopenfilename()
clip1 = cv2.VideoCapture(file_path)
file_path = filedialog.askopenfilename()
clip2 = cv2.VideoCapture(file_path)

while True:
    read, frame= clip1.read()
    if not read:
        break
    frames1.append(frame)
frames1 = np.array(frames1)

while True:
    read, frame= clip2.read()
    if not read:
        break
    frames2.append(frame)
frames2 = np.array(frames2)

videolength = min(len(frames1),len(frames2))

output = args['output']

print(args['all'])
print(type(args['all']))
al = True
if (args['all'] == "0" or args['all'] == "False" or args['all'] == "false"):
    al = False

# Determine the width and height from the first image
cv2.imshow('video',frames1[0])
height, width, channels = frames1[0].shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

print(al)
print(type(al))

for i in range(videolength):
    if (i % 2 == 0 or al):
        out.write(frames1[i])
    if (i % 2 == 1 or al):
        out.write(frames2[i])

# Release everything if job is finished
out.release()