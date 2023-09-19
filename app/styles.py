# styles.py
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel

# Définissez les variables pour la police et la taille de police
button_font_family = "Arial, sans-serif"
button_font_size = "14px"
button_font_weight = "bold"
button_border_radius = "10px"

class StyledButton(QPushButton):
    def __init__(self, text, parent=None):
        super(StyledButton, self).__init__(text, parent)
        self.setFixedHeight(50)  # Hauteur du bouton

app_style = """
    background-color: #333333; /* Gris foncé */
"""

button_styles = {
    "default": f"""
        QPushButton {{
            background-color: #AAAAAA;
            border: 2px solid #555555;
            border-radius: {button_border_radius};
            color: white;
            padding: 10px 20px;
            text-align: center;
            font-size: {button_font_size};
            font-family: {button_font_family};
            font-weight: {button_font_weight};
        }}
        QPushButton:hover {{
            background-color: #888888;
        }}
    """,
    "excel": f"""
        QPushButton {{
            background-color: #217346; /* Vert d'Excel */
            border: 2px solid #185C3C;
            border-radius: {button_border_radius};
            color: white;
            padding: 10px 20px;
            text-align: center;
            font-size: {button_font_size};
            font-family: {button_font_family};
            font-weight: {button_font_weight};
        }}
        QPushButton:hover {{
            background-color: #185C3C; /* Vert plus foncé */
        }}
    """,
    "option": f"""
        QPushButton {{
            background-color: #0078D4; /* Bleu de Windows */
            border: 2px solid #005A9E;
            border-radius: {button_border_radius};
            color: white;
            padding: 10px 20px;
            text-align: center;
            font-size: {button_font_size};
            font-family: {button_font_family};
            font-weight: {button_font_weight};
        }}
        QPushButton:hover {{
            background-color: #005A9E; /* Bleu plus foncé */
        }}
    """,
    
    "start_import": f"""
        QPushButton {{
            background-color: #db6b09; /* Orange personnalisé */
            border: 2px solid #c25f08; /* Bordure légèrement plus foncée */
            border-radius: {button_border_radius};
            color: white;
            padding: 10px 20px;
            text-align: center;
            font-size: {button_font_size};
            font-family: {button_font_family};
            font-weight: {button_font_weight};
        }}
        QPushButton:hover {{
            background-color: #c25f08; /* Orange plus foncé au survol */
        }}
    """,
    
    "save_option": f"""
        QPushButton {{
            background-color: #00A600; /* Vert */
            border: 2px solid #007D00; /* Bordure légèrement plus foncée */
            border-radius: {button_border_radius};
            color: white;
            padding: 10px 20px;
            text-align: center;
            font-size: {button_font_size};
            font-family: {button_font_family};
            font-weight: {button_font_weight};
        }}
        QPushButton:hover {{
            background-color: #007D00; /* Vert plus foncé au survol */
        }}
    """,
    
    "help_option": f"""
        QPushButton {{
            background-color: #FFA500; /* Orange */
            border: 2px solid #FF8400; /* Bordure légèrement plus foncée */
            border-radius: {button_border_radius};
            color: white;
            padding: 10px 20px;
            text-align: center;
            font-size: {button_font_size};
            font-family: {button_font_family};
            font-weight: {button_font_weight};
        }}
        QPushButton:hover {{
            background-color: #FF8400; /* Orange plus foncé au survol */
        }}
    """
}

# Style pour le texte blanc
white_text = """
    color: white;
"""

# Style pour la barre d'emplacement de Raptor blanche
white_edit_background = """
    background-color: white;
"""
