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
