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

time.sleep(10)

lookup_button = driver.find_element(By.LINK_TEXT, "تفاصيل شارع")
lookup_button.click()

lookup_street_text = "برغوثي" # ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT *****
lookup_street_text_box = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtRoadsDescription")
lookup_street_text_box.clear()
lookup_street_text_box.send_keys(lookup_street_text)

search_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSearch")
search_button.click()

street_rows = driver.find_elements(By.CSS_SELECTOR, "td.sbrowntxt")

street_names = []
for row in street_rows:
    reshaped_text = reshape(row.text)
    display_text = get_display(reshaped_text)
    street_name = display_text.strip()
    street_names.append(street_name)

street_names = street_names[1:-3]

x = 0
for street_name in street_names:
    x = x + 1
    print(f'{x}- {street_name}')

button_elements = driver.find_elements(By.XPATH, "//td[@class='sbrowntxt']/following-sibling::td[@class='menu2']//a")
button_indexes = []
for i, button_element in enumerate(button_elements):
    button_index = i + 1
    button_indexes.append(button_index)

selected_number = 5 # ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT *****
selected_button_index = button_indexes[selected_number - 1]

button_xpath = f"(//td[@class='sbrowntxt']/following-sibling::td[@class='menu2']//a)[{selected_button_index}]"
button = driver.find_element(By.XPATH, button_xpath)
button.click()

street_info_rows = driver.find_elements(By.CSS_SELECTOR, "td.vbodytxt table tr")

for i, row in enumerate(street_info_rows):
    if i < 1:
        continue

    reshaped_text = reshape(row.text)
    display_text = get_display(reshaped_text)
    print(display_text)

driver.quit()