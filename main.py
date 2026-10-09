
productos = [
    [],
    [],
] # [[],[],[]]

while True:
    print("="*30) # <-  ==================================
    print("Sistema de getion de productos") 
    print("="*30) # <-  ==================================
    print("""
    1. Agregar productos
    2. Mostrar productos
    3. Buscar producto
    4. Eliminar producto
    5. Salir
    """)  

    opcion = input("Elegi una opción (1-5): ").strip()  #"     1    " 

    if opcion == "1":
        
        print("--- Agregar producto ---")
        # validaciones de los datos agregados

        nombre = input("Nombre del producto: ").strip() # ""
        while nombre == "":
            print("Error: el nombre no puede estar vacio.")
            nombre = input("Nombre del producto: ").strip()

        categoria = input("Categoria del producto: ").strip() # ""
        while categoria == "":
            print("Error: la categoria no puede estar vacia.")
            categoria = input("Categoria del producto: ").strip()

        precio_str = input("Precio (sin centavos): ").strip()
        while not precio_str.isdigit():
            print("Error: ingresa solo numeros positivos.")
            precio_str = input("Precio (sin centavos): ").strip()
        precio = int(precio_str)

        datos = [nombre,categoria,precio]
        productos.append(datos)

    elif opcion == "2":  
        print("--- lista de productos ---") 
        # [  
        #  0 -> [ 0 -> mouse ,1 -> asdadsa,2 -> 123123 ] , 
        #   [teclado, categoria, precio] ,  
        # [mate, categoria, precio]   
        # ]

        if len(productos) == 0:
            print("Todavia no hay productos cargados.")
        else:
            for i in range(len(productos)):  # 3  -> i = 0 , i = 1 , i = 2
                print(f"ID:{i+1}\n-Nombre: {productos[i][0]}\n-Categoria: {productos[i][1]}\n-Precio: ${productos[i][2]}")

    elif opcion == "3":
        print("--- Buscar producto ---")

        if len(productos) == 0:
            print("Todavia no hay productos cargados.")
        else:
            busqueda = input("Nombre del producto a buscar: ").strip().lower()

            while busqueda == "":
                print("Error: escribi algo para buscar")
                busqueda = input("Nombre del producto a buscar: ").strip().lower() # moUse

            encontrado = 0
            for i in range(len(productos)): # 0 -> mouse 1 2 
                if busqueda in productos[i][0].lower():
                    print(f"ID:{i+1}\n-Nombre: {productos[i][0]}\n-Categoria: {productos[i][1]}\n-Precio: ${productos[i][2]}")
                    encontrado += 1

            if encontrado == 0:
                print("No se encontra ningun resultado.")
            else:
                print(f"Productos encontrados {encontrado}")


    elif opcion == "4":
        print("--- Eliminar producto ---")
        if len(productos) == 0:
            print("Todavia no hay productos cargados.")
        else:
            for i in range(len(productos)):
                print(f"{i+1}. {productos[i][0]} - {productos[i][1]} - ${productos[i][2]}")  

            id_elminar = input("Numero de producto a elminar: ").strip()

            while not id_elminar.isdigit():
                print("Error: ngresa un numero")
                id_elminar = input("Numero de producto a elminar: ").strip()
            posicion = int(id_elminar) - 1
            # ["algo",[nombre,categoria,precio]].pop(1) -> [nombre,categoria,precio]
            eliminado = productos.pop(posicion)
            print(f"se elimino el producto: {eliminado[0]} ")

    elif opcion == "5":
        print("¡Gracias por usar esta beta XD!")
        break

    else:
        print("Opcion no valida. tenes que elegir entre (1-5)")
