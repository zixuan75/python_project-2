import glob, os
for file in glob.glob("/"):
    if file != "/home":
        print(file)
