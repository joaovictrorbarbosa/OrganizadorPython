import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title= "Selecione a pasta que deseja organizar.")

listaarq = os.listdir(caminho)
print(listaarq)

locais = {
    "documentos": ['.docx','.pdf'],
    'Banco de dados':['.sql'],
    'EXCEL': ['.xlsx']
    }

for arq in listaarq:
    nome, extensao = os.path.splitext(f'{caminho}/{arq}')
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arq}', f'{caminho}/{pasta}/{arq}')
