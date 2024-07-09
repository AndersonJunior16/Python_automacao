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

time.sleep(3)

pa.click(x=580, y=374)
pa.hotkey('ctrl', 'a')
pa.write('pythonimpressionador@gmail.com')
pa.press('tab')
pa.write('123456789')
pa.press('enter')

time.sleep(3)
# Importar a base de dados

tabela = pd.read_csv("C:/Users/Juninho/Documents/GitHub/Hashtag-Python/AUTOMACAO/produtos.csv")
print(tabela)

# Cadastrar os produtos
