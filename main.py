import serial
from Views.MainView import MainView
from Models.Manager import HouseManager
from Models.ReadingDatas import ReadingData
from Models.ProximityAlarm import ProximityAlarm
from Models.ControllerTemp import ControllerTemp

class MainApp():
    class Constants:
        port = "COM4"
        port_Mac = "/dev/cu.usbmodem1411"
        baud = 115200
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):
        self.__master = MainView(tap_button_handler = self.__toggle_did_change)
        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.close_event, self.__on_closing)
        self.__house = HouseManager(sending_arduino_handler = self.__sending_to_arduino)
        self.__receive_data()

    def run(self):
        self.__master.mainloop()

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

    def __receive_data(self):
        datas = self.__arduino.readline().decode()
        self.__datas = ReadingData(datas)
        self.__is_someone(self.__house.alarm_state(),self.__datas.get_proximity_data())
        self.__temperature = self.__datas.get_temperature_data()
        self.__master.updating_temperature_text(self.__temperature)
        self.__fans_updating(self.__temperature)
        self.__master.after(2, self.__receive_data)

    def __update_temperature(self):
        return str(self.__temperature)

    def __is_someone(self, state, data):
        is_someone = ProximityAlarm(state, data)
        is_someone.there_is_someone()

    def __fans_updating(self, temperatures):
        self.__fan = ControllerTemp(temperatures)
        fan1 = self.__fan.fan1_function()
        self.__sending_to_arduino(fan1)

    def __sending_to_arduino(self, order):
        arduino_order = order.encode('ascii')
        self.__arduino.write(arduino_order)

    def __toggle_did_change(self, state, room_name):
        self.__house.house_menu(state, room_name)

if __name__ == "__main__":
    app = MainApp()
    app.run()