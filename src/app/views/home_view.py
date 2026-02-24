"""------------------------------------------------------------------------------------------------
    Home View File - UI class for main app landing screen
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
from tkinter import Frame
from tkinter import Label
from tkinter import Button


class HomeView(Frame):
    """
    Home view class inherited from the Tkinter Frame class, contains the widgets and UI 
    elements for the home/landing screen of the app. The UI here will contain two buttons for
    predicting the success of a movie or adding a released movie to the database locally. The
    UI will also contain hidden text boxes for showing messages, a title with stylized text,
    and a custom background.
    """
    def __init__(self, controller) -> None:
        super().__init__(controller.get_window())
        self.controller = controller
        
        self.label = Label(
            self,
            text="Scene 1 App GUI",
            font=("Terminal", 18)
        )
        self.label.pack(pady=50)
        
        self.toggle_btn = Button(
            self,
            text="toggle",
            command=lambda:
                self.controller.switch_views('home view', 'predictor view')
        )
        self.toggle_btn.pack()
        
        self.print_btn = Button(
            self,
            text="print an action message",
            command=lambda:
                self.controller.print_view_message('Home view event')
        )
        self.print_btn.pack(pady=20)
