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

midspans = [...midspans]
classified = [...midspans]

def check_midspan(inches, span_type):
    if span_type == 'backyard':
        if inches < 114:
            return True
    if span_type == 'roadway' or span_type == 'driveway':
        if inches < 186:
            return True
    if span_type == 'highway' or 'interstate':
        if inches < 216:
            return True

def get_midspans():
    # Collect all midspan heights come how
    number_of_midspans = get_number_of_midspans()
    midspan_height = [] * number_of_midspans
    for i in range(len(midspan_height)):
        # do we collect midspan type before or after the loop?
        for j in range(len(midspan_height[i])):
            if check_midspan(midspan_height):
                # ma

def get_number_of_midspans():
    # Get each branch form the pole
    number_of_midspans = 1 #fill in value
    return number_of_midspans

def collect_midspan_type():
    # Collect midspan type
    midspan_type = ....
    return midspan_type




 for i in range(len(midspans)):
        # [TODO] make changes to screen
        else:
            continue