import pytesseract
from PIL import Image
import cv2
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

front_face_license = 'Image/photo1687858460(1).jpeg' # USER INPUt FRONT FACE OF LICENCE
rear_face_license = 'Image/photo1687858460.jpeg' # USER INPUT REAR FACE OF LICENSE

image = cv2.imread(front_face_license)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
preprocessed = cv2.GaussianBlur(gray, (5, 5), 0)
preprocessed = cv2.threshold(preprocessed, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
pil_image = Image.fromarray(preprocessed)
text = pytesseract.image_to_string(pil_image, lang='eng+ara', config='--psm 6')

number_pattern = r'\b(\d{2})-(\d+)\b'
number_match = re.search(number_pattern, text)
first_two_numbers = number_match.group(1) if number_match else None
remaining_numbers = number_match.group(2) if number_match else None

print("First Two Numbers:", first_two_numbers)
print("Remaining Numbers:", remaining_numbers)

rear_image = cv2.imread(rear_face_license)
rear_gray = cv2.cvtColor(rear_image, cv2.COLOR_BGR2GRAY)
rear_preprocessed = cv2.GaussianBlur(rear_gray, (5, 5), 0)
rear_preprocessed = cv2.threshold(rear_preprocessed, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
rear_pil_image = Image.fromarray(rear_preprocessed)
rear_text = pytesseract.image_to_string(rear_pil_image, lang='eng+ara', config='--psm 6')

registration_number_pattern = r'\b(133\d+)\b'
registration_number_match = re.search(registration_number_pattern, rear_text)
registration_number = registration_number_match.group(1) if registration_number_match else None

print("Registration Number:", registration_number)