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

    
def maybe_switch():
    try:
        if pyautogui.locateOnScreen("switch.png", grayscale=True, confidence=0.8) != None:
            print("Time to switch accounts")
            time.sleep(random.uniform(0.5,1.0))
            click(pyautogui.locateOnScreen("switch.png", grayscale=True, confidence=0.8)[0], pyautogui.locateOnScreen("switch.png", grayscale=True, confidence=0.8)[1])
            return True
                
                   
    except Exception as e:
        print("conitnur you ganme")
        

    

def do_switch():
    main = True
    while True:
        try:
            if pyautogui.locateOnScreen("step1.png", grayscale=True, confidence=0.8) != None:
                print("broken")
                time.sleep(1)
        except ImageNotFoundException:
            print("still loading from reload")
            time.sleep(1)
            
        try:
            if pyautogui.locateOnScreen("step1.png", grayscale=True, confidence=0.8) != None:
                print("proceed with steps")
                time.sleep(1)
        except ImageNotFoundException:
            print("still loading from reload")
            time.sleep(1)
            continue
        break
        
        
       
    try: 
        if pyautogui.locateOnScreen("fear.png", grayscale=True, confidence=0.8) == None:
            main = False
        else:
            main = True
    except ImageNotFoundException:
        main = False
    print(main)
    click(pyautogui.locateOnScreen("step1.png", grayscale=True, confidence=0.8)[0], pyautogui.locateOnScreen("step1.png", grayscale=True, confidence=0.8)[1])
    print("Completed step 1 of switch")
    time.sleep(random.uniform(0.5,1.0))
    click(pyautogui.locateOnScreen("step2.png", grayscale=True, confidence=0.8)[0], pyautogui.locateOnScreen("step2.png", grayscale=True, confidence=0.8)[1])
    print("Completed step 2 of switch")
    time.sleep(random.uniform(0.5,1.0))
    while True:
        try:
            if main == False:
                click(pyautogui.locateOnScreen("step3main.png", grayscale=False, confidence=0.8)[0], pyautogui.locateOnScreen("step3main.png", grayscale=False, confidence=0.9)[1])
                time.sleep(random.uniform(0.5,1.0))
                print("Completed step 3 of switch: False")
            if main == True:
                click(pyautogui.locateOnScreen("step3alt.png", grayscale=False, confidence=0.8)[0], pyautogui.locateOnScreen("step3alt.png", grayscale=False, confidence=0.9)[1])
                time.sleep(random.uniform(0.5,1.0))
                print("Completed step 3 of switch: True")
            
        except ImageNotFoundException:
            print("image not found")
            continue
        break

        
    print("successful switch")
    return False

def combat(switch):
    # CHECK_IF_END
    the_fight_has_ended = False
    while not the_fight_has_ended:
        

        rando = random.randint(1,4)
        if rando == 1:
            click(849,952)
            time.sleep(random.uniform(0.5,1.5))
        elif rando == 2:
            click(958,953)
            time.sleep(random.uniform(0.5,1.5))
        elif rando == 3:
            click(1069,952)
            time.sleep(random.uniform(0.5,1.5))
        elif rando == 4:
            click(1171,957)
            time.sleep(random.uniform(0.5,1.5))
        time.sleep(random.uniform(0.5,1.0))
        click(random.randint(750,1138),random.randint(516,753))
        print("random card placed")
        time.sleep(random.uniform(0.5,1.0))
        try:
            if pyautogui.locateOnScreen("cup.png", grayscale=True, confidence=0.8) != None:
                print("The fight has not ended")
                time.sleep(random.uniform(0.5,1.0))
                if not switch:
                    switch = maybe_switch()
                continue
        except ImageNotFoundException:
            print("The fight has ended")
            time.sleep(random.uniform(0.5,1.0))
            the_fight_has_ended = True
            if not switch:
                switch = maybe_switch()
        return switch
        break
    













amount_games = 1
sleeep = 0
switch = False
while True:
    time.sleep(random.randint(1,4))
    if not switch:
         switch = maybe_switch()
    if switch:
        do_switch()
        switch = False
    print(f"Amount of Games Played: {amount_games-1}")
    if amount_games % 27 == 0:
        sleeep += 1
        print("sleepy..")
        time.sleep(random.randint(600,1500))
        print(f"It has been many games. I now have slept a total of {sleeep} time(s) this session.")
        if not switch:
            switch = maybe_switch()
        if switch:
            do_switch()
            switch = False

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
                if not switch:
                    switch = maybe_switch()          
        except ImageNotFoundException:
            print("Battle button not found.")
            time.sleep(random.uniform(0.5,1))
            if not switch:
                switch = maybe_switch()
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

    started = False





    # PRE_LOADING
    loading = True
    while loading:
        # pyautogui.pixel(1169, 48)[2] == 173
        # X: 1169 Y:   48 RGB: (238, 221, 162)
        try:
            if pyautogui.locateOnScreen("cup.png", grayscale=True, confidence=0.8) != None:
                print("The fight has begun")
                time.sleep(random.uniform(0.5,1.0))
                if not switch:
                    switch = maybe_switch()
        except ImageNotFoundException:
            print("Loading...")
            time.sleep(random.uniform(0.5,1.0))
            try:
                if pyautogui.locateOnScreen("battle.png", grayscale=True, confidence=0.8) != None:
                    click(pyautogui.locateOnScreen("battle.png", grayscale=True, confidence=0.8)[0], pyautogui.locateOnScreen("battle.png", grayscale=True, confidence=0.8)[1])
                    print("Battle clicked:dif")
                    time.sleep(random.uniform(0.5,1))         
            except ImageNotFoundException:
                pass
            try:
                if pyautogui.locateOnScreen("end_ok.png", grayscale=True, confidence=0.8) != None:
                    print("Unexepected screen has appeared, loacted problem")
                    xpro = pyautogui.locateOnScreen("end_ok.png", grayscale=True, confidence=0.8)[0]
                    ypro = pyautogui.locateOnScreen("end_ok.png", grayscale=True, confidence=0.8)[1]
                    click(xpro, ypro)
                    print("passed problem")
                    time.sleep(random.uniform(0.5,1.0))
                    if not switch:
                        switch = maybe_switch()
                          
            except ImageNotFoundException:
                if not switch:
                    switch = maybe_switch()
                print("nothing unexpected happened")
                time.sleep(random.uniform(0.5,1.0))
            continue
        break
    
    



    combat(switch)
    if not switch:
        switch = combat(switch)




    the_fight_has_ended = True
    # EXIT
    while the_fight_has_ended:
        try:
            if not switch:
                switch = maybe_switch()
            # button- X:  956 Y:  940
            if pyautogui.locateOnScreen("end_ok.png", grayscale=True, confidence=0.8) != None:
                click(956, 940)
                print("OK to end game pressed")
                time.sleep(random.uniform(0.5,1.0))
                
        except ImageNotFoundException:
            print("ok end button not found.")
            time.sleep(random.uniform(0.5,1.0))
            try:
                if pyautogui.locateOnScreen("battle.png", grayscale=True, confidence=0.8) != None:
                    click(pyautogui.locateOnScreen("battle.png", grayscale=True, confidence=0.8)[0], pyautogui.locateOnScreen("battle.png", grayscale=True, confidence=0.8)[1])
                    print("Battle clicked:dif")
                    started = True
                    time.sleep(random.uniform(0.5,1))
                    break
            except ImageNotFoundException:
                pass
            continue # keep checking
        break  
    the_fight_has_ended = False
    amount_games += 1
  

