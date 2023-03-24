# APPLICATION FOR FITNESS APPLICATION
# ===============================================

# LIBRARIES AND MODULES
# ---------------------

import sys  # For accessing system parameters
import os  # For file path handling
from PyQt6 import QtCore
from PyQt6 import QtWidgets  # UI elements functionality
from PyQt6.uic import loadUi # For loading the UI file
# from qt_material import QtStyleTools, apply_stylesheet  # For theme adjustments


# Class for the main window
class MainWindow(QtWidgets.QMainWindow):
    """MainWindow for the fitness app."""
    
    def __init__(self):
        super().__init__()    
    
    # Constructor for the main window
        loadUi('main.ui', self)
        self.setWindowTitle('Fitness')

        # Load the UI file

           # Define UI Controls ie buttons and input fields
        self.calculatePushButton = self.calculatePushButton
        self.calculatePushButton.clicked.connect(self.calculateAll)

    # Define slots ie methods 
    def calculateAll(self):
        self.bmiLabel.setValue('100') 

if __name__ == "__main__":
    # Create the application

    # Create the mainwindow(and show it)

    # Start the application

 # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Create the Main Window object from MainWindow class and show it on the screen
    appWindow = MainWindow()
    appWindow.main.show()
    sys.exit(app.exec())
