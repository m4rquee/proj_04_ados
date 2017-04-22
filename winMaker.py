import json
import tkinter as tk
from dataGetter import DataGetter as DGet


class discForm():
    def __init__(self, title, width, height, rwidth, rheight, url):
        self.dataGet = DGet(url)

        self.window = tk.Tk()
        self.window.title(title)
        self.window.resizable(width=rwidth, height=rheight)

        # Set window size and position
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen

        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)

        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))

        self.makeComponents()

    def makeComponents(self):
        # Status bar
        self.lblStatus = tk.Label(self.window, text="", bd=1, relief=tk.SUNKEN, anchor=tk.S)
        self.lblStatus.pack(side=tk.BOTTOM, fill=tk.X)

        # Labels
        self.lblCod = tk.Label(self.window, text="Código", font=("Consolas", 15))
        self.lblCod.place(x=10, y=10)

        self.lblMat = tk.Label(self.window, text="Matéria", font=("Consolas", 15))
        self.lblMat.place(x=10, y=60)

        # Button
        self.btnObter = tk.Button(self.window, text="Obter dados", font=("Consolas", 16),
                                  command=self.onClickBtnObter)
        self.btnObter.place(x=140, y=150)

        # Entrys (txt field)
        self.enCod = tk.Entry(self.window, font=("Arial", 10))
        self.enCod.place(x=140, y=15)

        self.enMat = tk.Entry(self.window, font=("Arial", 10))
        self.enMat.place(x=140, y=65)

    def changeStatus(self, message):
        self.lblStatus.config(text=message)

    def onClickBtnObter(self):
        disc = self.dataGet.get_json_data()["Disciplinas"][0]

        discCod = disc["cod"]
        discMat = disc["mat"]

        self.changeStatus("Código: " + str(discCod) + ", Matéria: " + str(discMat))

    def activateLoop(self):
        self.window.mainloop()
