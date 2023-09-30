
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QPixmap
import requests
import pokepy
import urllib.request
from PIL import Image

class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()

        self.w = None
        self.setFixedSize(850, 500)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.setGeometry(50, 50, 280, 40)


        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.search_button_clicked)

        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.capture_button_clicked)

        self.captured_label = QLabel("", self)
        self.captured_label.setGeometry(50, 370, 160, 43)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.display_button_clicked)

        self.name_label = QLabel("", self)
        self.name_label.setGeometry(550, 250, 160, 43)

        self.image_label = QLabel("", self)
        self.image_label.setGeometry(550, 50, 160, 43)

        self.ability_label = QLabel("", self)
        self.ability_label.setGeometry(550, 300, 160, 43)

        self.type_label = QLabel("", self)
        self.type_label.setGeometry(550, 350, 160, 43)

        self.stat_label = QLabel("", self)
        self.stat_label.setGeometry(550, 400, 160, 43)

        self.client = pokepy.V2Client()

    ## TO-DO ##

    # 1 #
    # Fetch the data from from the API.
    # Display the name, official artwork (image), abilities, types and stats when queried with a Pokémon name.
    # Add the background provided in assets
    def search_button_clicked(self):
        # changing the text of label after button get clicked
        search_term = self.textbox.text()
        pokemon = self.client.get_pokemon(search_term)[0]

        self.name = pokemon.name
        self.artwork_url = pokemon.sprites.front_default
        an_ability = pokemon.abilities[0].ability.name
        a_type = pokemon.types[0].type.name
        a_stat = pokemon.stats[0].stat.name

        self.name_label.setText("Name: " + self.name)

        request = requests.get(self.artwork_url)
        self.im = QPixmap(self.artwork_url)
        self.im.loadFromData(request.content)
        self.image_label.setPixmap(self.im)

        self.ability_label.setText("An ability: " + an_ability)
        self.type_label.setText("A Type: " + a_type)
        self.stat_label.setText("A Stat: " + a_stat)

    # 2 #
    # Capture the Pokémon i.e. download the image.
    def capture_button_clicked(self):
        urllib.request.urlretrieve(self.artwork_url, self.name + ".png")
        self.captured_label.setText("Captured..")

    # 3 #
    # Display all the Pokémon captured with their respective names using a new window.
    def display_button_clicked(self):
        pass

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
