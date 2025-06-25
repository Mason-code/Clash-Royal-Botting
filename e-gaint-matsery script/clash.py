from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import pyscreeze

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



def combat():
    # CHECK_IF_END
    the_fight_has_ended = False
    while not the_fight_has_ended:

        #start

        try:

            if pyautogui.locateOnScreen("target.png", grayscale=True, confidence=0.8) and (pyautogui.pixel(1098, 1041)[0] == 198) != None:
                target = pyautogui.locateOnScreen("target.png", grayscale=True, confidence=0.8)[0]
                click(target+35,925)
                print("I have a visual")
                time.sleep(2.5)
                if random.randint(0,1) == 0:
                    click(random.randint(748,883),random.randint(501,566))
                    time.sleep(2.5)
                else:
                    click(random.randint(1009,1144),random.randint(501,566))
                    time.sleep(1.5)
                
                time.sleep(2.0)

        

        
        except ImageNotFoundException:

            print("i blind")

            # X:  860 Y: 1042 RGB: (240, 137, 244)
            try:
                if pyautogui.locateOnScreen("ex.png", grayscale=True, confidence=0.8) and pyautogui.locateOnScreen("target.png", grayscale=True, confidence=0.8) != None:
                    xtarget = pyautogui.locateOnScreen("ex.png", grayscale=True, confidence=0.8)[0]
                    ytarget = pyautogui.locateOnScreen("ex.png", grayscale=True, confidence=0.8)[1]
                    click(xtarget,ytarget)
                    time.sleep(random.uniform(0.5,1.5))
                    click(random.randint(750,1138),random.randint(516,753))

            except ImageNotFoundException:
                print("weird sitch")

            
            time.sleep(random.uniform(0.5,1.0))




            

        #end
        if pyautogui.pixel(1169, 48)[2] != 173:
            print("The fight has ended")
            time.sleep(random.uniform(0.5,1.0))
            the_fight_has_ended = True
        else:
            print("The fight has not ended")
            time.sleep(random.uniform(0.5,1.0))
            continue
        break
    


amount_games = 1
sleeep = 0

while True:
    time.sleep(random.randint(1,4))
    print(f"Amount of Games Played: {amount_games-1}")
    if amount_games % 27 == 0:
        sleeep += 1
        print("sleepy..")
        time.sleep(random.randint(600,1500))
        print(f"It has been many games, time to temporarly go to sleep. I now have slept a total of {sleeep} time(s) this session.")

    # BATTLE
    started = False
    while not started:
        try:
            # check if battle button is there
            # button- X:  879 Y:  698
            if pyautogui.locateOnScreen("battle.png", grayscale=True, confidence=0.8) != None:
                click(879, 698)
                print("Battle clicked")
                time.sleep(random.uniform(0.5,1))
                          
        except ImageNotFoundException:
            print("Battle button not found.")
            time.sleep(random.uniform(0.5,1))
            try:
                if pyautogui.locateOnScreen("end_ok.png", grayscale=True, confidence=0.8) != None:
                    print("Unexepected screen has appeared, loacted problem")
                    xpro = pyautogui.locateOnScreen("end_ok.png", grayscale=True, confidence=0.8)[0]
                    ypro = pyautogui.locateOnScreen("end_ok.png", grayscale=True, confidence=0.8)[1]
                    click(xpro, ypro)
                    print("passed problem")
                    time.sleep(random.uniform(0.5,1.0))
                          
            except ImageNotFoundException:
                print("nothing unexpected happened")
                time.sleep(random.uniform(0.5,1.0))
            continue # keep checking

        break # break out of the started while loop and go to whats after


    # PRE_LOADING
    loading = True
    while loading:
        if pyautogui.pixel(1169, 48)[2] == 173:
            print("The fight has begun")
            time.sleep(random.uniform(0.5,1.0))
        else:
            print("Loading...")
            time.sleep(random.uniform(0.5,1.0))
            continue
        break





    combat()




    the_fight_has_ended = True
    # EXIT
    while the_fight_has_ended:
        try:
            # button- X:  956 Y:  940
            if pyautogui.locateOnScreen("end_ok.png", grayscale=True, confidence=0.8) != None:
                click(956, 940)
                print("OK to end game pressed")
                time.sleep(random.uniform(0.5,1.0))
                          
        except ImageNotFoundException:
            print("ok end button not found.")
            time.sleep(random.uniform(0.5,1.0))
            continue # keep checking

        break # break out of the started while loop and go to whats after
    the_fight_has_ended = False
    amount_games += 1
  


    

