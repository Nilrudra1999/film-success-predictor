"""------------------------------------------------------------------------------------------------
    Main App Controller File - Controls the event logic and execution flow for the app
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
from tkinter import Tk
from views.home_view import HomeView
from views.predictor_view import PredictorView
from views.add_movie_view import AddMovieView

class AppController:
    """
    Initializes a Tkinter root object, and a dictionary of inherited Tkinter Frame objects
    decorated with various widgets. The controller connects the views to the event logic used
    by the app, which connects to the models to maintain the business logic thus, acting like
    a bridge between the views and the models.
    """
    def __init__(self) -> None:
        self.__window = Tk()
        self.__window.title("Film Success Predictor")
        self.__window.geometry("1280x720")
        self.__window.resizable(width=False, height=False)
        
        self.__views = {}
        self.__views['home view'] = HomeView(self)
        self.__views['predictor view'] = PredictorView(self)
        self.__views['add movie view'] = AddMovieView(self)
    
    
    
    def get_window(self):
        return self.__window
    
    
    def launch(self):
        self.__views['home view'].pack(expand=True, fill="both")
        self.__window.mainloop()
