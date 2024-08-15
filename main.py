import json
from datetime import datetime
from os import system # Limpiar pantalla

def Openmenu():#Abre el json del menu 
    with open("menu.json", encoding="utf8") as openfile:
        return json.load(openfile)

def Openpagos():
    with open("pagos.json", encoding="utf8") as openfile:
        return json.load(openfile)

def Savepagos(midato):#Guarda los nuevos datos en ese json
    with open("pagos.json", "w") as mysave:
        json.dump(midato, mysave)

def Openpedidos():
    with open("pedidos.json", encoding="utf8") as openfile:
        return json.load(openfile)

def Savepedidos(midato):
    with open("pedidos.json", "w") as mysave:
        json.dump(midato, mysave)


def cambiar_estado(pedido, NewStatus):#Con esta funcion hace cambiar el estado de un pedido a un nuevo estado dependiento al que el cliente eliga teniendo encuenta ciertas condiciones 
    if NewStatus == "servido" and pedido["estado"] == "pagado":
        pedido["estado"] = NewStatus # Cambia el estado del pedido a "servicio" solo si el estado actual es pagado
    elif NewStatus in ["preparacion", "servido", "cancelado"]:
        if NewStatus == "cancelado" and pedido["estado"] == "creado":# si el nuevo estado es cancelado el estado actual del cliente debe ser creado, el pido solo se puede cancelar si no lo pagado
            pedido["estado"] = NewStatus
        elif pedido["estado"] != "cancelado":
            pedido["estado"] = NewStatus
    else:
        print("No se puede cambiar al estado solicitado.")# si el nuevo estado no cumple con las condiciones se le imprimatra eso

def registrar_pago(cliente, monto):# Realiza el pago realizado por un cliente y lo guarda en el archivo de json pagos
    pagos = Openpagos()
    fecha_pago = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pagos.append({"cliente": cliente, "total": monto, "fecha_pago": fecha_pago})# crea un nuevo registro de pago donde se guardara el nombre del cliente, el total de lo pedido y la fecha y hora del pago 
    Savepagos(pagos)# se guardara los nuevos datos al json de pagos

def calcular_total(pedido):
    return sum(item["precio"] for item in pedido["items"])# en el json de pedidos lo que va hacer es contar todos las cosas que pidio cliente realizando una suma  y extraera su precio


