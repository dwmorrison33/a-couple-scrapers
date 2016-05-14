from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("selenium") #look up selenium in search box
elem.send_keys(Keys.RETURN) # return results from search
assert "No results found." not in driver.page_source
#driver.close()




