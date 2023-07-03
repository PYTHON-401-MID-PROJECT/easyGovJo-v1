from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://eservices.ssc.gov.jo/external/login')

# ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT *****
user_name = 0
user_pass = ""
# ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT *****

user_name_input_field = driver.find_element(By.ID, "mat-input-0")
user_name_input_field.clear()
user_name_input_field.send_keys(user_name)

user_pass_input_field = driver.find_element(By.ID, "mat-input-1")
user_pass_input_field.clear()
user_pass_input_field.send_keys(user_pass)

sign_in_button = driver.find_element(By.CLASS_NAME, "btn-success")
sign_in_button.click()

time.sleep(3)

whom_it_concern_button = driver.find_element(By.ID, "mat-expansion-panel-header-8")
driver.execute_script("arguments[0].scrollIntoView(true);", whom_it_concern_button)
whom_it_concern_button.click()

time.sleep(4)

driver.switch_to.window(driver.window_handles[-1])

dropdown_menu = driver.find_element(By.XPATH, '//*[@id="scaleSelect"]')
dropdown_menu.click()

option = driver.find_element(By.XPATH, '//*[@id="pageFitOption"]')
option.click()

page_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[6]/div[2]/div/div[1]')
page_location = page_element.location
page_size = page_element.size
page_screenshot = page_element.screenshot_as_png
with open('page123123_screenshot.png', 'wb') as file:
    file.write(page_screenshot)