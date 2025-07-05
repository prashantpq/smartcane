import serial

ser = serial.Serial('/dev/rfcomm0', 9600)  
def send_data(data):
    try:
        ser.write(data.encode())
        print(f"Sent via Bluetooth: {data}")
    except Exception as e:
        print("Bluetooth Error:", e)
