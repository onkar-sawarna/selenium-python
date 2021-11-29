from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
serv=Service("./chromedriver")
driver=webdriver.Chrome(service=serv)
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
print(driver.find_element(By.ID,"RESULT_RadioButton-7_1").is_selected())
#driver.find_element(By.ID,"RESULT_RadioButton-7_1").click()
#driver.find_element(By.ID,"RESULT_CheckBox-8_0").click()


# Using chrome driver
#driver = webdriver.Chrome()


# Web page url
#driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


# Selecting raido button
# Select male
driver.find_element(By.XPATH,
	'//*[@id="q26"]/table/tbody/tr[2]/td/label').click()


# Selecting check box
# Select sunday
driver.find_element(By.XPATH,
	'//*[@id="q15"]/table/tbody/tr[6]/td/label').click()
#//*[@id="q26"]/table/tbody/tr[2]/td/label

# Select monday
driver.find_element(By.XPATH,
	'//*[@id="q15"]/table/tbody/tr[2]/td/label').click()


