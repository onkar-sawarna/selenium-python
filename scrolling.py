import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.wait import WebDriverWait
serv=Service("./chromedriver")
driver=webdriver.Chrome(service=serv)


driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# maximize window
driver.maximize_window()

# scroll by pixcel
driver.execute_script("window.scrollBy(0,2000)", "")
time.sleep(4)

#scroll till the element is visible
#scroll down till page ends
















































































































































































































































































































































































































