# Nom de l'auteur : Michaël Boucher
# Date de création : 19 septembre 2023
# Copyright (c) 2023 Michaël Boucher. Tous droits réservés.
# interface.py

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog,
    QCheckBox, QHBoxLayout, QMessageBox, QStackedWidget, QGridLayout, QDialog
)
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from styles import button_styles, app_style, white_text, white_edit_background
from fonctions import open_excel, create_excel, start_import, save_options
from version import APP_NAME, APP_VERSION, APP_AUTHOR, APP_COPYRIGHT, APP_DEV, APP_PROD


class HelpWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aide Raptor Import")
        self.setFixedSize(800, 600)

        # Créez un widget QWebEngineView pour afficher le contenu HTML
        self.webview = QWebEngineView(self)
        self.webview.setGeometry(0, 0, 800, 600)

        # Chargez le fichier HTML dans le widget QWebEngineView
        self.webview.setHtml(open('help.html').read())

        back_button = QPushButton('Retour', self)
        back_button.setGeometry(10, 10, 75, 30)
        back_button.clicked.connect(self.close)

class Application(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"{APP_NAME} v{APP_VERSION} {APP_DEV}")
        self.setFixedSize(450, 155)
        self.in_options_page = False
        
        self.help_window = None  # Gardez une référence à la fenêtre d'aide
        
        main_layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        central_widget.setStyleSheet(app_style)
        self.setCentralWidget(central_widget)

        self.stacked_widget = QStackedWidget()
        self.page_main = QWidget()
        self.page_options = QWidget()

        self.stacked_widget.addWidget(self.page_main)
        self.stacked_widget.addWidget(self.page_options)

        main_layout.addWidget(self.stacked_widget)

        self.create_main_page()
        self.create_options_page()

        copyright_label = QLabel(f"{APP_COPYRIGHT}")
        copyright_label.setStyleSheet("color: white; font-size: 10px;")
        main_layout.addWidget(copyright_label)

    def create_main_page(self):
        layout = QVBoxLayout()
        grid_layout = QGridLayout()

        btn_open = QPushButton('Ouvrir le fichier Excel', self)
        btn_create = QPushButton('Créer le fichier Excel', self)
        btn_start_import = QPushButton("Démarrer l'importation", self)
        btn_options = QPushButton('Options', self)

        btn_open.clicked.connect(self.open_excel)
        btn_create.clicked.connect(self.create_excel)
        btn_start_import.clicked.connect(self.start_import)
        btn_options.clicked.connect(self.toggle_options)

        btn_open.setStyleSheet(button_styles["excel"])
        btn_create.setStyleSheet(button_styles["excel"])
        btn_start_import.setStyleSheet(button_styles["start_import"])
        btn_options.setStyleSheet(button_styles["option"])

        grid_layout.addWidget(btn_open, 0, 0)
        grid_layout.addWidget(btn_create, 0, 1)
        grid_layout.addWidget(btn_start_import, 1, 0)
        grid_layout.addWidget(btn_options, 1, 1)

        layout.addLayout(grid_layout)
        self.page_main.setLayout(layout)

    def create_options_page(self):
        layout = QVBoxLayout()

        raptor_executable_label = QLabel("Emplacement de l'exécutable de Raptor:")
        self.raptor_executable_edit = QLineEdit()
        self.raptor_executable_edit.setPlaceholderText("Sélectionnez l'emplacement de Raptor...")
        browse_button = QPushButton("Parcourir")
        browse_button.clicked.connect(self.browse_raptor_executable)

        checkbox_style = "QCheckBox { color: white; }"

        browse_button.setStyleSheet(white_text)
        raptor_executable_label.setStyleSheet(white_text)
        self.raptor_executable_edit.setStyleSheet(white_edit_background)

        always_on_top_checkbox = QCheckBox("Toujours afficher par-dessus les autres applications")
        always_on_top_checkbox.stateChanged.connect(self.toggle_always_on_top)
        always_on_top_checkbox.setStyleSheet(checkbox_style)

        log_checkbox = QCheckBox("Activer les logs")
        log_checkbox.setStyleSheet(checkbox_style)

        save_button = QPushButton('Enregistrer', self)
        save_button.clicked.connect(self.save_options)
        back_button = QPushButton('Retour', self)
        back_button.clicked.connect(self.toggle_options)

        help_button = QPushButton('Aide', self)  # Bouton d'aide
        help_button.clicked.connect(self.show_help)  # Affichez la page d'aide dans une nouvelle fenêtre

        # Utilisez les styles définis dans styles.py pour les boutons de la page Options
        save_button.setStyleSheet(button_styles["excel"])
        back_button.setStyleSheet(button_styles["option"])
        help_button.setStyleSheet(button_styles["start_import"])

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(save_button)
        buttons_layout.addWidget(help_button)
        buttons_layout.addWidget(back_button)

        layout.addWidget(raptor_executable_label)
        layout.addWidget(self.raptor_executable_edit)
        layout.addWidget(browse_button)
        layout.addWidget(always_on_top_checkbox)
        layout.addWidget(log_checkbox)
        layout.addLayout(buttons_layout)  # Ajoutez le bouton d'aide au layout des boutons

        self.page_options.setLayout(layout)

    def show_help(self):
        if self.help_window is None:
            # Si la fenêtre d'aide n'existe pas encore, créez-la
            self.help_window = HelpWindow()

        # Ouvrez la fenêtre d'aide en utilisant exec_()
        self.help_window.exec_()

    def show_main_page(self):
        # Retournez au menu principal depuis n'importe quelle page
        self.stacked_widget.setCurrentWidget(self.page_main)

    def keyPressEvent(self, event):
        # Capturez l'appui sur la touche F1 pour afficher la page d'aide
        if event.key() == Qt.Key_F1:
            self.show_help()
        else:
            super().keyPressEvent(event)

    def browse_raptor_executable(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog(self)
        file_dialog.setOptions(options)
        file_dialog.setNameFilter("Raptor Executable (*.exe)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.raptor_executable_edit.setText(selected_files[0])

    def toggle_options(self):
        if self.in_options_page:
            # Masquez les options
            self.setFixedSize(450, 155)  # Revenez à la taille d'origine 450x155
            self.stacked_widget.setCurrentWidget(self.page_main)
        else:
            # Affichez les options et agrandissez la fenêtre
            self.setFixedSize(500, 225)  # Changez la taille en 500x225
            self.stacked_widget.setCurrentWidget(self.page_options)
        self.in_options_page = not self.in_options_page

    def toggle_always_on_top(self, state):
        if state == Qt.Checked:
            self.always_on_top = True
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.show()
        else:
            self.always_on_top = False
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
            self.show()

    def open_excel(self):
        # Utilisez la fonction open_excel du fichier fonctions.py
        open_excel(self)

    def create_excel(self):
        # Utilisez la fonction create_excel du fichier fonctions.py
        create_excel(self)

    def start_import(self):
        # Utilisez la fonction start_import du fichier fonctions.py
        start_import(self)

    def save_options(self):
        # Utilisez la fonction save_options du fichier fonctions.py
        save_options(self)
