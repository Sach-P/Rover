import serial
import os
from flask import Flask, render_template, request
ser = serial.Serial('/dev/ttyACM0', 9600) # This finds a device connected to the ACM0 port. The port can change every time the Pi boots up. 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<deviceName>")
def action(deviceName):
    if deviceName == 'F':
        ser.write(str.encode('F'))
    if deviceName == 'B':
        ser.write(str.encode('B'))
    if deviceName == 'L':
        ser.write(str.encode('L'))
    if deviceName == 'R':
        ser.write(str.encode('R'))
    if deviceName == 'S':
        ser.write(str.encode('S'))
    if deviceName == '1':
        ser.write(str.encode('1'))
    if deviceName == '2':
        ser.write(str.encode('2'))
    if deviceName == '3':
        ser.write(str.encode('3'))
    if deviceName == '4':
        ser.write(str.encode('4'))
    if deviceName == '5':
        ser.write(str.encode('5'))
    if deviceName == 'Con':
        os.system("sudo motion")
    if deviceName == 'Coff':
        os.system("sudo killall motion")
    if deviceName == 'Snap':
        os.system("curl -s -o /dev/null http://10.0.0.101:8080/0/action/snapshot")
    if deviceName == 'Vid':
        os.system("curl -s -o /dev/null http://10.0.0.101:8080/0/action/makemovie")
        
    return render_template('index.html')
    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80, debug=True)
