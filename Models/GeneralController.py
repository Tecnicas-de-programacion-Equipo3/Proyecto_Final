from Views.MainView import MainView
import serial


class GeneralController():

    class Constants:
        port = "/dev/cu.usbmodem1411"
        baud = 115200
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):
        self.__master = MainView(tap_button_handler=self.__order, button_handler=self.__toggle_did_change)
        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)


    def __order(self, number_room):
        self.__number_room = number_room

    def __toggle_did_change(self, state):
        value = str(0 if state else 1).encode('ascii')
        number_room = str(self.__number_room).encode('ascii')
        self.__arduino.write(number_room + value)