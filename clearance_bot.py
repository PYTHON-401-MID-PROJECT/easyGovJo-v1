from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bidi.algorithm import get_display
from arabic_reshaper import reshape
from selenium.common.exceptions import StaleElementReferenceException

url = 'https://www.amman.jo/ar/clearance/clearance.aspx'
driver = webdriver.Firefox()
driver.get(url)

wait = WebDriverWait(driver, 50)

# Get user input
user_nat_no = input("Enter User Nat No: ")
persone_card_no = input("Enter Registration No: ")

# print(type(user_phone_no))

radio_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='1']")))
radio_button.click()

radio_button2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='0101']")))
radio_button2.click()

user_nat_no_input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="ctl00$ContentPlaceHolder1$txt_persone_nat"]')))
user_nat_no_input_field.clear()
user_nat_no_input_field.send_keys(user_nat_no)

user_persone_card_no_input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="ctl00$ContentPlaceHolder1$txt_persone_card_no"]')))
user_persone_card_no_input_field.clear()
user_persone_card_no_input_field.send_keys(persone_card_no)

submit_button = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_btn_chk_order_by')
driver.execute_script("arguments[0].click();", submit_button)

time.sleep(5)

try :

    text_print = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="ctl00_ContentPlaceHolder1_lbl_chk_order_ok"]')))
    check_msg = text_print.text
    reshaped_msg = reshape(check_msg)
    displayed_msg = get_display(reshaped_msg)
    print(displayed_msg)

    radio_button3 = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='63']")))
    radio_button3.click()
    
    user_phone_no = input("Enter User Phone No: ")

    user_phone_no_input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="ctl00$ContentPlaceHolder1$txt_owner_phone"]')))
    user_phone_no_input_field.clear()
    user_phone_no_input_field.send_keys(user_phone_no)

    submit_button = wait.until(EC.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_btn_next_step')))

    # Click the element
    try:
        submit_button.click()
    except StaleElementReferenceException:
        submit_button = wait.until(EC.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_btn_next_step')))
        submit_button.click()

    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, '//td[@class="buildwhitesitefont"]')))
        if element:
            text_element = element.text
            reshaped_element = reshape(text_element)
            displayed_element = get_display(reshaped_element)
            print(displayed_element)

    except:
        element_except = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@id="ctl00_ContentPlaceHolder1_lblmsg"]')))
        text_except = element_except.text
        reshaped_except = reshape(text_except)
        displayed_except = get_display(reshaped_except)
        print(displayed_except)
except :
    error_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="ctl00_ContentPlaceHolder1_lblmsg"]')))
    error_msg = error_text.text
    reshaped_error = reshape(error_msg)
    displayed_error = get_display(reshaped_error)
    print(displayed_error)


driver.quit()
