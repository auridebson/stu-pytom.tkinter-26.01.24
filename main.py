from tkinter import *

def clicou():
    nome = usuario_input.get()
    print(f"Olá {nome}")

janelinha = Tk()
janelinha.title("My first Phyton Window")
janelinha.geometry("200x400")

usuario_label = Label(text="Usuário")
usuario_label.pack()
usuario_input = Entry()
usuario_input.pack()

pass_label = Label(text="Password")
pass_label.pack()
pass_input = Entry()
pass_input.pack()

botao = Button(janelinha, text="Enviar", command=clicou)
botao.pack()


janelinha.mainloop()