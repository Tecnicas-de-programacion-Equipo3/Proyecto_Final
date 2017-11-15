from tkinter import Tk , PhotoImage
from Views.Labels import BackGround

class MainView(Tk):
    class Images:
        house = "assets/BackGhouse.png"
    class Positions:
        x_house = 100
        y_house = 5

    class Constants:
        title = "Smart House"
        heigth = 700
        width = 1000
        widthB =600
        bg = "#eee8dc"

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.configure(bg = self.Constants.bg)
        self.__interfaz_configure()

    def __interfaz_configure(self):

        self.__the_house = PhotoImage(file=self.Images.house)
        self.__backG = BackGround(self, self.Positions.x_house, self.Positions.y_house, image=self.__the_house, width=self.Constants.widthB)
