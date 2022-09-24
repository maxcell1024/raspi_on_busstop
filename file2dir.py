import os

os.chdir(r"/home/pi/EXTRAFS/mp4")
files = os.listdir()
for file in files:
    # rgb動画のとき
    if len(file) == 28:
        print(file[9:17])
        os.renames(file,file[9:17] + "/" + file)
    # ther動画のとき
    if len(file) == 29:
        print(file[10:18])
        os.renames(file,file[10:18] + "/" + file)



