from PyQt5 import QtCore, QtGui, QtWidgets, uic 
from PyQt5.Qt import Qt
import sys
sys.path.insert(0, 'Instruments/')
import Piano #This imports a python script called Piano.py

#variables 



class Ui (QtWidgets.QMainWindow): 
    def __init__(self): 
        super(Ui, self).__init__() 
        uic.loadUi('Ui/Test.ui', self) 
        self.show()
        




        #Instrument keys 
        self.button = self.findChild(QtWidgets.QPushButton, 'HighC_Button')
        self.button.clicked.connect(Piano.value_HighC)

        self.button = self.findChild(QtWidgets.QPushButton, 'B_Button')
        self.button.clicked.connect(Piano.value_B)
       

        self.button = self.findChild(QtWidgets.QPushButton, 'ASharp_Button')
        self.button.clicked.connect(Piano.value_As)

        self.button = self.findChild(QtWidgets.QPushButton, 'A_Button')
        self.button.clicked.connect(Piano.value_A)
        
        self.button = self.findChild(QtWidgets.QPushButton, 'GSharp_Button')
        self.button.clicked.connect(Piano.value_Gs)

        self.button = self.findChild(QtWidgets.QPushButton, 'G_Button')
        self.button.clicked.connect(Piano.value_G)

        self.button = self.findChild(QtWidgets.QPushButton, 'FSharp_Button')
        self.button.clicked.connect(Piano.value_Fs)

        self.button = self.findChild(QtWidgets.QPushButton, 'F_Button')
        self.button.clicked.connect(Piano.value_F)

        self.button = self.findChild(QtWidgets.QPushButton, 'E_Button')
        self.button.clicked.connect(Piano.value_E)

        self.button = self.findChild(QtWidgets.QPushButton, 'DSharp_Button')
        self.button.clicked.connect(Piano.value_Ds)
        
        self.button = self.findChild(QtWidgets.QPushButton, 'D_Button')
        self.button.clicked.connect(Piano.value_D)
        
        self.button = self.findChild(QtWidgets.QPushButton, 'CSharp_Button')
        self.button.pressed.connect(Piano.value_Cs)

        self.button = self.findChild(QtWidgets.QPushButton, 'LowC_Button')
        self.button.clicked.connect(Piano.value_LowC)
    
    
   #Plaies a node when pressing a keyboard key 
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Z: 
            Piano.value_HighC()
        elif event.key() == Qt.Key_X:
            Piano.value_B()
        elif event.key() == Qt.Key_C:
            Piano.value_As()
        elif event.key() == Qt.Key_V:
            Piano.value_A()
        elif event.key() == Qt.Key_B:
            Piano.value_Gs()
        elif event.key() == Qt.Key_N:
            Piano.value_G()




app = QtWidgets.QApplication(sys.argv) 
window = Ui()
app.exec_()



    
    
    
    
    
