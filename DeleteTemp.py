import os
import shutil

thelink='C:/Users/devos/AppData/Local/Temp'
for filename in os.listdir(thelink):
    print(filename)
    if filename!="cam_clean.bat":#cam_clean.bat is the file doesnt appear and doesnt let me to delet
        shutil.rmtree(thelink+"/"+filename)
    
    

    
