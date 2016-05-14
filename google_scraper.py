import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException

 
def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 10)
    return driver
 
 
def lookup(driver, query):
    driver.get("http://www.google.com")
    try:
        form = driver.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        button = driver.wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
        form.send_keys(query)
        try:
            button.click()
        except ElementNotVisibleException:
            button = driver.wait.until(EC.visibility_of_element_located((By.NAME, "btnG")))
            button.click()
    except TimeoutException:
        print("Form or Button not found in google.com")
 
 
if __name__ == "__main__":
    driver = init_driver()
    lookup(driver, "David Morrison") #change oout david morrison to search for any combo in google
    time.sleep(5)
    