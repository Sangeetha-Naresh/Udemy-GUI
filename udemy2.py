# QApplication: Manages the GUI application's control flow and main settings.
# QMainWindow: Provides a main application window with common UI elements like menus and toolbars.
# QVBoxLayout: A layout manager that arranges widgets vertically in a container.
# QLabel: A widget used to display text or images.
# QMenu: Represents a menu within a menu bar.
# QMenuBar: Holds and manages QMenu objects (like the top bar of the window).
# QWidget: The base class for all UI objects in PyQt/PySide. Used to create custom widgets.

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QMenu, QMenuBar, QWidget
)

#QAction: Represents an action that can be added to menus, toolbars, or used as a standalone action.
from PySide6.QtGui import  QAction

# Define a custom class MainWindow that inherits from QMainWindow. 
# This allows you to customize the main window's behavior and appearance.
class MainWindow(QMainWindow):

    def __init__(self):
        # Call the constructor of the parent class (QMainWindow) to initialize 
        # the main window properly.
        super().__init__()

        self.setWindowTitle("Udemy-like GUI")
        self.setGeometry(100, 100, 1200, 800)
        
        # Create an instance of QMenuBar that will be used to hold menus.
        menu_bar = QMenuBar()


        # Create a QMenu object named "Categories". 
        # The self argument specifies that the menu belongs to the MainWindow.
        categories_menu = QMenu("Categories", self)

        # Calls the create_category_action method to add an action (menu item) 
        # for the "Development" category to the categories_menu. 
        # This method is called multiple times to add different categories.
        self.create_category_action(categories_menu, "Development")
        self.create_category_action(categories_menu, "Business")
        self.create_category_action(categories_menu, "Finance & Accounting")
        self.create_category_action(categories_menu, "IT & Software")
        self.create_category_action(categories_menu, "Office Productivity")
        self.create_category_action(categories_menu, "Personal Development")
        self.create_category_action(categories_menu, "Design")
        self.create_category_action(categories_menu, "Marketing")
        self.create_category_action(categories_menu, "Lifestyle")
        self.create_category_action(categories_menu, "Photography & Video")
        self.create_category_action(categories_menu, "Health & Fitness")
        self.create_category_action(categories_menu, "Music")
        self.create_category_action(categories_menu, "Teaching & Academics")

        #  method to add a QMenu object (in this case, categories_menu) to the menu_bar.
        menu_bar.addMenu(categories_menu)

        # method of QMainWindow attaches the menu_bar to the main window.
        self.setMenuBar(menu_bar)


    def create_category_action(self, menu, category_name):

        # Creates an action with the name provided by category_name (e.g., "Development").
        # This action can be added to a menu or toolbar.
        action = QAction(category_name, self)

        # Connects the action's triggered signal to a lambda function that calls show_category_courses with the category_name. 
        # When the action is selected from the menu, the corresponding category page will be displayed.
        action.triggered.connect(lambda: self.show_category_courses(category_name))

        # Adds the action to the specified menu.
        menu.addAction(action)

    def show_category_courses(self, category_name):

        #  Creates a new widget that will serve as the container for the category page.
        category_page = QWidget()

        # Creates a vertical layout to arrange the widgets (like labels) vertically.
        category_layout = QVBoxLayout()

        # Adds a label to the layout that displays the selected category's name.
        category_layout.addWidget(QLabel(f"Category: {category_name}"))

        #  Sets the layout of the category_page to the vertical layout created earlier.
        category_page.setLayout(category_layout)

        # Set the category_page as the central widget
        # which means it will be displayed in the main area of the window.
        self.setCentralWidget(category_page)
   

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

