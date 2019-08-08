"""
This is a script to quickly process the time-lapse photo taken by go pro Hero 7 Black
The maximum time between two shots is every 60s.
Therefore, everyday it will take 24*60 = 1440 photos
If the project goes on for more than 1 week, it will generate a lot of photos
Maybe too many for a < 1 min / 30 sec / 10 sec short video.

This scripts helps to evenly copy the photo by every X photos from source folder to destination
    X will be determined by the total number of photo N and target video time T (sec):
    Therefore X = N // (T * 24 frame/s)
"""


import os
import shutil

print("Go-pro photo selector:")

currentdir = os.getcwd()
print("current directory:", os.getcwd())
try:
    os.mkdir("output")
except FileExistsError:
    pass

sourcedir = currentdir + "/gopro/"
destdir = currentdir + "/output/"

fileNum = len(os.listdir(sourcedir))
print("current photo number: ", fileNum)
targetVideoLength = int(input("How long should this video output in secs: "))
totalFrame = targetVideoLength * 24
pickRate = fileNum // totalFrame
print("pick rate is:", pickRate)

start = False
go = input("Start processing? Y/N:")
if go == "Y":
    start = True

if start:
    count = 0
    for f in os.listdir(sourcedir):
        if count % pickRate == 0:
            shutil.copy2(sourcedir + f, destdir)
        count += 1

    print("All done")
    print(len(os.listdir(destdir)), "photos generated")
else:
    print("Job cancelled")
