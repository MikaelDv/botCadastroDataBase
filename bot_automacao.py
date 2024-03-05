#Passo 1: Entrar no sistema da empresa
#pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(3)

#Passo 2: Fazer login
pyautogui.click(x=706, y=360)
pyautogui.write('emailexample@gmail.com')   
pyautogui.press('tab')
pyautogui.write('senhaX')
pyautogui.press('enter')

time.sleep(3)

# Passo 3: Importar a base de dados
# pip install pandas numpy openpyx1
import pandas
tabela = pandas.read_csv('produtos.csv')

# Passo 4: Cadastrar 1 produto

for linha in tabela.index:

    pyautogui.click(x=697, y=243)

    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')
    
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(tabela.loc[linha, 'obs'])
    pyautogui.press('tab')
    
    pyautogui.press('enter')

    pyautogui.scroll(10000)