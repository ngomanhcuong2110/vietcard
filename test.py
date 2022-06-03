import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Remove horizontal and vertical lines
image = cv2.imread('test.png')
kernel_vertical = cv2.getStructuringElement(cv2.MORPH_RECT, (1,50))
temp1 = 255 - cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel_vertical)
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50,1))
temp2 = 255 - cv2.morphologyEx(image, cv2.MORPH_CLOSE, horizontal_kernel)
temp3 = cv2.add(temp1, temp2)
result = cv2.add(temp3, image)

data = pytesseract.image_to_string(result, lang='vie',config='--psm 6')
print(data)

cv2.imshow('result', result)
cv2.waitKey()