"""------------------------------------------------------------------------------------------------
    Main App Controller File - Controls the event logic and execution flow for the app
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
from customtkinter import CTk
from re import match
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
        self.__views["home view"].pack_forget()
        self.__views["predictor view"].pack(expand=True, fill="both")
    

    def home_view_event_add_movie(self):
        self.__views["home view"].pack_forget()
        self.__views["add movie view"].pack(expand=True, fill="both")


    def add_movie_view_event_go_back(self):
        self.__views["add movie view"].pack_forget()
        self.__views["home view"].pack(expand=True, fill="both")
    

    def predict_view_event_go_back(self):
        self.__views["predictor view"].pack_forget()
        self.__views["home view"].pack(expand=True, fill="both")
    
    
    def predictor_form_error_clearing(self, view):
        view.input_error_label.configure(text="")
        view.dir_name_tbox.configure(border_color="#110f24")
        view.genre_name_tbox.configure(border_color="#110f24")
        view.Prod_bgt_tbox.configure(border_color="#110f24")
        view.actor_name_tbox.configure(border_color="#110f24")
        view.writer_name_tbox.configure(border_color="#110f24")



    def predict_view_event_clear_form(self):
        view = self.__views["predictor view"]
        view.dir_name_tbox.delete(0, "end")
        view.genre_name_tbox.delete(0, "end")
        view.Prod_bgt_tbox.delete(0, "end")
        view.actor_name_tbox.delete(0, "end")
        view.writer_name_tbox.delete(0, "end")
        self.predictor_form_error_clearing(view)
    
    
    
    def valid_response(self, input_box, regex):
        user_input = input_box.get().strip()
        if not match(regex, user_input):
            input_box.configure(border_color="#b42b68")
            return False
        else:
            return True
    
    
    
    def predict_view_event_input_validation(self):
        view = self.__views["predictor view"]
        valid = True
        error_text = "ERROR: Add valid responses to highlighted boxes."
        re_name = r"^[A-Za-z\s\-\']+$"
        re_num = r"^\d+(\.\d{1,2})?$"
        self.predictor_form_error_clearing(view)
        valid = self.valid_response(view.dir_name_tbox, re_name) and valid
        valid = self.valid_response(view.genre_name_tbox, re_name) and valid
        valid = self.valid_response(view.Prod_bgt_tbox, re_num) and valid
        valid = self.valid_response(view.actor_name_tbox, re_name) and valid
        valid = self.valid_response(view.writer_name_tbox, re_name) and valid
        if not valid:
            view.input_error_label.configure(text=error_text)
