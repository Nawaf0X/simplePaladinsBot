import keyboard
import pyautogui
import time
import win32api, win32con, win32gui
import random
#------------------------
def screen():
    if pyautogui.locateOnScreen('play.png',confidence=0.8) or pyautogui.locateOnScreen('play2.png',confidence=0.8) != None:
        print("lobby")
        screeninfo = "lobby"
    elif pyautogui.locateOnScreen('quick play.png',confidence=0.8) and pyautogui.locateOnScreen('quick play2.png',confidence=0.8) != None:
        print("quick play")
        screeninfo = "quick play"
    elif pyautogui.locateOnScreen('tdm.png',confidence=0.8) != None:
        print("training")
        screeninfo = "training"
    elif pyautogui.locateOnScreen('Search.png',confidence=0.8) != None:
        print("Search")
        screeninfo = "Search"
    elif pyautogui.locateOnScreen('championselection.png',confidence=0.8) != None:
        print("champion selection")
        screeninfo = "champion selection"
    elif pyautogui.locateOnScreen('requeue.png',confidence=0.8) != None:
        print("requeue")
        screeninfo = "requeue"
    elif pyautogui.locateOnScreen('choose your talent.png',confidence=0.8) != None:
        print("choose your talent")
        screeninfo = "choose your talent"
    elif pyautogui.locateOnScreen('choose your loadout.png',confidence=0.8) != None:
        print("choose your loadout")
        screeninfo = "choose your loadout"
    elif pyautogui.locateOnScreen('confirm your loadout.png',confidence=0.8) != None:
        print("confirm your loadout")
        screeninfo = "confirm your loadout"
    elif pyautogui.locateOnScreen('game4.png',confidence=0.8) or pyautogui.locateOnScreen('game3.png',confidence=0.8)  != None:
        screeninfo = "in match"
    elif pyautogui.locateOnScreen('eventpass.png',confidence=0.8) != None:
        screeninfo = "eventpass"
    elif pyautogui.locateOnScreen('reconnect.png',confidence=0.8) != None:
        screeninfo = "reconnect"

        
        
 
    else:
        screeninfo = None
    return screeninfo

#-------------------------------
def mouse_move(x_end,y_end):
    x,y= 1265,705
    x_end = x_end + 22
    y_end = y_end + 68
    while True:
        
         
        if x > x_end:
            x = x -1
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,-1,0,0,0)
        if y > y_end:
            y = y - 1
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,0,-1,0,0)
        if x < x_end:
            x = x + 1
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,1,0,0,0)
        if y < y_end:
            y = y + 1
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,0,1,0,0)
        if (x_end == x) and (y_end == y):
            break
        print(pyautogui.position())
        time.sleep(0.0000000005)
    
        
    
