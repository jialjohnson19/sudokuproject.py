#Alejandra


class Cell:
    def __init__(self, value, row, col, screen):
        # constructor for cell class
        # screen is a window from pycharm
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

        self.selected = False
        pass

    def set_cell_value(self, value):
        # setter for this cell's value
        pass

    def set_sketched_value(self, value):
        # setter for this cell's sketched value
        pass

    def draw(self):
        # draws cell w value inside it
        # if cell is not 0, value is displayed
        # if cell has a 0 value, no value is displayed in cell
        # cell is outlined red if it is currently selected
        pass

    #hah