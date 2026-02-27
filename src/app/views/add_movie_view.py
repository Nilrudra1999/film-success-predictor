"""------------------------------------------------------------------------------------------------
    Add Movie View File - UI class for adding movies to the local database
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
from customtkinter import CTkFrame

BG_COLOR_ALL = "transparent"
TEXT_PRIMARY_COLOR = "#b01756"
TEXT_SECONDARY_COLOR = "#b42b68"
TILE_FOCUS_COLOR = "#292450"


class AddMovieView(CTkFrame):
    """
    Add movie UI class inherited from Custom Tkinter Frame class, provides a collection of UI 
    elements which allow users to add movies to their local database. The view contains a form 
    to collect movie information and will auto-alert if any of the info entered is "incorrect".
    """
    def __init__(self, controller, window) -> None:
        super().__init__(window, fg_color=BG_COLOR_ALL)
        self.controller = controller
