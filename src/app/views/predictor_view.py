"""------------------------------------------------------------------------------------------------
    Predictor View File - UI class for machine learning prediction screen
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
from tkinter import Frame
from tkinter import Label
from tkinter import Button


class PredictorView(Frame):
    """
    Predictor UI class inherited from the Tkinter Frame class, contains the UI elements for the
    predicting the success of a movie after being presented with some information. The view
    will contain a form like section to accept movie info along with a data visualization zone
    for displaying the predictive analytics for the movie.
    """
    def __init__(self, controller) -> None:
        super().__init__(controller.get_window())
        self.controller = controller
        
        self.label = Label(
            self,
            text="Scene 2 App GUI",
            font=("Terminal", 18)
        )
        self.label.pack(pady=50)
        
        self.toggle_btn = Button(
            self,
            text="toggle",
            command=lambda:
                self.controller.switch_views('predictor view', 'home view')
        )
        self.toggle_btn.pack()
        
        self.print_btn = Button(
            self,
            text="print an action message",
            command=lambda:
                self.controller.print_view_message('Predictor view event')
        )
        self.print_btn.pack(pady=20)
