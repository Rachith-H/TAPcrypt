# TAPcrypt : Tap-Sequence Based Encryption with Image Steganography 
This project introduces a novel approach to secure communication by integrating tap-pattern 
based encryption with image steganography, providing an innovative and unbreakable layer 
of security for confidential messages. The proposed system leverages an Arduino 
microcontroller interfaced with a tap sensor and a push button to generate a unique 
encryption key based on a user-defined tap sequence. This dynamic key, created through 
physical taps, acts as a one-time passphrase to encrypt the message, adding an additional 
layer of security.   

The encryption process is performed using the Advanced Encryption Standard (AES) algorithm 
in Python where the tap sequence acts as the key. The encrypted message is then embedded 
within an image file using the Least Significant Bit (LSB) steganography method, ensuring that 
the hidden message remains undetectable to unauthorized recipients. The image appears 
visually unchanged, concealing the encrypted content from third parties.   

To retrieve the hidden message, the receiver uses the Arduino setup, re-entering the same 
tap sequence to regenerate the key. This key is sent to the Python interface, which decrypts 
the hidden message only if the exact tap sequence is matched. Any incorrect sequence results 
in either decryption failure or misleading output, preventing unauthorized access.    

This project offers a real-world demonstration of secure communication, where both 
cryptographic strength and physical security measures converge. It has potential applications 
in data encryption, personal data security, and covert communication where secure message 
transmission is paramount. The combination of physical key generation through Arduino, AES 
encryption, and image steganography creates a robust and novel security mechanism. This 
project introduces an innovative method of physical key-based encryption, making it 
exceptionally resistant to traditional cryptographic attacks. 
