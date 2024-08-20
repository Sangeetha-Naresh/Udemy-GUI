from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
    QListWidget, QLabel, QListWidgetItem, QStackedWidget, QMenu, QMenuBar, QWidget,
)
from PySide6.QtGui import QPixmap, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Udemy-like GUI with Cart")
        self.setGeometry(100, 100, 1200, 800)

        # Load the stylesheet
        with open("style.qss", "r") as style_file:
            self.setStyleSheet(style_file.read())

        # Create Menu Bar
        menu_bar = QMenuBar()
        # Categories Menu
        categories_menu = QMenu("Categories", self)
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
        menu_bar.addMenu(categories_menu)
        self.setMenuBar(menu_bar)

        # Main layout
        main_layout = QVBoxLayout()

        # Add Image
        self.image_label = QLabel(self)
        pixmap = QPixmap("image2.png")  # Replace with your image path
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.image_label.setFixedSize(1300, 390)  # Adjust size as needed
        main_layout.addWidget(self.image_label)

        # Main content area with sidebar and central widget
        content_layout = QHBoxLayout()

        # Sidebar
        self.sidebar = QListWidget()
        self.sidebar.addItem(QListWidgetItem("Home"))
        self.sidebar.addItem(QListWidgetItem("Available Courses"))
        self.sidebar.addItem(QListWidgetItem("My Courses"))
        self.sidebar.addItem(QListWidgetItem("Categories"))
        self.sidebar.addItem(QListWidgetItem("Cart")) 
        self.sidebar.addItem(QListWidgetItem("Login"))
        self.sidebar.addItem(QListWidgetItem("Sign Up"))
        
        self.sidebar.setStyleSheet(
            "background-color: #343a40; color: white; border-right: 2px solid #495057;"
        )

        self.sidebar.setFixedWidth(200)
        self.sidebar.currentItemChanged.connect(self.change_page)
        
        content_layout.addWidget(self.sidebar, 1)
        
        # Central widget area
        self.central_widget = QStackedWidget()

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

    def create_category_action(self, menu, category_name):
        action = QAction(category_name, self)
        action.triggered.connect(lambda: self.show_category_courses(category_name))
        menu.addAction(action)

    def show_category_courses(self, category_name):
        # Implement the logic to display category-specific content
        # For now, we can just display the category name in the central widget
        category_page = QWidget()
        category_layout = QVBoxLayout()
        category_layout.addWidget(QLabel(f"Category: {category_name}"))
        category_page.setLayout(category_layout)
        self.central_widget.addWidget(category_page)
        self.central_widget.setCurrentWidget(category_page)

    def change_page(self, current_item):
        if current_item:
            current_text = current_item.text()
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
