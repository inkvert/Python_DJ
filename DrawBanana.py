from tkinter import *


root = Tk()
canvas = Canvas(root, width=300, height=200, bg="white")
canvas.pack()

# Draw the banana body
x1, y1 = 50, 50
x2, y2 = 250, 90
canvas.create_oval(x1, y1, x2, y2, fill="yellow", outline="yellow")

# Draw the banana stem
x1, y1 = 250, 70
x2, y2 = 270, 50
canvas.create_line(x1, y1, x2, y2, width=5, fill="brown")

'''
# Add some shading for a more realistic look
x1, y1 = 70, 60
x2, y2 = 150, 120
canvas.create_oval(x1, y1, x2, y2, fill="yellow", outline="yellow")
'''

root.mainloop()
