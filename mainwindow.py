import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
 
class App(QMainWindow):
 
   def __init__(self):
      super().__init__()
      self.title = 'One time pad encryption decryption'
      self.left = 10
      self.top = 10
      self.width = 640
      self.height = 480
      self.initUI()


   def initUI(self):
      self.setWindowTitle(self.title)
      self.setGeometry(self.left, self.top, self.width, self.height)
      self.statusBar().showMessage('Message in statusbar.')
      button = QPushButton('Click', self)
      button.clicked.connect(self.on_click)
      button.setToolTip('This is an example button')
      buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you like PyQt5?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
      if buttonReply == QMessageBox.Yes :
         print('Yes clicked.')
      else :
         print('No clicked.')
      button.move(100,70)
      self.show()

   pyqtSlot()
   def on_click(self):
      print('PyQt5 button click')
      
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = App()
   sys.exit(app.exec())
   