import tkinter as tk
from tkinter import messagebox

def verificar_idade():
    nome = entry_nome.get()
    idade = entry_idade.get()

    try:
        idade = int(idade)
        msg_preso = f"Você já pode ser aprisionado!"
        msg_solto = f"Você está liberado!"
        if idade >= 18:
            messagebox.showinfo("ALERTA DE PRISÃO", msg_preso)
        else:
            messagebox.showinfo("INFORMAÇÃO", msg_solto)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira uma idade válida.")

janela = tk.Tk()
janela.title("Verificar Idade")

label_nome = tk.Label(janela, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_idade = tk.Label(janela, text="Idade:")
label_idade.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_idade = tk.Entry(janela)
entry_idade.grid(row=1, column=1, padx=10, pady=10)

botao_verificar = tk.Button(janela, text="Verificar Idade", command=verificar_idade)
botao_verificar.grid(row=2, column=0, columnspan=2, pady=10)





janela.mainloop()