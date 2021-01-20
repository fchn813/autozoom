import os
import pyautogui
import time
import win32gui
    
# handle = win32gui.FindWindow(0, "Zoom")  #paassing 0 as I dont know classname 


# print (handle)
# win32gui.SetForegroundWindow(handle)  #put the window in foreground

# zw = pyautogui.getAllWindows()

# for w in zw:
#     if w.title == "Zoom" :
#         w.activate()
        

confi = 0.9  # GUI finding confident level, reduce to 0.9 to improve result. openCL required.



def shareVideo() :
    #get focus
    zoomWindow = pyautogui.getWindowsWithTitle("Zoom")
    zoomWindow[0].SetFocus()

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
shareVideo()



