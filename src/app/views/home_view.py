"""------------------------------------------------------------------------------------------------
    Home View File - UI class for main app landing screen
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
from tkinter import Frame
from tkinter import Canvas
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
        self.canvas = self.make_background(1280, 720)
        self.title1 = self.canvas.create_text(
            640,
            150,
            text="Film Success",
            fill="#2c6eb2",
            font=("System", 64, "bold")
        )
        self.title2 = self.canvas.create_text(
            640,
            230,
            text="P R E D I C T O R",
            fill="#164a97",
            font=("System", 52, "bold")
        )
        self.predict_btn = self.make_button("Predict Film's Success", 0.6)
        # self.add_movie_btn = self.make_button("Add Released Movie", 6.0)
    
    
    
    def get_color_at_position(self, ratio: float):
        color_top = (31, 9, 70)
        color_bot = (10, 7, 31)
        r = int(color_top[0] + (color_bot[0] - color_top[0]) * ratio)
        g = int(color_top[1] + (color_bot[1] - color_top[1]) * ratio)
        b = int(color_top[2] + (color_bot[2] - color_top[2]) * ratio)
        return f'#{r:02x}{g:02x}{b:02x}'
    
    
    
    def make_background(self, width: int, height: int):
        canvas = Canvas(self, width=width, height=height, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        color_top = (31, 9, 70)
        color_bot = (10, 7, 31)
        for i in range(720):
            ratio = i / 720
            r = int(color_top[0] + (color_bot[0] - color_top[0]) * ratio)
            g = int(color_top[1] + (color_bot[1] - color_top[1]) * ratio)
            b = int(color_top[2] + (color_bot[2] - color_top[2]) * ratio)
            color_hex = f'#{r:02x}{g:02x}{b:02x}'
            canvas.create_line(0, i, 1280, i, fill=color_hex)
        return canvas
    
    
    
    def make_button(self, btn_text: str, y_pos_ratio: int):
        target_y = int(720 * y_pos_ratio) 
        btn_base_color = self.get_color_at_position(y_pos_ratio)
        btn_interact_color = "#09071c"
        btn_text_color  = "#2c6eb2"
        button = Button(
            self.canvas,
            text=btn_text,
            background=btn_base_color,
            foreground=btn_text_color,
            activebackground=btn_interact_color,
            activeforeground=btn_text_color,
            font=("System", 18),
            bd=0,
            highlightthickness=0,
            padx=40,
            pady=10,
            cursor="hand2"
        )
        self.canvas.create_window(640, target_y, window=button)
        return button
