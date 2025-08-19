import sqlite3  # Import the SQLite3 module for database operations

class accessdata:
    """
    A class to handle basic SQLite database operations: insert, delete, update, and search.

    Attributes
    ----------
    connectionString : str
        The SQLite database file path.
    
    Methods
    -------
    insertQuery(query, records):
        Inserts multiple records into the database.
    deleteQuery(query):
        Deletes records from the database.
    updateQuery(query):
        Updates records in the database.
    searchData(query):
        Executes a SELECT query and returns the results.
    """

    def __init__(self):
        """
        Initialize the accessdata class with the database connection string.
        """
        self.connectionString = "FIFA24.db"  # SQLite database file

    # Insert data into the database
    def insertQuery(self, query, records):
        """
        Insert multiple records into the database using a parameterized query.

        Parameters
        ----------
        query : str
            SQL insert query with placeholders.
        records : list of tuples
            Data records to insert.
        """
        try:
            # Connect to the SQLite database and automatically close the connection using 'with'
            with sqlite3.connect(self.connectionString) as connection:
                connection.executemany(query, records)  # Execute the insert query for multiple records
                connection.commit()  # Commit changes to the database
        except Exception as err:
            print(err)  # Print any error that occurs

    # Delete data from the database
    def deleteQuery(self, query):
        """
        Delete records from the database.

        Parameters
        ----------
        query : str
            SQL delete query.
        """
        try:
            with sqlite3.connect(self.connectionString) as connection:
                connection.execute(query)  # Execute the delete query
                connection.commit()  # Commit changes
        except Exception as err:
            print(err)  # Print any error

    # Update data in the database
    def updateQuery(self, query):
        """
        Update records in the database.

        Parameters
        ----------
        query : str
            SQL update query.
        """
        try:
            with sqlite3.connect(self.connectionString) as connection:
                connection.execute(query)  # Execute the update query
                connection.commit()  # Commit changes
        except Exception as err:
            print(err)  # Print any error

    # Search data in the database
    def searchData(self, query):
        """
        Execute a SELECT query and return the result rows.

        Parameters
        ----------
        query : str
            SQL select query.
        
        Returns
        -------
        list of tuples
            Query result rows.
        """
        try:
            with sqlite3.connect(self.connectionString) as connection:
                results = connection.execute(query)  # Execute the select query
                rows = results.fetchall()  # Fetch all rows from the query result
                return rows  # Return the results
        except Exception as err:
            print(err)  # Print any error
