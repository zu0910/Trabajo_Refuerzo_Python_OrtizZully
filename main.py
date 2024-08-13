import json 

def Openmenu():
    info=[]
    with open("menu.json", encoding="utf8") as openfile:
        info=json.load(openfile)
        return info
def Savemenu(midato):
    with open("menu.json", "w") as mysave:
        json.dump(midato,mysave)
        
def Openpagos():
    info=[]
    with open("pagos.json", encoding="utf8") as openfile:
        info=json.load(openfile)
        return info
def Savepagos(midato):
    with open("pagos.json", "w") as mysave:
        json.dump(midato,mysave)


def Openpedidos():
    info=[]
    with open("pedidos.json", encoding="utf8") as openfile:
        info=json.load(openfile)
        return info
def Savepedidos(midato):
    with open("pedidos.json", "w") as mysave:
        json.dump(midato,mysave)
    
booleanito=True
while booleanito==True:

    print("""
///////////////////////////////////////////////////////////////////
-------------------------  MOLIPOLLITO  ---------------------------
                    Bienvenidso a MoliPollito
          1). Realizar pedido.
          0). Finalizar
-------------------------------------------------------------------         
""")
    opc=int(input("Ingresa una de las opciones anteriores: \n"))
    
    booleanito2=True
    while booleanito==True:

        if opc==1:
            print("""
            ------------- EJECUCIÓN DE PEDIDOS ---------------
                1). Ver menu
                2). Realizar pedido
            --------------------------------------------------
            """)
            opci=int(input("Ingresa la opción que desees realizar: \n"))
            if opci==1:
                menucito=Openmenu()
                print(" ---------------- MENUS -----------------------")
                print(" __________________ ENTRADA __________________ \n")
                for i in menucito["menu"]:
                    if i["categoria"]=="entrada":
                        print(" - " , i["nombre"], "  $" , i["precio"])
                        print("")

                print(" __________________ PLATO FUERTE  _______________\n ")
                for i in menucito["menu"]:
                    if i["categoria"]=="plato_fuerte":
                        print(" - " , i["nombre"], "  $" , i["precio"])
                        print("")

                print(" __________________ BEBIDA ________________________\n ")
                for i in menucito["menu"]:
                    if i["categoria"]=="bebida":
                        print(" - " , i["nombre"], "  $" , i["precio"])
                        print("")

            elif opci==2:

                NomClien=input("Por favor ingresa su nombre: \n")

                print("------------- WELCOME ",NomClien," ----------------")
                print("""
                     ¿Que categoria deseas pedir primero?: \n
                      a. Entrada
                      b. Plato fuerte
                      c. Bebida
                """)
                cate=input("Ingrese la categoria deseada: \n")
                if cate=="a":
                    menucito=Openmenu()
                    pedidos=Openpedidos()

                    print(" __________________ ENTRADA __________________ \n")
                    for i in menucito["menu"]:
                        if i["categoria"]=="entrada":
                            print(" - ", i["nombre"], "  $", i["precio"])
                            print("")

                    NomEntra=input("Por favor ingrese el nombre del plato de entrada: ")
                    for i in menucito["menu"]:
                        if i["nombre"]==NomEntra:
                            pedidos.append({"cliente": NomClien, "items": {"categoria":i["categoria"], "nombre":i["nombre"],"precio": i["precio"]}})
                    Savepedidos(pedidos)
                     
                elif cate=="b":
                    menucito=Openmenu()
                    print(" __________________ PLATO FUERTE __________________ \n")
                    for i in menucito["menu"]:
                        if i["categoria"]=="entrada":
                            print(" - ", i["nombre"], "  $", i["precio"])
                            print("")
                    NomPlato=input("Por favor ingrese el nombre del plato fuerte: ")

                elif cate=="c":
                    menucito=Openmenu()
                    print(" __________________ BEBIDAS __________________ \n")
                    for i in menucito["menu"]:
                        if i["categoria"]=="entrada":
                            print(" - ", i["nombre"], "  $", i["precio"])
                            print("")
                    NomBebi=input("Por favor ingrese el nombre de la bebida: ")
                    print("")
                







