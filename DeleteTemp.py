import os
import shutil

thelink='C:/Users/devos/AppData/Local/Temp'
for filename in os.listdir(thelink):
    print(filename)
    if filename!="cam_clean.bat":
        shutil.rmtree(thelink+"/"+filename)
    
    
