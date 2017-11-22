from tkinter import Label

class BackGround(Label):

    class Constants:
        bg='#eee8dc'

    def __init__ (self, master, x, y, width, image,text):
        self.__label = Label(master, image = image, width=width)
        self.__label.configure(bg = self.Constants.bg)
        self.__label.place(x = x, y = y)
        self.__text = text

