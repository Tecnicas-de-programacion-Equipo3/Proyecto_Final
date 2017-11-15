from tkinter import Tk

class MainView(Tk):
    class Constants:
        title = "Smart House"
        heigth = 600
        width = 800

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())