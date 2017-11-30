class ControllerGarage():
    class Motors:
        garage_motor= "Garage"
    class Constants:
        garage="7"
        up = "1"
        down = "0"

    def __init__(self,state, room, motor_handler):
        self.__motor_handler = motor_handler
        self.__state = state
        self.__name_room = room
        self.__turn_up = True
        self.__turn_down = False
        self.__control_garage()

    def __state_garage(self):
        if self.__state == self.__turn_up:
            return self.Constants.up
        elif self.__state == self.__turn_down:
            return self.Constants.down

    def __room (self):
         if self.__name_room == self.Motors.garage_motor:
             return self.Constants.garage


    def __control_garage(self):
        state_garage = self.__state_garage()
        room = self.__room()
        self.__motor_handler(room+state_garage)
