import os
# os.add_dll_directory(os.getcwd())
import pyautogui
import time
from datetime import datetime
# import vlc





def playVideoAndZoom():

    os.system("taskkill /f /im  zoom.exe")
    os.system("taskkill /f /im  vlc.exe")

    confi = 0.9

    # os.startfile(r'C:\Users\T420s\Desktop\HappyWalk\PlayHappyWalk.lnk')
    os.startfile(r'C:\Users\T420s\Desktop\HappyWalk\happyWalkPlusSong.xspf')
    time.sleep(2) 
    x,y = pyautogui.size()
    pyautogui.click(x/2, y/2)
    pyautogui.press('space')  #pause the video
    pyautogui.hotkey('win','down')  #pause the video
    


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


    time.sleep(10)
    print("start sharing")
    pyautogui.getActiveWindow()
    pyautogui.hotkey("alt","s")
    time.sleep(5)
     
    print("start find VLC icon")
    selectVLC =pyautogui.locateCenterOnScreen(r'C:\autozoom\selectVLC.png', confidence=confi)
    print(selectVLC)
    pyautogui.click(selectVLC)   

    print("start find Sound icon")
    shareSound =pyautogui.locateCenterOnScreen(r'C:\autozoom\shareSound.png', confidence=confi)
    print(shareSound)
    pyautogui.click(shareSound)  
    time.sleep(1)

    print("start find optVideo icon")
    optVideo =pyautogui.locateCenterOnScreen(r'C:\autozoom\optVideo.png', confidence=confi)
    print(optVideo)
    pyautogui.click(optVideo)   
    time.sleep(1)

    print("start find share icon")
    share =pyautogui.locateCenterOnScreen(r'C:\autozoom\share.png', confidence=confi)
    print(share)
    pyautogui.click(share)   
    time.sleep(1)

    #show video panel
    pyautogui.moveTo(800,0)
    time.sleep(3)
    pyautogui.moveTo(1250,30)
    time.sleep(2)
    pyautogui.moveTo(1300,230)
    pyautogui.click(1300,230)


    more =pyautogui.locateCenterOnScreen(r'C:\autozoom\more.png', confidence=confi)
    print('more done')
    pyautogui.click(more)   
    time.sleep(1)
    vp =pyautogui.locateCenterOnScreen(r'C:\autozoom\vp.png', confidence=confi)
    print('videoPanle done')
    pyautogui.click(vp)   
    time.sleep(1)


    #start video play
    x,y = pyautogui.size()
    pyautogui.click(x/2, y/2)
    pyautogui.hotkey('space')  #pause the video
    
#wake up screen
pyautogui.moveTo(200, 200, 2)
pyautogui.moveTo(500, 600, 2)

playVideoAndZoom()



