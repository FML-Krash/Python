def menu_Agenda():
    print("\n\nAgenda:\n1 - Mostrar\n2 - Apagar\n3 - Adicionar\n4 - Atualizar\n5 - Sair\n\n")

def mostrar_Contactos():
    for x, y in contactos.items():
        print("{} : {}".format(x, y))

def apagar_Contactos():
    c=0
    try:
        c=(input("Qual o Contacto a eliminar: "))
        del contactos["contacto" + c]
    except:
        print("Contacto Inexistente.")

def adicionar_Contactos():
    nome =(input("Qual o nome do Contacto: "))
    telefone =(input("Qual o Contacto: "))
  
    for y in contactos:
        id=int(y[8])+1
    contactos.update({"contacto" + str(id) + "": {"nome": nome, "telefone": telefone}})

def atualizar_Contactos():
    id=str(input("Qual o conctacto a atualizar: "))
    nome=str(input("Qual o nome: "))
    telefone=str(input("Qual o número de Contacto: "))
    contactos.update({"contacto"+id:{"nome":nome,"telefone":telefone}})


def opcoes(x):
    if x==1:
        mostrar_Contactos()
    elif x==2:
        apagar_Contactos()
    elif x==3:
        adicionar_Contactos()
    elif x==4:
        atualizar_Contactos()
    elif x==5:
        exit()
    else:
        print("Escolha Inválida!!")

escolha = 0
contactos = {
    "contacto1": {
        "nome": "Mauro",
        "telefone": "*********"
},
    "contacto2": {
        "nome": "Sandra",
        "telefone": "*********"
    }
}
while True:
    menu_Agenda()
    try:
        escolha=int(input("Escolha uma Opcao: "))
    except:
        print("Opção Invalida")
    opcoes(escolha)
