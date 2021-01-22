import os
import pyautogui
import time
    

confi = 0.9  # GUI finding confident level, reduce to 0.9 to improve result. openCL required.



def shareVideo() :
    #get focus
    # zoomWindow = pyautogui.getWindowsWithTitle("Zoom")
    # zoomWindow[0].SetFocus()

    x,y = pyautogui.size()
    pyautogui.click(x/2, y/2)

    #start video sharing
    pyautogui.hotkey("alt","s")  # start Zoom sharing
    time.sleep(3)
     
    print("start find VLC icon") 
    selectVLC =pyautogui.locateCenterOnScreen(r'C:\autozoom\selectVLC.png', confidence=confi)
    print(selectVLC)
    pyautogui.click(selectVLC)   

    print("start find Sound icon")
    shareSound =pyautogui.locateCenterOnScreen(r'C:\autozoom\shareSound.png', confidence=confi)
    print(shareSound)
    pyautogui.click(shareSound)  
    time.sleep(1)

    pyautogui.click(shareSound.x+200,shareSound.y)   
    time.sleep(1)

    #share video
    print("start find share icon")
    share =pyautogui.locateCenterOnScreen(r'C:\autozoom\share.png', confidence=confi)
    print(share)
    pyautogui.click(share)   
    time.sleep(1)

    #start video play
    x,y = pyautogui.size()
    pyautogui.click(x/2, y/2)
    pyautogui.hotkey('space')  #pause the video

    #show video panel
    pyautogui.moveTo(800,0,0.5) 
    time.sleep(1)
    pyautogui.moveTo(1250,30,0.5)
    time.sleep(1)
    pyautogui.moveTo(1300,260,0.5)
    time.sleep(0.5)
    pyautogui.click()

    
#wake up screen
shareVideo()



