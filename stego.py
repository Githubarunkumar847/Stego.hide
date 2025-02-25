import cv2 # machine learning to read pip install opencv-python
import os
import string # add,hide in side specific image

img = cv2.imread("mypic.jpg") # Replace with the correct image path

msg = input("Please enter the confedential message:")
password = input("Please enter a strong passcode, Try mix of letters, numbers & symbols:")

d = {} # stores ascii value
c = {} # stores data

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows
print("Please remember your passcode and make sure you enter the same when you try decrypt.")

message = ""
n = 0
m = 0
z = 0

pas = input("Welcome!, Enter passcode for Decryption:")
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")