booleanito = True
while booleanito:# Mientras el booleanito sea verdadero se hara 
    # Menu principal 
    print("""
///////////////////////////////////////////////////////////////////
-------------------------  MOLIPOLLITO  ---------------------------
                    Bienvenidos a MoliPollito
          1). Realizar pedido
          2). Consultar pedido
          3). Cambiar estado de pedido
          4). Registrar pago
          5). Cancelar pedido
          0). Finalizar
-------------------------------------------------------------------         
""")
    opc = int(input("Ingresa una de las opciones anteriores: \n"))
    system("clear")
    #Si la opcion eslegida es uno se hara:
    if opc == 1:
        #Primero le pedira el nombre a la persona que se le va a atender
        nomClien= input("Por favor ingresa su nombre: \n")
        #Se guarda el nombre y su estado pasa a ser creado
        pedido = {"cliente": nomClien, "items": [], "estado": "creado"}
        # se crea un ssegundo booleano ya que utilizare un submenu
        booleanito2 = True
        while booleanito2:
            # sub menu
            print("            ---------------- Welcome", nomClien , "---------------" )
            print("""
            ¿Qué categoría deseas pedir?: 
                  
                a. Entrada
                b. Plato fuerte
                c. Bebida
                d. Finalizar pedido
                  
            -------------------------------------------
            """)
            print("")
            cate = input("Ingrese la categoría deseada: \n")
            system("clear")
            menucito = Openmenu()#Abrira el json de menu
            #Depende de la opcion que el cliente ejecuta se le mostrara los nombres y precios de cada categoria y le preguntara que el nombre del plato que guste comprar
            if cate == "a":
                print(" __________________ ENTRADA __________________ \n")
                #para i en menucito que es el json menu
                for i in menucito["menu"]:
                    #aca solo le imprimira las cateteteref vjnvdfn
                    if i["categoria"] == "entrada":
                        print(f" - {i['nombre']}  $ {i['precio']}\n")
                
                NomPlato = input("Por favor ingrese el nombre del plato de entrada: \n")
                print("")
                for i in menucito["menu"]:
                    if i["nombre"] == NomPlato:
                        pedido["items"].append(i)
                        print(f"{i['nombre']} añadido al pedido.")

                system("clear")

            elif cate == "b":
                print(" __________________ PLATO FUERTE __________________ \n")
                for i in menucito["menu"]:
                    if i["categoria"] == "plato_fuerte":
                        print(f" - {i['nombre']}  $ {i['precio']} \n")
                
                NomPlato = input("Por favor ingrese el nombre del plato fuerte: \n")
                print("")
                for i in menucito["menu"]:
                    if i["nombre"] == NomPlato:
                        pedido["items"].append(i)
                        print(f"{i['nombre']} añadido al pedido.")
                
                system("clear")
                
            elif cate == "c":
                print(" __________________ BEBIDAS __________________ \n")
                for i in menucito["menu"]:
                    if i["categoria"] == "bebida":
                        print(f" - {i['nombre']}  $ {i['precio']} \n")
                print("")
                
                NomPlato = input("Por favor ingrese el nombre de la bebida: \n")
                for i in menucito["menu"]:
                    if i["nombre"] == NomPlato:
                        pedido["items"].append(i)
                        print(f"{i['nombre']} añadido al pedido.")

                system("clear")
            
            elif cate == "d":
                pedidos = Openpedidos()
                pedidos.append(pedido)
                Savepedidos(pedidos)
                print("Pedido guardado exitosamente.")
                booleanito2 = False

                system("clear")
            
            else:
                print("Opción inválida. Intente de nuevo.")
    
    elif opc == 2:
        pedidos = Openpedidos()
        cliente = input("Ingresa el nombre del cliente: \n")

        system("clear")

        for pedido in pedidos:
            if pedido["cliente"]== cliente:
                print("-------------- HISTORIAL ---------------")
                print("   Pedido de ", pedido["cliente"])
                print("   El orden de tu pedido es:")
                for item in pedido["items"]:
                    print(f" - {item['nombre']} ($ {item['precio']})")
                print("\n")

        system("clear")
    
    elif opc == 3:
        pedidos = Openpedidos()
        cliente = input("Ingresa el nombre del cliente: \n")
        print("")
        system("clear")
        for i in pedido: 
            if pedido["cliente"] == cliente:
             print("Estado del pedido:", pedido["estado"])
             print("")
        NewStatus = input("Ingresa el nuevo estado (preparacion, servido, cancelado): \n")
        print("")
        
        for pedido in pedidos:
            if pedido["cliente"] == cliente:
                cambiar_estado(pedido, NewStatus)
                Savepedidos(pedidos)
                print("")
                print(f"Estado del pedido de {cliente} actualizado a {NewStatus}.")
        system("clear")
    elif opc == 4:
        pedidos = Openpedidos()
        cliente = input("Ingresa el nombre del cliente para registrar el pago: \n")
        system("clear")
        for pedido in pedidos:
            if pedido["cliente"] == cliente and pedido["estado"] != "pagado":
                total = calcular_total(pedido)
                registrar_pago(cliente, total)
                pedido["estado"] = "pagado"
                Savepedidos(pedidos)
                print("")
                print(f"Pago registrado para {cliente} por un total de ${total}.")
        system("clear")
    elif opc == 5:
        pedidos = Openpedidos()
        cliente = input("Ingresa el nombre del cliente para cancelar el pedido: \n")
        system("clear")
        for pedido in pedidos:
            if pedido["cliente"] == cliente and pedido["estado"] == "creado":
                pedido["estado"] = "cancelado"
                Savepedidos(pedidos)
                print("")
                print(f"Pedido de {cliente} cancelado exitosamente.")
        system("clear")
    elif opc == 0:
        print("¡Gracias por usar MoliPollito! ¡Hasta luego!")
        booleanito = False
    
