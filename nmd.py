from sense_hat import SenseHat
import sys
import time
import random
sense = SenseHat()
sense.set_imu_config(False, False, False)

def main():
    text = "NMD"
    while True:
        for x in text:
            rnd1 = random.randrange(0,255)
            rnd2 = random.randrange(0,255)
            rnd3 = random.randrange(0,255)
            sense.set_rotation(180)
            sense.show_letter(x,[rnd1,rnd2,rnd3], [0,0,0])
            time.sleep(1)
            sense.clear()
        time.sleep(3)
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit()
