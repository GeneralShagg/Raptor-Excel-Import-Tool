# Nom de l'auteur : Michaël Boucher
# Date de création : 19 septembre 2023
# Copyright (c) 2023 Michaël Boucher. Tous droits réservés.
# interface.py

# Imports des bibliothèques tierces
from PyQt5.QtCore import Qt  # Importe le module Qt de PyQt5 pour gérer les fonctionnalités de base.
from PyQt5.QtWebEngineWidgets import QWebEngineView  # Importe le widget QWebEngineView pour afficher du contenu Web.
from PyQt5.QtWidgets import (  # Importe divers composants d'interface utilisateur de PyQt5.
    QCheckBox, QDialog, QFileDialog, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMessageBox, QPushButton, QStackedWidget,
    QVBoxLayout, QWidget
)

# Imports de fonctions locales
from excel import create_excel, open_excel  # Importe des fonctions pour travailler avec Excel.
from fonctions import load_options, save_options, start_import  # Importe des fonctions utilitaires.
from raptor import get_raptor_window, is_raptor_open, maximize_raptor, select_raptor_window  # Importe des fonctions pour interagir avec Raptor.
from styles import app_style, button_styles, white_edit_background, white_text  # Importe des styles d'interface utilisateur.
from version import APP_AUTHOR, APP_COPYRIGHT, APP_DEV, APP_NAME, APP_PROD, APP_VERSION  # Importe des informations de version de l'application.

# Définition de la fenêtre d'aide
class HelpWindow(QDialog):
    def __init__(self):
        super().__init__()

        # Configure la fenêtre d'aide
        self.setWindowTitle("Aide Raptor Import")  # Définit le titre de la fenêtre d'aide.
        self.setFixedSize(800, 600)  # Fixe la taille de la fenêtre d'aide à 800x600 pixels.

        # Crée une vue WebEngine pour afficher le contenu HTML de l'aide.
        self.webview = QWebEngineView(self)
        self.webview.setGeometry(0, 0, 800, 600)  # Positionne la vue WebEngine dans la fenêtre.

        # Charge le contenu HTML de l'aide depuis un fichier.
        with open('help.html', 'r') as file:
            self.webview.setHtml(file.read())

        # Crée un bouton "Retour" pour fermer la fenêtre d'aide.
        back_button = QPushButton('Retour', self)
        back_button.setGeometry(10, 10, 100, 35)  # Positionne et dimensionne le bouton.
        back_button.clicked.connect(self.close)  # Connecte le clic sur le bouton à la fermeture de la fenêtre.
        back_button.setStyleSheet(button_styles["option"])  # Applique un style au bouton.

# Page principale de l'application
class MainPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # Crée un layout vertical pour organiser les éléments de l'interface utilisateur.
        layout = QVBoxLayout()

        # Crée un layout de grille pour organiser les boutons en deux lignes et deux colonnes.
        grid_layout = QGridLayout()

        # Crée quatre boutons pour les actions principales de l'application.
        btn_open = QPushButton('Ouvrir le fichier Excel', self)
        btn_create = QPushButton('Créer le fichier Excel', self)
        btn_start_import = QPushButton("Démarrer l'importation", self)
        btn_options = QPushButton('Options', self)

        # Associe des actions aux boutons en connectant les clics à des fonctions spécifiques.
        btn_open.clicked.connect(self.parent().open_excel)
        btn_create.clicked.connect(self.parent().create_excel)
        btn_start_import.clicked.connect(self.parent().start_import)
        btn_options.clicked.connect(self.parent().toggle_options)

        # Applique des styles différents aux boutons.
        btn_open.setStyleSheet(button_styles["excel"])
        btn_create.setStyleSheet(button_styles["excel"])
        btn_start_import.setStyleSheet(button_styles["start_import"])
        btn_options.setStyleSheet(button_styles["option"])

        # Place les boutons dans le layout de grille.
        grid_layout.addWidget(btn_open, 0, 0)  # Bouton "Ouvrir le fichier Excel" en haut à gauche.
        grid_layout.addWidget(btn_create, 0, 1)  # Bouton "Créer le fichier Excel" en haut à droite.
        grid_layout.addWidget(btn_start_import, 1, 0)  # Bouton "Démarrer l'importation" en bas à gauche.
        grid_layout.addWidget(btn_options, 1, 1)  # Bouton "Options" en bas à droite.

        # Ajoute le layout de grille au layout vertical.
        layout.addLayout(grid_layout)
        self.setLayout(layout)

