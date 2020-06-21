import os
import shutil
thelink='C:/Users/mypc/AppData/Local/Temp'
for filename in os.listdir(thelink):
    try:
       shutil.rmtree(thelink+"/"+filename)
    except:
        try:
            os.unlink(thelink+"/"+filename)
        except:
            print("can't delete file ",filename)
            
    
    

    
