from tkinter import Tk , PhotoImage , Label
from Views.Labels import BackGround
import win32com.client

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
        lecturas = "assets/lecturas.png"
        on = "assets/on.png"
        off = "assets/off.png"
        sensor = "assets/movement.png"

    class Positions:
        x_house =50
        y_house = 5
        x_garaje =750
        y_garaje =480
        x_comedor_habitacion1 = 140
        y_comedor_sala = 455
        x_sala_habitacion2 = 495
        y_habitaciones = 254

    class Constants:
        title = "Smart House"
        heigth = 700
        up_button_height = 100
        low_button_height = 125
        width = 1000
        widthB =600
        widthT = 211
        bg = "#eee8dc"


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

        self.__the_house = PhotoImage(file=self.Images.house)
        self.__backG = BackGround(self, self.Positions.x_house, self.Positions.y_house, image=self.__the_house, width=self.Constants.widthB,text=None)

        self.__clock_term= PhotoImage(file=self.Images.lecturas)
        self.__backG = BackGround(self, 700, self.Positions.y_house, image=self.__clock_term, width=260, text=None)

        self.__sens = PhotoImage(file=self.Images.sensor)
        self.__sen_mov = BackGround(self, 720, 180, image=self.__sens, width=230, text=None)



        self.__term = Label(self, font=('Haettenschweiler', 50, 'bold'), bg='#D0E9F3', fg='BLACK', bd=0 , text='22')
        self.__term.place(x=770,y=60),

        self.__sala = PhotoImage(file = self .Images.sala)
        self.__living_room_button = ChangeRoomButton(self, self.Positions.x_sala_habitacion2, self.Positions.y_comedor_sala,self.Constants.low_button_height,"You are in the living room" ,self.__sala , action = self.__did_button_tap)

        self.__comedor = PhotoImage(file = self .Images.comedor)
        self.__dining_room_button = ChangeRoomButton(self, self.Positions.x_comedor_habitacion1, self.Positions.y_comedor_sala,self.Constants.low_button_height,"You are in the living room" , self.__comedor,action = self.__did_button_tap)

        self.__rooms = PhotoImage(file = self .Images.recamara)
        self.__room1_button = ChangeRoomButton(self, self.Positions.x_comedor_habitacion1, self.Positions.y_habitaciones,self.Constants.up_button_height,"You are in the living room" , self.__rooms ,action = self.__did_button_tap)

        self.__room2_button = ChangeRoomButton(self, self.Positions.x_sala_habitacion2, self.Positions.y_habitaciones,self.Constants.up_button_height,"You are in the living room" ,self.__rooms ,action = self.__did_button_tap)

        self.__garge_open_close = ToggleButton(self , tap_handler,self.Positions.x_garaje, self.Positions.y_garaje, self.Images.parking_close, self.Images.parking_open, self.Constants.bg)
        self.__on_of_sensor = ToggleButton(self , tap_handler,780, 400, self.Images.on, self.Images.off, self.Constants.bg)

    def __did_button_tap(self, text):
        if self.__tap_button_handler is None: return
        self.__tap_button_handler(text)

    def text_to_voice(self):
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.speaker.Speak(self.Speaking.s)