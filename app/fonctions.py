# Nom de l'auteur : Michaël Boucher
# Date de création : 19 septembre 2023
# Copyright (c) 2023 Michaël Boucher. Tous droits réservés.
# fonctions.py

import configparser
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

# Fonction pour afficher un message indiquant qu'une fonctionnalité n'est pas encore implémentée
def function_not_available(self):
    try:
        # Vérifiez si l'option "Toujours afficher par-dessus les autres applications" est activée
        always_on_top_checked = self.always_on_top

        # Désactivez temporairement l'option "Toujours afficher par-dessus les autres applications"
        self.toggle_always_on_top(Qt.Unchecked)

        # Crée une boîte de dialogue d'information
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setWindowTitle("Fonctionnalité non implémentée")
        message_box.setText("Cette fonctionnalité n'a pas encore été implémentée. Veuillez attendre la prochaine mise à jour.")

        # Utilisez Qt.WindowStaysOnTopHint pour forcer la boîte de dialogue à rester au-dessus de la fenêtre principale
        message_box.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)

        message_box.exec_()

        # Réactivez l'option "Toujours afficher par-dessus les autres applications" si elle était activée auparavant
        if always_on_top_checked:
            self.toggle_always_on_top(Qt.Checked)
    except Exception as e:
        print(f"Erreur dans function_not_available : {str(e)}")

# Fonction pour démarrer l'importation (cette fonction peut être remplacée lorsque l'importation réelle est implémentée)
def start_import(self):
    try:
        return function_not_available(self)
    except Exception as e:
        print(f"Erreur dans start_import : {str(e)}")

# Fonction pour sauvegarder les options de l'application
def save_options(executable_location, always_on_top, enable_logging):
    try:
        # Créez un objet ConfigParser pour gérer la configuration
        config = configparser.ConfigParser()

        # Créez ou ouvrez le fichier de configuration
        config.read('config.ini')

        # Ajoutez ou mettez à jour les paramètres dans la section "Options"
        if not config.has_section('Options'):
            config.add_section('Options')

        config.set('Options', 'ExecutableLocation', executable_location)
        config.set('Options', 'AlwaysOnTop', str(always_on_top))
        config.set('Options', 'EnableLogging', str(enable_logging))

        # Écrivez les modifications dans le fichier
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    except Exception as e:
        print(f"Erreur dans save_options : {str(e)}")

# Fonction pour charger les options de l'application
def load_options():
    try:
        # Créez un objet ConfigParser pour gérer la configuration
        config = configparser.ConfigParser()

        # Lisez le fichier de configuration
        config.read('config.ini')

        # Récupérez les valeurs des paramètres
        if config.has_section('Options'):
            executable_location = config.get('Options', 'ExecutableLocation')
            always_on_top = config.getboolean('Options', 'AlwaysOnTop')
            enable_logging = config.getboolean('Options', 'EnableLogging')
        else:
            # Valeurs par défaut si la section n'existe pas
            executable_location = ''
            always_on_top = False
            enable_logging = False

        return executable_location, always_on_top, enable_logging
    except Exception as e:
        print(f"Erreur dans load_options : {str(e)}")