from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import requests
import base64

def image_to_base64(image_path):

    with open(image_path, "rb") as image_file:
        encoded_bytes = base64.b64encode(image_file.read())
        encoded_string = encoded_bytes.decode('utf-8')
        return encoded_string

def land_location(land_key):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://maps.dls.gov.jo/dlsweb/index.html")
    select_element = Select(driver.find_element(By.ID, "form-search-select"))
    select_element.select_by_value("search_dlskey")
    ard = driver.find_element(By.ID, "txt_dlskey_search")
    ard.send_keys(land_key)
    ard_key = driver.find_element(By.ID, "dlskey_search-button")
    ard_key.click()
    driver.implicitly_wait(30)
    sleep(10)
    driver.save_screenshot("./images/land_location.png")
    driver.quit()

    # "imgbb api" to generate public url for the image to make twilio able to deal with it
    url = "https://api.imgbb.com/1/upload"
    image_base64 = image_to_base64("../images/land_location.png")
    payload = {
        'key': "f79ac5a6e8f4a1e56b9ad2b245229f04",
        'image': image_base64
    }
    response = requests.post(url, payload)
    response_json = response.json()
    
    if response.status_code == 200 and 'data' in response_json:
        image_url = response_json['data']['url']
        return image_url
    else:
        return None

