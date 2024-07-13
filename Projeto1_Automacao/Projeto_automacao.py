# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
#  https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login
# Passo 3: Pegar/importar a base de dados
# Passo 4 : Cadastrar um produto
# Passo 5: Repetur o passo 4 até cadastrar todos os produtos

import pyautogui
import time
# o time é outra biblioteca de comandos do python, mas essa já vem instalada.

pyautogui.PAUSE = 0.5 #esse é um comando para dar uma pausa entre cada comando, como a automatização é muito rápida, é necessário colocar pelo menos 0.5 segundos para funcionar.
# Primeiro vamos automatizar para o computador abrir o Safari e depois digitar o site que queremos abrir:
# Para funcionar o command + space foi preciso adicionar um pequeno intervalo de tempo
pyautogui.hotkey('command','space', interval=0.1)  
pyautogui.write('safari')
pyautogui.press('enter')
pyautogui.hotkey('command','n', interval=0.1)  
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# depois de abrir o site vou usar um comando da biblioteca time, para dar um intervalo de tempo especificamente nesse momento.
# isso pois cada site pode demorar um tempo maior ou menor para carregar.

time.sleep(2)

# passo 2: fazer login
pyautogui.click(x=467, y=391)
pyautogui.hotkey('command','a', interval=0.1) 
pyautogui.write('teste@gmail.com')
pyautogui.press('tab')
pyautogui.hotkey('command','a', interval=0.1) 
pyautogui.write('senhafake')
pyautogui.click(x=770, y=546)

time.sleep(2)

# passo 3: importar a base de dados

import pandas

tabela = pandas.read_csv("produtos.csv")

# passo 4: cadastrar o produto
for linha in tabela.index:
    pyautogui.click(x=646, y=278)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("enter")

    #para subir a tela e recomeçar
    pyautogui.scroll(50000)

