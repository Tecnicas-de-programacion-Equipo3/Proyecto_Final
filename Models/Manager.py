from Models.ProximityAlarm import ProximityAlarm
from Models.ControllerLights import ControllerLights

class HouseManager():
    class Constants:
        Garage = "Garage"
        Alarm = "Alarm"

    def __init__(self, lights_handler = None, fan_handler = None, motor_handler = None, alarm_handler = None):
        self.__lights_handler = lights_handler
        self.__fan_handler = fan_handler
        self.__alarm_handler = alarm_handler
        self.__motor_handler = motor_handler
        self.__alarm = None

    def house_menu(self, state, room):
        if room == self.Constants.Garage:
            self.garage_door()
        elif room == self.Constants.Alarm:
            self.__alarm = ProximityAlarm(state, self.__alarm_handler)
            self.alarm()
        else:
            ControllerLights(state, room, self.__lights_handler)

    def garage_door(self):
        pass

    def alarm(self):
        pass

    def actual_temperature(self):
        pass


