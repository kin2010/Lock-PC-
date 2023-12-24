import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect, QCoreApplication
from PyQt5.QtWidgets import QApplication,QWidget, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox,QMessageBox
import keyboard
from PyQt5.QtCore import Qt, QEvent
import ctypes
import firebase
class LockScreen(QWidget):
    
    
    def __init__(self):
        print('KHOITAO')
        super().__init__()
        self.pw='a'
        # Dialog.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        
        # Tính toán kích thước tổng cộng của tất cả các màn hình
        total_rect = QRect()
        for screen in QApplication.screens():
            print(screen.geometry(),total_rect.united(screen.geometry()))
            total_rect = total_rect.united(screen.geometry())

        # Thiết lập kích thước cửa sổ khóa màn hình
        self.setGeometry(total_rect)


        Dialog = QtWidgets.QDialog()
        dialogLayout = QVBoxLayout()
        dialogLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QtWidgets.QGroupBox(Dialog)
        self.container.setStyleSheet("background-image:url(D:/CODE/Python/LockPC/index.pyi/images/2.jpg)")
        self.container.setGeometry(Dialog.rect())
        self.container.setTitle("")
        self.container.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        dialogLayout.addWidget(self.container)
        
        self.groupBox = QtWidgets.QGroupBox( self.container)
        self.groupBox.setStyleSheet("background:rgb(255, 255, 255)")
        self.groupBox.setGeometry(QtCore.QRect(200, 200, 661, 591))
        # self.groupBox.setGeometry(QtCore.QRect(2550, 200, 661, 591))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setContentsMargins(400, 400, 0, 0)
         
        self.note = QtWidgets.QLineEdit(self.groupBox)
        self.note.setGeometry(QtCore.QRect(180, 230, 401, 91))
        self.note.setObjectName("note")
         
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(180, 100, 401, 41))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
          
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 50, 121, 20))
       
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 260, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.username = QtWidgets.QLineEdit(self.groupBox)
        self.username.setGeometry(QtCore.QRect(180, 40, 401, 41))
        self.username.setObjectName("username")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(180, 340, 271, 41))
        
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/CODE/Python/LockPC/index.pyi/images/1.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(65, 73))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.unlock)
        
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(40, 170, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.name = QtWidgets.QLineEdit(self.groupBox)
        self.name.setGeometry(QtCore.QRect(180, 160, 401, 41))
        self.name.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(320, 510, 461, 391))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("D:/CODE/Python/LockPC/index.pyi/images/1.jpg"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 410, 181, 151))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("D:/CODE/Python/LockPC/index.pyi/images/3.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(270, 430, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(270, 470, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(690, 300, 600, 600))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("D:/CODE/Python/LockPC/index.pyi/images/1.jpg"))
        self.label_4.setObjectName("label_4")
        # QtWidgets.setTabOrder(self.plainTextEdit, self.password)
       
        self.setLayout(dialogLayout)
        
        # self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Tool | Qt.FramelessWindowHint | Qt.WindowDoesNotAcceptFocus)
        # self.setAttribute(Qt.WA_ShowWithoutActivating)

        # self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Tool | Qt.FramelessWindowHint )
         # Đặt sự kiện bắt phím cho cửa sổ chính
        # self.installEventFilter(self) 
        # keyboard.add_hotkey('win',self.prevent_close)
        self.hideTaskbar()

    # end style
        self.retranslateUi(Dialog)
    def prevent_close(self):
        print("Win + Tab Pressed. Ignoring...")

    def unlock(self):
        
        username=self.username.text()
        entered_password = self.password.text()
        name=self.name.text()
        note=self.note.text()
        isChecked=self.checkBox.checkState() and self.checkBox_2.checkState()
        
        if username=='' or note=='' or isChecked==True or entered_password=='' or name=='':
          QMessageBox.warning(self, 'Điền cho đủ !!!','Không được để trống')
        elif entered_password == self.pw :
            self.hide()
            close()
        else:
            QMessageBox.warning(self, 'Mật khẩu không đúng', 'Mật khẩu không đúng. Vui lòng thử lại.')
        
    # def keyPressEvent(self, event):
    #     # Handle key press events for the entire window
    #     # if event.key() == 'space':
    #     #     self.close()
    #     return

    def eventFilter(self, obj, event):
        # Kiểm tra sự kiện keyPressEvent
        if event.type() == QEvent.KeyPress:
            # Kiểm tra xem Ctrl và Tab có được nhấn cùng một lúc hay không
            if Qt.Key_Tab:
                print(22,event.modifiers() )
                return True

        # Cho phép xử lý sự kiện tiếp theo
        return super().eventFilter(obj, event)
         
    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.note.setPlaceholderText(_translate("Dialog", "Vô pc để làm chi ??? : D"))
        self.label.setText(_translate("Dialog", "Tên đăng nhập"))
        self.label_3.setText(_translate("Dialog", "Note : = )))"))
        self.label_2.setText(_translate("Dialog", "Mật khẩu :"))
        self.pushButton.setText(_translate("Dialog", "Ok, xài thôiiiiii"))
        self.label_5.setText(_translate("Dialog", "Ai đấy ?"))
        self.checkBox.setText(_translate("Dialog", "1. Giữ vệ sinh phòng"))
        self.checkBox_2.setText(_translate("Dialog", "2. Xài cẩn thận nhé"))
        
    def hideTaskbar(self,hide=5):
    
        # Định nghĩa các hằng số từ WinAPI
        SW_HIDE = 0
        SW_SHOW = 5

        # Lấy handle của thanh taskbar
        hwnd_taskbar = ctypes.windll.user32.FindWindowW(u"Shell_traywnd", None)

        # Ẩn thanh taskbar
        ctypes.windll.user32.ShowWindow(hwnd_taskbar, hide)

        # Gọi hàm này để hiện thanh taskbar lại (nếu cần)
        # ctypes.windll.user32.ShowWindow(hwnd_taskbar, SW_SHOW)

def close():
    isLock=firebase.db.reference('open_lock')
    if isLock.get()==True:
        isLock.set(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = LockScreen()
    # ui.setupUi(Dialog)
    ui.show()
    
    sys.exit(app.exec_())
