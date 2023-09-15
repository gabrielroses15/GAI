import win32gui
import time
import pygetwindow as gw

def mudar_foco_para_janela(titulo):
    janela = gw.getWindowsWithTitle(titulo)
    if janela:
        janela[0].activate()
    else:
        print(f"Janela com título '{titulo}' não encontrada.")

def obter_nome_janela_sobre_mouse():
    _, _, (x, y) = win32gui.GetCursorInfo()
    hwnd = win32gui.WindowFromPoint((x, y))
    nome = win32gui.GetWindowText(hwnd)
    return nome

while True:
    nome_elemento = obter_nome_janela_sobre_mouse()
    print(f"Mouse sobre: {nome_elemento}")
    time.sleep(1)
    mudar_foco_para_janela(nome_elemento)