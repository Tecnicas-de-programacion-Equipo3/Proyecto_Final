import serial
from Views.MainView import MainView
from Models.Manager import HouseManager
from Models.ReadingDatas import ReadingData
from Models.ProximityAlarm import ProximityAlarm
from Models.ControllerTemp import ControllerTemp

class MainApp():
    class Constants:
        port = "COM3"
        port_Mac = "/dev/cu.usbmodem1411"
        baud = 115200
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):
        self.__master = MainView(tap_button_handler = self.__toggle_did_change, temperature_text = self.__update_temperature)
        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.close_event, self.__on_closing)
        self.__house = HouseManager(lights_handler = self.__controller_lights, fan_handler = None, alarm_handler = self.__activate_alarm)
        self.__receive_data()

    def run(self):
        self.__master.mainloop()

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

    def __receive_data(self):
        datas = self.__arduino.readline().decode()
        self.__datas = ReadingData(datas)
        there_is = self.__datas.get_proximity_data()
        self.__is_someone(self.__house.alarm_state(), there_is)
        self.__fans_updating(self.__datas.get_temperature_data())
        self.__master.after(2, self.__receive_data)

    def __update_temperature(self):
        pass

    def __is_someone(self, state, data):
        is_someone = ProximityAlarm(state, data)
        is_someone.there_is_someone()

    def __activate_alarm(self, is_active):
        activate = is_active.encode('ascii')
        self.__arduino.write(activate)

    def __fans_updating(self, temperatures):
        self.__fan = ControllerTemp(temperatures)
        fan1 = self.__fan.fan1_function()
        self.__controller_lights(fan1)

    def __controller_lights(self, order):
        arduino_order = order.encode('ascii')
        self.__arduino.write(arduino_order)

    def __toggle_did_change(self, state, room_name):
        self.__house.house_menu(state, room_name)

if __name__ == "__main__":
    app = MainApp()
    app.run()