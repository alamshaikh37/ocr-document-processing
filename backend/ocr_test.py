import pytesseract
import cv2
import os

# set tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Alam shaikh\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# give correct file path
image_path = "../dataset/invoices/invoice1.png"

# check file exists
if not os.path.exists(image_path):

    print("❌ File not found:", image_path)
    print("👉 Put image inside dataset/invoices folder")

    exit()

# read image
image = cv2.imread(image_path)

# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# improve OCR accuracy
gray = cv2.resize(gray, None, fx=2, fy=2)

# threshold
gray = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

# extract text
text = pytesseract.image_to_string(gray)

print("\n=========== OCR OUTPUT ===========\n")

print(text)

print("\n==================================")

