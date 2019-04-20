import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox, QTextEdit
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from algorithm import vernam
 
class App(QMainWindow):
 
   def __init__(self):
      super().__init__()
      self.title = 'One time pad encryption decryption'
      self.left = 10
      self.top = 10
      self.width = 700
      self.height = 480
      self.initUI()


   def initUI(self):
      self.setWindowTitle(self.title)
      self.setGeometry(self.left, self.top, self.width, self.height)

      self.plaintextbox = QTextEdit(self)
      self.plaintextbox.move(20, 20)
      self.plaintextbox.resize(280,400)

      self.encryptbutton = QPushButton('Encrypt', self)
      self.encryptbutton.clicked.connect(self.encrypt_on_click)
      self.encryptbutton.move(300,150)
      self.encryptbutton.setToolTip('This is an example button')

      self.decryptbutton = QPushButton('Decrypt', self)
      self.decryptbutton.clicked.connect(self.decrypt_on_click)
      self.decryptbutton.move(300,180)
      self.decryptbutton.setToolTip('This is an example button')
      
      self.ciphertextbox = QTextEdit(self)
      self.ciphertextbox.move(380, 20)
      self.ciphertextbox.resize(280,400)

      self.show()

   @pyqtSlot()
   def encrypt_on_click(self):
      plaintext=self.plaintextbox.toPlainText()
      cipher_text = vernam("mykey123",plaintext)
      self.ciphertextbox.setText(cipher_text)      

   @pyqtSlot()
   def decrypt_on_click(self):
      ciphertext=self.ciphertextbox.toPlainText()
      plain_text = vernam("mykey123",ciphertext)
      self.plaintextbox.setText(plain_text)      

            
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = App()
   sys.exit(app.exec())
   