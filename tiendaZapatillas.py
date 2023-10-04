def MenuInicial ():
    print ('\n--------------------------')
    print ('        MOLT STORE')
    print ('==========================')
    print ('[1] Ver catálogo completo')
    print ('[2] Buscar por marca')
    print ('[3] Buscar por talle')
    print ('[4] Agregar/Eliminar modelo')
    print ('[0] Para salir')
    print ('==========================')
    return

def OpenFile(path='./stock.txt'):
    import os.path
    if os.path.exists(path):
        archivo = open(path, 'r')
        return archivo.readlines()
    else:
        return None

def Catálogo (Contenido):
    Contador = 1
    Marcas = []
    Modelos = []
    Precios = []
    print('  \tMarca\t\t Modelo')
    for i in Contenido:
        if '-' not in i and 'Marca' not in i:
            i = i.replace('\n', '')
            i = i.replace(' ', '')
            Catálogo = i.split(',')
            print ('\n[',Contador, ']', '\t' ,Catálogo[0], '\t\t',Catálogo[1],sep = '',end = '')
            Contador = Contador + 1
            Marcas.append(Catálogo[0])
            Modelos.append(Catálogo[1])
            Precios.append(Catálogo[2])
    print ('\n=======================================')
    return Marcas,Modelos,Precios

def BuscarPorMarca(Contenido, Marca):
    Modelos = []
    Precios = []
    for x in Contenido: 
        if '-' not in x:
            if Marca in x:
                linea = x.split(Marca)[1]
                linea = linea.replace(',', '',1)
                linea = linea.replace(' ', '')
                linea = linea.replace('\n', '')
                lista = linea.split(',')
                Modelos.append(lista[0])
                Precios.append(lista[1])
    return Modelos, Precios

def MenúMarcas():
    print ('\n__________________') #Imprime el menú de búsqueda por marca
    print ('Búsqueda por marca')
    print ('==================')
    print ('[1] Adidas')
    print ('[2] Nike')
    print ('[3] Puma') 
    print ('[4] Vans')
    print ('[5] "Volver"')
    print ('==================')

def MenuAgregarEliminar():
    print ('\n=========================') #Imprime el menú para agregar/eliminar un modelo
    print ('[1] Agregar un modelo')
    print ('[2] Eliminar un modelo')
    print ('[0] Volver')
    print ('=========================')
    entrada = (input('\nElija una opción: '))
    return entrada

def ListaDeModelos(Modelos_precios,Contenido):
    contador = 0
    print ("\nLista de modelos:")
    for i in Modelos_precios[0]:
        Modelo = i
        print ('____________________________________________')
        print ('\n>',i,'\t','$' + Modelos_precios[1][contador])
        contador = contador +1
        Modelos = ImprimirTalles(Contenido,Modelos_precios,Modelo)
    print ('____________________________________________\n')
    return Modelos

def ImprimirTallesModelo(Marca,Modelo,Contenido):
    print ('\nUsted eligió',Marca, Modelo) #Imprime los talles y unidades del modelo seleccionado
    print ("\nTalles\t | Disponibilidad")
    TallesCantidad = TallesUnidades(Contenido, Modelo)
    contador = 0
    indice = len(TallesCantidad)
    while True:
        print ('-',TallesCantidad[contador],'\t','|','  -', TallesCantidad[contador+1])
        contador = contador + 2
        if indice == contador:
            break

def TallesUnidades (Contenido, Modelo):
    TallesCantidad = [] #Primero se agrega el talle y en la siguiente posición las unidades
    for x in Contenido:
        if Modelo in x:
            if '-' in x:
                linea = str(x)
                linea = linea.replace('-', '')
                linea = linea.replace(Modelo, '')
                linea = linea.replace(',', '', 1)
                linea = linea.replace(' ', '')
                linea = linea.replace('\n', '')
                lista = linea.split(',') #Se eliminan elementos que no queremos y se hace una lista con el talle y sus unidades
                for y in lista:
                    TallesCantidad.append(y)  
    return TallesCantidad

def ImprimirTalles(Contenido, ListaModelos, Modelo):
    Modelos = []
    for i in ListaModelos[0]:
        Modelos.append(i)
        if i == Modelo:
            TallesCantidad = TallesUnidades(Contenido, Modelo)
            contador = 0
            indice = len(TallesCantidad)
            while True:
                contador = contador + 2
                if indice == contador:
                    break
    return Modelos

