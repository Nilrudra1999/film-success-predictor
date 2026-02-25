"""------------------------------------------------------------------------------------------------
    Add Movie View File - UI class for adding movies to the local database
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
from tkinter import Frame
from tkinter import Label

class AddMovieView(Frame):
    """
    Add movie UI class inherited from the Tkinter Frame class, connects to the app controller
    and provides a collection of widgets/UI elements which allow users to add movies to the 
    local database. The view will contain a form to collect movie information and will auto
    check if the information being entered is correct or already existing internally.
    """
    def __init__(self, controller) -> None:
        super().__init__(controller.get_window())
        self.controller = controller
        
        self.label = Label(
            self,
            text="UI for Adding Movies",
            font=("Terminal", 18)
        )
        self.label.pack(pady=50)
