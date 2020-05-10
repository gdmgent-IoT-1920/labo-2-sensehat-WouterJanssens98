from sense_hat import SenseHat
import sys
import time
import random
sense = SenseHat()
sense.set_imu_config(False, False, False)

def main():
    rnd1 = random.randrange(0,255)
    rnd2 = random.randrange(0,255)
    rnd3 = random.randrange(0,255)
    text = "Hello! We are New Media Development :)"
    while True:
            rnd1 = random.randrange(0,255)
            rnd2 = random.randrange(0,255)
            rnd3 = random.randrange(0,255)
            rnd4 = random.randrange(0, rnd1)
            rnd5 = random.randrange(0, rnd2)
            rnd6 = random.randrange(0, rnd3)
            
            sense.set_rotation(180)
            sense.show_message(text, 0.1 ,[rnd1,rnd2,rnd3], [rnd4,rnd5,rnd6])
            time.sleep(1)
        
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit()