def ModificarStock(Modelo, Talle, Unidades, Contenido, Entrada):
    import os
    #Se restan las unidades correspondientes al archivo txt del stock
    Linea_mod = []
    Unidades = int(Unidades) - int(Entrada)
    Linea = (Modelo,Talle,Unidades)
    Linea_mod = '-'+str(Linea)
    Linea_mod = Linea_mod.replace('(', '')
    Linea_mod = Linea_mod.replace(')', '')
    Linea_mod = Linea_mod.replace("'", '')

    archivo = open("modificación.txt", "w")

    for linea in Contenido:
        if Modelo not in linea:
            archivo.write(linea)
        elif str(Talle) in linea:
            archivo.write(str(Linea_mod))
            archivo.write("\n")
        else:
            archivo.write(linea)

    archivo.close()
    os.replace('modificación.txt', 'stock.txt') #Se reemplaza el archivo modificado por el original

def BuscarTalleModelo(Modelo, TalleEntrada, Contenido):
    Talle = []
    Unidad = []
    for x in Contenido:
        if Modelo in x:
            if '-' in x:
                if str(TalleEntrada) in x:
                    linea = str(x)
                    linea = linea.replace('-', '')
                    linea = linea.replace(Modelo, '')
                    linea = linea.replace(',', '', 1)
                    linea = linea.replace(' ', '')
                    linea = linea.replace('\n', '')
                    lista = linea.split(',')
                    Talle.append(lista[0])
                    Unidad.append(lista[1])
    return Talle, Unidad

def BuscarPorTalle(Talle,Contenido):
    Modelos = []
    Precios = []
    Marcas = []
    for x in Contenido:
        if '-' in x:
            if Talle in x:
                linea = str(x)
                linea = linea.replace('-', '')
                linea = linea.replace(' ', '')
                linea = linea.replace('\n', '')
                lista = linea.split(',')
                Unidades = int(lista[2])
                if Unidades > 0:
                    Modelos.append(lista[0])
    for i in Modelos:
        for x in Contenido:
            if i in x:
                if '-' not in x:
                    linea = str(x)
                    linea = linea.replace(' ', '')
                    linea = linea.replace('\n', '')
                    lista = linea.split(',')
                    Marcas.append(lista[0])
                    Precios.append(lista[2])
    return Modelos, Precios, Marcas

def TallesStock (Contenido, Modelos, modelo, entrada_talle):
    for x in Contenido:
        lista = x.split(',')
        if '-' + Modelos[int(modelo) - 1] in lista:
            if ' ' + entrada_talle in lista:
                Talle = lista[1]
                Unidades = lista[2]
                Talle = Talle.replace(' ','')
                Unidades = Unidades.replace(' ', '')
                Unidades = Unidades.replace('\n','')
                Unidades = Unidades.replace(' ', '')
    return Talle, Unidades

def OpcionSalir():
    print ("\n____________________________________")
    print ("\n[1] Volver al 'Menú Principal':")
    print ("[2] Salir:")
    return

def AgregarModelo(Marca,Modelo,Talles,Unidades,Precio):
    archivo = open('stock.txt','a')
    linea1 = Marca + ', ' + Modelo + ', ' + Precio
    cantidad = len(Talles)
    contador = 0
    archivo.write(linea1)
    archivo.write('\n')
    while contador != cantidad:
        archivo.write('-'+Modelo + ', ' + Talles[contador] + ', ' + Unidades[contador])
        archivo.write('\n')
        contador = contador + 1

def BorrarModelo(Modelo,Contenido):
    import os
    archivo = open("modificación.txt", "w")
    for linea in Contenido:
        if Modelo not in linea:
            archivo.write(linea)
    archivo.close()
    os.replace('modificación.txt', 'stock.txt')

def Ticket(Marca,Modelo,Precio,Talle,Cantidad):
    print ('\n=======================================================')
    print ('                      MOLT STORE                        ')
    print ('=======================================================')
    print ('['+Cantidad+']',Marca,Modelo,'talle',Talle,'\t$',Precio)
    print ('\nSubtotal:\t\t\t$',int(Cantidad)*int(Precio))
    print ('\n     IVA:\t\t\t$',(int(Cantidad)*int(Precio)*21/100))
    print ('-------------------------------------------------------')
    print ('\n   Total:\t\t\t$',int(Cantidad)*int(Precio)+(int(Cantidad)*int(Precio)*21/100))
    print ('=======================================================')

