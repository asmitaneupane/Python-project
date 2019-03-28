import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QComboBox, QDialog, QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,QVBoxLayout
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

import sys
 
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
      
      button.setToolTip('This is an example button')
      button.move(100,70)
      self.show()

   pyqtSlot()
   def on_click(self):
      print('PyQt5 button click')
      
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = App()
   sys.exit(app.exec())
   