"""------------------------------------------------------------------------------------------------
    Predictor View File - UI class for machine learning prediction screen
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


class PredictorView(CTkFrame):
    """
    Predictor UI class inherited from Custom Tkinter Frame class, contains UI elements for 
    predicting the success of movies when presented with information. The view contains a form 
    section to accept movie info and data visualization zone to display predictive analytics.
    """
    def __init__(self, controller, window) -> None:
        super().__init__(window, fg_color=BG_COLOR_ALL)
        self.controller = controller
        self.form_frame = self.make_frame(self, 340, 680, TILE_FOCUS_COLOR)
        self.form_frame.pack_propagate(False)
        self.form_frame.place(x=20, y=20)
        
        self.bo_rev_frame = self.make_frame(self, 840, 440, BG_COLOR_ALL)
        self.bo_rev_frame.pack_propagate(False)
        self.bo_rev_frame.place(x=380, y=20)
        
        self.ratings_frame = self.make_frame(self, 840, 220, BG_COLOR_ALL)
        self.ratings_frame.pack_propagate(False)
        self.ratings_frame.place(x=380, y=480)
        
        self.back_btn = self.make_back_button(
            self, "B\nA\nC\nK",
            lambda: self.controller.predict_view_event_go_back()
        )
        self.back_btn.place(x=1233, y=20)
    
    
    
    def make_frame(self, root, width: int, height: int, bg_color):
        return CTkFrame(
            root, fg_color=bg_color,
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
    