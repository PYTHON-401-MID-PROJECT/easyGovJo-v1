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

lookup_button = driver.find_element(By.LINK_TEXT, "ضريبة الأبنية والمسقفات")
lookup_button.click()

id_ = 0 # ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT *****
id_num = "" # ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT *****

id_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtNationalNo")
id_input_field.clear()
id_input_field.send_keys(id_)

id_num_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ID_NO")
id_num_input_field.clear()
id_num_input_field.send_keys(id_num)

search_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSearch")
search_button.click()

header_row = driver.find_element(By.CSS_SELECTOR, "table#ctl00_ContentPlaceHolder1_get_real tr:first-child")
headers = [header.text for header in header_row.find_elements(By.TAG_NAME, "th")]

data_rows = driver.find_elements(By.CSS_SELECTOR, "table#ctl00_ContentPlaceHolder1_get_real tr:not(:first-child)")

table_data = []
for row in data_rows:
    row_data = [cell.text.strip() for cell in row.find_elements(By.TAG_NAME, "td")]
    row_dict = dict(zip(headers, row_data))
    table_data.append(row_dict)

for row in table_data:
    for header, value in row.items():
        reshaped_text = reshape(header)
        display_text = get_display(reshaped_text)
        header = display_text.strip()
        reshaped_text2 = reshape(value)
        display_text2 = get_display(reshaped_text2)
        value = display_text2.strip()
        print(f"{header}: {value}")

button_elements = driver.find_elements(By.XPATH, "//td[@class='sbrowntxt']//a[contains(text(), 'التفاصيل')]")
button_indexes = list(range(1, len(button_elements) + 1))

selected_number = 1 # ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT *****
selected_button_index = button_indexes[selected_number - 1]

button = button_elements[selected_button_index - 1]
button.click()

street_info_rows = driver.find_elements(By.ID, "ctl00_ContentPlaceHolder1_pnlContents")

for row in street_info_rows:
    reshaped_text = reshape(row.text)
    display_text = get_display(reshaped_text)
    print(display_text)