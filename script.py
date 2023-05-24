import pyautogui
# from selenium import webdriver
from selenium.webdriver.chrome.service import Service, By

service = Service(executable_path="/path/to/chromedriver")
driver = webdriver.Chrome(service=service)

# # This needs to be the current page
# # driver.get("https://katapultpro.com/map/#-NVj5c3UJChii6bl29uW/n-NSqv6LZOuKvI6KuOe3g")

# moveContainer is the class name
comm_bottom = driver.find_element(by=By.CLASS, value="moveContainer")

screen_width, screen_height = pyautogui.size()
pyautogui.moveTo(100, 200, duration=.25)
pyautogui.moveRel(0, -100, duration=.25)

moveToX = 1000
moveToY = 800
pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
pyautogui.scroll(500, x=moveToX, y=moveToY)


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
    # Collect all midspan heights 
    number_of_midspans = get_number_of_midspans()
    midspan_height = [] * number_of_midspans

def get_number_of_midspans():
    # Get each branch form the pole
    number_of_midspans = 1 #fill in value
    return number_of_midspans

def collect_midspan_type():
    # Collect midspan type
    midspan_type = 'backyard' 
    return midspan_type

def located_icon():
    # TODO [] GET PNG FILE OF KATAPULT HEIGHT ICON
    location = pyautogui.locateOnScreen('violation.png')
    if location == 'ImageNotFoundException':
        return 0
    else:
        return location
    # THIS WILL RETURN THE LOCATION OF PIXELS (LEFT, TOP, WIDTH, HEIGHT)

def move_icon_down():
    x, y = located_icon()
    pyautogui.click(x, y) 