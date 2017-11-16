from Views.MainView import MainView

class MainApp():

    def __init__(self):
        self.__master = MainView()

    def run(self):
        self.__master.mainloop()

    def __toggle_did_change(self, state):
        value = str(1 if state else 0).encode('ascii')


if __name__ == "__main__":
    app = MainApp()
    app.run()