import shutil
import datetime
from time import sleep

path = 'C:/Users/user_name/AppData/Local/Temp'

while True:
    current_time = datetime.datetime.now()
    print(current_time)
    if current_time.hour == 10:
        shutil.rmtree(path)
        print('Temporary Files Deleted Successfully!')
        break
    else:
        sleep(60)
        continue
