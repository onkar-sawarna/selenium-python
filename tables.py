import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.wait import WebDriverWait
serv=Service("./chromedriver")
driver=webdriver.Chrome(service=serv)
driver.get(
    "https://www.geeksforgeeks.org/find_element_by_link_text-driver-method-selenium-python/")

# Make Python sleep for some time
time.sleep(2)

# Obtain the number of rows in body
rows = 1 + len(driver.find_elements(By.XPATH,
    "/html/body/div[3]/div[2]/div/div[1]/div/div/div/article/div[3]/div/table/tbody/tr"))

# Obtain the number of columns in table
cols = len(driver.find_elements(By.XPATH,
    "/html/body/div[3]/div[2]/div/div[1]/div/div/div/article/div[3]/div/table/tbody/tr[1]/td"))

# Print rows and columns
print(rows)
print(cols)

# Printing the table headers
print("Locators           " + "             Description")

# Printing the data of the table
for r in range(2, rows + 1):
    for p in range(1, cols + 1):
        # obtaining the text from each column of the table
        value = driver.find_element(By.XPATH,
            "/html/body/div[3]/div[2]/div/div[1]/div/div/div/article/div[3]/div/table/tbody/tr[" + str(
                r) + "]/td[" + str(p) + "]").text
        print(value, end='       ')
    print()