from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
from bidi.algorithm import get_display
from arabic_reshaper import reshape

# Configure Firefox to run in headless mode

url='https://eservices.cspd.gov.jo/index-rtl.html'
driver = webdriver.Firefox()
driver.get(url)

wait = WebDriverWait(driver,50)


user_name = 9912017766
user_pass = "luluRe*91"
 
user_name_input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"]')))
user_name_input_field.clear()
user_name_input_field.send_keys(user_name)

user_pass_input_field =wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))  # Replace with the actual name attribute of the password field
user_pass_input_field.clear()
user_pass_input_field.send_keys(user_pass)

login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]')))
login_button.click()

button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-filter=".Passports"]')))
time.sleep(5)
button.click()

element_id="ServicesMenu_widget_ServicesMenu_0"
element = wait.until(EC.visibility_of_element_located((By.ID, element_id)))
child_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h4")))

target_text='خدمة تجديد جواز السفر الدائم'
for i in child_elements :
        if (i.text == target_text):
           print('i is',i)
           print(i.text)
           parent_element = i.find_element(By.XPATH, '..')
           parent_html = parent_element.get_attribute('outerHTML')
           print(parent_html)
           parent_element.click()
           
        continue

# wait.until(EC.staleness_of((By.CLASS_NAME, "mx-underlay")))

next_button= wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn.mx-button.mx-name-actionButton9.fa.Next.mobilebtn.btn-default")))
time.sleep(5)
next_button.click()

dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "mxui_widget_ReferenceSelector_0_input"))
)

select = Select(dropdown)

provided_text = "تميم ابراهيم"

for option in select.options:
    if provided_text in option.text:
        option.click()
        break


time.sleep(2)
element3 = driver.find_element(By.CSS_SELECTOR, "[data-button-id='687.Passport.Step1PassportRenewal.actionButton9']")
time.sleep(2)
element3.click()
time.sleep(5)

place_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "mxui_widget_ReferenceSelector_3_input"))
)

select_place = Select(place_dropdown)

provided_text = "الاردن"

for option in select_place.options:
    if provided_text in option.text:
        option.click()
        break
time.sleep(5)

recived_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "mxui_widget_ReferenceSelector_4_input"))
)

select_recieved = Select(recived_dropdown)

provided_text = "الاردن"

for option in select_recieved.options:
    if provided_text in option.text:
        option.click()
        break

time.sleep(5)

review_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "mxui_widget_ReferenceSelector_5_input"))
)

select_review = Select(review_dropdown)
time.sleep(5)
provided_text = "عمان الغربيه"

for option in select_review.options:
    if provided_text in option.text:
        option.click()
        break
# driver.maximize_window()

radio_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='No']")))

print (radio_button)
radio_button.click()
time.sleep(5)

next_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn mx-button mx-name-actionButton9 fa Next mobilebtn btn-default' and text()='التالي']")))
next_button.click()

time.sleep(5)
reason_dropdown =  WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.ID, "694.Passport.Step3PassportRenewal.dropDown3.235_lit_419"))
)
time.sleep(5)

select_reason = Select(reason_dropdown)
provided_text = "تجديد منتهي الصلاحية "

time.sleep(5)

for option in select_reason.options:
    if provided_text in option.text:
        option.click()
        break

time.sleep(5)

upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn mx-button mx-name-actionButton14 viewbtn2 btn-default' and text()='تحميل']")))
next_button.click()

time.sleep(5)

search_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn mx-button mx-fileinput-upload-button' and text()='تصفح']")))
next_button.click()

time.sleep(5)

user_pic = 'c:\\Users\\User\\Documents\\images\\pic.jpg'

user_pic_input_field =wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))  # Replace with the actual name attribute of the password field
user_pic_input_field.clear()
user_pic_input_field.send_keys(user_pic)

time.sleep(5)

save_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn mx-button mx-name-actionButton1 btn-success' and text()='حفظ']")))
next_button.click()

time.sleep(5)

# driver.find_element_by_xpath("//input[@id='691.Passport.Step2PassportRenewal.radioButtons1.580_ngn_243_1']").click()
                       



# driver.quit()




