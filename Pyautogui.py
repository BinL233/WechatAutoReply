import pyautogui
import time

'''

size = pyautogui.size()  #Get size of screen
print(size)

mouse_pos = pyautogui.position()  #Get position of mouse
print(mouse_pos)

print(pyautogui.onScreen(100,100))  #Whether the position in screen

pyautogui.moveTo(size.width / 2, size.height / 2, duration = 0.5)  #Move to center

pyautogui.moveTo(100,100,duration = 3)

pyautogui.moveRel(50, pyautogui.position().y, duration = 0.4)  #Relative move


last_pos = pyautogui.position()
try:
    while True:
        new_pos = pyautogui.position()
        if last_pos != new_pos:
            print(new_pos)
            last_pos = new_pos

except KeyboardInterrupt:
    print('\nExit')



'''
def work():
    print('成功执行，请稍等...')
    help_pos = pyautogui.locateCenterOnScreen('Wechat.png')  #Find the image
    while help_pos == None:
        help_pos = pyautogui.locateOnScreen("Wechat.png")


    print('识别成功!')

    pyautogui.moveTo(help_pos, duration= 0.1)  #Move the mouse
    pyautogui.click() #Click
    pyautogui.moveTo(1025,318, duration = 0.1)
    pyautogui.click()
    pyautogui.moveRel(258, 430, duration = 0.1)  #Relative move
    pyautogui.click()
    pyautogui.typewrite('wozaishuijiao')
    pyautogui.press('space')
    pyautogui.typewrite('~')    
    pyautogui.press('enter')
    pyautogui.moveRel(529,-503, duration = 0.1)
    pyautogui.click()


while True:
    work()
    time.sleep(0.1)
    print('Wait')


