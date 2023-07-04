from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC


# Create a new instance of the Chrome web driver
driver = webdriver.Chrome()

# Open the website
website_url = 'https://www.modee.gov.jo/AR/Forms/%D8%AD%D8%A7%D9%81%D8%B2_%D9%81%D8%B1%D8%B5_%D8%A7%D9%84%D8%B9%D9%85%D9%84_%D8%A7%D9%84%D9%85%D8%A4%D9%82%D8%AA%D8%A9_%D9%81%D9%8A_%D8%A7%D9%84%D9%82%D8%B7%D8%A7%D8%B9_%D8%A7%D9%84%D8%B1%D9%82%D9%85%D9%8A_%D9%88%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%AF%D9%8A____%D8%B7%D9%84%D8%A8_%D8%AA%D9%82%D8%AF%D9%8A%D9%85_%D8%A7%D9%84%D8%A3%D9%81%D8%B1%D8%A7%D8%AF'
driver.get(website_url)
time.sleep(5)
# Find the username input element and enter your username

ID_number=input("Please enter your ID_number:")

ID_input = driver.find_element(by=By.ID, value='MainContent_ContentDetails_Textbox_2602')

ID_input.send_keys(ID_number)

# Find the password input element and enter your password

name=input("Please enter your full name :")

name_input = driver.find_element(by=By.ID, value='MainContent_ContentDetails_Textbox_2603')
name_input.send_keys(name)



phone=input("Please enter your phone number :")
phone_input = driver.find_element(by=By.ID, value='MainContent_ContentDetails_Textbox_2604')
phone_input.send_keys(phone)

Email=input("Please enter your E-mail")
Email_input = driver.find_element(by=By.ID, value='MainContent_ContentDetails_EmailEmail_2605')
Email_input.send_keys(Email)






loc=input("Please inter your location : ")
loc_input = driver.find_element(by=By.ID, value='MainContent_ContentDetails_Textbox_2606')
loc_input.send_keys(loc)




addres=input("Please inter your addres: ")

fulladdres_input = driver.find_element(by=By.ID, value='MainContent_ContentDetails_Textbox_2607')
fulladdres_input.send_keys(addres)




university_name=input("Please inter your university name : ")

university_name_input = driver.find_element(by=By.ID, value='MainContent_ContentDetails_Textbox_2608')
university_name_input.send_keys(university_name)




major=input("Please inter your major : ")

major_input = driver.find_element(by=By.ID, value='MainContent_ContentDetails_Textbox_2609')
major_input.send_keys(major)



Graduation_Year=input("Please inter your Graduation Year : ")

Graduation_Year_input = driver.find_element(by=By.ID, value='MainContent_ContentDetails_txtNumber_2610')
Graduation_Year_input.send_keys(Graduation_Year)



driver.find_element(by=By.NAME,value="ctl00$ctl00$MainContent$ContentDetails$afuOtherDocuments_2612$ctl04").send_keys("C:/Users/user/Desktop/cv.pdf")
time.sleep(60)
driver.find_element(by=By.ID, value="MainContent_ContentDetails_afuOtherDocuments_2612_UploadOrCancelButton").click()
time.sleep(60)


body=driver.find_element(by=By.ID,value="c_pages_viewforms_maincontent_contentdetails_captcha_CaptchaImage")
body.screenshot('blog.png')

BDC = input("Please enter the value for BDC: ")

# Find the BDC input element and enter the user-provided value
BDC_input = driver.find_element(by=By.NAME, value='ctl00$ctl00$MainContent$ContentDetails$txtCaptcha')
BDC_input.send_keys(BDC)




