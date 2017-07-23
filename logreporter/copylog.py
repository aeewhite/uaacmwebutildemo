from shutil import copyfile
import time

while 1:
    time.sleep(10)
    copyfile('../log.html', 'log.html')
