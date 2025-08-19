import PyQt6
import sys
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLineEdit, QLabel, QSlider, QPushButton, QGridLayout, QTableView
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtGui import QIcon
from FifaBLL import players  # Import the players business logic class
from FifaDataModel import Datamodel  # Import custom table model for QTableView
import sqlite3

class form(QWidget):
    """
    Main GUI form for managing FIFA players.

    Attributes
    ----------
    players : players
        Instance of players class for database operations.
    flag : bool
        Indicates whether initial data has been created.
    overall : int
        Current minimum overall filter value.
    labeloverall : QLabel
        Label to display the value of the slider.
    layoutList : list
        List of layouts for organizing widgets.
    table : QTableView
        Table view to display player data.
    """

    def __init__(self):
        """
        Initialize the main form, create layouts, input widgets, buttons, and table view.
        """
        QWidget.__init__(self)  # Initialize base QWidget
        self.resize(500, 500)  # Set default window size

        # Initialize player data manager
        self.players = players()
        self.flag = True  # Flag for CREATE button to insert data only once
        self.overall = 30  # Default minimum overall value
        self.labeloverall = QLabel(self)  # Label to display slider value
        self.labeloverall.move(250, 70)  # Set position of label

        # Main layout and sub-layouts
        self.layoutList = []  # Store three sub-layouts
        mainLayout = QGridLayout()  # Main grid layout
        for i in range(3):
            layout = QGridLayout()
            mainLayout.addLayout(layout, i, 0, 1, 1)
            self.layoutList.append(layout)
        self.setLayout(mainLayout)

        # --- Layout 1: Input Widgets ---
        labeList = ["FirstName", "Overall", "Position", "Nation"]
        for i, txt in enumerate(labeList):
            label = QLabel()
            label.setText(f"{txt}: ")  # Set label text
            self.layoutList[0].addWidget(label, i, 0, 1, 1)

        # Player Name input
        self.playername = QLineEdit()
        self.playername.setStyleSheet(
            'QLineEdit {border: 1px solid purple; border-radius:2; background-color: #F4E3FF; padding:4}')
        self.playername.setPlaceholderText("Please Enter Player's First Name")
        self.layoutList[0].addWidget(self.playername, 0, 1, 1, 1)

        # Overall slider
        self.minOverall = QSlider(Qt.Orientation.Horizontal, self)
        self.minOverall.setMinimum(30)
        self.minOverall.setMaximum(99)
        self.minOverall.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.minOverall.setTickInterval(5)
        self.minOverall.valueChanged.connect(self.values)  # Connect to update label
        self.layoutList[0].addWidget(self.minOverall, 1, 1, 1, 1)

        # Player Position input
        self.playerpost = QLineEdit()
        self.playerpost.setStyleSheet(
            'QLineEdit {border: 1px solid purple; border-radius:2; background-color: #F4E3FF; padding:4}')
        self.playerpost.setPlaceholderText("Please Enter Player's Position")
        self.layoutList[0].addWidget(self.playerpost, 2, 1, 1, 1)

        # Nation dropdown
        self.playerNation = QComboBox(self)
        self.playerNation.addItems([
            "Any", "Argentine", "Austria", "Belgium", "Brazil", "Croatia", "England",
            "France", "Germany", "Iran", "Italy", "Norway", "Portugal", "Spain"
        ])
        self.playerNation.setStyleSheet(
            'QComboBox {border: 1px solid purple; border-radius:2; background-color: #F4E3FF; padding:4} '
            'QComboBox QAbstractItemView {background-color:#e8bcf0; color:purple}'
        )
        self.layoutList[0].addWidget(self.playerNation, 3, 1, 1, 1)

        # --- Layout 2: Buttons ---
        buttons = [
            ("CREATE", self.Create),
            ("SEARCH", self.select),
            ("UPDATE", self.updateForm),
            ("DELETE", self.deleteForm),
            ("CLOSE", self.closeForm)
        ]
        for i, (text, func) in enumerate(buttons):
            button = QPushButton()
            button.setText(text)
            button.clicked.connect(func)  # Connect button to function
            button.setStyleSheet(
                'QPushButton {background-color: purple; color: white; border-radius:6; padding:4; font-weight:bold}'
            )
            self.layoutList[1].addWidget(button, 0, i, 1, 1)

        # --- Layout 3: Table View ---
        self.table = QTableView()
        self.table.setStyleSheet(
            'QTableView {background-color: #F4E3FF; border:2px solid purple; border-radius:6}'
        )
        self.table.resize(500, 300)
        self.layoutList[2].addWidget(self.table)

    # --- Button Functions ---
    def Create(self):
        """Insert initial player data into the database if not done yet."""
        if self.flag:
            self.players.createData()
            self.flag = False

    def select(self):
        """Search players based on filters and display in the table."""
        overall = self.overall
        post = self.playerpost.text()
        nation = self.playerNation.currentText()
        playername = self.playername.text()
        rows = self.players.searchData(playername, overall, post, nation)
        if len(rows):
            self.datamodel = Datamodel(rows)
            self.table.setModel(self.datamodel)

    def values(self):
        """Update the slider label and current overall filter value."""
        self.labeloverall.setText("Value: " + str(self.sender().value()))
        self.labeloverall.adjustSize()
        self.overall = self.sender().value()

    def updateForm(self):
        """Update a player's data in the database based on input fields."""
        overall = self.overall
        post = self.playerpost.text()
        nation = self.playerNation.currentText()
        playername = self.playername.text()
        if playername != "" and nation != "Any" and overall and post != "":
            self.players.updateData(playername, overall, post, nation)

    def deleteForm(self):
        """Delete a player's data from the database based on input fields."""
        overall = self.overall
        post = self.playerpost.text()
        nation = self.playerNation.currentText()
        playername = self.playername.text()
        if playername != "" and nation != "Any" and overall and post != "":
            self.players.deletesData(playername, overall, post, nation)

    def closeForm(self):
        """Delete all data from the database and close the form."""
        self.players.deleteData()
        self.close()


# --- Main Application ---
app = QApplication(sys.argv)
app.setApplicationName("Football Bartar")  # Set application name
app.setWindowIcon(QIcon('icon.webp'))  # Set window icon

# --- Background Music ---
filename = "music.mp3"
player = QMediaPlayer()
audio_output = QAudioOutput()
player.setAudioOutput(audio_output)
player.setSource(QUrl.fromLocalFile(filename))  # Load audio file
audio_output.setVolume(50)
player.play()  # Play music

# --- Launch Form ---
form = form()
form.show()  # Show the GUI window
sys.exit(app.exec())  # Start the Qt event loop
