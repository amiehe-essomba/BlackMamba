import sys, msvcrt, re


def cursor():
    sys.stdout.write("\x1b[6n")
    sys.stdout.flush()
    buffer = bytes()
    while msvcrt.kbhit():
        buffer += msvcrt.getch()
    hex_loc = buffer.decode()
    res = re.match(r".*\[(?P<y>\d*);(?P<x>\d*)R", hex_loc)
    
    if (res):
        return res.group("x"), res.group("y")
    else: return (-1, -1)

#Add Any helpfull stuff in functions here for later use
def GetMouseInfos(WhatToGet="leaving emety will get you x and y", GetXOnly=False, GetYOnly=False, GetColor=False, Key='Right', OverrideKey=False):#gets color of whats under Key cursor on right click
    try:
        import win32api
    except ModuleNotFoundError:
        print("win32api not found, to install do pip install pywin32")
    try:
        import time
    except ModuleNotFoundError:
        print("time not found, to install do pip install time?")
    try:
        import pyautogui
    except ModuleNotFoundError:
        print("py auto gui not found, to install do pip install pyautogui")
    #--------------------------------------------------------------
    #above checks if needed modules are installed if not tells user
    #code below is to get all varibles needed
    #---------------------------------------------------------------
    print(WhatToGet, OverrideKey, Key )
    if OverrideKey:
        Key_To_click = Key
    if Key == 'Left':
        Key_To_click = 0x01
    if Key == 'Right':
        Key_To_click = 0x02
    if Key == 'Wheel':
        Key_To_click = 0x04
    state_left = win32api.GetKeyState(Key_To_click)  # Left button up = 0 or 1. Button down = -127 or -128
    IsTrue = True
    
    while IsTrue:
        a = win32api.GetKeyState(Key_To_click)
       
        if a != state_left:  # Button state changed
            state_left = a
            if a < 0:
                global Xpos, Ypos
                Xpos, Ypos = win32api.GetCursorPos()
                x, y = pyautogui.position()
                pixelColor = pyautogui.screenshot().getpixel((x, y))
            else:
                posnowX, posnowY = win32api.GetCursorPos()
                #posnowX, posnowY = int( posnowX), int( posnowY)
                Xpos, Ypos = posnowX, posnowY 
                win32api.SetCursorPos((posnowX, posnowY))
                IsTrue = False#remove this for it to keep giving coords on click without it just quitting after 1 click
                print(Xpos, Ypos)
        time.sleep(0.001)
    #--------------------------------------------------------------------
    #The Code above is the code to get all varibles and code below is for the user to get what he wants
    #--------------------------------------------------------------------
    
    if GetXOnly: #Checks if we should get Only X (def options) the command to do this would be GetKeyInfos("Click To get X ONLY", True)
        if GetYOnly:
            return(Xpos , Ypos)
        if GetColor:
            return(Xpos, pixelColor)
        return(Xpos)
    if GetYOnly: #Checks if we should get Only Y (def options) the command to do this would be GetKeyInfos("Click To get X ONLY",False, True)
        if GetXOnly:
            return(Xpos , Ypos)
        if GetColor:
            return(Ypos, pixelColor) 
        return(Ypos)
    if GetColor:
        return(pixelColor) #Checks 
    return(Xpos, Ypos)


if __name__ == '__main__':
    s = GetMouseInfos("", Key='Right')
    print(s)