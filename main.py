from Views.MainView import MainView

class MainApp():

    def __init__(self):
        self.__master = MainView(tap_button_handler = self.__toggle_did_change, temperature_text = self.__update_temperature)

    def run(self):
        self.__master.mainloop()

    def __update_temperature(self):
        pass

    def __toggle_did_change(self, state ):
        pass

if __name__ == "__main__":
    app = MainApp()
    app.run()