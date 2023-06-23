import serial
import time


ser = serial.Serial("COM7",9600)
num = 4532
ser.write(b'312312\n')

while True:
    data = ser.readline().decode().strip()
    print (data, len(data))

# while True:
#     inp = ser.readline().decode().strip()
#     print(len(inp))
#     if len(inp) == 3:
#         ser.write(b'a')
#         time.sleep(2)
#         ser.write(input("Nhap so ").encode())
#         time.sleep(2)
#         ser.write(input("Nhap so ").encode())
#         time.sleep(10)
#     while True:
#         print(ser.readline().decode())
        

# while True:
#     inp = ser.readline().decode().strip()
#     ser.write(b'r')
#     time.sleep(5)
#     ser.write(input("Nhap so ").encode())
#     time.sleep(2)
#     ser.write(input("Nhap so ").encode())
#     time.sleep(5)
#     while True:
#         try:
#             print(ser.readline().decode())
#         except:
#             print("loi")
            
        