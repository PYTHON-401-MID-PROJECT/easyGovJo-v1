from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bidi.algorithm import get_display
from arabic_reshaper import reshape
import time

# Configure Firefox to run in headless mode
# options = webdriver.FirefoxOptions()
# options.add_argument("--headless")
# driver = webdriver.Firefox(options=options)

driver = webdriver.Firefox()
driver.get('https://www.amman.jo/ar/eservices/login.aspx')

user_name = 0
user_pass = ""

user_name_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtUserName")
user_name_input_field.clear()
user_name_input_field.send_keys(user_name)

user_pass_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtPassword")
user_pass_input_field.clear()
user_pass_input_field.send_keys(user_pass)

sign_in_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_cmdSubmit")
sign_in_button.click()

time.sleep(9)

lookup_button = driver.find_element(By.LINK_TEXT, "قيم مخالفات السير")
lookup_button.click()

lookup_villations_text = "وقوف" # ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT *****
lookup_villations_text_box = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtTicketDescription")
lookup_villations_text_box.clear()
lookup_villations_text_box.send_keys(lookup_villations_text)

search_vehicle_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSearch")
search_vehicle_button.click()

violations_table_id = "ctl00_ContentPlaceHolder1_ytr"

violation_rows = driver.find_elements(By.CLASS_NAME, "tableView")

for row in violation_rows:
    reshaped_text = reshape(row.text)
    display_text = get_display(reshaped_text)
    print(display_text)

driver.quit()