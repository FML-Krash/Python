from tkinter import *


def calcular():
    if(radioValue.get() == 1):
        try:
            res=int(inValor1.get())+int(inValor2.get())
            lbl03.config(text=res)
        except:
            lbl03.config(text="Um dos valores esta incorreto.")
        return
    if(radioValue.get() == 2):
        try:
            res = int(inValor1.get()) - int(inValor2.get())
            lbl03.config(text=res)
        except:
            lbl03.config(text="Um dos valores esta incorreto.")
        return
    if(radioValue.get() == 3):
        try:
            res = int(inValor1.get()) * int(inValor2.get())
            lbl03.config(text=res)
        except:
            lbl03.config(text="Um dos valores esta incorreto.")
        return
    if(radioValue.get() == 4):
        try:
            res = int(inValor1.get()) / int(inValor2.get())
            lbl03.config(text=res)
        except:
            lbl03.config(text="Um dos valores esta incorreto.")
        return


app = Tk()
radioValue = tkinter.IntVar()
app.title("Calculadora")
app.geometry("500x300")

lbl01 = Label(app, text="Valor 1")
lbl02 = Label(app, text="Valor 2")
lbl03 = Label(app, text="Resultado")

inValor1 = tkinter.Entry(app, width=200)
inValor2 = tkinter.Entry(app, width=200)

rd1 = tkinter.Radiobutton(app, text='Somar', variable=radioValue, value=1, command=calcular)
rd2 = tkinter.Radiobutton(app, text='Subtrair', variable=radioValue, value=2, command=calcular)
rd3 = tkinter.Radiobutton(app, text='Multiplicar', variable=radioValue, value=3, command=calcular)
rd4 = tkinter.Radiobutton(app, text='Dividir', variable=radioValue, value=4, command=calcular)


lbl01.pack()
inValor1.pack()
lbl02.pack()
inValor2.pack()

rd1.pack()
rd2.pack()
rd3.pack()
rd4.pack()

lbl03.pack()

app.mainloop()
