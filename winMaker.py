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

        self.enNome = tk.Entry(self.window, font=("Arial", 10))
        self.enNome.place(x=140, y=65)

    def changeStatus(self, message):
        self.lblStatus.config(text=message)

    def onClickBtnObter(self):
        try:
            nome = self.enNome.get()
            codigo = self.enCod.get()

            if codigo:
                try:
                    int_cod = int(codigo)
                except Exception as e:
                    self.changeStatus("Código inválido!!!") 
                    return

            if codigo and nome:
                disc = self.dataGet.get_json_data(codigo=int_cod, nome=nome)
            elif codigo:
                disc = self.dataGet.get_json_data(codigo=int_cod)
            elif nome:
                disc = self.dataGet.get_json_data(nome=nome)
            else:
                disc = "Campo(s) vazio(s)!!!"

            if type(disc) is str:
                self.changeStatus(disc)
            else:
                self.changeStatus("Código: " + str(disc["codigo"]) + ", Nome: " + str(disc["nome"]))
        except Exception as e:
            self.changeStatus(str(e)) 
        
    def activateLoop(self):
        self.window.mainloop()
