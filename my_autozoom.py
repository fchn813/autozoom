import os
import pyautogui
import time
from datetime import datetime

confi = 0.9  # GUI finding confident level, reduce to 0.9 to improve result. openCL required.

def playVideoAndZoom(sleepmin):

    # close zoom and vlc if they are runing, to make sure UI state are consistant
    os.system("taskkill /f /im  zoom.exe")
    os.system("taskkill /f /im  vlc.exe")


    os.startfile(r'C:\Users\T420s\Desktop\HappyWalk\PlayHappyWalk.lnk')
    # os.startfile(r'C:\Users\T420s\De sktop\HappyWalk\happyWalkPlusSong.xspf')
    time.sleep(0.2) 
    x,y = pyautogui.size()
    pyautogui.click(x/2, y/2)
    pyautogui.press('space')  #pause the video
    # pyautogui.hotkey('win','down')  #pause the video
    


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

    time.sleep(sleepmin*60)
    shareVideo()


def shareVideo() :
    #get focus
    x,y = pyautogui.size()
    pyautogui.click(x/2, y/2)
    print("start sharing")

    pyautogui.hotkey("alt","s")
    time.sleep(5)
     
    print("start find VLC icon")
    selectVLC =pyautogui.locateCenterOnScreen(r'C:\autozoom\selectVLC.png', confidence=0.95)
    print(selectVLC)
    pyautogui.click(selectVLC)   

    print("start find Sound icon")
    shareSound =pyautogui.locateCenterOnScreen(r'C:\autozoom\shareSound.png', confidence=confi)
    print(shareSound)
    pyautogui.click(shareSound)  
    time.sleep(1)

    print("start find optVideo icon")
    # optVideo =pyautogui.locateCenterOnScreen(r'C:\autozoom\optVideo.png', confidence=confi)

    pyautogui.click(shareSound.x+200,shareSound.y)   
    time.sleep(1)

    print("start find share icon")
    share =pyautogui.locateCenterOnScreen(r'C:\autozoom\share.png', confidence=confi)
    print(share)
    pyautogui.click(share)   
    time.sleep(1)

    #show video panel
    pyautogui.moveTo(800,0) 
    time.sleep(2)
    pyautogui.moveTo(1250,30)
    time.sleep(2)
    # pyautogui.moveTo(1300,260)
    # time.sleep(1)
    pyautogui.click(1300,260)


    #start video play
    x,y = pyautogui.size()
    pyautogui.click(x/2, y/2)
    pyautogui.hotkey('space')  #pause the video
    
#wake up screen
pyautogui.moveTo(200, 200, 1)
pyautogui.moveTo(500, 600, 1)

startPlayatMin = 9
playVideoAndZoom(startPlayatMin)



