
from Models.ControllerLights import ControllerLights

class HouseManager():
    class Constants:
        Garage = "Garage"
        Alarm = "Alarm"

    def __init__(self, lights_handler = None, fan_handler = None, alarm_handler = None):
        self.__lights_handler = lights_handler
        self.__fan_handler = fan_handler
        self.__alarm_handler = alarm_handler
        self.__alarm_state = False

    def house_menu(self, state, room):
        if room == self.Constants.Garage:
            pass
        elif room == self.Constants.Alarm:
            #ProximityAlarm(state, self.__alarm_handler, self.__datas)
            if state:
                self.__alarm_handler('T')
            else:
                self.__alarm_handler("F")
            self.__alarm_state = state
        else:
            ControllerLights(state, room, self.__lights_handler)

    def alarm_state(self):
        return self.__alarm_state

    def actual_temperature(self):
        pass


