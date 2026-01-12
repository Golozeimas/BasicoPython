import tkinter as tk

# 1 - Criando a janela
janela = tk.Tk()

# 2 - Titulo para a janela
janela.title("Gerenciar frases")

# 3 - Tamanho da janela
janela.geometry("300x150")

# 4 - Adiciona um frame na janela - um frame é como se fosse uma janela em branco dentro da outra
frame = tk.Frame(janela) # precisa de uma janela, para definir seu lugar
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 5 - Adiciona label - label geralmente fica textos ou botões dentro
label = tk.Label(frame, text="Olá, mundo!")
label.pack(fill='x', expand=True)

# 6 - Adiciona input
text_label_frase = tk.Label(frame, text="Frase para substituir (Digite abaixo)")
text_label_frase.pack(fill='x', expand=True)

inpt_text = tk.Entry(frame)
inpt_text.pack(fill='x', expand=True)

def click():
    label.config(text=inpt_text.get())

# 7 - Adiciona botão de substituição
botao = tk.Button(frame, text="Substituir", command=click) # (define o local onde fica, pode ser um texto)
botao.pack() # o .pack é pra fazer aparecer, pode modificar o a cor ou expandir o mesmo 


# Roda o loop principal
janela.mainloop()

