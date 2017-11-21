from tkinter import Tk , PhotoImage , Label
from Views.Labels import BackGround
from Views.Buttons import ChangeRoomButton
from Views.ToggleButton import ToggleButton


class MainView(Tk):
    class Images:
        house = "assets/BackGhouse.png"
        comedor = "assets/comedor.png"
        sala = "assets/sala.png"
        recamara = "assets/sleep.png"
        parking_close = "assets/garaje_closed.png"
        parking_open = "assets/garaje_opened.png"
    class Positions:
        x_house =50
        y_house = 5
        x_garaje =750
        y_garaje =480
        x_comedor_habitacion1 = 140
        y_comedor_sala = 475
        x_sala_habitacion2 = 495
        y_habitaciones = 260

    class Constants:
        title = "Smart House"
        heigth = 700
        width = 1000
        widthB =600
        widthT = 211
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



    def __interfaz_configure(self, tap_handler = None):

        self.__the_house = PhotoImage(file=self.Images.house)
        self.__backG = BackGround(self, self.Positions.x_house, self.Positions.y_house, image=self.__the_house, width=self.Constants.widthB)

        self.__sala = PhotoImage(file = self .Images.sala)
        self.__living_room_button = ChangeRoomButton(self, self.Positions.x_sala_habitacion2, self.Positions.y_comedor_sala,self.Constants.bg, self.__sala)

        self.__comedor = PhotoImage(file = self .Images.comedor)
        self.__dining_room_button = ChangeRoomButton(self, self.Positions.x_comedor_habitacion1, self.Positions.y_comedor_sala, self.Constants.bg, self.__comedor)

        self.__rooms = PhotoImage(file = self .Images.recamara)
        self.__room1_button = ChangeRoomButton(self, self.Positions.x_comedor_habitacion1, self.Positions.y_habitaciones, self.Constants.bg, self.__rooms)

        self.__room1_button = ChangeRoomButton(self, self.Positions.x_sala_habitacion2, self.Positions.y_habitaciones, self.Constants.bg, self.__rooms)

        self.__toogle1 = ToggleButton(self , tap_handler,self.Positions.x_garaje, self.Positions.y_garaje, self.Images.parking_close, self.Images.parking_open, self.Constants.bg)
