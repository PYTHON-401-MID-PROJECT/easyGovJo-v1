
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bidi.algorithm import get_display
from arabic_reshaper import reshape



def run_bot(user_nat_no, persone_card_no):
    url = 'http://enq-sys.csb.gov.jo/'
    driver = webdriver.Firefox()
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    user_nat_no_input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="ctl00$ContentPlaceHolder1$txt_natno"]')))
    user_nat_no_input_field.clear()
    user_nat_no_input_field.send_keys(user_nat_no)

    user_persone_card_no_input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="ctl00$ContentPlaceHolder1$txt_name"]')))
    user_persone_card_no_input_field.clear()
    user_persone_card_no_input_field.send_keys(persone_card_no)

    login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]')))
    login_button.click()
    time.sleep(5)
    try :

        
        info_element = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_EmploymentData1_GridCOMP_DXMainTable"]')
        info_screenshot = info_element.screenshot_as_png
        with open('info_screenshot.png', 'wb') as file:
            file.write(info_screenshot)
            
        # compititive_ranking = wait.until(EC.presence_of_element_located((By.ID, 'ContentPlaceHolder1_EmploymentData1_GridCOMP_DXMainTable')))
        # rows = compititive_ranking.find_elements(By.TAG_NAME, 'tr')

        # header_printed = False

        # for i, row in enumerate(rows):
        #     if i == 0:
        #         continue  # Skip the header row
          
        #     columns = row.find_elements(By.TAG_NAME, 'td')
        #     for column in columns:
        #         if column.text == 'المؤهل العلمي':
        #             if not header_printed:
        #                 res3 = wait.until(EC.presence_of_element_located((By.ID, 'ContentPlaceHolder1_EmploymentData1_GridCOMP_DXHeadersRow0')))
        #                 res3_text = res3.text
        #                 reshaped_text3 = reshape(res3_text)
        #                 display_text3 = get_display(reshaped_text3)
        #                 print(display_text3)
        #                 header_printed = True
 
        #             res = wait.until(EC.presence_of_element_located((By.ID, 'ContentPlaceHolder1_EmploymentData1_GridCOMP_DXDataRow0')))
        #             res_text = res.text
        #             reshaped_text = reshape(res_text)
        #             display_text = get_display(reshaped_text)
        #             lst_text = display_text.split(" ")
        #             if len(lst_text) % 2 != 0:
        #                 print("{:<30}{:<10}".format("", lst_text[-1]))
        #             for j in reversed(range(0, len(lst_text) - 1, 2)):
        #                 print("{:<30}{:<10}{}".format("", lst_text[j], lst_text[j + 1]))
        #             break  # Exit the loop after processing the first row
    except :
        
        error_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_Error_Messg"]')))
        error_text = error_element.text
        reshaped_error_text = reshape(error_text)
        display_error_text = get_display(reshaped_error_text)
        print(display_error_text)

    driver.quit()

# Get user inputs
user_nat_no = input("Enter User Nat No: ")
persone_card_no = input("Enter Persone Card No: ")

# Run the bot
run_bot(user_nat_no, persone_card_no)

