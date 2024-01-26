from tkinter import *

def calcular():
    x = float(num1_input.get())
    y = float(num2_input.get())
    resultado = x / y
    print(resultado)


janelinha = Tk()
janelinha.title("Calculadora")
janelinha.geometry("200x200")

num1_label = Label(text="Número 1")
num1_label.pack()
num1_input = Entry()
num1_input.pack()


num2_label = Label(text="Número 2")
num2_label.pack()
num2_input = Entry()
num2_input.pack()

btn_calcular = Button(janelinha, text="Calcular", command=calcular)
btn_calcular.pack()


janelinha.mainloop()