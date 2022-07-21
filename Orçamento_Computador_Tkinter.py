from tkinter import *

def calcular():
    valorIva = 0
    subTotal = 0
    valorTotal = 0

    if section_1.get() == 1:
        valorRam = 60
    else:
        valorRam = 100

    if section_2.get() == 1:
        valorCpu = 340
    else:
        valorCpu = 390

    if section_3.get() == 1:
        valorDisco = 80
    else:
        valorDisco = 100

    if section_4.get() == 1:
        valorMotherBoard = 120
    else:
        valorMotherBoard = 100

    if section_5.get() == 1 and section_6.get() == 1:
        valorMontagem = 50
        valorEntrega=20
    elif section_5.get() == 1 and section_6.get() == 0:
        valorMontagem = 50
        valorEntrega = 0
    elif section_5.get() == 0 and section_6.get() == 1: 
        valorEntrega = 0
        valorMontagem = 20
    else:
        valorEntrega = 0
        valorMontagem = 0


    subTotal = valorRam + valorCpu + valorDisco + valorMotherBoard + valorMontagem + valorEntrega
    valorIva = subTotal * 0.23
    valorTotal = subTotal + valorIva

    varSubTotal.set("{:,.2f} €".format(subTotal))
    varIva.set("{:,.2f} €".format(valorIva))
    varTotal.set("{:,.2f} €".format(valorTotal))

app = Tk()
app.title("Orcamento - Computador")
app.geometry("700x500")

#Frames Conteudo

frame_1 = LabelFrame(app, text="RAM",)
frame_1.place(x=15, y=15, width=200, height=120)

frame_2 = LabelFrame(app, text="CPU")
frame_2.place(x=15, y=135, width= 200,height= 120)

frame_3 = LabelFrame(app, text="Capacidade de Disco")
frame_3.grid(row=0, column=1, padx=10)
frame_3.place(x=220, y=15, width= 200,height= 120)

frame_4 = LabelFrame(app, text="MotherBoard")
frame_4.grid(row=1, column=1, padx=10)
frame_4.place(x=220, y=135, width= 200,height= 120)

frame_5 = LabelFrame(app, text="Outros")
frame_5.grid(row=0, column=2, padx=10)
frame_5.place(x=425, y=15, width= 200,height= 120)

frame_6 = LabelFrame(app, text="Total")
frame_6.grid(row=1, column=2, padx=10)
frame_6.place(x=425, y=135, width= 200,height= 120)

#Labels

label_1 = Label(frame_6, text="Subtotal:")
label_1.grid(row=1,column=0)

label_2 = Label(frame_6, text="IVA:")
label_2.grid(row=2, column=0)
label_3 = Label(frame_6, text="Total:")
label_3.grid(row=3, column=0)

varSubTotal = StringVar()
varIva = StringVar()
varTotal = StringVar()

text_1 = Label(frame_6, borderwidth=1, relief="solid", textvariable = varSubTotal, width=15)
text_1.grid(row=1, column=1)

text_2 = Label(frame_6, borderwidth=1, relief="solid", textvariable = varIva, width=15)
text_2.grid(row=2, column=1)

text_3 = Label(frame_6, borderwidth=1, relief="solid", textvariable = varTotal, width=15)
text_3.grid(row=3, column=1)

# RadioButton_Value

section_1 = IntVar()
section_2 = IntVar()
section_3 = IntVar()
section_4 = IntVar()

# CheckBox_Value

section_5 = IntVar()
section_6 = IntVar()

Radiobutton(frame_1, text="8 GB", variable=section_1, value=1).pack()
Radiobutton(frame_1, text="16 GB", variable=section_1, value=2).pack()

Radiobutton(frame_2, text="AMD", variable=section_2, value=1).pack()
Radiobutton(frame_2, text="Intel", variable=section_2, value=2).pack()

Radiobutton(frame_3, text="1 TB", variable=section_3, value=1).pack()
Radiobutton(frame_3, text="2 TB", variable=section_3, value=2).pack()

Radiobutton(frame_4, text="Asus", variable=section_4, value=1).pack()
Radiobutton(frame_4, text="Asrock", variable=section_4, value=2).pack()

montagem=Checkbutton(frame_5, text="Montagem", variable=section_5, onvalue=1, offvalue=0).pack()
entrega=Checkbutton(frame_5, text="Entrega", variable=section_6, onvalue=1, offvalue=0).pack()

button = Button(frame_6, text="Calcular", command=calcular)
button.grid(row=0,column=1)

app.mainloop()
