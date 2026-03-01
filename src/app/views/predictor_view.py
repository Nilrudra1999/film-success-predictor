"""------------------------------------------------------------------------------------------------
    Predictor View File - UI class for machine learning prediction screen
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
from customtkinter import CTkFrame
from customtkinter import CTkButton
from customtkinter import CTkLabel
from customtkinter import CTkEntry

BG_COLOR_ALL = "transparent"
TEXT_PRIMARY_COLOR = "#b01756"
TEXT_SECONDARY_COLOR = "#b42b68"
TILE_FOCUS_COLOR = "#201d35"
BTN_FOCUS_COLOR  = "#292450"
FORM_BTN_NO_FOCUS = "#110f24"
FORM_BTN_FOCUS = "#090714"


class PredictorView(CTkFrame):
    """
    Predictor UI class inherited from Custom Tkinter Frame class, contains UI elements for 
    predicting the success of movies when presented with information. The view contains a form
    section to accept movie info and data visualization zone to display predictive analytics.
    """
    def __init__(self, controller, window) -> None:
        super().__init__(window, fg_color=BG_COLOR_ALL)
        self.controller = controller
        self.form_frame = CTkFrame(self, fg_color=TILE_FOCUS_COLOR, width=340, height=680)
        self.bo_rev_frame = CTkFrame(self, fg_color=TILE_FOCUS_COLOR, width=840, height=440)
        self.ratings_frame = CTkFrame(self, fg_color=TILE_FOCUS_COLOR, width=840, height=220)
        
        self.dir_name_tbox = self.make_entry_box(self.form_frame, "Enter Director Name")
        self.genre_name_tbox = self.make_entry_box(self.form_frame, "Enter Genre Name")
        self.Prod_bgt_tbox = self.make_entry_box(self.form_frame, "Enter Production Budget")
        self.actor_name_tbox = self.make_entry_box(self.form_frame, "Enter Lead Actor Name")
        self.writer_name_tbox = self.make_entry_box(self.form_frame, "Enter Writer Name")
        self.input_error_label = self.make_label(self.form_frame, "", 20, 260)

        self.form_predict_btn = self.make_button(self.form_frame, "Make Prediction", 260, 35,
            lambda: self.controller.predict_view_event_input_validation())
        self.form_clear_btn = self.make_button(self.form_frame, "Clear Form", 260, 35,
            lambda: self.controller.predict_view_event_clear_form())
        self.back_btn = self.make_button(self, "B\nA\nC\nK", 20, 50,
            lambda: self.controller.predict_view_event_go_back())
        self.set_view_widgets()
    
    
    
    def set_view_widgets(self):
        self.form_frame.pack_propagate(False)
        self.form_frame.place(x=20, y=20)
        self.dir_name_tbox.pack(pady=(20, 0))
        self.genre_name_tbox.pack(pady=(10, 0))
        self.Prod_bgt_tbox.pack(pady=(10, 0))
        self.actor_name_tbox.pack(pady=(10, 0))
        self.writer_name_tbox.pack(pady=(10, 0))
        self.input_error_label.pack(pady=(20, 0))
        self.form_predict_btn.pack(pady=(20, 0))
        self.form_clear_btn.pack(pady=(10, 10))
        
        self.bo_rev_frame.pack_propagate(False)
        self.bo_rev_frame.place(x=380, y=20)
        self.ratings_frame.pack_propagate(False)
        self.ratings_frame.place(x=380, y=480)

        self.back_btn.configure(font=("System", 26))
        self.back_btn.configure(fg_color=BG_COLOR_ALL)
        self.back_btn.bind("<Enter>", lambda e: 
            self.back_btn.configure(fg_color=BTN_FOCUS_COLOR))
        self.back_btn.bind("<Leave>", lambda e: 
            self.back_btn.configure(fg_color=BG_COLOR_ALL))
        self.back_btn.place(x=1233, y=20)
        
        
        
    def make_label(self, root, text: str, font_size: int, wrap: int):
        return CTkLabel(
            master=root, text=text, font=("System", font_size),
            text_color=TEXT_SECONDARY_COLOR, wraplength=wrap, justify="left"
        )
    
    
    
    def make_button(self, root, text: str, width: int, height: int, function):
        btn =  CTkButton(
            master=root, width=width, height=height, text=text,
            font=("Terminal", 18), text_color=TEXT_PRIMARY_COLOR,
            fg_color=FORM_BTN_NO_FOCUS, hover=False, command=function
        )
        btn.bind("<Enter>", lambda e: btn.configure(fg_color=FORM_BTN_FOCUS))
        btn.bind("<Leave>", lambda e: btn.configure(fg_color=FORM_BTN_NO_FOCUS))
        return btn
    
    
    
    def make_entry_box(self, root, placeholder: str):
        return CTkEntry(
            master=root, font=("System",18), placeholder_text=placeholder,
            placeholder_text_color=BTN_FOCUS_COLOR,
            text_color=TEXT_SECONDARY_COLOR, fg_color=FORM_BTN_NO_FOCUS,
            border_color=FORM_BTN_NO_FOCUS, width=260, height=35
        )
    