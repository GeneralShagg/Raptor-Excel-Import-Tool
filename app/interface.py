from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMainWindow, QGridLayout, QCheckBox, QLineEdit, QHBoxLayout, QLabel, QFileDialog, QStackedWidget, QMessageBox
from PyQt5.QtCore import Qt
from styles import button_styles, app_style, white_text

class Application(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Raptor Import")
        self.setFixedSize(450, 155)  # Empêche le redimensionnement initial

        main_layout = QVBoxLayout()

        self.stacked_widget = QStackedWidget()

        # Créez des widgets pour les différentes pages
        self.page_main = QWidget()
        self.page_options = QWidget()

        self.stacked_widget.addWidget(self.page_main)
        self.stacked_widget.addWidget(self.page_options)

        self.create_main_page()
        self.create_options_page()

        main_layout.addWidget(self.stacked_widget)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        central_widget.setStyleSheet(app_style)  # Appliquez le style du fond d'application

        self.setCentralWidget(central_widget)

        # Variable pour indiquer si vous êtes dans la page d'options ou non
        self.in_options_page = False
        
        # Créez un label pour le copyright
        copyright_label = QLabel("© 2023 Michael Boucher. Tous droits réservés.")

        # Créez un style pour le label de copyright (blanc)
        copyright_style = "color: white; font-size: 10px;"

        # Appliquez le style au label de copyright
        copyright_label.setStyleSheet(copyright_style)

        # Ajoutez le label de copyright au bas de chaque page
        main_layout.addWidget(copyright_label)
        
        # Variable pour indiquer si la fenêtre doit rester par dessus les autres applications ou non.
        self.always_on_top = False  # Variable pour stocker l'état de la case à cocher

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

        # Appliquez le style aux boutons
        btn_open.setStyleSheet(button_styles["excel"])  # Style Excel (vert)
        btn_create.setStyleSheet(button_styles["excel"])  # Style Excel (vert)
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

        # Emplacement de l'exécutable de Raptor
        raptor_executable_label = QLabel("Emplacement de l'exécutable de Raptor:")
        self.raptor_executable_edit = QLineEdit()
        self.raptor_executable_edit.setPlaceholderText("Sélectionnez l'emplacement de Raptor...")
        browse_button = QPushButton("Parcourir")
        browse_button.clicked.connect(self.browse_raptor_executable)
        
        # Créez un style pour la case à cocher (blanc)
        checkbox_style = "QCheckBox { color: white; }"
        
        # Appliquez le style au bouton "Parcourir"
        browse_button.setStyleSheet(white_text)

        # Appliquez le style de texte blanc au label et à la boîte d'édition
        raptor_executable_label.setStyleSheet("color: white;")
        self.raptor_executable_edit.setStyleSheet("color: white;")
        
        # Case à cocher pour toujours afficher la fenêtre par-dessus les autres applications
        always_on_top_checkbox = QCheckBox("Toujours afficher par-dessus les autres applications")
        always_on_top_checkbox.stateChanged.connect(self.toggle_always_on_top)
        
        # Appliquez le style à la case à cocher
        always_on_top_checkbox.setStyleSheet(checkbox_style)

        # Créez la case à cocher "Activer les logs"
        log_checkbox = QCheckBox("Activer les logs")

        # Appliquez le style à la case à cocher
        log_checkbox.setStyleSheet(checkbox_style)

        # Bouton pour enregistrer les options
        save_button = QPushButton('Enregistrer', self)
        save_button.clicked.connect(self.save_options)

        # Bouton pour retourner à la page principale
        back_button = QPushButton('Retour', self)
        back_button.clicked.connect(self.toggle_options)

        # Appliquez le style aux nouveaux boutons
        save_button.setStyleSheet(button_styles["default"])
        back_button.setStyleSheet(button_styles["default"])

        # Créez un QHBoxLayout pour les boutons "Enregistrer" et "Retour"
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(save_button)
        buttons_layout.addWidget(back_button)

        # Ajoutez les widgets à la mise en page
        layout.addWidget(raptor_executable_label)
        layout.addWidget(self.raptor_executable_edit)
        layout.addWidget(browse_button)
        layout.addWidget(always_on_top_checkbox)
        layout.addWidget(log_checkbox)
        layout.addLayout(buttons_layout)  # Ajoutez le QHBoxLayout à la mise en page

        self.page_options.setLayout(layout)

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
            self.setFixedSize(500, 225)  # Changez la taille en 550x255
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
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setWindowTitle("Fonctionnalité non implémentée")
        message_box.setText("Cette fonctionnalité n'a pas encore été implémentée. Veuillez attendre la prochaine mise à jour.")
        message_box.exec_()

    def create_excel(self):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setWindowTitle("Fonctionnalité non implémentée")
        message_box.setText("Cette fonctionnalité n'a pas encore été implémentée. Veuillez attendre la prochaine mise à jour.")
        message_box.exec_()

    def start_import(self):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setWindowTitle("Fonctionnalité non implémentée")
        message_box.setText("Cette fonctionnalité n'a pas encore été implémentée. Veuillez attendre la prochaine mise à jour.")
        message_box.exec_()

    def save_options(self):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setWindowTitle("Fonctionnalité non implémentée")
        message_box.setText("Cette fonctionnalité n'a pas encore été implémentée. Veuillez attendre la prochaine mise à jour.")
        message_box.exec_()
