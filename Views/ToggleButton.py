from tkinter import Label, PhotoImage

class ToggleButton(Label):

    class Constants:

        event = "<Button-1>"

    def __init__(self, master, tap_toggle_handler = None ,room_function_room = None, x = None, y = None, file_1 = None, file_2 = None, bg = None):
        super().__init__(master)
        self.__tap_handler = tap_toggle_handler
        self.__state = False
        self.__file_1 = file_1
        self.__file_2 = file_2
        self.__open_image = PhotoImage(file = file_1)
        self.__close_image = PhotoImage(file = file_2)
        self.__set_image(self.__close_image)
        self.config(bg = bg)
        self.bind(self.Constants.event, self.__toggle)
        self.place(x = x , y = y)
        self.__room_function_room = room_function_room

    def __toggle(self, event):
        self.__state = not self.__state
        image = self.__open_image if self.__state else self.__close_image
        self.__set_image(image)

        if self.__tap_handler is None: return
        self.__tap_handler(self.__state)


    def __set_image(self, image):
        self.configure(image = image)
        self.image = image