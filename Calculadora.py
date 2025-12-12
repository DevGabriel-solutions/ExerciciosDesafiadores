import math
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculadora!")

frm = ttk.Frame(root, padding=10)
frm.grid()

# Display
display = ttk.Entry(frm, width=20, justify="right", font=("arial", 20))
display.grid(column=0, row=0, columnspan=4, pady= 10)

# Função para inserir os números
def inserir(valor):
    display.insert(END, valor)
def limpar():
    display.delete(0, END)
def apagar():
    display.delete(len(display.get())-1, END)
def calcular():
    try:
        conta = display.get()
        conta = conta.replace("%", "/100")
        resultado = eval(conta)
        display.delete(0, END)
        display.insert(0,str(resultado))
    except:
        display.delete(0, END)
        display.insert(0,"ERRO!")
def raiz():
    try:
        valor = float(display.get())
        resultado = math.sqrt(valor)
        display.delete(0, END)
        display.insert(0,str(resultado))
    except:
        display.delete(0, END)
        display.insert(0, "ERRO!")

ttk.Button(frm, text="C", command=limpar).grid(column=0, row=1)
ttk.Button(frm, text="←", command=apagar).grid(column=1, row=1)
ttk.Button(frm, text="%", command=lambda: inserir("%")).grid(column=2, row=1)
ttk.Button(frm, text="√", command=raiz).grid(column=3, row=1)

# Linha 2
ttk.Button(frm, text="7", command=lambda: inserir("7")).grid(column=0, row=2)
ttk.Button(frm, text="8", command=lambda: inserir("8")).grid(column=1, row=2)
ttk.Button(frm, text="9", command=lambda: inserir("9")).grid(column=2, row=2)
ttk.Button(frm, text="/", command=lambda: inserir("/")).grid(column=3, row=2)

# Linha 3
ttk.Button(frm, text="4", command=lambda: inserir("4")).grid(column=0, row=3)
ttk.Button(frm, text="5", command=lambda: inserir("5")).grid(column=1, row=3)
ttk.Button(frm, text="6", command=lambda: inserir("6")).grid(column=2, row=3)
ttk.Button(frm, text="*", command=lambda: inserir("*")).grid(column=3, row=3)

# Linha 4
ttk.Button(frm, text="1", command=lambda: inserir("1")).grid(column=0, row=4)
ttk.Button(frm, text="2", command=lambda: inserir("2")).grid(column=1, row=4)
ttk.Button(frm, text="3", command=lambda: inserir("3")).grid(column=2, row=4)
ttk.Button(frm, text="-", command=lambda: inserir("-")).grid(column=3, row=4)

# Linha 5
ttk.Button(frm, text=".", command=lambda: inserir(".")).grid(column=0, row=5)
ttk.Button(frm, text="0", command=lambda: inserir("0")).grid(column=1, row=5)
ttk.Button(frm, text="=", command=calcular).grid(column=2, row=5)
ttk.Button(frm, text="+", command=lambda: inserir("+")).grid(column=3, row=5)

root.mainloop()