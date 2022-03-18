import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
# Canvas
canvas = tk.Canvas(root, height=700, width=900, bg='#1f1f1f')
canvas.pack()
# Frames
frame = tk.Frame(canvas, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1 )

root.mainloop()
