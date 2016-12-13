import serial
import time
import re
import def_email
import def_tech
i=0
def wait():
    reply = "wait"
    while("ok" not in reply):
        reply=ser.readline()
        #time.sleep(0.2)
        reply=reply.decode('utf-8',"ignore")
        print(reply)
    time.sleep(0.2)
    ser.flushInput()

ser = serial.Serial('\\.\COM6', 9600)
print("Connected")
ser.flushInput()
while 1:
    mess=def_email.check()
    if  mess == 'no':
        ser.write(b"tech")
        #wait()
        time.sleep(0.1)
        news=def_tech.news(i)
        newstr = re.sub('[^a-zA-Z0-9\s\n\.]', '', news)
        i=(i+1)%3
        ser.write(b"News:"+str.encode(newstr))
        #wait()
        time.sleep(5)
    else:
        ser.write(b"mail")
        #wait()
        time.sleep(0.1)
        print(mess)
        for a in mess:
            print(a)
            print(a[0])
            print (a[1])
            ser.write(b"From:"+a[0])
            time.sleep(0.1)
            #wait()
            ser.write(b"Subject:"+a[1])
            time.sleep(0.1)
            #wait()
            time.sleep(5)
