import Adafruit_DHT


class DHT11:
    def __init__(self, pin=18):
        self.pin = pin
        self.temp_c = 0
        self.temp_f = 0
        self.hum = 0

    def read(self):
        self.hum, self.temp_c = \
            Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, self.pin)
        return self.hum, self.temp_c, self.to_fahrenheit(self.temp_c)

    def to_fahrenheit(self):
        self.temp_f = (self.temp_c * 9 / 5) + 32
        return self.temp_f


if __name__ == '__main__.py':
    dht = DHT11()
    dht.read()
    dht.to_fahrenheit()
