import os
from tkinter.filedialog import askdirectory

def organizador(caminho):
    locais = {
        "documentos": ['.docx', '.pdf'],
        'Banco de dados': ['.sql'],
        'EXCEL': ['.xlsx'],
        'Imagens': ['.png', '.jpg', '.jfif']
    }
    listaarq = os.listdir(caminho)
    for arq in listaarq:
        nome, extensao = os.path.splitext(f'{caminho}/{arq}')
        for pasta in locais:
            if extensao in locais[pasta]:
                if not os.path.exists(f'{caminho}/{pasta}'):
                    os.mkdir(f'{caminho}/{pasta}')
                os.rename(f'{caminho}/{arq}', f'{caminho}/{pasta}/{arq}')