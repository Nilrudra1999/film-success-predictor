"""------------------------------------------------------------------------------------------------
    Main App Controller File - Controls the event logic and execution flow for the app
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
from customtkinter import CTk
from views.home_view import HomeView
from views.predictor_view import PredictorView
from views.add_movie_view import AddMovieView

BG_COLOR_LIGHT = "#28253b"
BG_COLOR_DARK  = "#13121e"


class AppController:
    """
    Initializes a Tkinter root object, and a dictionary of inherited Tkinter Frame objects
    decorated with various widgets. The controller connects the views to the event logic used
    by the app, which connects to the models to maintain the business logic thus, acting like
    a bridge between the views and the models.
    """
    def __init__(self) -> None:
        self.__window = CTk()
        self.__window.title("Film Success Predictor")
        self.__window.geometry("1280x720")
        self.__window.resizable(width=False, height=False)
        self.__window.configure(fg_color=(
            BG_COLOR_LIGHT,
            BG_COLOR_DARK
        ))
        self.__views = {
            "home view": HomeView(self, self.get_window()),
            "predictor view": PredictorView(self, self.get_window()),
            "add movie view": AddMovieView(self, self.get_window())
        }
    
    
    
    def get_window(self):
        return self.__window
    
    
    def launch(self):
        self.__views["home view"].pack(expand=True, fill="both")
        self.__window.mainloop()
    
    
    def home_view_event_predict_movie(self):
        print("Predicting movies")
    
    
    def home_view_event_add_movie(self):
        print("Adding movies")
