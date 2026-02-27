"""------------------------------------------------------------------------------------------------
    Predictor View File - UI class for machine learning prediction screen
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


class PredictorView(CTkFrame):
    """
    Predictor UI class inherited from Custom Tkinter Frame class, contains UI elements for 
    predicting the success of movies when presented with information. The view contains a form 
    section to accept movie info and data visualization zone to display predictive analytics.
    """
    def __init__(self, controller, window) -> None:
        super().__init__(window, fg_color=BG_COLOR_ALL)
        self.controller = controller
