import time


class TrafficLight:

    def running(self):
        while True:
            self.__color = "Красный"
            print(f"{self.__color}")
            time.sleep(7)
            self.__color = "Жёлтый"
            print(f"{self.__color}")
            time.sleep(2)
            self.__color = "Зелёный"
            print(f"{self.__color}")
            time.sleep(3)


trafficlight = TrafficLight()
trafficlight.running()
