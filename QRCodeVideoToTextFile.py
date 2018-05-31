#Author: Tudor Gheorghiu, Prodicode
# Modified by John Shearing

# Note from John Shearing: The original version of this program
# was made to reconstruct a png file which had been converted to 
# a video stream of QR-Codes.

# This version has been modified from the original.
# It's purpose is to reconstruct a text file from a video
# of QR-codes each made from a line base64 encoded text 
# from the original file. 

import argparse
import qrtools
import cv2
import os
import numpy as np
import progressbar
import base64 

parser = argparse.ArgumentParser(description="QR Code data reconstructor - made by Tudor Gheorghiu, Prodicode");
parser.add_argument("video", help="Video file containing QR codes", type=str);
parser.add_argument("output", help="The file to output the data to. (output is in base64)", type=str);
args = parser.parse_args();

cap = cv2.VideoCapture(args.video);
qr = qrtools.QR();

print("""\


 Reconstruct Text File from Video Parade of QR-Codes

 by Tudor Gheorghiu
 modified by John Shearing


""");
print("Processing video frames...")
print("NOTE: This process requires time and resources. Please be patient.")
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
print("Processing "+str(total_frames)   +" frames!")
bar = progressbar.ProgressBar(maxval=total_frames, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
currentFrame = 0
tempData = ""
open(args.output, "w")

while(currentFrame <= total_frames):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    cv2.imwrite("temp.jpg", frame)
    qr.decode("temp.jpg")

    # To stop duplicate images
    if (tempData != qr.data):
        tempData = qr.data
        decoded = base64.b64decode(tempData)
        open(args.output, "a").write(decoded)            

    bar.update(currentFrame)
    currentFrame += 1

# This strips out 3 unwanted characters that appear in the ouput file
# for some unknown reason. 
fileString = open(args.output, "r").read()
slicedFileString = fileString[3:]
open(args.output, "w").write(slicedFileString)

# When everything done, release the capture
bar.finish()
os.remove("temp.jpg")
cap.release()
cv2.destroyAllWindows()
print("Data written to "+args.output)
