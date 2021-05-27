import time

from tuyapy import TuyaApi
from config import SL_USERNAME, SL_PASSWORD, SL_COUNTRYCODE, SL_APPLICATION

api = TuyaApi()
api.init(SL_USERNAME, SL_PASSWORD, SL_COUNTRYCODE, SL_APPLICATION)


class AC:
    def __init__(self):
        dev = None
        for dev in api.get_all_devices():
            if dev.name() == 'AC':
                break
        self.device = dev

        assert self.device is not None
        self.device.turn_off()
        self.status = False

    def turn_on(self):
        self.device.turn_on()
        self.status = True

    def turn_off(self):
        self.device.turn_off()
        self.status = False

    def toggle(self):
        if self.status:
            self.turn_off()
        else:
            self.turn_on()


if __name__ == '__main__':
    ac = AC()
    ac.toggle()
    time.sleep(10)
    ac.toggle()
