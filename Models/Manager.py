class HouseManager():
    class Constants:
        Garage = "Garage"
        Alarm = "Alarm"

    def __init__(self, lights_handler = None, fan_handler = None, motor_handler = None):
        self.__temperature_handler = lights_handler
        self.__fan_handler = fan_handler
        self.__motor_handler = motor_handler


    def house_menu(self, state, room):
        if room == self.Constants.Garage:
            self.garage_door()
        elif room == self.Constants.Alarm:
            self.alarm()
        else:
            self.control_lights()

    def garage_door(self):
        pass

    def alarm(self):
        pass

    def control_lights(self):
        pass

    def actual_temperature(self):
        pass

