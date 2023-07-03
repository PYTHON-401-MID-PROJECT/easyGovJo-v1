from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from bidi.algorithm import get_display
# from arabic_reshaper import reshape

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

element_id = "table1"
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, element_id)))

driver.get('https://www.amman.jo/ar/eservices/TicketQueryCS.aspx')

license_plate = 0 # ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT *****
license_plate_id = 0 # ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT *****
registration_num = 0 # ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT *****

license_plate_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtLicenseNo")
license_plate_input_field.clear()
license_plate_input_field.send_keys(license_plate)

# def handle_user_input1(gg):
#     if not gg.isdigit():
#         print ("Input should only be numbers")
#     elif len(gg) != 2:
#         print ("Input should be two numbers")
#     else:
#         license_plate_input_field.send_keys(gg)

# handle_user_input1(license_plate_id)

license_plate_id_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtNo")
license_plate_id_input_field.clear()
license_plate_id_input_field.send_keys(license_plate_id)

# def handle_user_input2(ffd):
#     if not ffd.isdigit():
#         print ("Input should only be numbers")
#     elif len(ffd) > 5 or license_plate_id == '0':
#         print ("Input can have up to 5 numbers only")
#     else:
#         license_plate_id_input_field.send_keys(ffd)

# handle_user_input2(license_plate)

registration_num_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtregNo")
registration_num_input_field.clear()
registration_num_input_field.send_keys(registration_num)

# def handle_user_input3(ssa):
#     if not ssa.isdigit():
#         print ("Input should only be numbers")
#     elif len(ssa) != 10:
#         print ("Input should have 10 numbers only")
#     else:
#         registration_num_input_field.send_keys(ssa)

# handle_user_input3(registration_num)

search_vehicle_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSearch")
search_vehicle_button.click()

# violations_table_id = "ctl00_ContentPlaceHolder1_ytr"
# wait.until(EC.visibility_of_element_located((By.ID, violations_table_id)))

# violation_rows = driver.find_elements(By.CLASS_NAME, "browntxt")

# for row in violation_rows:
#     reshaped_text = reshape(row.text)
#     display_text = get_display(reshaped_text)
#     print(display_text)

page_element = driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_ytr > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(9) > td:nth-child(1) > table:nth-child(1)')
page_location = page_element.location
page_size = page_element.size
page_screenshot = page_element.screenshot_as_png
with open('vehcile_violations_screenshot.png', 'wb') as file:
    file.write(page_screenshot)

driver.quit()