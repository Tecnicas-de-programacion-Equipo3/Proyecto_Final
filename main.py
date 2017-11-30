import serial
from Views.MainView import MainView
from Models.Manager import HouseManager
from Models.ReadingDatas import ReadingData

class MainApp():
    class Constants:
        port = "COM3"
        baud = 115200
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):
        self.__master = MainView(tap_button_handler = self.__toggle_did_change, temperature_text = self.__update_temperature)
        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.close_event, self.__on_closing)
        self.__house = HouseManager(lights_handler = None, fan_handler = None, motor_handler = None, alarm_handler = self.__activate_alarm)
        self.__datas = None
        self.__receive_data()

    def run(self):
        self.__master.mainloop()

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

    def __receive_data(self):
        datas = self.__arduino.readline().decode()
        self.__datas = ReadingData(datas)
        self.__master.after(2, self.__receive_data)

    def __update_temperature(self):
        pass

    def __activate_alarm(self, is_active):
        self.__arduino.write(is_active)

    def __toggle_did_change(self, state, room_name):
        self.__house.house_menu(state, room_name)

if __name__ == "__main__":
    app = MainApp()
    app.run()