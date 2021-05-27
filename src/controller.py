from time import sleep
from tuyapy import TuyaApi

from .ac import AC
from .dht11 import DHT11
from config import SL_USERNAME, SL_PASSWORD, SL_COUNTRYCODE, SL_APPLICATION


def controller(target_temp_f=75):
    api = TuyaApi()
    api.init(SL_USERNAME, SL_PASSWORD, SL_COUNTRYCODE, SL_APPLICATION)

    ac = AC(api)
    dht = DHT11()

    while(True):
        if dht.read():
            if dht.temp_f > target_temp_f:
                ac.turn_on()
            elif dht.temp_f < target_temp_f-2:
                ac.turn_off()
        else:
            return 1

        sleep(60)


if __name__ == '__main__':
    controller()
