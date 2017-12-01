class ControllerTemp():

    class Temperatures:
        TempLivingroom = 20
        TempDiningroom = 24

    class Constants:
        on = "1"
        off = "0"

    class Room:
        fan1 = '5'
        fan2 = '6'

    def __init__(self, temperature_1):
        self.__Temp1 = temperature_1
        self.__Temp2 = None

    def fan1_function(self):
         if self.__Temp1 >= self.Temperatures.TempDiningroom:
             return self.Room.fan1 + self.Constants.on
         elif self.__Temp1 < self.Temperatures.TempDiningroom:
             return self.Room.fan1 + self.Constants.off

    def __fan2_function(self):
        if self.__Temp2 >= self.Temperatures.TempLivingroom:
            return self.Room.fan1 + self.Constants.on
        elif self.__Temp2 < self.Temperatures.TempLivingroom:
            return self.Room.fan1 + self.Constants.off




