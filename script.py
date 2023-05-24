import pyautogui
pyautogui.PAUSE=1
pyautogui.FAILSAFE=True

print(pyautogui.size())

width, height = pyautogui.size()
# pyautogui.moveTo(100, 200, duration=.25)


# pyautogui.moveRel(0, -100, duration=.25)


moveToX = 1000
moveToY = 800
pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')


pyautogui.scroll(500, x=moveToX, y=moveToY)
