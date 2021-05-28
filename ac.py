from tuyapy import TuyaApi

from config import SL_USERNAME, SL_PASSWORD, SL_COUNTRYCODE, SL_APPLICATION


class AC:
    def __init__(self, api):
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
        return self.status

    def turn_off(self):
        self.device.turn_off()
        self.status = False
        return self.status

    def toggle(self):
        if self.status:
            self.turn_off()
        else:
            self.turn_on()
        return self.status


if __name__ == '__main__':
    import time
    api = TuyaApi()
    api.init(SL_USERNAME, SL_PASSWORD, SL_COUNTRYCODE, SL_APPLICATION)
    ac = AC(api)
    ac.toggle()
    time.sleep(10)
    ac.toggle()
