# Nom de l'auteur : Michaël Boucher
# Date de création : 19 septembre 2023
# Copyright (c) 2023 Michaël Boucher. Tous droits réservés.
# fonctions.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
    

        
def fonction_not_available(self):
    # Vérifiez si l'option "Toujours afficher par-dessus les autres applications" est activée
    always_on_top_checked = self.always_on_top

    # Désactivez temporairement l'option "Toujours afficher par-dessus les autres applications"
    self.toggle_always_on_top(Qt.Unchecked)

    message_box = QMessageBox()
    message_box.setIcon(QMessageBox.Information)
    message_box.setWindowTitle("Fonctionnalité non implémentée")
    message_box.setText("Cette fonctionnalité n'a pas encore été implémentée. Veuillez attendre la prochaine mise à jour.")
    
    # Définissez la modalité de la fenêtre d'erreur pour qu'elle soit une fenêtre d'application modale
    message_box.setWindowModality(Qt.ApplicationModal)

    # Utilisez Qt.WindowStaysOnTopHint pour forcer la boîte de dialogue à rester au-dessus de la fenêtre principale
    message_box.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)

    message_box.exec_()

    # Réactivez l'option "Toujours afficher par-dessus les autres applications" si elle était activée auparavant
    if always_on_top_checked:
        self.toggle_always_on_top(Qt.Checked)
        

def start_import(self):
    return fonction_not_available(self)       
        
def save_options(self):
    return fonction_not_available(self)
