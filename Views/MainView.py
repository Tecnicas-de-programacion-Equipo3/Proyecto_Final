from tkinter import Tk , PhotoImage , Label
from Views.Labels import BackGround
from Views.ToggleButton import ToggleButton

class MainView(Tk):
    class Images:
        house = "assets/BackGhouse.png"
        comedor_on = "assets/comedor_on.png"
        comedor_off = "assets/comedor_off.png"
        sala_on = "assets/sala_on.png"
        sala_off = "assets/sala_off.png"
        room_on = "assets/sleep_on.png"
        room_off = "assets/sleep_off.png"
        parking_close = "assets/garaje_closed.png"
        parking_open = "assets/garaje_opened.png"
        sensor_on = "assets/movement_on.png"
        sensor_off = "assets/movement_off.png"
        lecturas = "assets/lecturas.png"

    class Positions:
        x_house =50
        y_house = 5
        x_temp = 770
        y_temp = 60
        x_garaje =750
        y_garaje =480
        x_comedor_habitacion1 = 138
        y_comedor_sala = 456
        x_sala_habitacion2 = 493
        y_habitaciones = 255
        x_sensor = 745
        y_sensor = 200
        x_clock_term =700

    class Constants:
        title = "Smart House"
        heigth = 700
        up_button_height = 100
        low_button_height = 125
        width = 1000
        width_clock_term = 260
        widthB =600
        widthT = 211
        bg = "#eee8dc"
        bgS = '#b22222'
        bg_temp = '#D0E9F3'
        font_type = 'Haettenschweiler'
        font_size = 50

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    class Speaking:
        s = "hello"

    def __init__(self , tap_button_handler = None):
        super().__init__()
        self.__tap_button_handler = tap_button_handler
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.configure(bg = self.Constants.bg)
        self.__interfaz_configure()


    def __interfaz_configure(self, tap_handler = None):

        self.__the_house = PhotoImage(file = self.Images.house)
        self.__backG = BackGround(self, self.Positions.x_house, self.Positions.y_house, image = self.__the_house, width = self.Constants.widthB, text=None)

        self.__clock_term= PhotoImage(file = self.Images.lecturas)
        self.__backG = BackGround(self, self.Positions.x_clock_term, self.Positions.y_house, image=self.__clock_term, width=self.Constants.width_clock_term, text=None)

        self.__term = Label(self, font=(self.Constants.font_type, self.Constants.font_size), bg=self.Constants.bg_temp, text='22')
        self.__term.place(x = self.Positions.x_temp,y = self.Positions.y_temp)

        self.__sensor_on_off = ToggleButton(self , self.__tap_button_handler,self.Positions.x_sensor, self.Positions.y_sensor, self.Images.sensor_on, self.Images.sensor_off, self.Constants.bg)
        self.__garge_open_close = ToggleButton(self , self.__tap_button_handler,self.Positions.x_garaje, self.Positions.y_garaje, self.Images.parking_close, self.Images.parking_open, self.Constants.bg)
        self.__on_of_room1 = ToggleButton(self , tap_handler,self.Positions.x_comedor_habitacion1 ,self.Positions.y_habitaciones, self.Images.room_on, self.Images.room_off, None)
        self.__on_of_room2 = ToggleButton(self, tap_handler, self.Positions.x_sala_habitacion2, self.Positions.y_habitaciones, self.Images.room_on, self.Images.room_off, None)
        self.__on_of_living_room = ToggleButton(self, tap_handler, self.Positions.x_sala_habitacion2, self.Positions.y_comedor_sala, self.Images.sala_on, self.Images.sala_off, None)
        self.__on_of_dining_room = ToggleButton(self, tap_handler, self.Positions.x_comedor_habitacion1, self.Positions.y_comedor_sala, self.Images.comedor_on, self.Images.comedor_off, None)

    def __did_button_tap(self, text):
        if self.__tap_button_handler is None: return
        self.__tap_button_handler(text)
