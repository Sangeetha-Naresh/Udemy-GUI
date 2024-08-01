import hashlib
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QListWidget, QLabel, QListWidgetItem, QStackedWidget, QMenu, QMenuBar, QWidget,
    QMessageBox
)
from PySide6.QtGui import QPixmap, QIcon, QAction
from PySide6.QtCore import Qt, QSize
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Udemy-like GUI with Cart")
        self.setGeometry(100, 100, 1200, 800)
        
        # Read courses and users from Excel files
        self.courses_df = pd.read_excel("courseinfo.xlsx")
        self.courses = self.courses_df["coursename"].tolist()
        self.users_df = pd.read_excel("usersinfo.xlsx")
        
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

        # Top bar for search and profile
        top_bar = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search for courses")
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.perform_search)

        # Add profile icon button
        self.profile_button = QPushButton()
        self.profile_button.setIcon(QIcon("profile_icon.jpg"))  # Replace with your profile icon path
        self.profile_button.setIconSize(QSize(30, 30))  # Adjust size as needed
        self.profile_button.clicked.connect(self.show_profile_page)

        top_bar.addWidget(self.search_input)
        top_bar.addWidget(search_button)
        top_bar.addWidget(self.profile_button)

        main_layout.addLayout(top_bar)

        # Add Image
        self.image_label = QLabel(self)
        pixmap = QPixmap("image.png")  # Replace with your image path
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.image_label.setFixedSize(1300, 410)  # Adjust size as needed
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
        self.sidebar.addItem(QListWidgetItem("Profile"))  # Add Profile to sidebar
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
        self.available_courses_list.addItems(self.courses)
        self.add_to_cart_button = QPushButton("Add to Cart")
        self.add_to_cart_button.clicked.connect(self.add_to_cart)
        available_courses_layout.addWidget(QLabel("Available Courses"))
        available_courses_layout.addWidget(self.available_courses_list)
        available_courses_layout.addWidget(self.add_to_cart_button)
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
        self.cart_list = QListWidget()
        self.cart_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.cart_list.customContextMenuRequested.connect(self.show_context_menu)
        cart_layout.addWidget(self.cart_list)
        purchase_button = QPushButton("Purchase Courses")
        purchase_button.clicked.connect(self.purchase_courses)
        cart_layout.addWidget(purchase_button)
        cart_page.setLayout(cart_layout)

        # Login page
        login_page = QWidget()
        login_layout = QVBoxLayout()
        login_layout.addWidget(QLabel("Login"))
        self.login_username_input = QLineEdit()
        self.login_username_input.setPlaceholderText("Username")
        self.login_password_input = QLineEdit()
        self.login_password_input.setPlaceholderText("Password")
        self.login_password_input.setEchoMode(QLineEdit.Password)
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login)
        login_layout.addWidget(self.login_username_input)
        login_layout.addWidget(self.login_password_input)
        login_layout.addWidget(login_button)
        login_page.setLayout(login_layout)

        # Sign Up page
        signup_page = QWidget()
        signup_layout = QVBoxLayout()
        signup_layout.addWidget(QLabel("Sign Up"))
        self.signup_username_input = QLineEdit()
        self.signup_username_input.setPlaceholderText("Username")
        self.signup_password_input = QLineEdit()
        self.signup_password_input.setPlaceholderText("Password")
        self.signup_password_input.setEchoMode(QLineEdit.Password)
        signup_button = QPushButton("Sign Up")
        signup_button.clicked.connect(self.sign_up)
        signup_layout.addWidget(self.signup_username_input)
        signup_layout.addWidget(self.signup_password_input)
        signup_layout.addWidget(signup_button)
        signup_page.setLayout(signup_layout)

         # Profile page
        self.profile_page = QWidget()
        self.profile_layout = QVBoxLayout()
        self.profile_welcome_label = QLabel("Profile Page")
        self.profile_layout.addWidget(self.profile_welcome_label)
        self.logout_button = QPushButton("Logout")
        self.logout_button.hide()
        self.logout_button.clicked.connect(self.logout)
        self.profile_layout.addWidget(self.logout_button)
        # Add more widgets and profile information here
        self.profile_page.setLayout(self.profile_layout)

        self.central_widget.addWidget(home_page)
        self.central_widget.addWidget(available_courses_page)
        self.central_widget.addWidget(my_courses_page)
        self.central_widget.addWidget(categories_page)
        self.central_widget.addWidget(cart_page)
        self.central_widget.addWidget(login_page)
        self.central_widget.addWidget(signup_page)
        self.central_widget.addWidget(self.profile_page)
        
        content_layout.addWidget(self.central_widget, 4)
        
        main_layout.addLayout(content_layout)
        
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
        
        # Set styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 18px;
                color: #333;
            }
           QPushButton {
                background-color: #007bff;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QLineEdit {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QListWidget {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)

        # Initialize logged in user
        self.logged_in_username = None

    def create_category_action(self, menu, category_name):
        action = QAction(category_name, self)
        action.triggered.connect(lambda: self.show_category_page(category_name))
        menu.addAction(action)
        
    def show_category_page(self, category_name):
        print(f"Showing category: {category_name}")
        # Implement the logic to display category-specific content
        # For now, we can just display the category name in the central widget
        category_page = QWidget()
        category_layout = QVBoxLayout()
        category_layout.addWidget(QLabel(f"Category: {category_name}"))
        category_page.setLayout(category_layout)
        self.central_widget.addWidget(category_page)
        self.central_widget.setCurrentWidget(category_page)
    
    def change_page(self, current, previous):
        if current is not None:
            page = current.text()
            if page == "Home":
                self.central_widget.setCurrentIndex(0)
            elif page == "Available Courses":
                self.central_widget.setCurrentIndex(1)
            elif page == "My Courses":
                self.central_widget.setCurrentIndex(2)
            elif page == "Categories":
                self.central_widget.setCurrentIndex(3)
            elif page == "Cart":
                self.central_widget.setCurrentIndex(4)
            elif page == "Login":
                self.central_widget.setCurrentIndex(5)
            elif page == "Sign Up":
                self.central_widget.setCurrentIndex(6)
            elif page == "Profile":
                self.central_widget.setCurrentIndex(7)
    
    def show_profile_page(self):
        self.central_widget.setCurrentWidget(self.central_widget.widget(7))  # Show profile page
        


    def perform_search(self):
        search_text = self.search_input.text().strip().lower()
        course_names = [course.lower() for course in self.courses]
        
        if search_text in course_names:
            course_index = course_names.index(search_text)
            course_name = self.courses[course_index]
            QMessageBox.information(self, "Course Found", f"Details of course: {course_name}")
        else:
            QMessageBox.warning(self, "Course Not Found", "The course does not exist!")

    def add_to_cart(self):
        selected_items = self.available_courses_list.selectedItems()
        for item in selected_items:
            course_name = item.text()
            if not self.cart_list.findItems(course_name, Qt.MatchExactly):
                self.cart_list.addItem(course_name)

    def show_context_menu(self, pos):
        context_menu = QMenu(self)
        remove_action = QAction("Remove from Cart", self)
        remove_action.triggered.connect(self.remove_from_cart)
        context_menu.addAction(remove_action)
        context_menu.exec(self.cart_list.mapToGlobal(pos))

    def remove_from_cart(self):
        selected_items = self.cart_list.selectedItems()
        for item in selected_items:
            self.cart_list.takeItem(self.cart_list.row(item))

    def purchase_courses(self):
        total_price = 0
        purchased_courses = []
        for i in range(self.cart_list.count()):
            item = self.cart_list.item(i)
            course_name = item.text()
            course_price = self.courses_df[self.courses_df["coursename"] == course_name]["price"].values[0]
            total_price += course_price
            purchased_courses.append(course_name)
            
            # Add to My Courses
            self.my_courses_list.addItem(course_name)

            # Remove the course from the available courses list
            available_items = self.available_courses_list.findItems(course_name, Qt.MatchExactly)
            if available_items:
                for available_item in available_items:
                    self.available_courses_list.takeItem(self.available_courses_list.row(available_item))
        
        QMessageBox.information(self, "Purchase Successful", f"Purchased courses: {', '.join(purchased_courses)}\nTotal Price: ${total_price:.2f}")
        self.cart_list.clear()
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def login(self):
        username = self.login_username_input.text().strip()
        password = self.login_password_input.text().strip()
        hashed_password = self.hash_password(password)
        
        if username in self.users_df['username'].values:
            stored_password = self.users_df[self.users_df['username'] == username]['password'].values[0]
            if hashed_password == stored_password:
                self.logged_in_username = username
                self.update_profile_page()
                QMessageBox.information(self, "Login Successful", f"Welcome back, {username}!")
            else:
                QMessageBox.warning(self, "Login Failed", "Incorrect password.")
        else:
            QMessageBox.warning(self, "Login Failed", "Username not found.")

         # Clear the input boxes
        self.login_username_input.clear()
        self.login_password_input.clear()
    
    def sign_up(self):
        username = self.signup_username_input.text().strip()
        password = self.signup_password_input.text().strip()
        hashed_password = self.hash_password(password)
    
        if username in self.users_df['username'].values:
            QMessageBox.warning(self, "Sign Up Failed", "Username already exists.")
        else:
            new_user = pd.DataFrame({'username': [username], 'password': [hashed_password]})
            self.users_df = pd.concat([self.users_df, new_user], ignore_index=True)
            self.users_df.to_excel("usersinfo.xlsx", index=False)
            QMessageBox.information(self, "Sign Up Successful", "You have successfully signed up!")
         # Clear the input boxes
        self.signup_username_input.clear()
        self.signup_password_input.clear()

    def update_profile_page(self):
        if self.logged_in_username:
            self.profile_welcome_label.setText(f"Welcome, {self.logged_in_username}!")
            self.logout_button.show()
        else:
            self.profile_welcome_label.setText("Profile Page")
            self.logout_button.hide()

    def logout(self):
        self.logged_in_username = None
        QMessageBox.information(self, "Logout Successful", "You have been logged out.")
        self.update_profile_page()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
