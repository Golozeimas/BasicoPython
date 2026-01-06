import os
from os import system
# 1 - Retorna o caminho para a pasta atual
print(os.getcwd())

# 2 - Listar arquivos e pastas
print(os.listdir())

# 3 - O system, comandos nos terminais
os.system("ver")

# 4 - Ver as informações do sistema
os.system("systeminfo")

# 5 - Limpar o terminal
os.system("cls")

# 6 - desligar o computador
os.system("shutdown /s /t 3600") # desliga em uma hora
os.system("shutdown /a") # cancelar o desligamento
system("shutdown /s /t 0") # desliga o computador imediatamente