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
        self.title1 = CTkLabel(
            self, text="Film Success", text_color=TEXT_PRIMARY_COLOR,
            fg_color="transparent", font=("System", 64, "bold")
        )
        self.title2 = CTkLabel(
            self, text="P R E D I C T O R", text_color=TEXT_SECONDARY_COLOR,
            fg_color="transparent", font=("System", 128)
        )
        self.title1.pack(pady=(150, 0))
        self.title2.pack()

        self.btn_frame = CTkFrame(self, fg_color=BG_COLOR_ALL)
        self.btn_frame.pack(pady=50)
        self.subtext_frame = CTkFrame(self, fg_color=BG_COLOR_ALL)
        self.subtext_frame.pack(pady=10) # explains button functions
        
        self.predict_btn = self.make_button(
            self.btn_frame, "Make Prediction",
            "Uses ML to estimate box office and ratings performance",
            lambda: self.controller.home_view_event_predict_movie()
        )
        self.add_movie_btn = self.make_button(
            self.btn_frame, "Add New Movie",
            "Updates the local database with new a new movie",
            lambda: self.controller.home_view_event_add_movie()
        )
        self.predict_btn.pack(side="left", padx=20)
        self.add_movie_btn.pack(side="left", padx=20)
        
        self.button_info = CTkLabel( # explains button functions
            self.subtext_frame, text="", font=("System", 22),
            text_color=TEXT_SECONDARY_COLOR
        )
        self.button_info.pack()
    
    
    
    def make_button(self, root, text: str, subtext: str, function):
        btn = CTkButton(
            root, width=275, height=45, 
            text=text, font=("System", 32),
            text_color=TEXT_PRIMARY_COLOR, 
            fg_color=BG_COLOR_ALL,
            hover=False, command=function
        )
        btn.bind("<Enter>", lambda e: [
            btn.configure(fg_color=TILE_FOCUS_COLOR),
            self.button_info.configure(text=subtext)
        ])
        btn.bind("<Leave>", lambda e: [
            btn.configure(fg_color=BG_COLOR_ALL),
            self.button_info.configure(text="")
        ])
        return btn
