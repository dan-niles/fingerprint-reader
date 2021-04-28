import serial

ser = serial.Serial(
    port='COM5',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=3000)

print("connected to: " + ser.portstr)
count=1

print(ser.readline())
line = ser.readline()
new_line = line.decode("utf-8")
print(new_line)
text_array = new_line.split()
print(text_array[0])
print(text_array[1])
print(text_array[2])
nn = 0
while nn > 1:
    nn += 1
    line = ser.readline()
    new_line = line.decode("utf-8")
    print(new_line)
    #print(line.decode('"utf-8"'))


ser.close()