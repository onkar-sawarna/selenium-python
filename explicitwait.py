from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

serv=Service("./chromedriver")
driver=webdriver.Chrome(service=serv)
import time
from selenium.webdriver.support import expected_conditions as EC
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.expedia.com/")
driver.find_element(By.XPATH,"//*[@id='wizardMainRegionV2']/div/div/div[2]/div/div/ul/li[2]/a/span").click()
#driver.find_element(By.XPATH,"//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[1]/div/div[1]/div/div/div/button").send_keys("SFO")
#time.sleep(2)
#driver.find_element(By.ID,"location-field-leg1-destination-dialog-trigger").send_keys("NYC")
#explicit wait
wait=WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable())

#driver.close()


