from tkinter import Tk, Label
from Helpers.InterfaceConfigureParameters import UIGraphics
from Views.Labels import BackGround
from Views.ToggleButton import ToggleButton

class MainView(Tk):
    class Constants:
        title = "Smart House"
        heigth = 700
        width = 1000
        bg = "#eee8dc"

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self , tap_button_handler = None, temperature_text=None):
        super().__init__()
        self.__tap_button_handler = tap_button_handler
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.configure(bg = self.Constants.bg)
        self.__UI_configure(temperature_text)


    def __UI_configure(self, temperature_text):

        for graphics in UIGraphics.background_graphics:
            self.__backG = BackGround(self, graphics[1], graphics[2], width = graphics[3], file_1 = graphics[0], text = graphics[4])

        self.__term = Label(self, font = (UIGraphics.font_type, UIGraphics.font_size), bg = UIGraphics.bg_temp, textvariable = temperature_text )
        self.__term.place(x = UIGraphics.x_temp, y = UIGraphics.y_temp)

        for button in UIGraphics.toggle_button_grapgics:
            self.__creating_the_button = ToggleButton(self, self.__tap_button_handler, button[0], button[1], button[2], button[3], button[4], button[5] )