Bucle = 1
while Bucle == 1:
    MenuInicial ()
    Entrada = input("\nIngrese el número de la operación: ")
    if Entrada.isdigit() == False:
        print ('\nOpción no válida\n' , end = '')
        continue
    if Entrada == '1':
        Contenido = OpenFile()
        if Contenido == None:
            print ('\nEl archivo no existe')
        else:
            print ('\n=======================================')
            MarcasModelos = Catálogo(Contenido)
            Marcas = MarcasModelos[0]
            Modelos = MarcasModelos[1]
            Precios = MarcasModelos[2]
            Entrada = (input ('\nElija el modelo que desea: '))
            if Entrada.isdigit() == False:
                print ('\nOpción no válida\n' , end = '')
                continue
            if int(Entrada) <= len(Modelos) and int(Entrada) >= 0:
                Marca = Marcas[int(Entrada)-1]
                Modelo = Modelos[int(Entrada)-1]
                Precio = Precios[int(Entrada)-1]
                ImprimirTallesModelo(Marca,Modelo,Contenido)
                Entrada = input('\n¿Le interesa el modelo? [1 si] [2 no]: ')
                if Entrada.isdigit() == False:
                    print ('\nOpción no válida\n' , end = '')
                    continue
                if Entrada == '1':
                    Talle = (input('\n¿Qué talle quiere llevar?: '))
                    if Talle.isdigit() == False:
                        print ('\nOpción no válida\n' , end = '')
                        continue
                    if int(Talle)<10:
                        print ('\nOpción no válida\n' , end = '')
                        continue
                    ListaTallesUnidades = BuscarTalleModelo(Modelo, Talle, Contenido)
                    if ListaTallesUnidades == ([], []):
                        print('\nNo hay stock de ese talle.')
                        OpcionSalir()
                        entrada = (input('\nIngrese la opción que desea: '))
                        if entrada.isdigit() == False:
                            print ('\nOpción no válida\n' , end = '')
                            continue
                        if entrada == '1': continue
                        elif entrada == '2': 
                            Bucle = 0
                            break
                        else: 
                            print ('Opción no válida')
                            continue
                    elif int(Talle) < 0:
                        print('\nNo puede ingresar un valor negativo.') 
                    else:
                        for i in ListaTallesUnidades[1]:
                            Unidades = str(i)
                        print('\nHay',Unidades,'unidades disponibles del talle seleccionado')
                        CompraUnidades = (input('\n¿Unidades que desea comprar?: '))
                        if CompraUnidades.isdigit() == False:
                            print ('\nOpción no válida\n' , end = '')
                            continue
                        if int(CompraUnidades) > int(Unidades):
                            print('\nNo hay suficiente stock')
                            continue
                        else: 
                            entrada = (input('\n¿Está seguro de comprar el modelo? [1 si] [2 no]: '))
                            if entrada.isdigit() == False:
                                print ('\nOpción no válida\n' , end = '')
                                continue
                            if entrada == '1':
                                ModificarStock(Modelo, Talle, Unidades, Contenido, CompraUnidades)
                                Ticket(Marca,Modelo,Precio,Talle,CompraUnidades)
                                break
                            elif entrada == '2': break
                            else: 
                                print ('Opción no válida')
                                continue
                elif Entrada == '2': continue
                else: 
                    print ('\nOpción no válida\n' , end = '')
                    continue
            else:
                print ('\nOpción no válida\n' , end = '')
                continue
    elif Entrada == '2':
        Contenido = OpenFile()
        if Contenido == None:
            print('\nEl archivo no existe')
        else:
            while True:
                MenúMarcas()
                Entrada = (input("\nIngrese el número de la operación: "))
                if Entrada.isdigit() == False:
                    print ('\nOpción no válida\n' , end = '')
                    continue
                if Entrada == '1': Marca = 'Adidas'
                elif Entrada == '2': Marca = 'Nike'
                elif Entrada == '3': Marca = 'Puma'
                elif Entrada == '4': Marca = 'Vans'
                elif Entrada == '5': break
                else:
                    print ('\nOpción no válida.' , end = '')
                    continue
                Modelos_precios = BuscarPorMarca(Contenido, Marca)
                Precios = Modelos_precios[1]
                Modelos = ListaDeModelos(Modelos_precios,Contenido)
                entrada = (input('\n¿Le interesa algún modelo? [1 si] [2 no]: '))
                if entrada.isdigit() == False:
                    print ('\nOpción no válida\n' , end = '')
                    continue
                if entrada == '1':
                    contador = 0
                    for i in Modelos:
                        contador = contador + 1
                        print('[',contador,']','\t',i, sep = '')
                    entrada = (input('\nIngrese el número del modelo que desea: '))
                    if entrada.isdigit() == False:
                        print ('\nOpción no válida\n' , end = '')
                        continue
                    if int(entrada) > 0 and int(entrada) <= contador:
                        Modelo = Modelos[int(entrada)-1]
                        Precio = Precios[int(entrada)-1]
                        print('\n¡Usted eligió',Marca,Modelo,'!')
                        entrada = (input('\n¿Qué talle quiere llevar?: '))
                        if entrada.isdigit() == False:
                            print ('\nOpción no válida\n' , end = '')
                            continue
                        if int(entrada) < 0:
                            print('\nNo puede ingresar un valor negativo.')
                            continue
                        if int(entrada) < 10:
                            print('\nDato inválido')
                            continue
                        Talle_Unidad = BuscarTalleModelo(Modelo,entrada, Contenido)
                        if Talle_Unidad == ([], []):
                            print('\nNo hay stock de ese talle.')
                            OpcionSalir()
                            entrada = (input('\nIngrese la opción que desea: '))
                            if entrada.isdigit() == False:
                                print ('\nOpción no válida\n' , end = '')
                                continue
                            if entrada == '1': break
                            elif entrada == '2':
                                Bucle = 0
                                break
                            else: 
                                print ('Opción no válida')
                                break
                        else:
                            Talle = (Talle_Unidad[0][0])
                            Unidades = (Talle_Unidad[1][0])
                            print('\nHay',Unidades,'unidades disponibles del talle seleccionado')
                            CompraUnidades = (input('\n¿Cuántas unidades desea comprar?: '))
                            if CompraUnidades.isdigit() == False:
                                print ('\nOpción no válida\n' , end = '')
                                continue
                            if int(CompraUnidades) > int(Unidades) or int(CompraUnidades) < 0:
                                print('\nNo hay suficiente stock')
                                continue
                            else:
                                entrada = (input ('\n¿Está seguro de hacer la compra? [1 si] [2 no]: '))
                                if entrada.isdigit() == False:
                                    print ('\nOpción no válida\n' , end = '')
                                    continue
                                if entrada == '1':
                                    ModificarStock(Modelo, Talle, Unidades, Contenido, CompraUnidades)
                                    Ticket(Marca,Modelo,Precio,Talle,CompraUnidades)
                                    Bucle = 0
                                    break
                                elif entrada == '2': break
                                else: 
                                    print ('\nOpción no válida\n' , end = '')
                                    continue
                    else:
                        print('\nNo hay stock de ese talle.')
                        OpcionSalir()
                        entrada = int(input('\nIngrese la opcion que desea: '))
                        if entrada == 1: continue
                        elif entrada == 2:
                            Bucle = 0
                            break
                        elif entrada < 1 or entrada > 2: print ('Opcion no valida')
                elif entrada == '2':
                    OpcionSalir()
                    entrada = (input('\nIngrese la opcion que desea: '))
                    if entrada == '1': break
                    elif entrada == '2':
                        Bucle = 0
                        break
                    elif int(entrada) < 1 or int(entrada) > 2: print ('Opcion no valida')
                else: 
                    print ('Opcion no valida')
                    continue
            continue              
    elif Entrada == '3':
        Contenido = OpenFile()
        if Contenido == None:
            print('\nEl archivo no existe')
        else:
            entrada_talle = input(('\n¿Qué talle de zapatilla está buscando? '))
            if entrada_talle.isdigit() == False:
                print ('\nOpción no válida\n' , end = '')
                continue
            Modelos_Precios = BuscarPorTalle(entrada_talle, Contenido)
            Modelos = Modelos_Precios[0]
            Precios = Modelos_Precios[1]
            Marcas = Modelos_Precios[2]
            contador = 0
            if int(entrada_talle) > 10:
                if Modelos_Precios == ([], [], []):
                    print('\nNo hay stock de ese talle.')
                    OpcionSalir()
                    entrada = (input('\nIngrese la opcion que desea: '))
                    if entrada_talle.isdigit() == False:
                        print ('\nOpción no válida\n' , end = '')
                        continue
                    if entrada == '1': continue
                    elif entrada == '2':
                        Bucle = 0
                        break
                    else: 
                        print ('Opcion no valida')
                        continue
                else:
                    print ('_______________________________________')
                    print ('\nEstos son los resultados para el talle elegido [', entrada_talle, ']', sep = '')
                    for i in Modelos:
                        print ('_______________________________________\n')
                        print ('>',Marcas[contador],i+'\t$'+Precios[contador])
                        contador = contador + 1
                    entrada = (input('\n¿Le interesa algún modelo? [1 si] [2 no]: '))
                    if entrada.isdigit() == False:
                        print ('\nOpción no válida\n' , end = '')
                        continue
                    if entrada == '1':
                        contadorMarca = 0
                        contador = 1
                        print()
                        for i in Modelos:
                            print ('[' , contador , ']', ' ', Marcas[contadorMarca], ' ', i, sep = '')
                            contador = contador + 1
                            contadorMarca = contadorMarca + 1
                        modelo = (input('\n¿Qué modelo desea comprar? '))
                        if modelo.isdigit() == False:
                            print ('\nOpción no válida\n' , end = '')
                            continue
                        if int(modelo) > 0 and int(modelo) <= contadorMarca:
                            print ('\n¡Usted eligió' , Marcas[int(modelo) - 1], Modelos [int(modelo) - 1],'!')
                            talle_stock = TallesStock(Contenido, Modelos, modelo, entrada_talle) 
                            Precio = Precios[int(modelo) - 1]
                            Unidades = talle_stock[1]
                            Talle = talle_stock[0]
                            Modelo = Modelos[int(modelo)-1]
                            print('\nHay',Unidades,'unidades disponibles del talle seleccionado')
                            CompraUnidades = (input('\n¿Cuántas unidades desea comprar?: '))
                            if CompraUnidades.isdigit() == False:
                                print ('\nOpción no válida\n' , end = '')
                                continue
                            if int(CompraUnidades) > int(Unidades) or int(CompraUnidades) < 0:
                                print('\nNo hay suficiente stock')
                            else:
                                entrada = (input ('\n¿Está seguro de hacer la compra? [1 si] [2 no]: '))
                                if entrada.isdigit() == False:
                                    print ('\nOpción no válida\n' , end = '')
                                    continue
                                if entrada == '1':
                                    Marca = Marcas[int(modelo) - 1]
                                    Modelo = Modelos [int(modelo) - 1]
                                    ModificarStock(Modelo, Talle, Unidades, Contenido, CompraUnidades)
                                    Ticket(Marca,Modelo,Precio,Talle,CompraUnidades)
                                    break
                                elif entrada == '2':
                                    Bucle = 0
                                    break
                                else: 
                                    print ('\nOpción no válida\n' , end = '')
                                    continue
                    elif entrada == '2':
                        OpcionSalir()
                        entrada = (input('\nIngrese la opcion que desea: '))
                        if entrada.isdigit() == False:
                            print ('\nOpción no válida\n' , end = '')
                            continue
                        if entrada == '1': continue
                        elif entrada == '2':
                            Bucle = 0
                            break
                        else:
                            print ('\nOpción no válida\n' , end = '')
                            continue
                    else:
                        print ('Opción no válida')
                        continue
            else:
                print('\nNo hay stock de ese talle.')
                OpcionSalir()
                entrada = (input('\nIngrese la opción que desea: '))
                if entrada.isdigit() == False:
                    print ('\nOpción no válida\n' , end = '')
                    continue
                if entrada == '1': continue
                elif entrada == '2': break
                else: 
                    print ('Opción no válida')
                    continue
    elif Entrada == '4':
        entrada = MenuAgregarEliminar()
        if entrada.isdigit() == False:
            print ('\nOpción no válida\n' , end = '')
            continue
        if entrada == '1':
            print ('\n=========================')
            print ('\n[1] Adidas')
            print ('[2] Nike')
            print ('[3] Puma') 
            print ('[4] Vans')
            Entrada = (input('\nIngrese la marca: '))
            if Entrada.isdigit() == False:
                print ('\nOpción no válida\n' , end = '')
                continue
            if Entrada == '1': Marca = 'Adidas'
            elif Entrada == '2': Marca = 'Nike'
            elif Entrada == '3': Marca = 'Puma'
            elif Entrada == '4': Marca = 'Vans'
            else: 
                print ('\nOpción no válida\n' , end = '')
                continue
            Modelo = input('Ingrese el modelo: ')
            Precio = (input('Ingrese el precio: '))
            if Precio.isdigit() == False or int(Precio) < 0:
                print ('\nOpción no válida\n' , end = '')
                continue
            Talles = []
            Unidades = []
            while True:
                Talle = input('Ingrese el talle: ')
                if Talle.isdigit() == False or int(Talle) < 0:
                    print ('\nOpción no válida\n' , end = '')
                    break
                else:
                    Talles.append(Talle)
                    Cantidad = input('Ingrese las unidades: ')
                    if Cantidad.isdigit() == False or int(Cantidad) < 0:
                        print ('\nOpción no válida\n' , end = '')
                        break
                    Unidades.append(Cantidad)
                Entrada = (input('[1] Seguir [0] Terminar: '))
                if Entrada.isdigit() == False:
                    print ('\nOpción no válida\n' , end = '')
                    continue
                elif int(Entrada) != 1 and not int(Entrada) == 0:
                    print ('\nOpción no válida\n' , end = '')
                    break
                elif int(Entrada) == 1: continue
                Entrada = (input('\n¿Está seguro que desea agregar el modelo al catálogo? [1 si] [2 no]: '))
                if Entrada.isdigit() == False:
                    print ('\nOpción no válida\n' , end = '')
                    continue
                elif int(Entrada) == 1:
                    print('\n¡Producto agregado con éxito!')
                    AgregarModelo(Marca,Modelo,Talles,Unidades,Precio)
                    break
                elif int(Entrada) == 2: break
            continue
        elif entrada == '2':
            Contenido = OpenFile()
            print ('\n=========================')
            print ('[1] Adidas')
            print ('[2] Nike')
            print ('[3] Puma') 
            print ('[4] Vans')
            Entrada = (input('\nIngrese la marca del modelo que desea eliminar: '))
            if Entrada.isdigit() == False:
                print ('\nOpción no válida\n' , end = '')
                continue
            if Entrada == '1': Marca = 'Adidas'
            elif Entrada == '2': Marca = 'Nike'
            elif Entrada == '3': Marca = 'Puma'
            elif Entrada == '4': Marca = 'Vans'
            else: 
                print ('\nOpción no válida\n' , end = '')
                continue
            Modelos_precios = BuscarPorMarca(Contenido, Marca)
            Modelos = ListaDeModelos(Modelos_precios,Contenido)
            entrada = (input('¿Desea elegir un modelo? [1 si] [2 no]: '))
            if entrada.isdigit() == False:
                print ('\nOpción no válida\n' , end = '')
                continue
            if entrada == '1':
                contador = 0
                for i in Modelos:
                    contador = contador + 1
                    print('[',contador,']','\t',i, sep = '')
                print('')
                entrada = (input ('Ingrese el número del modelo: '))
                if entrada.isdigit() == False:
                    print ('\nOpción no válida\n' , end = '')
                    continue
                if int(entrada) > 0 and int(entrada) <= contador:
                    Modelo = Modelos[int(entrada) - 1]
                    print('\nUsted eligió',Marca,Modelo)
                Entrada = (input('\n¿Está seguro que desea eliminar el modelo del catálogo? [1 si] [2 no]: '))
                if Entrada.isdigit() == False:
                    print ('\nOpción no válida\n' , end = '')
                    continue
                if Entrada == '1':
                    BorrarModelo(Modelo,Contenido)
                    print('\nModelo eliminado con éxito')
                    continue
                elif Entrada == '2': continue
                else: 
                    print ('\nOpción no válida\n' , end = '')
                    continue
        elif entrada == '0': 
            continue
        else:
            print ('\nOpción no válida\n' , end = '')
            continue
    elif Entrada == '0': 
        Bucle = 0
        break
    else:
        print ('\nOpción no válida\n' , end = '')
        continue