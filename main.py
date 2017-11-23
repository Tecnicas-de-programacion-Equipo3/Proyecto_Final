from Views.MainView import MainView
import serial

class MainApp():
    class Constants:
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):
        self.__master = MainView(tap_button_handler = self.__toggle_did_change)

    def run(self):
        self.__master.mainloop()

    def __toggle_did_change(self, state ):
        value = str(1 if state else 'a').encode('ascii')

if __name__ == "__main__":
    app = MainApp()
    app.run()