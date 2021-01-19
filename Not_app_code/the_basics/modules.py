#import sys

#sys.builtin_module_names
#import time
#dir(time)
#time.sleep(#)

#to import non built ins use
#import os
#sys.prefix to get source


import time
import os 
import pandas


while True:
    if os.path.exists("temps_today.csv"):
        data=pandas.read_csv("temps_today.csv")
        print(data.mean())
    else:
        print("File does not exist")
    time.sleep(10)


#here panda has its own type