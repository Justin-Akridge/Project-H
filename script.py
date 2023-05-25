from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options= chrome_options)

driver.get('https://katapultpro.com/map/#-NVj5c3UJChii6bl29uW')

print(driver)
#name of the png

clickable = driver.find_element(By.PARTIAL_LINK_TEXT, "https://maps.gstatic.com/mapfiles/transparent.png")
print(clickable)
ActionChains(driver)\
    .double_click(clickable)\
    .perform()

clickable = driver.find_element(By.CLASS, "moveContainer")
print(clickable)
ActionChains(driver)\
    .double_click(clickable)\
    .perform()