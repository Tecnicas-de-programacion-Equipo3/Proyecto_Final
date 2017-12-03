
from Models.ControllerLights import ControllerLights
from Models.ControllerGarage import ControllerGarage
class HouseManager():
    class Constants:
        Garage = "Garage"
        Alarm = "Alarm"
        Alarm_active = "T"
        Alarm_no_active = "F"

    def __init__(self, lights_handler = None, fan_handler = None, alarm_handler = None):
        self.__lights_handler = lights_handler
        self.__fan_handler = fan_handler
        self.__alarm_handler = alarm_handler
        self.__alarm_state = False

    def house_menu(self, state, room):
        if room == self.Constants.Garage:
            ControllerGarage(state, room, self.__motor_handler)
        elif room == self.Constants.Alarm:
            if state:
                self.__alarm_handler(self.Constants.Alarm_active)
            else:
                self.__alarm_handler(self.Constants.Alarm_no_active)
            self.__alarm_state = state
        else:
            ControllerLights(state, room, self.__lights_handler)

    def alarm_state(self):
        return self.__alarm_state


