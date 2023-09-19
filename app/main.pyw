# main.py
import sys
from PyQt5.QtWidgets import QApplication
from interface import Application
from PyQt5.QtGui import QIcon

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    
    # Définissez l'icône de l'application
    app_icon = QIcon("C:/Users/user18/Documents/IER/IER-v0.5/assets/images/ico.ico")  # Utilisez le chemin complet
    app.setWindowIcon(app_icon)

    window.show()
    sys.exit(app.exec_())
