"""------------------------------------------------------------------------------------------------
    Add Movie View File - UI class for adding movies to the local database
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
from customtkinter import CTkFrame
from customtkinter import CTkButton

BG_COLOR_ALL = "transparent"
TEXT_PRIMARY_COLOR = "#b01756"
TEXT_SECONDARY_COLOR = "#b42b68"
TILE_FOCUS_COLOR = "#201d35"
BTN_FOCUS_COLOR  = "#292450"


class AddMovieView(CTkFrame):
    """
    Add movie UI class inherited from Custom Tkinter Frame class, provides a collection of UI 
    elements which allow users to add movies to their local database. The view contains a form 
    to collect movie information and will auto-alert if any of the info entered is "incorrect".
    """
    def __init__(self, controller, window) -> None:
        super().__init__(window, fg_color=BG_COLOR_ALL)
        self.controller = controller
        self.form_frame = self.make_frame(self, 780, 680)
        self.form_frame.pack_propagate(False)
        self.form_frame.place(x=20, y=20)
        self.form_info_frame = self.make_frame(self, 400, 680)
        self.form_info_frame.pack_propagate(False)
        self.form_info_frame.place(x=820, y=20)
        self.back_btn = self.make_back_button(
            self, "B\nA\nC\nK",
            lambda: self.controller.add_movie_view_event_go_back()
        )
        self.back_btn.place(x=1233, y=20)
    
    
    
    def make_frame(self, root, width: int, height: int):
        return CTkFrame(
            root, fg_color=TILE_FOCUS_COLOR,
            width=width, height=height
        )
    
    
    
    def make_back_button(self, root, text: str, function):
        btn = CTkButton(
            root, width=20, height=50, 
            text=text, font=("System", 26),
            text_color=TEXT_PRIMARY_COLOR, 
            fg_color=BG_COLOR_ALL,
            hover=False, command=function
        )
        btn.bind("<Enter>", lambda e: 
            btn.configure(fg_color=BTN_FOCUS_COLOR)
        )
        btn.bind("<Leave>", lambda e: 
            btn.configure(fg_color=BG_COLOR_ALL)
        )
        return btn
