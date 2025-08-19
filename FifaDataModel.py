from PyQt6.QtCore import *  # Import Qt core classes
from PyQt6.QtWidgets import *  # Import Qt widget classes
from PyQt6.QtGui import *  # Import Qt GUI classes

class Datamodel(QAbstractTableModel):
    """
    A Qt table model to represent tabular data in a QTableView.

    Attributes
    ----------
    data : list of tuples
        The main data to display in the table.
    header : list of str
        Column headers for the table view.

    Methods
    -------
    headerData(section, orientation, role):
        Returns header labels or row numbers.
    data(index, role):
        Returns cell data or alignment.
    rowCount(index):
        Returns the number of rows.
    columnCount(index):
        Returns the number of columns.
    """

    def __init__(self, data):
        """
        Initialize the table model with data and headers.

        Parameters
        ----------
        data : list of tuples
            The dataset to be displayed in the table.
        """
        super(Datamodel, self).__init__()  # Initialize the base QAbstractTableModel
        self.data = data  # Store the data
        self.header = ["Id", "FirstName", "LastName", "Nation", "Club", "Post", "Overall"]  # Define column headers

    def headerData(self, section, orientation, role):
        """
        Provide header information for the table view.

        Parameters
        ----------
        section : int
            Column or row number.
        orientation : Qt.Orientation
            Horizontal or vertical orientation.
        role : Qt.ItemDataRole
            Role indicating the type of data requested.

        Returns
        -------
        str or int
            Column header label for horizontal, row number for vertical.
        """
        if role == Qt.ItemDataRole.DisplayRole:  # Only provide data for display
            if orientation == Qt.Orientation.Horizontal:  # Column headers
                return str(self.header[section])
            return section + 1  # Row numbers starting from 1

    def data(self, index, role):
        """
        Return data for each cell in the table.

        Parameters
        ----------
        index : QModelIndex
            The index of the table cell.
        role : Qt.ItemDataRole
            Role indicating the type of data requested.

        Returns
        -------
        Any
            The data to display or the alignment.
        """
        if role == Qt.ItemDataRole.DisplayRole:  # Display the actual data
            return self.data[index.row()][index.column()]
        if role == Qt.ItemDataRole.TextAlignmentRole:  # Center-align all text
            return Qt.AlignmentFlag.AlignCenter

    def rowCount(self, index):
        """
        Return the number of rows in the table.

        Parameters
        ----------
        index : QModelIndex
            Required parameter (not used here).

        Returns
        -------
        int
            Number of rows.
        """
        return len(self.data)

    def columnCount(self, index):
        """
        Return the number of columns in the table.

        Parameters
        ----------
        index : QModelIndex
            Required parameter (not used here).

        Returns
        -------
        int
            Number of columns.
        """
        return len(self.data[0]) if self.data else 0  # Return 0 if data is empty
