class ControllerLights():

    class Rooms:
        Bedroom1 = "Bedroom1"
        Bedroom2 = "Bedroom2"
        Livingroom = "Livingroom"
        Diningroom = "Diningroom"

    class Constants:
        Bedroom1 = "1"
        Bedroom2 = "2"
        Livingroom = "3"
        Diningroom = "4"
        on = "1"
        off = "0"

    def __init__(self,state, room, lights_handler):
        self.__lights_handler = lights_handler
        self.__state = state
        self.__name_room = room
        self.__turn_on = True
        self.__turn_off = False
        self.__control_lights()

    def __state_room(self):
        if self.__state == self.__turn_on:
            return self.Constants.on
        elif self.__state == self.__turn_off:
            return self.Constants.off


    def __room (self):
         if self.__name_room == self.Rooms.Bedroom1:
             return self.Constants.Bedroom1
         elif self.__name_room == self.Rooms.Bedroom2:
             return self.Constants.Bedroom2
         elif self.__name_room == self.Rooms.Diningroom:
             return self.Constants.Livingroom
         elif self.__name_room == self.Rooms.Livingroom:
             return self.Constants.Diningroom

    def __control_lights(self):
        state_room = self.__state_room()
        room = self.__room()
        self.__lights_handler(room+state_room)

