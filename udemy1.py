# imports the sys module, which provides access to some variables used or maintained by 
# the Python interpreter 
# and to functions that interact strongly with the interpreter.
import sys

# QApplication manages application-wide resources, and 
# QMainWindow provides a main application window.
from PySide6.QtWidgets import QApplication, QMainWindow



def main():
    # Creates an instance of the QApplication class. 
    # sys.argv is passed to allow command-line arguments to control the application's behavior.
    app = QApplication(sys.argv)

    #  Creates an instance of the QMainWindow class, 
    # which will serve as the main window for the application.
    window = QMainWindow()

    # Sets the title of the main window
    window.setWindowTitle("Hello PySide6")

    # Sets the position and size of the window. The window will appear at 
    # coordinates (100, 100) on the screen and will be 800 pixels wide and 600 pixels tall.
    window.setGeometry(100, 100, 800, 600)

    # Displays the main window on the screen.
    window.show()

    #  Enters the main event loop of the application, where it waits for user events 
    # such as key presses or mouse clicks. 
    #  sys.exit ensures that the application exits cleanly when the event loop ends.
    sys.exit(app.exec())

# checks if the script is being run as the main module. 
# If it is, it calls the main function to start the application
if __name__ == "__main__":
    main()

# Summary
#This script sets up a basic PySide6 application with a main window that has a title 
# "Hello PySide6" and is sized 800x600 pixels. 
# It initializes the application, creates the main window, sets its title and geometry,
#  shows the window, and starts the event loop to keep the application running and 
# responsive to user interactions.