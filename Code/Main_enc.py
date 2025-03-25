with open("tap_sequence.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]
diff = []
for val in range(len(numbers) - 1):
    if val < len(numbers):
        diff.append(numbers[val + 1] - numbers[val])
ndiff = [round(dif, -1) for dif in diff]
fdiff=[]
s = 239
m = 432
l= 543
for vol in ndiff:
    if (vol <=350):
        fdiff.append(s)
    elif (vol>350 and vol<=600):
        fdiff.append(m)
    else:
        fdiff.append(l)

# -------------------------------------------------------------------------------------------------------------------------

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import base64

def generate_aes_key(number_sequence, key_size=16):
    """ Convert a numeric sequence to a valid AES key (128, 192, or 256-bit) """
    number_string = ''.join(map(str, number_sequence))  # Convert numbers to string
    key = hashlib.sha256(number_string.encode()).digest()[:key_size]  # Hash and truncate
    return key

def aes_encrypt(message, key):
    """ Encrypt a message using AES-CBC and encode the output as Base64 """
    cipher = AES.new(key, AES.MODE_CBC)  # Generate a new AES cipher
    iv = cipher.iv  # Initialization Vector (IV)
    padded_message = pad(message.encode(), AES.block_size)  # Pad message
    encrypted_message = cipher.encrypt(padded_message)
    return base64.b64encode(iv + encrypted_message).decode()  # Convert to Base64 string

key = generate_aes_key(fdiff)
mnmsg = input("Enter your message : ")
encrypted_string = aes_encrypt(mnmsg, key)

# -------------------------------------------------------------------------------------------------------------------------

import cv2
import numpy as np

def text_to_binary(text):
    """ Convert text to binary representation """
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary_str):
    """ Convert binary string to text """
    chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def hide_text(image_path, secret_message, output_image):
    """ Hide text inside an image using LSB """
    img = cv2.imread(image_path)
    binary_message = text_to_binary(secret_message) + '1111111111111110'  # End marker

    idx = 0
    for row in img:
        for pixel in row:
            for color in range(3):  # Iterate over R, G, B channels
                if idx < len(binary_message):
                    pixel[color] = (pixel[color] & ~1) | int(binary_message[idx])
                    idx += 1
                else:
                    cv2.imwrite(output_image, img)
                    return

hide_text("C:\\Engineering\\1.Cognition\\Normal.png",encrypted_string,"C:\\Engineering\\1.Cognition\\stego.png")

