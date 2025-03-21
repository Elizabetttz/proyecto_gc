import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox


DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '12328',
    'database': 'login_db'
}

class LoginApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()     
        self.abrir_home()

        
    def setup_ui(self):
            self.setWindowTitle('Inicio de Sesión')
            self.setGeometry(100,100,300,200)
            
            self.label_user = QLabel('Usuario: ')
            self.input_user = QLineEdit()
            self.label_psw = QLabel('Contraseña: ')
            self.input_psw = QLineEdit()
            self.input_psw.setEchoMode(QLineEdit.EchoMode.Password)
            self.btn_login = QPushButton('Iniciar Sesión')
            self.btn_login.clicked.connect(self.check_login)
            
            layout = QVBoxLayout()
            layout.addWidget(self.label_user)
            layout.addWidget(self.input_user)
            layout.addWidget(self.label_psw)
            layout.addWidget(self.input_psw)
            layout.addWidget(self.btn_login)
            
            self.setLayout(layout)
            
    def check_login(self, home):
        usuario = self.input_user.text().strip()
        contraseña = self.input_psw.text().strip()
        
        if not usuario or not contraseña:
            QMessageBox.warning(self, 'Error', 'Todos los campos son necesarios')
            return
                
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            query = "SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s"
            cursor.execute(query,(usuario,contraseña))
            resultado = cursor.fetchone()
            conn.close()
            
            if resultado:
                QMessageBox.information(self, 'Éxito', 'en el inicio de sesion')
                self.abrir_home()
            else:
                QMessageBox.warning(self, 'Error', 'Contraseña o usuario incorrecto')
        except mysql.connector.Error as e:
            QMessageBox.critical(self, 'Error', f'Error de conexion: {e}')
            
    
    def abrir_home(self):
        self.hide()
        self.ventana_inicio = InicioApp()
        self.ventana_inicio.show()
        
class InicioApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Inicio')
        self.setGeometry(300,100,700,500)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_login = LoginApp()
    ventana_login.show()
    sys.exit(app.exec())