from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
serv=Service("./chromedriver")
driver=webdriver.Chrome(service=serv)
driver.get("https://www.expedia.com/")
inputBoxes=driver.find_elements(By.CLASS_NAME,'uitk-faux-input')
print((len(inputBoxes)))
driver.close()