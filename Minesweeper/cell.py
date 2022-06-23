from tkinter import Button, Label
import random
import settings
import ctypes
import sys

class Cell():
    all = []
    cell_count_label_object = None
    cell_count = settings.CELL_COUNT

    def __init__(self, x, y, is_mine = False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_potential_mine = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append button object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width = 15,
            height = 5
        )
        btn.bind("<Button-1>", self.left_click_actions) #Left Click
        btn.bind("<Button-3>", self.right_click_actions) #Right Click
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        label = Label(
            location,
            bg = "black",
            fg = "white",
            text = f'Cells Left: {Cell.cell_count}',
            font = ("Times", 35)
        )
        Cell.cell_count_label_object = label

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()

        else:
            if self.surrounded_cells_mine_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            #If mines count is equla to the cells left count, win game
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, "Congratulations! You Win!", "Game Over", 0)

        #Cancel interactivity of button if cell is already opened (Unbind left and right click events
        self.cell_btn_object.unbind("<Button-1>")
        self.cell_btn_object.unbind("<Button-3>")

    #Return a cell object's x and y values
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mine_length(self):
        total = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                total += 1
        return total

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mine_length)

            # Update the text of total cell count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f'Cells Left: {Cell.cell_count}')

            #If marked as potential mine, we will configure the cell bg color to SystemButtonFace
            self.cell_btn_object.configure(bg = "SystemButtonFace")
        #Marking the cell as opened (mined)
        self.is_opened = True


    def show_mine(self):
        self.cell_btn_object.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, "You clicked on a mine", "Game Over", 0)
        sys.exit()


    def right_click_actions(self, event):
        if not self.is_potential_mine:
            self.cell_btn_object.configure(bg = "orange")
            self.is_potential_mine = True
        else:
            self.cell_btn_object.configure(bg = "SystemButtonFace")
            self.is_potential_mine = False
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f'Cell({self.x},{self.y})'