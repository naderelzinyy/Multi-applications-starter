
import tkinter as tk
from tkinter import filedialog, Text
import os


apps = []
labels = []


class Controller:

    def add_app(self):

        # delete_redudance = [widget.destroy() for widget in frame.winfo_children()]
        for widget in frame.winfo_children():
            widget.destroy()
        file_name = filedialog.askopenfilename(initialdir='/applications', title="select an app",
                                               filetypes=(('executables', '*.app'), ("all files", "*.*")))
        if file_name != '':
            apps.append(file_name)
        print(file_name)
        controller.refresh_list()

    def run_apps(self):
        # open_app = [os.system("open "+app) for app in apps]
        for app in apps:
            os.system("open "+app)


    def clear(self):
        apps.clear()
        # clearing_labels = [label.destroy() for label in labels]
        for label in labels:
            label.destroy()

    def refresh_list(self):

        if len(apps) != 0:
            for app in apps:
                label = tk.Label(frame, text=app)
                label.pack()
                labels.append(label)

                # Delete Button
                # item_btn = tk.Button(master=frame, text='x', padx=10, pady=5, fg='black',
                #                      command=lambda: apps.remove(app))
                # item_btn.pack()


controller = Controller()
root = tk.Tk()
root.configure(background='black')
# root.geometry('100x1200')
# root.eval('tk::PlaceWindow . center')

# Canvas
canvas = tk.Canvas(master=root, height=700, width=900, bg='#1f1f1f')
canvas.pack()

# Frames
frame = tk.Frame(master=canvas, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Buttons
open_file = tk.Button(master=root, text='open file', padx=10, pady=5, fg='black', command=controller.add_app)
open_file.pack()

run_app = tk.Button(master=root, text='run apps', padx=10, pady=5, fg='black', command=controller.run_apps)
run_app.pack()

clear_apps = tk.Button(master=root, text='clear', padx=10, pady=5, fg='black', command=controller.clear)
clear_apps.pack()
root.mainloop()