#---------------------------------------
def PlayMatch():
    while True:
        
        pyautogui.keyDown('w')
        time.sleep(4)
        pyautogui.keyUp('w')
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        mouse_move(random.randrange(-1500, 1500),705)
        
        
        if pyautogui.locateOnScreen('enemy.png',confidence=0.8) != None:
            try:
                enemy = pyautogui.locateOnScreen('enemy.png',confidence=0.8)
                x_enemy = enemy[0]
                y_enemy = enemy[1]
                mouse_move(x_enemy,y_enemy)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                time.sleep(1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                pyautogui.press('q')
                time.sleep(1)
                pyautogui.press('e')
                time.sleep(1)
                pyautogui.press('shift')
                time.sleep(1)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                time.sleep(1)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

            except:
                continue
        
         

        elif pyautogui.locateOnScreen('enemy2.png',confidence=0.8) != None:
            try:
                enemy = pyautogui.locateOnScreen('enemy2.png',confidence=0.8)
                x_enemy = enemy[0]
                y_enemy = enemy[1]
                mouse_move(x_enemy,y_enemy)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                time.sleep(0.5)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                pyautogui.press('q')
                time.sleep(1)
                pyautogui.press('e')
                time.sleep(1)
                pyautogui.press('shift')
                time.sleep(1)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                time.sleep(1)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

            except:
                continue

        elif pyautogui.locateOnScreen('enemy4.png',confidence=0.8) != None:
            try:
                enemy = pyautogui.locateOnScreen('enemy4.png',confidence=0.8)
                x_enemy = enemy[0]
                y_enemy = enemy[1]
                mouse_move(x_enemy,y_enemy)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                time.sleep(0.5)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                pyautogui.press('q')
                time.sleep(1)
                pyautogui.press('e')
                time.sleep(1)
                pyautogui.press('shift')
                time.sleep(1)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                time.sleep(1)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

            except:
                continue
        elif pyautogui.locateOnScreen('enemy5.png',confidence=0.8) != None:
            try:
                enemy = pyautogui.locateOnScreen('enemy5.png',confidence=0.8)
                x_enemy = enemy[0]
                y_enemy = enemy[1]
                mouse_move(x_enemy,y_enemy)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                time.sleep(0.5)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                pyautogui.press('q')
                time.sleep(1)
                pyautogui.press('e')
                time.sleep(1)
                pyautogui.press('shift')
                time.sleep(1)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                time.sleep(1)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

            except:
                continue
        
        elif pyautogui.locateOnScreen('allie1.png',confidence=0.8) != None:
            try:
                allie = pyautogui.locateOnScreen('allie1.png',confidence=0.8)
                x_allie = allie[0]
                y_allie = allie[1]
                mouse_move(x_allie,y_allie)
                pyautogui.keyDown('w')
                time.sleep(4)
                pyautogui.keyUp('w')
            

            except:
                continue
        
        elif pyautogui.locateOnScreen('allie2.png',confidence=0.8) != None:
            try:
                allie = pyautogui.locateOnScreen('allie2.png',confidence=0.8)
                x_allie = allie[0]
                y_allie = allie[1]
                mouse_move(x_allie,y_allie)
                pyautogui.keyDown('w')
                time.sleep(4)
                pyautogui.keyUp('w')
            

            except:
                continue
        elif pyautogui.locateOnScreen('allie3.png',confidence=0.8) != None:
            try:
                allie = pyautogui.locateOnScreen('allie3.png',confidence=0.8)
                x_allie = allie[0]
                y_allie = allie[1]
                mouse_move(x_allie,y_allie)
                pyautogui.keyDown('w')
                time.sleep(4)
                pyautogui.keyUp('w')
            

            except:
                continue
        elif pyautogui.locateOnScreen('allie4.png',confidence=0.8) != None:
            try:
                allie = pyautogui.locateOnScreen('allie4.png',confidence=0.8)
                x_allie = allie[0]
                y_allie = allie[1]
                mouse_move(x_allie,y_allie)
                pyautogui.keyDown('w')
                time.sleep(4)
                pyautogui.keyUp('w')
            

            except:
                continue
        
        elif pyautogui.locateOnScreen('allie5.png',confidence=0.8) != None:
            try:
                allie = pyautogui.locateOnScreen('allie5.png',confidence=0.8)
                x_allie = allie[0]
                y_allie = allie[1]
                mouse_move(x_allie,y_allie)
                pyautogui.keyDown('w')
                time.sleep(4)
                pyautogui.keyUp('w')
            

            except:
                continue
        
        elif pyautogui.locateOnScreen('allie6.png',confidence=0.8) != None:
            try:
                allie = pyautogui.locateOnScreen('allie6.png',confidence=0.8)
                x_allie = allie[0]
                y_allie = allie[1]
                mouse_move(x_allie,y_allie)
                pyautogui.keyDown('w')
                time.sleep(4)
                pyautogui.keyUp('w')
            

            except:
                continue
            
        elif pyautogui.locateOnScreen('game4.png',confidence=0.8) != None:
            time.sleep(5)

        elif pyautogui.locateOnScreen('wingame.png',confidence=0.8) or pyautogui.locateOnScreen('losegame.png',confidence=0.8):
            break

        elif pyautogui.locateOnScreen('requeue.png',confidence=0.8) != None:
            break
        
        elif pyautogui.locateOnScreen('eventpass.png',confidence=0.8) != None:
            break
    
        
        else:
            print("i cant see help me plz")
            screeninfo = None
            if pyautogui.locateOnScreen('game4.png',confidence=0.8) or pyautogui.locateOnScreen('game4.png',confidence=0.8)  == None:
                break
                pyautogui.press('esc')
            
        time.sleep(0.5)

#-----------------------------
def champion():
    champ = ['Viktor','Khan','Furia','Ash','Lex' ]
    for i in range(0,5):
        try:
            ch = pyautogui.locateOnScreen('{}.png'.format(champ[i]),confidence=0.8)
            x_ch,y_ch = ch[0]+10,ch[1]+10
            pyautogui.moveTo(x_ch,y_ch, duration=0.19)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo('lockin.png', duration=0.19)
            pyautogui.click()
            break
        except:
            continue
                


#------------------------------

while True:
    try:
        print(time.ctime())
        screeninfo = screen()
        if screeninfo == "lobby":
            if pyautogui.locateOnScreen('play.png',confidence=0.8) != None:
                play = pyautogui.locateOnScreen('play.png',confidence=0.8)
                x,y = play[0],play[1]
                x = x +15
                y = y +15
                print("1")
                pyautogui.moveTo(x,y , duration=0.19)
            elif pyautogui.locateOnScreen('play2.png',confidence=0.8) != None:
                play = pyautogui.locateOnScreen('play2.png',confidence=0.8)
                x,y = play[0],play[1]
                x = x +15
                y = y +15
                print("2")
                pyautogui.moveTo(x,y , duration=0.19)
                
                
            pyautogui.click()
            time.sleep(0.5)
            if pyautogui.locateOnScreen('MatchError.png',confidence=0.8) != None:
                pyautogui.moveTo('MatchError.png', duration=0.30)
                pyautogui.click()
                pyautogui.move(20,90 , duration=0.30)
                pyautogui.click()
                
        
        elif screeninfo == "quick play":
            pyautogui.moveTo('quick play.png', duration=0.19)
            pyautogui.click()
            time.sleep(0.5)
        
        elif screeninfo == "training" :
            pyautogui.moveTo('tdm.png', duration=0.19)
            pyautogui.click()
            time.sleep(0.5)
        
        elif screeninfo == 'Search' :
            time.sleep(10)
        
        elif screeninfo == "champion selection":
            champion()
            time.sleep(20)
        
        elif screeninfo == "requeue":
            pyautogui.moveTo('requeue.png', duration=0.60)
            pyautogui.move(-527,-28 , duration=0.19)
            pyautogui.click()
            hwnd = win32gui.FindWindow(None, 'Paladins (64-bit, DX11)')
            rect = win32gui.GetWindowRect(hwnd)
            region = rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1]
            pyautogui.screenshot('g.png',region=region)

            pyautogui.moveTo('requeue.png', duration=0.60)
            pyautogui.click()
            pyautogui.move(-120,0 , duration=0.19)
            pyautogui.click()
            if pyautogui.locateOnScreen('unlocked.png',confidence=0.8) != None:
                pyautogui.press('esc')
            time.sleep(2)
            if pyautogui.locateOnScreen('requeue.png',confidence=0.8) != None:
                pyautogui.press('esc')
                
            if pyautogui.locateOnScreen('PaladinsRequeue.png',confidence=0.8) != None:
                pyautogui.moveTo('PaladinsRequeue.png', duration=0.30)
                pyautogui.click()
                
        
        elif screeninfo == "choose your talent" :
            CYT = pyautogui.locateOnScreen('choose your talent.png',confidence=0.8)
            CYT_x = CYT[0]
            CYT_y = CYT[1]
            pyautogui.moveTo(int(CYT_x),int(CYT_y) , duration=1.19)
            pyautogui.move(-250,250 , duration=1.19)
            pyautogui.click()
        
        elif screeninfo == "choose your loadout":
            pyautogui.move(250,-120 )
            pyautogui.click()
        
        elif screeninfo == "confirm your loadout":
            print("confirm your loadout")
            pyautogui.move(180,330 )
            pyautogui.click()
        
        elif screeninfo == "in match":
            print("in match")
            PlayMatch()
            
        elif screeninfo == "eventpass":
            print("eventpass")
            pyautogui.press('esc')

        elif screeninfo == "reconnect":
            print("reconnect")
            pyautogui.moveTo('reconnect.png', duration=0.30)
            pyautogui.click()
            


            

            
        else:
            print('erorr')
    except:
        print("erorr main")
        print(time.ctime())
        continue
    
        
        
        
        
        
        
        
        
    
