import os
import pyautogui
import time
from datetime import datetime

confi = 0.9  # GUI finding confident level, reduce to 0.9 to improve result. openCL required.

def playVideoAndZoom():

    # close zoom and vlc if they are runing, to make sure UI state are consistant
    os.system("taskkill /f /im  zoom.exe")
    os.system("taskkill /f /im  vlc.exe")


    os.startfile(r'C:\Users\T420s\Desktop\HappyWalk\PlayHappyWalk.lnk')
    # os.startfile(r'C:\Users\T420s\De sktop\HappyWalk\happyWalkPlusSong.xspf')
    time.sleep(0.5) 
    x,y = pyautogui.size()
    pyautogui.click(x/2, y/2)
    time.sleep(0.5)
    pyautogui.press('space')  #pause the video

    os.startfile(r'C:\Users\T420s\AppData\Roaming\Zoom\bin\Zoom.exe')
    time.sleep(10) 
 
    print("start find meeting icon") 
    meetingID =pyautogui.locateCenterOnScreen(r'C:\autozoom\happywalk.png', confidence=confi)
    # time.sleep(5)
    print(meetingID)
    pyautogui.click(meetingID)        

    print("start find Start icon")
    start =pyautogui.locateCenterOnScreen(r'C:\autozoom\Start.png', confidence=confi)
    print(start)
    pyautogui.click(start)   

#wake up screen
pyautogui.moveTo(200, 200, 1)

playVideoAndZoom()



