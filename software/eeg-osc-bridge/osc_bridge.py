# Just a reminder that the Python Code and the Arduino Code for “Motor” was created by my brother Jordan LeBlanc [10].	

import argparse
import math
import time
from pythonosc import dispatcher
from pythonosc import osc_server
import pyfirmata
import serial

# Initialize serial connection to Arduino
arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)
time.sleep(2)  # Wait for Arduino connection to establish

PORT_NUMBER = 8500
IP_DEFAULT = "127.0.0.1"

def filter_handler(address, *args):
    print(f"{address}: {args}")


def blink_light(address, *args):
    """Controls Arduino based on intensity value"""
    intensity = args[0]
    threshold = 0.25
    print(intensity, intensity > threshold)
    
    # Send command to Arduino based on intensity threshold
    if intensity > threshold:
        print("THINKING VERY LEFT - ACTIVATING ARDUINO")
        arduino.write(b'H')  # Send 'H' to Arduino (turn on)
    else:
        print("NOT LEFT - DEACTIVATING ARDUINO")
        arduino.write(b'L')  # Send 'L' to Arduino (turn off)
    
    print(f"{address}: {args[0]}")

def drop_handler(address, *args):
   
    intensity = args[0]
    # print("args : ", args)
    threshold = 0.25
    neutral = 0.005

    print(f"Address: {address}, Intensity: {intensity}")

    if intensity > threshold:
        print("Drop")
        arduino.write(b'D')  # 'A' for drop - opposite of angle of left
    elif intensity < neutral:
        print("'Intensity 0 => Stop Motor")
        arduino.write(b'S')
    

def left_handler(address, *args):
   
    intensity = args[0]
    # print("args : ", args)
    threshold = 0.25
    neutral = 0.005

    print(f"Address: {address}, Intensity: {intensity}")

    if intensity > threshold:
        print("Rotate Motor LEFT => rotate ANTICLOCKWISE")
        arduino.write(b'A')  # 'A' for anticlockwise
    elif intensity < neutral:
        print("'Intensity 0 => Stop Motor")
        arduino.write(b'S')

def stop_handler(address, *args):
    print(f"{address}: Stop Motor command recieved.")
    arduino.write(b'S')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default=IP_DEFAULT,
                        help="The IP address to listen on")
    parser.add_argument("--port",
                        type=int,
                        default=PORT_NUMBER,
                        help="The port to listen on")
    args = parser.parse_args()

  
    disp = dispatcher.Dispatcher()

    # === Facial Expressions Eye
    # disp.map("/fac/eyeAct/lookL", filter_handler)
    # disp.map("/fac/eyeAct/lookR", filter_handler) 
    # disp.map("/fac/eyeAct/winkL", filter_handler)
    # disp.map("/fac/eyeAct/winkR", filter_handler)

    # === Facial Expressions Upperface
    # disp.map("/fac/uAct/neutral", blink_light)
    # disp.map("/fac/uAct/frown", filter_handler)
    # disp.map("/fac/uAct/surprise", filter_handler)

    # === Facial Expressions Lowerface
    # disp.map("/fac/lAct/neutral", filter_handler)
    # disp.map("/fac/lAct/clench", filter_handler)
    # disp.map("/fac/lAct/laugh", filter_handler)
    # disp.map("/fac/lAct/smile", blink_light)
    # disp.map("/fac/lAct/smirkLeft", filter_handler)
    # disp.map("/fac/lAct/smirkRight", filter_handler)

    # === Mental Commands
    print("BLAH")
   # disp.map("/com/neutral", blink_light)
   # disp.map("/com/push", filter_handler)
    #disp.map("/com/pull", filter_handler)
    # disp.map("/com/left", filter_handler)
    # disp.map("/com/right", filter_handler)
    #disp.map("/com/lift", filter_handler)
    # disp.map("/com/drop", filter_handler)
    #disp.map("/com/rotateLeft", filter_handler)
    #disp.map("/com/rotateRight", filter_handler)
    #disp.map("/com/rotateClockwise", filter_handler)
    #disp.map("/com/rotateCounterClockwise", filter_handler)
    #disp.map("/com/rotateForwards", filter_handler)
    #disp.map("/com/rotateReverse", filter_handler)
    #disp.map("/com/disappear", filter_handler)
    disp.map("/com/drop", drop_handler)
    disp.map("/com/left", left_handler) # this is working 
    #disp.map("/com/right", stop_handler)

    # === Performance Metrics
    disp.map("/met/att", filter_handler)
    disp.map("/met/int", filter_handler)
    disp.map("/met/rel", filter_handler)
    disp.map("/met/str", filter_handler)
    disp.map("/met/exc", filter_handler)
    disp.map("/met/eng", filter_handler)
    disp.map("/met/cognitiveStress", filter_handler)
    disp.map("/met/visualAttention", filter_handler)
    disp.map("/met/auditoryAttention", filter_handler)

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), disp)
    print(f"Serving on {server.server_address}")
    server.serve_forever()



