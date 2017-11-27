from Views.MainView import MainView

class MainApp():

    def __init__(self):
        self.__master = MainView(tap_button_handler = self.__toggle_did_change)

    def run(self):
        self.__master.mainloop()

    def __toggle_did_change(self, state):
        value = str(1 if state else 0).encode('ascii')

if __name__ == "__main__":
    app = MainApp()
    app.run()