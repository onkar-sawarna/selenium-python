from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.wait import WebDriverWait
serv=Service("./chromedriver")
driver=webdriver.Chrome(service=serv)
driver.get("https://ide.geeksforgeeks.org/tryit.php/WXYeMD9tD4")
# create alert object
alert = Alert(driver)

# get alert text
print(alert.text)
alert.accept()


