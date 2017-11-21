from tkinter import Button

class ChangeRoomButton(Button):
    class Constants:
        width = 67
        height = 87
        bg= '#b22222'

    def __init__ (self, master, x, y, color, image):
        self.__button = Button(master, image = image)
        self.__color = color
        self.__button.configure(width = self.Constants.width, height = self.Constants.height,bg=self.Constants.bg)
        self.__button.place(x = x, y = y)



