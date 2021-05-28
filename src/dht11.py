import board
import adafruit_dht


class DHT11:
    def __init__(self):
        self.device = adafruit_dht.DHT11(board.D18)
        self.temp_c = 0
        self.temp_f = 0
        self.hum = 0

    def read(self):
        try:
            self.temp_c = self.device.temperature
            self.to_fahrenheit()
            self.hum = self.device.humidity
        except RuntimeError:
            return 0
        except Exception as error:
            self.device.exit()
            raise error
        return 1

    def to_fahrenheit(self):
        self.temp_f = (self.temp_c * 9 / 5) + 32
        return self.temp_f


if __name__ == '__main__.py':
    dht = DHT11()
    dht.read()
    dht.to_fahrenheit()
