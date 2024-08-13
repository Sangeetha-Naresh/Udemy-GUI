
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QListWidget, QLabel, QListWidgetItem, QStackedWidget, QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Udemy-like GUI with Cart")
        self.setGeometry(100, 100, 1200, 800)

        # Main layout
        main_layout = QVBoxLayout()

        # Main content area with sidebar and central widget
        #  creates a horizontal box layout. This layout will
        #  contain the sidebar and the central widget area, 
        # arranging them side by side horizontally.
        content_layout = QHBoxLayout()

        # Sidebar

        # creates a QListWidget, which serves as the sidebar.
        self.sidebar = QListWidget()

        # Items like "Home", "Available Courses", etc., are added to the sidebar. 
        # Each item represents a page in the application.
        self.sidebar.addItem(QListWidgetItem("Home"))
        self.sidebar.addItem(QListWidgetItem("Available Courses"))
        self.sidebar.addItem(QListWidgetItem("My Courses"))
        self.sidebar.addItem(QListWidgetItem("Categories"))
        self.sidebar.addItem(QListWidgetItem("Cart")) 
        self.sidebar.addItem(QListWidgetItem("Login"))
        self.sidebar.addItem(QListWidgetItem("Sign Up"))
        

        # The width of the sidebar is set to 200 pixels to keep it consistent.
        self.sidebar.setFixedWidth(200)

        # This connects the sidebar’s item selection change event to the change_page method. 
        # This method is called whenever a different item in the sidebar is selected.
        self.sidebar.currentItemChanged.connect(self.change_page)
        
        # This adds the sidebar to the content layout. 
        # The 1 indicates that the sidebar takes a fixed amount of space as determined 
        # by its set width.
        content_layout.addWidget(self.sidebar, 1)
        
        # Central widget area
        # This creates a QStackedWidget, which allows different widgets (pages) 
        # to be stacked on top of each other. Only the currently selected widget is visible.
        self.central_widget = QStackedWidget()


        # Page Creation and Adding to Central Widget:For each page (like the home page 
        # or available courses page), a new QWidget is created, and a QVBoxLayout is set for it.
        # Labels or other widgets are added to these layouts to display content specific to 
        # each page.
    

        # Home page
        home_page = QWidget()
        home_layout = QVBoxLayout()
        home_layout.addWidget(QLabel("Welcome to Udemy-like GUI"))
        home_page.setLayout(home_layout)

        # Available Courses page
        available_courses_page = QWidget()
        available_courses_layout = QVBoxLayout()
        self.available_courses_list = QListWidget()
        available_courses_page.setLayout(available_courses_layout)

        # My Courses page
        my_courses_page = QWidget()
        my_courses_layout = QVBoxLayout()
        my_courses_layout.addWidget(QLabel("My Courses"))
        self.my_courses_list = QListWidget()
        my_courses_layout.addWidget(self.my_courses_list)
        my_courses_page.setLayout(my_courses_layout)
        
        # Categories page
        categories_page = QWidget()
        categories_layout = QVBoxLayout()
        categories_layout.addWidget(QLabel("Course Categories"))
        categories_page.setLayout(categories_layout)
        
        # Cart page
        cart_page = QWidget()
        cart_layout = QVBoxLayout()
        cart_layout.addWidget(QLabel("Your Cart"))
        cart_page.setLayout(cart_layout)

        # Login page
        login_page = QWidget()
        login_layout = QVBoxLayout()
        login_layout.addWidget(QLabel("Login"))
        login_page.setLayout(login_layout)

        # Sign Up page
        signup_page = QWidget()
        signup_layout = QVBoxLayout()
        signup_layout.addWidget(QLabel("Sign Up"))
        signup_page.setLayout(signup_layout)

        # Profile page
        self.profile_page = QWidget()
        self.profile_layout = QVBoxLayout()
        self.profile_welcome_label = QLabel("Profile Page")
        self.profile_layout.addWidget(self.profile_welcome_label)
        self.profile_page.setLayout(self.profile_layout)
        
        # self.central_widget.addWidget(...): Each page widget is added to the central widget, 
        # allowing switching between them.
        self.central_widget.addWidget(home_page)
        self.central_widget.addWidget(available_courses_page)
        self.central_widget.addWidget(my_courses_page)
        self.central_widget.addWidget(categories_page)
        self.central_widget.addWidget(cart_page)
        self.central_widget.addWidget(login_page)
        self.central_widget.addWidget(signup_page)
        self.central_widget.addWidget(self.profile_page)
        

        #  This adds the central widget to the content layout. 
        # The 4 indicates that the central widget should take up the majority 
        # of the available space in the layout.
        content_layout.addWidget(self.central_widget, 4)
        

        # The content layout (containing the sidebar and central widget)
        #  is added to the main layout of the window.
        main_layout.addLayout(content_layout)

        # A container QWidget is created to hold the main layout.
        container = QWidget()

        # The main layout is set for the container.
        container.setLayout(main_layout)

        #  The container is set as the central widget of the main window, 
        #  making it the primary area where all content is displayed.
        self.setCentralWidget(container)

  # The change_page method is responsible for changing the displayed page 
  # in the central widget based on the selected item in the sidebar.
    def change_page(self, current_item):
        if current_item:
            current_text = current_item.text()

            # This method is called with the appropriate index, 
            # showing the corresponding page widget in the central widget.
            if current_text == "Home":
                self.central_widget.setCurrentIndex(0)
            elif current_text == "Available Courses":
                self.central_widget.setCurrentIndex(1)
            elif current_text == "My Courses":
                self.central_widget.setCurrentIndex(2)
            elif current_text == "Categories":
                self.central_widget.setCurrentIndex(3)
            elif current_text == "Cart":
                self.central_widget.setCurrentIndex(4)
            elif current_text == "Login":
                self.central_widget.setCurrentIndex(5)
            elif current_text == "Sign Up":
                self.central_widget.setCurrentIndex(6)
            elif current_text == "Profile":
                self.central_widget.setCurrentIndex(7)

  
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
