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




def wcount():
    count = 0
    found = False
    print("check vitcor")
    while not found:
        try:     
            if pyautogui.locateOnScreen("mew.png", grayscale=False, confidence=0.99) != None:
                print("You won")
                return "Win"
                          
        except ImageNotFoundException:
            print(".")
        try:     
            if pyautogui.locateOnScreen("enemyw.png", grayscale=False, confidence=0.99) != None:
                print("You lost")
                return "Lose"
                          
        except ImageNotFoundException:
            print(".")
        count += 1
        time.sleep(1)
        if count % 7 == 0: # broken update the winner symbol
            try:
                if pyautogui.locateOnScreen("end_ok.png", grayscale=True, confidence=0.8) != None:
                    click(pyautogui.locateOnScreen("end_ok.png", grayscale=True, confidence=0.8)[0], pyautogui.locateOnScreen("end_ok.png", grayscale=True, confidence=0.8)[1])
                    print("victory not decided")
                    time.sleep(random.uniform(0.5,1))
                    return "sad"
                      
            except ImageNotFoundException:
                print("check ok")
                time.sleep(random.uniform(0.5,1))
      
            try:
                if pyautogui.locateOnScreen("battle.png", grayscale=True, confidence=0.8) != None:
                    click(pyautogui.locateOnScreen("battle.png", grayscale=True, confidence=0.8)[0], pyautogui.locateOnScreen("battle.png", grayscale=True, confidence=0.8)[1])
                    print("victory not decided")
                    time.sleep(random.uniform(0.5,1))
                    return "sad"
                      
            except ImageNotFoundException:
                print("check battle")
                time.sleep(random.uniform(0.5,1))
    
            

def combat():
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
            if pyautogui.locateOnScreen("eventcup.png", grayscale=True, confidence=0.8) != None:
                print("The fight has not ended")
                time.sleep(random.uniform(0.5,1.0))
              
                continue
        except ImageNotFoundException:
            print("The fight has ended")
            time.sleep(random.uniform(0.5,1.0))
            the_fight_has_ended = True
           
        
        break
    


loses=0
wins=0
amount_games = 1
sleeep = 0
while True:
    
    time.sleep(random.randint(1,4))
    print(f"""
    Amount of Games Played: {amount_games-1}
    Wins:{wins}
    Losses:{loses}
          """)
    if amount_games % 28 == 0:
        sleeep += 1
        print("sleepy..")
        time.sleep(random.randint(600,900))
        print(f"It has been many games. I now have slept a total of {sleeep} time(s) this session.")
        
        

    # BATTLE
    started = False
    while not started:

           
        try:
            if pyautogui.locateOnScreen("event1.png", grayscale=True, confidence=0.8) != None:
                click(pyautogui.locateOnScreen("event1.png", grayscale=True, confidence=0.8)[0], pyautogui.locateOnScreen("event1.png", grayscale=True, confidence=0.8)[1])
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
                    print("passed problem and clicked ok")
                    time.sleep(random.uniform(0.5,1.0))
                    
            except ImageNotFoundException:
                print("nothing unexpected happened")
                time.sleep(random.uniform(0.5,1.0))
            continue # keep checking

        break # break out of the started while loop and go to whats after



    while True:
        try:
            if pyautogui.locateOnScreen("eventbattle.png", grayscale=True, confidence=0.8) != None:
                click(pyautogui.locateOnScreen("eventbattle.png", grayscale=True, confidence=0.8)[0]+20, pyautogui.locateOnScreen("eventbattle.png", grayscale=True, confidence=0.8)[1]+30)
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
                    print("passed problem and clicked ok")
                    time.sleep(random.uniform(0.5,1.0))
                    
            except ImageNotFoundException:
                print("nothing unexpected happened")
                time.sleep(random.uniform(0.5,1.0))
            continue # keep checking

        break 
    



    # PRE_LOADING
    loading = True
    while loading:

        try:
            if pyautogui.locateOnScreen("eventcup.png", grayscale=True, confidence=0.8) != None:
                print("The fight has begun")
                time.sleep(random.uniform(0.5,1.0))
                
        except ImageNotFoundException:
            print("Loading...")
            time.sleep(random.uniform(0.5,1.0))
            try:
                if pyautogui.locateOnScreen("end_ok.png", grayscale=True, confidence=0.8) != None:
                    print("Unexepected screen has appeared, loacted problem")
                    xpro = pyautogui.locateOnScreen("end_ok.png", grayscale=True, confidence=0.8)[0]
                    ypro = pyautogui.locateOnScreen("end_ok.png", grayscale=True, confidence=0.8)[1]
                    click(xpro, ypro)
                    print("passed problem(ok button)")
                    time.sleep(random.uniform(0.5,1.0))
                   
            except ImageNotFoundException:
                print("nothing unexpected happened")
                time.sleep(random.uniform(0.5,1.0))
            try:
                if pyautogui.locateOnScreen("battle.png", grayscale=True, confidence=0.8) != None:
                    print("Unexepected screen has appeared, loacted problem")
                    xpro = pyautogui.locateOnScreen("battle.png", grayscale=True, confidence=0.8)[0]
                    ypro = pyautogui.locateOnScreen("battle.png", grayscale=True, confidence=0.8)[1]
                    click(xpro, ypro)
                    print("passed problem(battle button)")
                    time.sleep(random.uniform(0.5,1.0))
                    break
                    
            except ImageNotFoundException:
                pass


            
            continue
        break
    
    



    combat()
   



    result = wcount()
    the_fight_has_ended = True
    if result == "Win":
        wins += 1
    elif result == "Lose":
        loses += 1
    elif result == "sad":
        the_fight_has_ended = False
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
  



