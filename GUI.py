import tkinter as tk
from tkinter import *

import tksheet

from main import *
if __name__ == "__main__":
    window = tk.Tk()

    window.title("Sudoku Solver")

    window.geometry('210x300')

    sheet = tksheet.Sheet(window)

    sheet.grid()

    sheet.set_sheet_data([[f"{board[ri][cj]}" for cj in range(9)] for ri in range(9)])

    button = tk.Button(window, text="SOLVE", command=lambda: [solve(board),
                                                              sheet.set_sheet_data(
                                                                  [[f"{board[ri][cj]}" for cj in range(9)] for ri in
                                                                   range(9)]),
                                                              width_of_col()])

    button.place(relx=0.5, rely=0.95, anchor=S)

    sheet.enable_bindings(("single_select",

                           "row_select",

                           "column_width_resize",

                           "arrowkeys",

                           "right_click_popup_menu",

                           "rc_select",

                           "rc_insert_row",

                           "rc_delete_row",

                           "copy",

                           "cut",

                           "paste",

                           "delete",

                           "undo",

                           "edit_cell"))

    for i in range(0, 9):
        sheet.column_width(column=i
                           , width=20)


    def width_of_col():
        for i in range(0, 9):
            sheet.column_width(column=i
                               , width=20)


    window.mainloop()
