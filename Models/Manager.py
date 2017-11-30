from Models.ControllerLights import ControllerLights
from Models.ControllerGarage import ControllerGarage
class HouseManager():
    class Constants:
        Garage = "Garage"
        Alarm = "Alarm"

    def __init__(self, lights_handler = None, fan_handler = None, motor_handler = None):
        self.__lights_handler = lights_handler
        self.__fan_handler = fan_handler
        self.__motor_handler = motor_handler


    def house_menu(self, state, room):
        if room == self.Constants.Garage:
            ControllerGarage(state, room, self.__motor_handler)
        elif room == self.Constants.Alarm:
            self.alarm()
        else:
            ControllerLights(state, room, self.__lights_handler)


    def alarm(self):
        pass

    def actual_temperature(self):
        pass


