import hashlib
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,  QPushButton,  QLineEdit,
    QListWidget, QLabel, QListWidgetItem, QStackedWidget, QMenu, QMenuBar, QWidget,QMessageBox
)
from PySide6.QtGui import QPixmap, QIcon, QAction
from PySide6.QtCore import Qt, QSize
import pandas as pd
from PySide6.QtCore import Qt
import json
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Udemy-like GUI with Cart")
        self.setGeometry(100, 100, 1200, 800)

        # Load the stylesheet
        with open("style.qss", "r") as style_file:
            self.setStyleSheet(style_file.read())


        # Read courses from Excel file
        self.courses_df = pd.read_excel("courseinfo.xlsx")
        self.all_courses = self.courses_df["coursename"].tolist() 
        self.courses = self.courses_df["coursename"].tolist()

        # Connect to SQLite database
        self.conn = sqlite3.connect('userinfo.db')
        self.create_users_table()

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

        # Top bar for search 
        top_bar = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search for courses")
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.perform_search)

        # Add profile icon button
        self.profile_button = QPushButton()
        self.profile_button.setIcon(QIcon("profile_icon.jpg"))
        self.profile_button.setIconSize(QSize(30, 30))
        self.profile_button.clicked.connect(self.show_profile_page)

        top_bar.addWidget(self.search_input)
        top_bar.addWidget(search_button)
        top_bar.addWidget(self.profile_button)

        main_layout.addLayout(top_bar)


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

        self.cart = []

        self.current_user = None

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
                self.update_my_courses()
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

    def add_to_cart(self):
        selected_item = self.available_courses_list.currentItem()
        if selected_item:
            course_name = selected_item.text()
            if course_name not in self.cart:
                self.cart.append(course_name)
                self.cart_list.addItem(course_name)

    def show_context_menu(self, position):
        context_menu = QMenu(self)
        delete_action = context_menu.addAction("Delete")
        action = context_menu.exec(self.cart_list.viewport().mapToGlobal(position))
        if action == delete_action:
            item = self.cart_list.currentItem()
            if item:
                self.cart.remove(item.text())
                self.cart_list.takeItem(self.cart_list.row(item))

    def perform_search(self):
        search_text = self.search_input.text().strip().lower()
        course_names = [course.lower() for course in self.courses]
        
        if search_text in course_names:
            course_index = course_names.index(search_text)
            course_name = self.courses[course_index]
            QMessageBox.information(self, "Course Found", f"Details of course: {course_name}")
        else:
            QMessageBox.warning(self, "Course Not Found", "The course does not exist!")

    def create_users_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                purchased_courses TEXT,
                available_courses TEXT
            )
        ''')
        self.conn.commit()

    def sign_up(self):
        username = self.signup_username_input.text()
        password = self.signup_password_input.text()
        avail_courses = json.dumps(self.courses)  # Convert the list to a JSON string
        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Username and password cannot be empty.")
            return
        cursor = self.conn.cursor()
        cursor.execute("SELECT username FROM users WHERE username=?", (username,))
        if cursor.fetchone():
            QMessageBox.warning(self, "Sign Up Failed", "Username already exists.")
            return
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("INSERT INTO users (username, password, purchased_courses, available_courses) VALUES (?, ?, ?, ?)", (username, hashed_password, "[]", avail_courses))
        self.conn.commit()
        QMessageBox.information(self, "Sign Up Successful", "Account created successfully. Please log in.")
        # Clear the input boxes
        self.signup_username_input.clear()
        self.signup_password_input.clear()



    def login(self):
        username = self.login_username_input.text()
        password = self.login_password_input.text()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor = self.conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username=?", (username,))
        result = cursor.fetchone()
        if result and result[0] == hashed_password:
            self.current_user = username
            self.refresh_available_courses()  # Refresh available courses on login
            self.update_profile_page()
            self.sidebar.setCurrentRow(0)
            self.central_widget.setCurrentIndex(0)
            QMessageBox.information(self, "Login Successful", f"Welcome, {username}!")
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

          # Clear the input boxes
        self.login_username_input.clear()
        self.login_password_input.clear()

    def show_profile_page(self):
        self.central_widget.setCurrentIndex(7)  # Show the profile page

    def logout(self):
        self.current_user = None
        self.central_widget.setCurrentIndex(0)
        self.logout_button.hide()
        self.refresh_available_courses()  # Refresh available courses on logout
        self.profile_welcome_label.setText("Profile Page")
        QMessageBox.information(self, "Logout Successful", "You have been logged out.")

    def update_profile_page(self):
        if self.current_user:
            self.profile_button.setIcon(QIcon("profile_icon.jpg")) 
            self.profile_welcome_label.setText(f"Welcome, {self.current_user}!")
            self.logout_button.show()
            cursor = self.conn.cursor()
            cursor.execute("SELECT purchased_courses FROM users WHERE username=?", (self.current_user,))
            purchased_courses = cursor.fetchone()[0]
            if not purchased_courses:
                purchased_courses = []
            else:
                purchased_courses = eval(purchased_courses)

    def purchase_courses(self):
        total_price = 0
        purchased_courses = []
        if self.current_user:
            cursor = self.conn.cursor()
            cursor.execute("SELECT purchased_courses FROM users WHERE username=?", (self.current_user,))
            purchased_courses_str = cursor.fetchone()[0]
            purchased_courses = json.loads(purchased_courses_str) if purchased_courses_str else []
            purchased_courses.extend(self.cart)
            purchased_courses = list(set(purchased_courses))  # Remove duplicates
            cursor.execute("UPDATE users SET purchased_courses=? WHERE username=?", (json.dumps(purchased_courses), self.current_user))

            # Calculate total price
            total_price = sum(self.courses_df[self.courses_df['coursename'] == course]['price'].values[0] for course in self.cart)

            # Update available courses based on the current user session
          
            self.avail_courses = [course for course in self.all_courses if course not in purchased_courses]
            cursor.execute("UPDATE users SET available_courses=? WHERE username=?", (json.dumps(self.avail_courses), self.current_user))
            self.refresh_available_courses()


            self.conn.commit()
            self.cart.clear()
            self.cart_list.clear()
            QMessageBox.information(self, "Purchase Successful", f"Courses purchased successfully!\nTotal Price: ${total_price:.2f}")
        else:
            QMessageBox.warning(self, "Not Logged In", "Please log in to purchase courses.")


    def refresh_available_courses(self):
        if self.current_user:
            cursor = self.conn.cursor()
            cursor.execute("SELECT available_courses FROM users WHERE username=?", (self.current_user,))
            available_courses = cursor.fetchone()[0]
            if not available_courses :
                available_courses  = []
            else:
                available_courses  = eval(available_courses )
            self.available_courses_list.clear()
            self.available_courses_list.addItems(available_courses)
        else:
            self.available_courses_list.clear()

    def update_my_courses(self):
        if self.current_user:
            cursor = self.conn.cursor()
            cursor.execute("SELECT purchased_courses FROM users WHERE username=?", (self.current_user,))
            purchased_courses = cursor.fetchone()[0]
            if not purchased_courses:
                purchased_courses = []
            else:
                purchased_courses = eval(purchased_courses)
            self.my_courses_list.clear()
            self.my_courses_list.addItems(purchased_courses)
        else:
            self.my_courses_list.clear()
            QMessageBox.warning(self, "Not Logged In", "Please log in to view your courses.")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
