from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options

from time import sleep

# Configure Firefox options for running in headless mode
# firefox_options = Options()
# firefox_options.add_argument("--headless")

# Create a new instance of the Firefox driver with the headless option
# driver = webdriver.Firefox(options=firefox_options)
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://maps.dls.gov.jo/dlsweb/index.html")


select_element = Select(driver.find_element(By.ID,"form-search-select"))
select_element.select_by_value("search_dlskey")

ard=driver.find_element(By.ID,"txt_dlskey_search")
ard.send_keys("017200100000002")
ard_key= driver.find_element(By.ID,"dlskey_search-button")
ard_key.click()
driver.implicitly_wait(30)

sleep(10)
driver.save_screenshot("screenshot.png")

# driver.quit()