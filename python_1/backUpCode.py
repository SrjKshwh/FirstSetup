

rows=10
cols=10
grid_cells = []
for r in range(rows):
    row_cells = []
    for c in range(cols):
        cell_label = tk.Label(mainWindow, text="", width=4, height=2, relief="solid", borderwidth=1)
        cell_label.grid(row=r, column=c, padx=1, pady=1) # Place in the grid
        row_cells.append(cell_label)
    grid_cells.append(row_cells)

for r in range(rows):
    for c in range(cols):
            # word search logic
        grid_cells[r][c].config(text=random.choice(string.ascii_uppercase))

mainWindow.mainloop()