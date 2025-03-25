# Instructions 
----
#### STEP 1: Tap Input  
- Upload the `tapcrypt.ino` file to the **Arduino** using the **Arduino IDE**.  
- Make the necessary connections with arduino and touch sensor.  
- Run the `serial_reader.py` file with the **Arduino connected to the serial port** to record the tap sequence.  
- The tap timestamps will be saved in a text file.  

---  
#### STEP 2: Encryption  
- Place an image in `.png` format at the location specified in the code or update the image path accordingly.  
- Run the `Main_enc.py` file and **enter your message** to be encrypted.  
- The message will be **AES-encrypted** using the tap-sequence-derived key.  
- Check the specified output location to obtain the **steganographed image**, which can be safely transferred.  

---  
#### STEP 3: Decryption  
- To retrieve the original message, **set up the Arduino** and input the same tap sequence as used during encryption.  
- Place the **steganographed image** at the location specified in the code, or modify the path accordingly.  
- Run the `main_dec.py` file to extract the **original message** from the image.    

---  
#### ⚠️ **NOTE:**  
- It is essential to use the **same tap sequence** with consistent **timing intervals** between consecutive taps for both encryption and decryption.  
- Any deviation in the tap rhythm or delays may result in decryption failure.  
