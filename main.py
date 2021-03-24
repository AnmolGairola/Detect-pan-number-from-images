import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' 

img1 = cv2.imread('one.jpg')
img2 = cv2.imread('two.jpg')
img3 = cv2.imread('three.jpg')

images = [img1, img2, img3]

pan = '[A-Z]{5}[0-9]{4}[A-Z]{1}'

for img in images:
    
    i = 0;
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    words = pytesseract.image_to_string(img)
    x = words.split()
    for word in x:
        if re.search(pan, word):
            print(word)
            i+=1


            
    if i == 0:
        for i in range(3):
            j = 0
            img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
            words = pytesseract.image_to_string(img)
            x = words.split()
            for word in x:
                if re.search(pan, word):
                    print(word)
                    j+=1
            if j == 1:
                break;
            
            
