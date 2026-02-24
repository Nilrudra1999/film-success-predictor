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

class AppController:
    """
    Initializes a Tkinter root object, and a dictionary of inherited Tkinter Frame objects
    decorated with various widgets. The controller connects the views to the event logic used
    by the app, which connects to the models to maintain the business logic thus, acting like
    a bridge between the views and the models.
    """
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Film Success Predictor")
        self.window.geometry("1280x720")
        self.window.resizable(width=False, height=False)
        
        self.views = {}
        self.views['home view'] = HomeView(self)
        self.views['predictor view'] = PredictorView(self)
    
    
    def get_window(self):
        return self.window
    
    
    def launch(self):
        self.views['home view'].pack(expand=True, fill="both")
        self.window.mainloop()
    
    
    def switch_views(self, old_view: str, new_view: str):
        self.views[old_view].pack_forget()
        self.views[new_view].pack(expand=True, fill="both")
    
    
    def print_view_message(self, text: str):
        print(text)
