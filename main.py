from Views.MainView import MainView

class MainApp():

    def __init__(self):
        self.__master = MainView(tap_button_handler = self.__did_button_tap)

    def run(self):
        self.__master.mainloop()

    def __did_button_tap(self, text):
        self.__master.Speaking.s = text

    def __toggle_did_change(self, state):
        value = str(1 if state else 0).encode('ascii')

    def convert_the_text(self):
        self.__master.text_to_voice()


if __name__ == "__main__":
    app = MainApp()
    app.run()