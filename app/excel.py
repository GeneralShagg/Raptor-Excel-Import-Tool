# Nom de l'auteur : Michaël Boucher
# Date de création : 19 septembre 2023
# Copyright (c) 2023 Michaël Boucher. Tous droits réservés.
# fonctions.py

import os
import xlsxwriter
import pygetwindow as gw
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

def open_excel():
    excel_file = "RaptorImport.xlsx"

    if os.path.exists(excel_file):
        os.startfile(excel_file)
        print(f"Fichier Excel '{excel_file}' ouvert avec succès.")
    else:
        error_message = (
            "Le fichier Excel 'RaptorImport.xlsx' n'a pas été trouvé. "
            "Vous pouvez créer le fichier à l'aide du bouton \"Créer un fichier Excel\"."
        )
        print(error_message)  # Imprimer dans la console (pour un futur fichier log)

        # Afficher un message d'erreur à l'utilisateur
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Critical)
        message_box.setWindowTitle("Erreur")
        message_box.setText(error_message)
        message_box.exec_()
        
def is_excel_window_open(window_name):
    try:
        window = gw.getWindowsWithTitle(window_name)
        if window:
            return True
        return False
    except Exception as e:
        return False

def create_excel(app_instance):
    # Vérifiez si le fichier existe déjà
    excel_file = "RaptorImport.xlsx"
    
    # Vérifiez si la fenêtre Excel avec le nom du fichier est ouverte
    if is_excel_window_open(excel_file):
        error_message = f"Vous devez fermer la fenêtre Excel '{excel_file}' avant de pouvoir le recréer."
        print(error_message)  # Imprimer dans la console (pour un futur fichier log)

        # Si l'option "Toujours afficher par-dessus les autres applications" est activée, demandez à l'utilisateur de la désactiver temporairement
        if app_instance.always_on_top_enabled:
            app_instance.toggle_always_on_top(Qt.Unchecked)
            message_box = QMessageBox(parent=app_instance)  # Spécifiez le parent ici
            message_box.setIcon(QMessageBox.Information)
            message_box.setWindowTitle("Option désactivée temporairement")
            message_box.setText("Pour afficher ce message, veuillez désactiver temporairement l'option "
                                "\"Toujours afficher par-dessus les autres applications\".")
            message_box.exec_()

        # Afficher un message d'erreur à l'utilisateur
        message_box = QMessageBox(parent=app_instance)  # Spécifiez le parent ici
        message_box.setIcon(QMessageBox.Critical)
        message_box.setWindowTitle("Erreur")
        message_box.setText(error_message)
        message_box.exec_()

        # Réactivez l'option "Toujours afficher par-dessus les autres applications" si elle était activée auparavant
        if app_instance.always_on_top_enabled:
            app_instance.toggle_always_on_top(Qt.Checked)
        return

    if os.path.exists(excel_file):
        # Si le fichier existe, demandez à l'utilisateur s'il souhaite le remplacer
        message_box = QMessageBox(parent=app_instance)  # Spécifiez le parent ici
        message_box.setIcon(QMessageBox.Question)
        message_box.setWindowTitle("Fichier existant")
        message_box.setText("Le fichier 'RaptorImport.xlsx' existe déjà. Voulez-vous le remplacer ?")
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        response = message_box.exec_()

        if response == QMessageBox.No:
            return  # Arrêtez la création du fichier si l'utilisateur ne souhaite pas le remplacer

    try:
        # Créez un classeur Excel avec xlsxwriter
        workbook = xlsxwriter.Workbook('RaptorImport.xlsx')

        # Créez une feuille de calcul
        worksheet = workbook.add_worksheet('RaptorImport')

        # Ajoutez une liste de validation avec des options visibles
        options = ["Construction Lines", "Construction Points", "Holes Singles", "Pop Marks"]
        worksheet.write('B3', "Sélectionnez une option :")
        worksheet.data_validation('B3', {'validate': 'list',
                                         'source': options,
                                         'input_message': "Choisissez une option dans la liste"})

        # Ajoutez du contenu à la feuille de calcul
        data = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
            [1, "Données à entrer", "Length", "Part Name", "Side", "Reference Location", "Abs-X-Dim", "Inc-X-Dim", "Rev-X-Dim", "Gage", "Type", "Diameter", "Oval Length", "Oval Angle"],
        ]

        # Remplissez les autres lignes avec les données numériques
        for i in range(2, 100):
            data.append([i])

        # Assurez-vous que chaque ligne a le même nombre d'éléments que la première ligne
        max_columns = len(data[0])
        for row in data:
            while len(row) < max_columns:
                row.append("")  # Ajoutez des chaînes vides pour combler les vides

        # Écrivez les données dans la feuille de calcul
        for row_index, row_data in enumerate(data):
            for col_index, cell_data in enumerate(row_data):
                worksheet.write(row_index, col_index, cell_data)

        # Ajustez automatiquement la largeur des colonnes à la longueur du texte
        for col_index, col_data in enumerate(data[0]):
            max_len = max((len(str(row[col_index])) for row in data), default=10)  # Taille minimale par défaut
            worksheet.set_column(col_index, col_index, max_len)  # Ajuste la largeur de la colonne

        # Créez une deuxième feuille de calcul "Project"
        worksheet2 = workbook.add_worksheet('Project')

        # Ajoutez du contenu à la feuille de calcul "Project"
        data2 = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [1, "Project #", "Start Date", "Fabricator", "Project Name", "End Date", "Designer", "Origin", "Address", "Description", "Builder"],
            [2, "", "=TODAY()", "Soudure Camille Castonguay Inc.", "", "=TODAY()+1", "", "Raptor Import Tool", "256 Rte Principale, Fortierville", "", "Soudure Camille Castonguay Inc."],
        ]

        # Assurez-vous que chaque ligne a le même nombre d'éléments que la première ligne
        max_columns2 = len(data2[0])
        for row in data2:
            while len(row) < max_columns2:
                row.append("")  # Ajoutez des chaînes vides pour combler les vides

        # Écrivez les données dans la feuille de calcul "Project"
        for row_index, row_data in enumerate(data2):
            for col_index, cell_data in enumerate(row_data):
                if row_index == 2 and (col_index == 2 or col_index == 5):  # Applique le format de date à C3 et F3
                    date_format = workbook.add_format({'num_format': 'yyyy-mm-dd'})  # Format de date
                    worksheet2.write(row_index, col_index, cell_data, date_format)
                else:
                    worksheet2.write(row_index, col_index, cell_data)

        # Ajustez automatiquement la largeur des colonnes à la longueur du texte pour la feuille "Project"
        for col_index, col_data in enumerate(data2[0]):
            max_len = max((len(str(row[col_index])) for row in data2), default=10)  # Taille minimale par défaut
            worksheet2.set_column(col_index, col_index, max_len)  # Ajuste la largeur de la colonne

        # Enregistrez le classeur Excel
        workbook.close()
        print("Fichier Excel 'RaptorImport.xlsx' créé avec succès.")

    except PermissionError as e:
        # Gestion de l'erreur de permission
        error_message = (
            "Erreur lors de la création du fichier Excel. Veuillez vérifier que le fichier "
            "'RaptorImport.xlsx' n'est pas ouvert dans une autre application et que vous avez "
            "les autorisations nécessaires pour écrire dans ce répertoire."
        )
        print(error_message)  # Imprimer dans la console (pour un futur fichier log)

        # Afficher un message d'erreur à l'utilisateur
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Critical)
        message_box.setWindowTitle("Erreur")
        message_box.setText(error_message)
        message_box.exec_()