# Page des options de l'application
class OptionsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # Crée un layout vertical pour organiser les éléments de l'interface utilisateur.
        layout = QVBoxLayout()

        # Crée une étiquette pour afficher le texte relatif à l'emplacement de l'exécutable de Raptor.
        raptor_executable_label = QLabel("Emplacement de l'exécutable de Raptor:")

        # Crée un champ de texte pour saisir ou afficher l'emplacement de l'exécutable de Raptor.
        self.raptor_executable_edit = QLineEdit()
        self.raptor_executable_edit.setPlaceholderText("Sélectionnez l'emplacement de Raptor...")

        # Crée un bouton "Parcourir" pour rechercher l'exécutable de Raptor.
        browse_button = QPushButton("Parcourir")
        browse_button.clicked.connect(self.parent().browse_raptor_executable)

        # Définit un style pour les cases à cocher.
        checkbox_style = "QCheckBox { color: white; }"

        # Applique des styles à certains éléments de l'interface utilisateur.
        browse_button.setStyleSheet(white_text)  # Applique un style au bouton "Parcourir".
        raptor_executable_label.setStyleSheet(white_text)  # Applique un style à l'étiquette.
        self.raptor_executable_edit.setStyleSheet(white_edit_background)  # Applique un style au champ de texte.

        # Crée une case à cocher pour activer/désactiver l'option "Toujours afficher par-dessus les autres applications".
        always_on_top_checkbox = QCheckBox("Toujours afficher par-dessus les autres applications")
        always_on_top_checkbox.stateChanged.connect(self.parent().toggle_always_on_top)
        always_on_top_checkbox.setStyleSheet(checkbox_style)  # Applique le style défini.

        # Crée une case à cocher pour activer/désactiver l'option "Activer les logs".
        log_checkbox = QCheckBox("Activer les logs")
        log_checkbox.setStyleSheet(checkbox_style)  # Applique le style défini.

        # Crée un bouton "Enregistrer" pour sauvegarder les options.
        save_button = QPushButton('Enregistrer', self)
        save_button.clicked.connect(self.parent().save_options)

        # Crée un bouton "Retour" pour revenir à la page principale.
        back_button = QPushButton('Retour', self)
        back_button.clicked.connect(self.parent().toggle_options)

        # Crée un bouton "Aide" pour afficher l'aide.
        help_button = QPushButton('Aide', self)
        help_button.clicked.connect(self.parent().show_help)

        # Applique des styles différents aux boutons.
        save_button.setStyleSheet(button_styles["excel"])
        back_button.setStyleSheet(button_styles["option"])
        help_button.setStyleSheet(button_styles["start_import"])

        # Crée un layout horizontal pour organiser les boutons "Enregistrer", "Aide" et "Retour".
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(save_button)
        buttons_layout.addWidget(help_button)
        buttons_layout.addWidget(back_button)

        # Ajoute les éléments à la page des options.
        layout.addWidget(raptor_executable_label)  # Ajoute l'étiquette de l'emplacement de l'exécutable.
        layout.addWidget(self.raptor_executable_edit)  # Ajoute le champ de texte pour l'emplacement.
        layout.addWidget(browse_button)  # Ajoute le bouton "Parcourir".
        layout.addWidget(always_on_top_checkbox)  # Ajoute la case à cocher "Toujours afficher par-dessus".
        layout.addWidget(log_checkbox)  # Ajoute la case à cocher "Activer les logs".
        layout.addLayout(buttons_layout)  # Ajoute le layout horizontal avec les boutons.

        self.setLayout(layout)

