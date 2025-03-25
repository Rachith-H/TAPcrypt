from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import base64


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

import cv2
import numpy as np

def text_to_binary(text):
    """ Convert text to binary representation """
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary_str):
    """ Convert binary string to text """
    chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)
def extract_text(image_path):
    """ Extract hidden text from an image """
    img = cv2.imread(image_path)
    binary_message = ""

    for row in img:
        for pixel in row:
            for color in range(3):
                binary_message += str(pixel[color] & 1)

                if binary_message.endswith('1111111111111110'):
                    return binary_to_text(binary_message[:-16])

    return "No hidden message found"

def generate_aes_key(number_sequence, key_size=16):
    """ Convert a numeric sequence to a valid AES key (128, 192, or 256-bit) """
    number_string = ''.join(map(str, number_sequence))
    key = hashlib.sha256(number_string.encode()).digest()[:key_size]
    return key

def aes_decrypt(encrypted_base64, key):
    """ Decrypt a Base64 encoded AES encrypted message """
    encrypted_data = base64.b64decode(encrypted_base64)
    iv = encrypted_data[:16]  # Extract IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return decrypted_message.decode()

key = generate_aes_key(fdiff)
aes_enc = extract_text("C:\\Engineering\\1.Cognition\\stego.png")
msg = aes_decrypt(aes_enc,key)
print(msg)
