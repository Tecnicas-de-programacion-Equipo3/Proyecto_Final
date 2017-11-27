from tkinter import Label, PhotoImage
class BackGround(Label):

    class Constants:
        bg = '#eee8dc'

    def __init__ (self, master, x = None, y = None, width = None, file_1 = None, text = None):
        super().__init__(master, width = width)
        self.configure(bg = self.Constants.bg)
        self.__file_1 = file_1
        self.__open_image = PhotoImage(file = file_1)
        self.__set_image(self.__open_image)
        self.place(x = x, y = y)
        self.__text = text

    def __set_image(self, image):
        self.configure(image = image)
        self.image = image
