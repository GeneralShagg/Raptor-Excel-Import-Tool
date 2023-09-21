# Nom de l'auteur : Michaël Boucher
# Date de création : 19 septembre 2023
# Copyright (c) 2023 Michaël Boucher. Tous droits réservés.
# raptor.py

import logging
import pygetwindow as gw
from PyQt5.QtWidgets import QMessageBox

def check_and_open_raptor():
    raptor_win = get_raptor_window()
    
    if raptor_win is not None:
        return True  # Raptor est en cours d'exécution
    else:
        reply = QMessageBox()
        reply.setWindowTitle("Raptor n'est pas en cours d'exécution")
        reply.setText("Voulez-vous ouvrir Raptor?")
        reply.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        
        result = reply.exec_()  # Affiche le dialogue et attend la réponse de l'utilisateur

        if result == QMessageBox.Yes:
            # Code pour ouvrir Raptor ici (vous devrez ajouter cette fonctionnalité)
            pass  # Remplacez par le code pour ouvrir Raptor

        return False  # Raptor n'est pas en cours d'exécution

def is_raptor_open():
    """
    Vérifie si l'application Raptor est ouverte. Si elle est fermée, propose de l'ouvrir.
    
    Returns:
        bool: True si Raptor est ouvert, False sinon.
    """
    return check_and_open_raptor()

def get_raptor_window():
    try:
        raptor_win = gw.getWindowsWithTitle("Raptor 2023")  # Titre complet de la fenêtre Raptor
        return raptor_win[0] if len(raptor_win) > 0 else None
    except Exception as e:
        logging.error(f"Erreur lors de la recherche de la fenêtre de Raptor : {str(e)}")
        return None

def select_raptor_window():
    try:
        # Cherchez la fenêtre de Raptor par le titre complet
        raptor_window = get_raptor_window()
        
        if raptor_window:
            # Activez la fenêtre trouvée
            raptor_window.activate()
            logging.info(f"Fenêtre de Raptor '{raptor_window.title}' trouvée et sélectionnée")
            print(f"Fenêtre de Raptor '{raptor_window.title}' trouvée et sélectionnée")  # Ajoutez cette ligne pour afficher un message
            return True
        else:
            logging.info("Fenêtre de Raptor non trouvée")
            print("Fenêtre de Raptor non trouvée")  # Ajoutez cette ligne pour afficher un message
            return False
    except Exception as e:
        # Gérer les erreurs éventuelles lors de la sélection de la fenêtre
        logging.error(f"Erreur lors de la sélection de la fenêtre de Raptor : {str(e)}")
        return False

def maximize_raptor():
    try:
        # Cherchez la fenêtre de Raptor par le titre complet
        raptor_window = get_raptor_window()
        
        if raptor_window:
            # Maximisez la fenêtre trouvée
            raptor_window.restore()
            raptor_window.maximize()
            logging.info(f"Fenêtre de Raptor '{raptor_window.title}' trouvée et maximisée avec succès")
            print(f"Fenêtre de Raptor '{raptor_window.title}' trouvée et maximisée avec succès")  # Ajoutez cette ligne pour afficher un message
            return True
        else:
            logging.info("Fenêtre de Raptor non trouvée")
            print("Fenêtre de Raptor non trouvée")  # Ajoutez cette ligne pour afficher un message
            return False
    except Exception as e:
        # Gérer les erreurs éventuelles lors de la maximisation de la fenêtre
        logging.error(f"Erreur lors de la maximisation de la fenêtre de Raptor : {str(e)}")
        return False

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def is_raptor_open():
#    raptor_win = get_raptor_window()
#    return raptor_win is not None    