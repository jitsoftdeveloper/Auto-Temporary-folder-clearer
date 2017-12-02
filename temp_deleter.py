import shutil
import datetime
from time import sleep

path = 'C:\\Users\\Jitender\\AppData\\Local\\Temp'
#path = 'C:/Users/Jitender/Desktop/rm/jj'

while True:
    current_time = datetime.datetime.now()
    print(current_time)
    if current_time.hour == 17:
        shutil.rmtree(path)
        print('Time Matched')
        break
    else:
        sleep(60)
        continue
