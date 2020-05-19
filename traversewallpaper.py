import os
import datetime as dt
import ctypes
import sys

path = 'E:\\Wallpapers\\'

today = dt.datetime.now().date()

files = []

for file in os.listdir(path):
    filetime = dt.datetime.fromtimestamp(os.path.getctime(path+file))
    if filetime.date() == today:
        files.append(path+file)

i = 'n'
for wall in files:
    ctypes.windll.user32.SystemParametersInfoW(20 ,0,wall,3)
    i = input()
    if i == 'x':
        sys.exit()
