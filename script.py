''' Entrar no sistema da empresa
    link:https://dlp.hashtagtreinamentos.com/python/intensivao/login'''

import pyautogui as pa
import time
import pandas as pd

pa.PAUSE = 0.5

pa.press('win')
pa.write('chrome')
pa.press('enter')
# Fazer o login
pa.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pa.press('enter')

time.sleep(5)

pa.click(x=580, y=374)
pa.hotkey('ctrl', 'a')
pa.write('pythonimpressionador@gmail.com')
pa.press('tab')
pa.write('123456789')
pa.press('enter')

time.sleep(3)
# Importar a base de dados

tabela = pd.read_csv("produtos.csv")
print(tabela)


# Cadastrar os produtos
for linha in tabela.index:
    #codigo
    pa.click(x=509, y=260)
    pa.write(str(tabela.loc[linha, 'codigo']))

    #marca
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'marca']))

    #tipo
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'tipo']))

    #categoria
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'categoria']))

    #preço
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'preco_unitario']))

    #custo
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'custo']))

    #Obs
    pa.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pa.write(obs)
    pa.press('enter')
    pa.scroll(500)