from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
chrome_options = Options()

chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options= chrome_options)


driver.get('https://katapultpro.com/map/#-NVj5c3UJChii6bl29uW')
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20)
clickable = driver.find_element(By.TAG_NAME, "input")
print(clickable)
ActionChains(driver)\
    .double_click(clickable)\
    .perform()
print("it worked")

# clickable = driver.find_element(By.CLASS, "moveContainer")
# print(clickable)
# ActionChains(driver)\
#     .double_click(clickable)\
#     .perform()

# import pyautogui
# pyautogui.PAUSE = 30

# button = pyautogui.locateOnScreen('https://maps.gstatic.com/mapfiles/transparent.png')
# print(button)