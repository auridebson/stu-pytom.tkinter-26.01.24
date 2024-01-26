from tkinter import *

def clicou():
    nome = usuario_input.get()
    idade = idade_input.get()
    print(f"Olá {nome}, você tem {idade} anos.")

janelinha = Tk()
janelinha.title("My first Phyton Window")
janelinha.geometry("200x400")

usuario_label = Label(text="Usuário")
usuario_label.pack()
usuario_input = Entry()
usuario_input.pack()

idade_label = Label(text="Idade")
idade_label.pack()
idade_input = Entry()
idade_input.pack()

botao = Button(janelinha, text="Enviar", command=clicou)
botao.pack()


janelinha.mainloop()