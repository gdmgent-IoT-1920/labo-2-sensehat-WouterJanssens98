from sense_hat import SenseHat
import sys
import time
import random
sense = SenseHat()
sense.set_imu_config(False, False, False)

def main():
    sense.clear()
    sense.set_pixel(1,7,139,69,19)
    sense.set_pixel(2,7,139,69,19)
    sense.set_pixel(2,6,139,69,19)
    sense.set_pixel(3,7,139,69,19)
    sense.set_pixel(3,5,0,0,255)
    sense.set_pixel(2,5,0,0,255)
    sense.set_pixel(1,5,0,0,255)
    sense.set_pixel(2,4,211,211,211)
   
     
    
    while True:
        event = sense.stick.wait_for_event(emptybuffer=True)
        if(event.action == "released" and event.direction == "up"):
            print("Pushed up!")
            list = sense.get_pixels()
            print(list)

            
            
        elif(event.action == "released" and event.direction == "down"):
            print("Pushed down!")
        elif(event.action == "released" and event.direction =="left"):
            print("Pushed left")
        elif(event.action == "released" and event.direction == "right"):
            print("Pushed right")
        
            
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit()


