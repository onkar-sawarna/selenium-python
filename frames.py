import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.wait import WebDriverWait
serv=Service("./chromedriver")
driver=webdriver.Chrome(service=serv)
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")

# switch to 1st frame
driver.switch_to.frame("packageListFrame")

# click on 1st frame
driver.find_element("org.openqa.selenium.cli").click()

# back to default web page frame
driver.switch_to.default_content()

# switch to 2nd frame
#driver.switch_to.frame("packageFrame")

# click on  2nd frame
#driver.find_element_by_link_text("OperaOptions").click()

# back to default web page frame
#driver.switch_to.default_content()

# switch to 3rd frame
driver.switch_to.frame("classFrame")

# click on  2nd frame
#driver.find_element(By.XPATH,'/html/body/div[1]/ul/li[4]/a').click()
#time.sleep(4)