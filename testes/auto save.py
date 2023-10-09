import tkinter as tk
from tkinter import filedialog, simpledialog
import subprocess
import pyautogui
import time

def escolher_pasta():
    root = tk.Tk()
    root.withdraw()  # Fecha a janela principal do tkinter
    pasta_escolhida = filedialog.askdirectory()  # Abre a janela para escolha de pasta
    return pasta_escolhida

def abrir_git_bash(caminho):
    comando = f'cd "{caminho}" && start "" "C:\\Users\\gabriel.rosa\\AppData\\Local\\Programs\\Git\\git-bash.exe"'
    subprocess.Popen(comando, shell=True)

pasta = escolher_pasta()
abrir_git_bash(pasta)
time.sleep(1)
pyautogui.typewrite("git status\n")
time.sleep(0.5)
pyautogui.typewrite("git add .\n")
time.sleep(0.5)
mensagem = simpledialog.askstring("Mensagem de Commit", "Digite a mensagem do commit:")
time.sleep(0.5)
pyautogui.typewrite('git commit -m "{}"\n'.format(mensagem))
time.sleep(0.5)
pyautogui.typewrite("git status\n")
time.sleep(0.5)
pyautogui.typewrite("git log\n")
time.sleep(3.5)
pyautogui.typewrite("q")