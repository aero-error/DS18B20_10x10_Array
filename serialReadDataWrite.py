# Michael Gromski
# This is a test program to read data from serial and save the data on a file
import serial

fname = input("Enter the name of the file: ")   # name of save data file
fvar =  open(fname,"w")
ser = serial.Serial('COM6', baudrate = 115200, timeout=1)   # Establish link withe serial port
i = 0

while i <= 100:
    arduinoData = ser.readline().strip().decode('ascii')    # reads and cleans up data
    dataNums = [float(n) for n in arduinoData.split()] # creates list with data as float variables
    print(arduinoData)
    fvar.write(arduinoData + '\n') # writes data on file and creates a seperator indicator
    i = i +1
fvar.close()    # saves file
print("File %s saved sucessfully." % fname)
