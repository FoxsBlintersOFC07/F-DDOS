import subprocess
import time
import os
import platform

libs = ['colorama'] # lista de bibliotecas a serem verificadas

def Instalação(): #CRIA A FUNÇÃO PRA LIMPAR A TELA
   if platform.system() == "Windows":
      instalaçãowin()
   elif platform.system() == "Linux":
      instalaçãoter()
   else:
       instalaçãoter()

def instalaçãowin():
    for lib in libs: 
     try:
        __import__(lib)
        print(f"{lib} já está instalada.")
        print(f"E as outras Bibliotecas tambem, a Instalcao foi concluida!.")
     except ImportError:
        print(f"{lib} não está instalada. Tentando instalar...")
        subprocess.check_call(["python", "-m", "pip", "install", lib]) # verifica se cada biblioteca está instalada e, se não estiver, tenta instalar usando o pip
        print("A instalacao foi Concluida!")

def instalaçãoter():
    for lib in libs: 
     try:
        __import__(lib)
        print(f"{lib} já está instalada.")
        print(f"{lib} E as outras Bibliotecas tambem, a Instalcao foi concluida!.")
     except ImportError:
        print(f"{lib} não está instalada. Tentando instalar...")
        subprocess.check_call(["python", "-m", "pip", "install", lib]) # verifica se cada biblioteca está instalada e, se não estiver, tenta instalar usando o pip
        print("A instalacao foi Concluida!")



Instalação()

