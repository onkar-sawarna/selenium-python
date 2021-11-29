import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.wait import WebDriverWait
serv=Service("./chromedriver")
driver=webdriver.Chrome(service=serv)
driver.get("http://demo.automationtesting.in/Windows.html")

# find xpath of button for child window page
# this page no. 2
driver.find_element(By.XPATH,'//*[@id="Tabbed"]/a/button').click()
print(driver.current_window_handle)
# return all handles value of open browser window
handles = driver.window_handles
for i in handles:
    driver.switch_to.window(i)

    # print every open window page title
    print(driver.title)
    print(driver.current_window_handle)
driver.quit()
