import cv2
import pyfirmata
import numpy as np 
from PIL import Image 
from itertools import count
try:
  board = pyfirmata.ArduinoMega("/dev/ttyUSB0")
except:
    try:
      board = pyfirmata.ArduinoMega("/dev/ttyUSB1")
    except:
        print("Dedevice connected")
it = pyfirmata.util.Iterator(board)
it.start()

board.analog[0].enable_reporting()
board.analog[1].enable_reporting() 
board.analog[2].enable_reporting() 
board.analog[3].enable_reporting() 
board.analog[4].enable_reporting() 
board.analog[5].enable_reporting() 
board.analog[6].enable_reporting()
board.analog[7].enable_reporting()
conv_units = 10000.0
for r in count(0):
    a0 = int(float(board.analog[0].read() or 0)*622.558)
    a1 = int(float(board.analog[1].read() or 0)*622.558) 
    a2 = int(float(board.analog[2].read() or 0)*622.558) 
    a3 = int(float(board.analog[3].read() or 0)*622.558) 
    a4 = int(float(board.analog[4].read() or 0)*622.558)
    a5 = int(float(board.analog[5].read() or 0)*622.558)
    a6 = int(float(board.analog[6].read() or 0)*622.558)
    a7 = int(float(board.analog[7].read() or 0)*622.558)
    #print(a0,type(a0),a1,a2,a3,a4,a5,a6,a7)
    list_array = list((a0,a1,a2,a3,a4,a5,a6,a7))
    print(list_array)
    #coff = np.asarray(list_array)
    #print(coff)
    array = np.array(list_array)
    print(array)
    array = array.astype(np.uint8)
    array = np.reshape(array, (4,2))
    color_image = cv2.cvtColor(array, cv2.COLOR_GRAY2RGB)*255
    #color_image = Image.fromarray(np.uint8(array))
    cv2.imshow("Sensor_array_image",array)
    cv2.imshow("Color visualize image",color_image)
    if cv2.waitKey(1) & 0xFF == ord(' '):
         break
cv2.destroyAllWindows()
    # EXERCISE add blinking of LEDs in response to reading
    # delay = ...
    # board.digital[LED_PIN].write(1)
    # board.pass_time(delay)
    # board.digital[LED_PIN].write(0)