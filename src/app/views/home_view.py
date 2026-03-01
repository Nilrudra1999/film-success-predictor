"""------------------------------------------------------------------------------------------------
    Home View File - UI class for main app landing screen
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
from customtkinter import CTkFrame
from customtkinter import CTkLabel
from customtkinter import CTkButton

BG_COLOR_ALL = "transparent"
TEXT_PRIMARY_COLOR = "#b01756"
TEXT_SECONDARY_COLOR = "#b42b68"
TILE_FOCUS_COLOR = "#292450"


class HomeView(CTkFrame):
    """
    Home view class inherited from Custom Tkinter Frame class, contains the UI elements for 
    the home screen of the app. The UI contains buttons to predict movie success or add newly 
    released movies to the local database. The UI also contains button-hover triggered texts.
    """
    def __init__(self, controller, window) -> None:
        super().__init__(window, fg_color=BG_COLOR_ALL)
        self.controller = controller
        self.title1 = self.make_label(self, "Film Success", 64)
        self.title2 = self.make_label(self, "P R E D I C T O R", 128)
        self.btn_frame = CTkFrame(self, fg_color=BG_COLOR_ALL)
        self.subtext_frame = CTkFrame(self, fg_color=BG_COLOR_ALL)
        self.btn_info = self.make_label(self.subtext_frame, "", 22)
        self.predict_btn = self.make_button(
            self.btn_frame, "Make Prediction",
            "Uses Machine Learning to estimate box-office revenues & ratings",
            lambda: self.controller.home_view_event_predict_movie()
        )
        self.add_movie_btn = self.make_button(
            self.btn_frame, "Add New Movie",
            "Updates the local database with new a new movie",
            lambda: self.controller.home_view_event_add_movie()
        )
        self.set_view_widgets()
    
    
    
    def set_view_widgets(self):
        self.title1.pack(pady=(150, 0))
        self.title2.configure(text_color=TEXT_SECONDARY_COLOR)
        self.title2.configure(font=("System", 128))
        self.title2.pack()
        self.btn_frame.pack(pady=50)
        self.predict_btn.pack(side="left", padx=20)
        self.add_movie_btn.pack(side="left", padx=20)
        self.subtext_frame.pack(pady=10)
        self.btn_info.configure(text_color=TEXT_SECONDARY_COLOR)
        self.btn_info.configure(font=("Terminal", 22))
        self.btn_info.pack()
    
    
    
    def make_label(self, root, text: str, font_size: int):
        return CTkLabel(
            master=root, text=text, font=("System", font_size, "bold"),
            text_color=TEXT_PRIMARY_COLOR, fg_color=BG_COLOR_ALL
        )
    
    
    
    def make_button(self, root, text: str, subtext: str, function):
        btn = CTkButton(
            master=root, 
            text=text, font=("System", 32),
            text_color=TEXT_PRIMARY_COLOR,
            fg_color=BG_COLOR_ALL,
            width=275, height=45,
            hover=False, command=function
        )
        btn.bind("<Enter>", lambda e: [
            btn.configure(fg_color=TILE_FOCUS_COLOR),
            self.btn_info.configure(text=subtext)
        ])
        btn.bind("<Leave>", lambda e: [
            btn.configure(fg_color=BG_COLOR_ALL),
            self.btn_info.configure(text="")
        ])
        return btn
