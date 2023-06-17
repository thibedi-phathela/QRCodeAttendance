import pyqrcode
from PIL import Image

print("This program creates a qr code")

details = input("Enter First name, Last name and Unique ID, Format:e.g 'first-last-18452': ")
qr_code = pyqrcode.create(details)
qr_code.png(f"./StudentsQRCode/Student-{details}.png",scale=15)
Image.open(f"./StudentsQRCode/Student-{details}.png")
print("QR created...")

