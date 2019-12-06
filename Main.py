from tkinter import *
import tkinter as tk
from tkinter import font
import serial
import time

def forward(*ignore): #Sends str 1 to arduino
    print("W")
    bluetooth.write(b'1') 
    
def right(*ignore): #Sends str 2 to arduino
    print("D")
    bluetooth.write(b'2')

def backward(*ignore): #Sends str 3 to arduino
    print("S")
    bluetooth.write(b'3')
    
def left(*ignore): #Sends str 4 to arduino
    print("A")
    bluetooth.write(b'4')

def stop(*ignore): #Sends str 5 to arduino
    print("Stop")
    bluetooth.write(b'5')

def hardRight(*ignore): #Sends str 6 to arduino
    print("DD")
    bluetooth.write(b'6')
    
def hardLeft(*ignore): #Sends str 7 to arduino
    print("AA")
    bluetooth.write(b'7')

def fullForward(*ignore): #Sends str 8 to arduino
    print("WW")
    bluetooth.write(b'8')

def fullBack(*ignore): #Sends str 9 to arduino
    print("SS")
    bluetooth.write(b'9')

def backRight(*ignore): #Sends str : to arduino
    print(":")
    bluetooth.write(b':')
    
def backLeft(*ignore): #Sends str ; to arduino
    print(";")
    bluetooth.write(b';')



def timer(): #Updates and tracks time for the timer
    x = 0.00
    if x >= 0.00:
        new_time = time.get() + 1
        time.set(new_time)
        can.after(1000, timer) #call this function again in 1,000 milliseconds
        x += 1

def start(*ignore): #starts the timer when the method is called
    timer()

print("Start")
port="COM3" #uses COM3 to connect with arduino
bluetooth=serial.Serial(port, 9600) #Connects over 9600
print("Connected")
bluetooth.reset_input_buffer() #clears what's being sent over bluetooth

can= tk.Tk() #Creates timer canvas

can.title("Timer") #Names canvas

frame = tk.Frame(can, width=200, height=90) #creates frame for timer
frame.pack()

time = tk.DoubleVar() #creates time var
time.set(0) #sets time to zero

t_font = font.Font(family= 'Arial', size = 30)

ticker = tk.Label(can, font = t_font, bg = "white", textvariable= time)
ticker.place(x= 100, y= 20, anchor = tk.CENTER)

#start button that starts timer
start = tk.Button(can, width=6, height=2, text = "Start", bg= "white", command=start)
start.place(x=100, y= 70, anchor = tk.CENTER) 

#following bind keys to to methods, when the key is pressed, the method is called
can.bind('<w>', forward) 
can.bind('<a>', left)
can.bind('<s>', backward)
can.bind('<d>', right)
can.bind('<space>', stop)
can.bind('<A>', hardLeft)
can.bind('<D>', hardRight)
can.bind('<W>', fullForward)
can.bind('<S>', fullBack)
can.bind('<z>', backLeft)
can.bind('<c>', backRight)

can.mainloop() #refreshes the GUI so new inputs are recieved
