import os
import shutil
path='C:/Users/mypc/AppData/Local/Temp'
for filename in os.listdir(path):
    try:
       shutil.rmtree(path+"/"+filename)
    except:
        try:
            os.unlink(path+"/"+filename)
        except:
            print("can't delete file ",filename)
            
    
    

    
