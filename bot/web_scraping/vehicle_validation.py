from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from arabic_reshaper import reshape
from selenium.webdriver.common.by import By


def vehicle_validation(license_plate, license_plate_id, registration_num):

    # Configure Firefox to run in headless mode
    # options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")
    # driver = webdriver.Firefox(options=options)

    driver = webdriver.Firefox()
    driver.get('https://www.amman.jo/ar/eservices/login.aspx')

    user_name = 9991015666
    user_pass = "Z=vNgg,;w5GNiRhd2f"

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

    license_plate = license_plate
    license_plate_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtLicenseNo")
    license_plate_input_field.clear()
    license_plate_input_field.send_keys(license_plate)

    license_plate_id = license_plate_id
    license_plate_id_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtNo")
    license_plate_id_input_field.clear()
    license_plate_id_input_field.send_keys(license_plate_id)

    registration_num = registration_num
    registration_num_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtregNo")
    registration_num_input_field.clear()
    registration_num_input_field.send_keys(registration_num)

    search_vehicle_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSearch")
    search_vehicle_button.click()

    violations_table_id = "ctl00_ContentPlaceHolder1_ytr"
    wait.until(EC.visibility_of_element_located((By.ID, violations_table_id)))

    violation_rows = driver.find_elements(By.CLASS_NAME, "browntxt")
    result = ""
    for row in violation_rows:
        reshaped_text = reshape(row.text)
        # display_text = get_display(reshaped_text)
        print(reshaped_text)
        result += f"\n{reshaped_text}"

    driver.quit()
    return result