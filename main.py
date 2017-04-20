import json
import requests
import tkinter as tk
from dataGetter import DataGetter as DGet

dataGet = DGet('https://api.github.com')

janela = tk.Tk()
janela.title('Disciplina')
janela.geometry('300x250')

janela.mainloop()
