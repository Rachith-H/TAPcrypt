import serial
import time

arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

print("Listening for tap sequence....")

with open("tap_sequence.txt", "w") as f:
    pass

with open("tap_sequence.txt", "w") as f:
    try:
        while True:
            if arduino.in_waiting > 0:
                data = arduino.readline().decode('utf-8').strip()
                if data.isdigit():
                    print(f"Tap recorded: {data}")
                    f.write(f"{data}\n")
                    f.flush()

    except KeyboardInterrupt:
        print("\nRecording stopped manually.")

print("Tap sequence saved to tap_sequence.txt")
