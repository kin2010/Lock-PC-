import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QRect
import keyboard
class LockScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.password = ""

        layout = QVBoxLayout()
        # Create labels (widgets) to be placed in the layout
        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")

        # Add labels to the layout
        layout.addWidget(label1)
        layout.addWidget(label2)

         # Apply styles using CSS to individual widgets
        label1.setStyleSheet("color: blue; font-size: 20px;")
        label2.setStyleSheet("background-color: lightgray; padding: 10px;")
        self.password_label = QLabel('Nhập mật khẩu:')
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.unlock_button = QPushButton('Mở khóa', self)
        self.unlock_button.clicked.connect(self.unlock)

        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.unlock_button)

        self.setLayout(layout)

        # Lấy danh sách các màn hình
        screen_list = QApplication.screens()

        # Tính toán kích thước tổng cộng của tất cả các màn hình
        total_rect = QRect()
        for screen in screen_list:
            total_rect = total_rect.united(screen.geometry())

        # Thiết lập kích thước cửa sổ khóa màn hình
        self.setGeometry(total_rect)

        # self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Tool | Qt.FramelessWindowHint | Qt.WindowDoesNotAcceptFocus)
        # self.setAttribute(Qt.WA_ShowWithoutActivating)

       
    
        
    def unlock(self):
        def on_key_event(e):
            print(f'Key {e.name} {e.event_type}')
            if e.name == 'Enter':
                self.close()
        keyboard.hook(on_key_event)    
        
        entered_password = self.password_input.text()
        if entered_password == self.password :
            self.close()
        else:
            QMessageBox.warning(self, 'Mật khẩu không đúng', 'Mật khẩu không đúng. Vui lòng thử lại.')

def show_lock_screen():
    app = QApplication(sys.argv)
    lock_screen = LockScreen()
    lock_screen.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    show_lock_screen()
