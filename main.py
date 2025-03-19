import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class LoginApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
            self.setWindowTitle('Inicio de Sesión')
            self.setGeometry(100,100,300,200)
            
            self.label_user = QLabel('Usuario: ')
            self.input_user = QLineEdit()
            self.label_psw = QLabel('Contraseña: ')
            self.input_psw = QLineEdit()
            self.input_psw.setEchoMode(QLineEdit.EchoMode.Password)
            self.btn_login = QPushButton('Iniciar Sesión')
            
            layout = QVBoxLayout()
            layout.addWidget(self.label_user)
            layout.addWidget(self.input_user)
            layout.addWidget(self.label_psw)
            layout.addWidget(self.input_psw)
            layout.addWidget(self.btn_login)
            
            self.setLayout(layout)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())