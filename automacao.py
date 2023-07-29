import pyautogui
import time
import pandas

pyautogui.PAUSE = 3.0
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Site falso somente para o exercicio do momento
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep (3)

pyautogui.click(x=491, y=391)
#Digitar email do usuario
pyautogui.write("12345@abdce.com")
pyautogui.press("tab")
#Senha do usuario
pyautogui.write("12345")
pyautogui.press("enter")
pyautogui.press("enter")
time.sleep (3)

tabela = pandas.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
    pyautogui.click(x=606, y=279)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pandas.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)