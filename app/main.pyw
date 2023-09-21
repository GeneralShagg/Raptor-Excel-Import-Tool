# Nom de l'auteur : Michaël Boucher
# Date de création : 19 septembre 2023
# Copyright (c) 2023 Michaël Boucher. Tous droits réservés.
# main.pyw

import sys
import os
from PyQt5.QtWidgets import QApplication
from interface import Application
from PyQt5.QtGui import QIcon
from version import APP_NAME, APP_VERSION, APP_AUTHOR, APP_COPYRIGHT
from raptor import is_raptor_open, get_raptor_window, select_raptor_window, maximize_raptor

if __name__ == "__main__":
    # Obtenez le répertoire du fichier main.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Chemin relatif vers l'icône depuis le répertoire de base
    icon_relative_path = "../assets/images/ico.ico"
    
    app = QApplication(sys.argv)
    window = Application()
    is_open = is_raptor_open()
    
    # Créez le chemin absolu vers l'icône en joignant le chemin de base avec le chemin relatif
    icon_path = os.path.join(base_dir, icon_relative_path)
    
    # Définissez l'icône de l'application en utilisant le chemin absolu
    app_icon = QIcon(icon_path)
    app.setWindowIcon(app_icon)
    
    window.show()
    sys.exit(app.exec_())