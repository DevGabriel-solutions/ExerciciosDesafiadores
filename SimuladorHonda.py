import math
from tkinter import *
from tkinter import ttk

def calcular_parcela(prestamo, taxa_mensal, n_meses):
    i = taxa_mensal
    n = n_meses
    if i == 0:
        return prestamo / n # caso sem juros
    pmt = prestamo * (i * (1+ i)**n) / ((1 +i) ** n - 1)
    return pmt

def formatar_moeda(v):
    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def calcular():
    try:
        valor = float(entry_valor.get().replace(",", "."))
        entrada = entry_entrada.get().strip()
        if entrada:
            entrada = float(entrada.replace(",", "."))
        else:
            entrada = 0.0
        taxa_juros_ano = float(entry_juros.get().replace(",", ".")) # em % ao ano ou ao mês?
        n = int(entry_parcelas.get())

        if modo == "anual":
            taxa_mensal = taxa_juros_ano / 100.0 / 12.0
        else:
            taxa_mensal = taxa_juros_ano / 100.0

        valor_financiado = valor - entrada
        if valor_financiado <= 0:
            raise ValueError("valor financiado invalído")

        pmt = calcular_parcela(valor_financiado, taxa_mensal, n)
        total_pago = pmt * n
        juros_totais = total_pago - valor_financiado

        lbl_resultado.config(text=
            f"Parcela mensal: {formatar_moeda(pmt)}\n"
            f"Total pago: {formatar_moeda(total_pago)}\n"
            f"Juros totais pagos: {formatar_moeda(juros_totais)}"
        )
    except Exception as e:
        lbl_resultado.config(text=f"Erro - verifique os valores inseridos")

root = Tk()
root.title("Simulador Honda")

frm = ttk.Frame(root,padding=10)
frm.grid()

ttk.Label(frm, text="Valor do bem: R$ ").grid(row=0, column=0,sticky=W)
entry_valor = ttk.Entry(frm)
entry_valor.grid(row= 0, column=1)

ttk.Label(frm, text="Entrada: R$").grid(row=1, column=0,sticky=W)
entry_entrada = ttk.Entry(frm)
entry_entrada.grid(row=1, column=1)

ttk.Label(frm, text= "Taxa de juros:").grid(row=2, column=0,sticky=W)
entry_juros = ttk.Entry(frm)
entry_juros.grid(row=2, column=1)

var_tipo = StringVar(value="mensal")
modo = var_tipo.get()
ttk.Radiobutton(frm,text= "mensal(%)", variable=var_tipo, value="mensal").grid(row=2, column=2)
ttk.Radiobutton(frm,text= "anual(%)", variable=var_tipo, value="anual").grid(row=2, column=3)

ttk.Label(frm, text="Número de parcelas (meses): ").grid(row=3, column=0,sticky=W)
entry_parcelas = ttk.Entry(frm)
entry_parcelas.grid(row=3, column=1)

ttk.Button(frm, text="Calcular", command=calcular).grid(row=4, column=0, columnspan=2,pady=5)

lbl_resultado = ttk.Label(frm, text="")
lbl_resultado.grid(row=5, column=0,columnspan=4)

root.mainloop()
