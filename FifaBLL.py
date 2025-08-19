from FifaDataAccess import accessdata  # Import the accessdata class from the FifaDataAccess module to handle database operations

class players:
    """
    A class to represent a collection of football players and perform CRUD operations
    on a database table 'tblPlayers'.

    Attributes
    ----------
    dataAccess : accessdata
        Instance of the accessdata class to handle database queries.
    records : list of tuples
        Predefined player records to be inserted into the database.

    Methods
    -------
    createData():
        Inserts all predefined player records into the database.
    deleteData():
        Deletes all records from the database.
    updateData(playername, overall, post, nation):
        Updates the record of a specific player with new values.
    deletesData(playername, overall, post, nation):
        Deletes specific player records based on given conditions.
    searchData(playername, overall, post, nation):
        Searches for players based on various filter criteria.
    """

    def __init__(self):
        """
        Initialize the players class with a database access instance
        and a predefined list of player records.
        """
        self.dataAccess = accessdata()  # Create a database access object for performing queries
        self.records = [
            # Tuple format: (ID, firstName, lastName, nation, club, position, overall)
            (1, "Leon", "Goretzka", "Germany", "Bayern Munich", "CM", 87),
            (2, "HamidReza", "Horr", "Iran", "Esteghlal", "LW", 99),
            (3, "Cristiano", "Ronaldo", "Portugal", "Al Nassr", "ST", 90),
            (4, "Lionel", "Messi", "Argentine", "PSG", "RW", 93),
            (5, "Kylian", "Mbappe", "France", "PSG", "ST", 92),
            (6, "Karim", "Benzema", "France", "Real Madrid", "ST", 92),
            (7, "Iker", "Casilas", "Spain", "LEGEND", "GK", 90),
            (8, "Andrea", "Pirlo", "Italy", "LEGEND", "CM", 89),
            (9, "Wayne", "Rooney", "England", "LEGEND", "ST", 88),
            (10, "Abbas", "Boazzar", "Iran", "Naft", "CM", 70),
            (11, "Vinicius", "Junior", "Brazil", "Real Madrid", "LW", 87),
            (12, "Kevin", "De bruyne", "Belgium", "Man City", "CAM", 88),
            (13, "Farhad", "Majidi", "Iran", "Esteghlal", "ST", 98),
            (14, "Mehdi", "Torabi", "Iran", "Long", "LW", 66),
            (15, "Vahid", "Amiri", "Iran", "Long", "RW", 30),
            (16, "Luka", "Modric", "Croatia", "Real Madrid", "CM", 88),
            (17, "Pablo", "Gavi", "Spain", "Barcelona", "CM", 83),
            (18, "David", "Alaba", "Austria", "Real Madrid", "CB", 86),
            (19, "Erling", "Halland", "Norway", "Man City", "ST", 90),
            (20, "Bruno", "Fernandes", "Portugal", "Man United", "CAM", 88),
            (21, "Neymar", "Jr", "Brazil", "PSG", "LW", 89),
            (22, "Thomas", "Muller", "Germany", "Bayern Munich", "CAM", 86),
            (23, "Naser", "Hejazi", "Iran", "Esteghlal", "GK", 98),
            (24, "Mansour", "Pourheidari", "Iran", "Esteghlal", "RB", 98),
            (25, "Gianluigi", "Buffon", "Italy", "LEGEND", "GK", 90),
            (26, "Zinedine", "Zidane", "France", "LEGEND", "GK", 95),
            (27, "Gerard", "Pique", "Spain", "Shakira", "CB", 84),
            (28, "Eric", "Cantona", "France", "LEGEND", "ST", 92),
            (29, "Paolo", "Maldini", "Italy", "LEGEND", "CB", 95),
            (30, "Jiloyd", "Samuel", "England", "Esteghlal", "RB", 75)
        ]

    def createData(self):
        """
        Insert all predefined player records into the 'tblPlayers' database table.
        """
        query = "INSERT INTO tblPlayers VALUES(?,?,?,?,?,?,?)"  # SQL query with placeholders for data
        self.dataAccess.insertQuery(query, self.records)  # Execute insert query with all records

    def deleteData(self):
        """
        Delete all player records from the 'tblPlayers' database table.
        """
        query = "DELETE FROM tblPlayers"  # SQL query to delete all rows
        self.dataAccess.deleteQuery(query)  # Execute the delete query

    def updateData(self, playername, overall, post, nation):
        """
        Update a specific player's details in the database.

        Parameters
        ----------
        playername : str
            First name of the player to update.
        overall : int
            New overall rating of the player.
        post : str
            New position of the player.
        nation : str
            New nationality of the player.
        """
        # SQL update query to modify player attributes
        query = f"UPDATE tblPlayers SET overall={overall}, nation='{nation}', position='{post}' WHERE firstName='{playername}'"
        self.dataAccess.updateQuery(query)  # Execute the update query

    def deletesData(self, playername, overall, post, nation):
        """
        Delete a specific player record based on multiple conditions.

        Parameters
        ----------
        playername : str
            First name of the player.
        overall : int
            Minimum overall rating.
        post : str
            Player position.
        nation : str
            Player nationality.
        """
        # SQL delete query with multiple conditions
        query = f"DELETE FROM tblPlayers WHERE overall>={overall} AND nation='{nation}' AND position='{post}' AND firstName='{playername}'"
        self.dataAccess.deleteQuery(query)  # Execute the delete query

    def searchData(self, playername, overall, post, nation):
        """
        Search for player records in the database based on filters.

        Parameters
        ----------
        playername : str
            First name of the player (empty string for any).
        overall : int
            Minimum overall rating to filter players.
        post : str
            Player position (empty string for any).
        nation : str
            Player nationality ('Any' for no filter).

        Returns
        -------
        list
            List of tuples containing player records that match the search criteria.
        """
        # Build the SQL query based on multiple filtering conditions
        if post == "" and nation == "Any" and playername == "":
            query = f"SELECT * FROM tblPlayers WHERE overall>={overall} ORDER BY overall DESC"
        elif post == "" and nation != "Any" and playername != "":
            query = f"SELECT * FROM tblPlayers WHERE overall >= {overall} AND nation='{nation}' AND firstName='{playername}' ORDER BY overall DESC"
        elif nation == "Any" and post != "" and playername != "":
            query = f"SELECT * FROM tblPlayers WHERE overall>={overall} AND position='{post}' AND firstName='{playername}' ORDER BY overall DESC"
        elif playername == "" and nation != "Any" and post != "":
            query = f"SELECT * FROM tblPlayers WHERE overall>={overall} AND position='{post}' AND nation='{nation}' ORDER BY overall DESC"
        elif post == "" and nation == "Any" and playername != "":
            query = f"SELECT * FROM tblPlayers WHERE overall>={overall} AND firstName='{playername}' ORDER BY overall DESC"
        elif post == "" and playername == "" and nation != "Any":
            query = f"SELECT * FROM tblPlayers WHERE overall>={overall} AND nation='{nation}' ORDER BY overall DESC"
        elif playername == "" and nation == "Any" and post != "":
            query = f"SELECT * FROM tblPlayers WHERE overall>={overall} AND position='{post}' ORDER BY overall DESC"
        else:
            query = f"SELECT * FROM tblPlayers WHERE overall>={overall} AND nation='{nation}' AND position='{post}' AND firstName='{playername}' ORDER BY overall DESC"

        rows = self.dataAccess.searchData(query)  # Execute the search query and get results
        return rows  # Return the search results
