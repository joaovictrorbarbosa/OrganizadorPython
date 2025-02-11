import os
from tkinter.filedialog import askdirectory
from biblioteca.organizador import (organizador)


caminho = askdirectory(title= "Selecione a pasta que deseja organizar.")

organizador(caminho)

print('Sua pasta foi organizada!')
