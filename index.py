import firebase_admin
import time
from datetime import datetime
from app import LockScreen
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect, QCoreApplication
from PyQt5.QtWidgets import QApplication,QWidget, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox,QMessageBox
import keyboard
from PyQt5.QtCore import Qt, QEvent
import ctypes
from PyQt5.QtCore import QTimer
import firebase

# Khởi tạo Firebase với tệp tin serviceAccountKey.json của bạn
# Khởi tạo Firebase với tệp tin serviceAccountKey.json của bạn
ui =None
ref = firebase.db.reference('time')
isLock = firebase.db.reference('open_lock')

# Thêm dữ liệu vào database
def openPC():
    ref = firebase.db.reference('lock')
    ref.push({
        'time': getTime()
    })

# Hàm kiểm tra trạng thái khóa
def check_lock_status():
    if isLock.get() == True and ui.isVisible() == False:
        ui.show()
        print("SHOWING")
    else:
        # ui.close()  # Bạn có thể đóng ui nếu cần
        pass
    print(f"Thay đổi giá trị mới: {isLock.get()}", ui.isVisible())

def handleOpenLock(event):
    global ui
    print(f"Thay đổi giá trị mới: {event.data} {ui}")
    if ui:
        print(f"UI: {event.data}", ui.isVisible())
        if event.data == True and ui.isVisible() == False:
            print("START SHOWING")
            ui.show()
            print("SHOWING")
        else:
            # ui.close()
            pass
        print(f"Thay đổi giá trị mới: {event.data}", ui.isVisible())

def getTime():
    # Trích xuất các thành phần thời gian từ đối tượng datetime
    current_time = datetime.now()
    year = current_time.year
    month = current_time.month
    day = current_time.day
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second
    return f"{year}/{month}/{day} {hour}:{minute}:{second}"

if __name__ == "__main__":
    openPC()  # Chạy một lần để khởi tạo dữ liệu
    app = QtWidgets.QApplication([])
    ui = LockScreen()
    # isLock.listen(handleOpenLock)

    # Tạo và kết nối QTimer
    timer = QTimer()
    timer.timeout.connect(check_lock_status)
    timer.start(1000)  # Cập nhật mỗi giây
    app.exec_()
    