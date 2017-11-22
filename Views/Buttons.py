from tkinter import Button

class ChangeRoomButton(Button):
    class Constants:
        width = 67
        bg= '#b22222'


    def __init__ (self, master, x, y, height,phrase, image, action = None):
        self.__button = Button(master,command = self.__did_button_tap, image = image)
        self.__button.configure(width = self.Constants.width, height = height, bg=self.Constants.bg)
        self.__heigt = height
        self.__action = action
        self.__phrase=phrase
        self.__button.place(x = x, y = y)

    def __did_button_tap(self):
         if self.__action is None: return
         self.__action(self.__phrase)