# Classe principale de l'application
class Application(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configure la fenêtre principale de l'application.
        self.setWindowTitle(f"{APP_NAME} v{APP_VERSION} {APP_DEV}")  # Définit le titre de la fenêtre.
        self.setFixedSize(450, 155)  # Fixe la taille de la fenêtre.

        # Initialise des variables pour les options de l'application en les chargeant depuis un fichier.
        self.in_options_page = False
        self.executable_location, self.always_on_top, self.enable_logging = load_options()

        # Initialise l'interface utilisateur.
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()  # Crée un widget central pour la fenêtre.
        central_widget.setStyleSheet(app_style)  # Applique un style au widget central.
        self.setCentralWidget(central_widget)  # Définit le widget central de la fenêtre.

        main_layout = QVBoxLayout(central_widget)  # Crée un layout vertical pour le widget central.

        self.stacked_widget = QStackedWidget()  # Crée un widget empilé pour gérer les pages.
        self.page_main = MainPage(self)  # Crée la page principale.
        self.page_options = OptionsPage(self)  # Crée la page des options.

        self.stacked_widget.addWidget(self.page_main)  # Ajoute la page principale au widget empilé.
        self.stacked_widget.addWidget(self.page_options)  # Ajoute la page des options au widget empilé.
        main_layout.addWidget(self.stacked_widget)  # Ajoute le widget empilé au layout principal.

        copyright_label = QLabel(f"{APP_COPYRIGHT}")  # Crée une étiquette pour le copyright.
        copyright_label.setStyleSheet("color: white; font-size: 10px;")  # Applique un style à l'étiquette du copyright.
        main_layout.addWidget(copyright_label)  # Ajoute l'étiquette du copyright au layout principal.

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:  # Si la touche F1 est pressée.
            self.show_help()  # Affiche l'aide.
        else:
            super().keyPressEvent(event)  # Appelle la méthode de la classe parente pour gérer l'événement.

    def show_help(self):
        always_on_top_checked = self.always_on_top

        self.toggle_always_on_top(Qt.Unchecked)  # Désactive temporairement l'option "toujours au premier plan".

        help_window = HelpWindow()  # Crée une fenêtre d'aide.
        help_window.exec_()  # Affiche la fenêtre d'aide en mode modal.

        if always_on_top_checked:
            self.toggle_always_on_top(Qt.Checked)  # Réactive l'option "toujours au premier plan".

    def toggle_always_on_top(self, state):
        if state == Qt.Checked:  # Si la case à cocher est cochée.
            self.always_on_top = True
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)  # Définit l'application comme toujours au premier plan.
        else:
            self.always_on_top = False
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)  # Désactive l'option "toujours au premier plan".

        self.show()  # Actualise l'affichage de la fenêtre.

    def toggle_options(self):
        if self.in_options_page:
            self.in_options_page = False
            self.setWindowTitle(f"{APP_NAME} v{APP_VERSION} {APP_DEV}")
            self.setFixedSize(450, 155)  # Redimensionne à 450x155.
            self.stacked_widget.setCurrentWidget(self.page_main)
        else:
            self.in_options_page = True
            self.setWindowTitle("Options")
            self.setFixedSize(500, 225)  # Redimensionne à 500x225.
            self.stacked_widget.setCurrentWidget(self.page_options)

    def save_options(self):
        self.executable_location = self.page_options.raptor_executable_edit.text()
        save_options(self.executable_location, self.always_on_top, self.enable_logging)  # Enregistre les options.

    def browse_raptor_executable(self):
        # Ouvre une boîte de dialogue pour sélectionner l'emplacement de l'exécutable de Raptor.
        file_name, _ = QFileDialog.getOpenFileName(self, 'Ouvrir Raptor', '', 'Exécutables (*.exe);;Tous les fichiers (*)')
        if file_name:
            self.page_options.raptor_executable_edit.setText(file_name)

    # Les méthodes suivantes sont des stubs. Vous devriez implémenter ces méthodes avec la logique appropriée.
    def open_excel(self):
        open_excel()  # Ouvre le fichier Excel.

    def create_excel(self):
        create_excel(self)  # Crée le fichier Excel.

    def start_import(self):
        start_import(self)  # Démarre l'importation.
