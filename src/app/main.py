"""------------------------------------------------------------------------------------------------
    Main App File - Main entry-point of the application, init then launches the app
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
from controllers.app_controller import AppController

# Initializing the app and passing control to its controller
if __name__ == "__main__":
    app = AppController()
    app.launch()
