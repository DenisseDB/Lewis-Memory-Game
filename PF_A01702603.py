#Denisse Dominguez
#Proyecto memorama de lewis

"""Este programa esta planeado y programado para que funcione como un memorama. Este memorama es un memorama de Lewis, por lo tanto,
el usuario debe relacionar las cartas que se correspondan, especificamente, debe relacionar el elemento quimico con el diagram de
Lewis que le corresponda. Este memorama busca favorecer el aprendizaje acerca de como debe estar representado el diagrama de Lewis
de ciertos elementos.
¿Como funciona el programa? principalmente se da una introduccion al ususario acerca de juego, despues se
realizan dos preguntas abiertas al usuario para poder hacer la impresión de menu, al imprimir el menu, el usuario podra escoger
que quiere hacer de las opciones que este marca; al inicar el juego se imprimen dos filas, la de arriba contiene los elementos quimicos
y la segunda los diagramas, el usuario debe relacionar las cartas con sus parejas y al hacerlo de manera correcta se imprime de nuevo el
tablero pero ahora con las cartas voletadas (las que tuvo o ha tenido bien), si el usuario no obtiene la respuesta correcta, las cartas no
se volearán"""

#--------------------------------------BIENVENIDA--------------------------------------------------------------------------------------------------------------------------------------
#def imprime_archivo(nombre):  #Esta funcion hace lectura del documento que se le pedirá al usuario
#    file = open(nombre, "r")
#   contenido = file.read()   #Solo se lee el documento, no se podrá escribir en el
#    print(contenido)
#    file.close()              
    
def listos(listo):  #Funcion de desición, dependiendo lo que el usuario introduzaca, se imprimira el mensaje correspondiente
    if listo == "si" or listo == "Si" or listo == "SI":
        print()
        print("¡Comencemos!")
    else:
        print()
        print("No te preocupes, el memorama es un juego que trabaja la memoria; juntos iremos dominando el tema")

#-----------------------------------DATOS DE INICIO--------------------------------------------------------------------------------------------------------------------------
matriz = [['1', '2', '3', '4', '5'],['6','7', '8', '9', '10']]   #Matriz a imprimir / tablero de cartas del memorama

def imprime_matriz(matriz): #Se manda llamar matriz para poder imprimirla en filas y columnas, no en una sola fila.
   for i in range(0, len(matriz)): 
        for j in range(0, len(matriz[i])): 
            print( matriz[i][j], end=" ")
        print()
        
def cadena_nombre(cadena):  #Funcion de cadena para que el nombre que el usuario introduzaca, se imprima con la inicial
    nombre = cadena.capitalize()              #con la inicial en mayuscula. (forma correcta de escribir un nombre propio)
    print(nombre)
    

#---------------------------------JUEGO-------------------------------------------------------------------------------------------------------------------------------------
    
matriz_llena1 = [['Hidrogeno', 'Carbono', 'Boro', 'Oxigeno', 'Magnesio'],['·B:', 'Mg:', 'H·', '¡:O:!', ':C:']] # Valores detras de las cartas del tabero

def primera_seleccion(carta1): # Dependiendo el numero que el usuario introduzaca, se imprimira el nombre del elemento quimico detras de esa carta.
        if carta1 == 1:
            print("1 = Hidrogeno")
        elif carta1 == 2:
            print("2 = Carbono")
        elif carta1 == 3:
            print ("3 = Boro")
        elif carta1 == 4:
            print ("4 = Oxigeno")
        elif carta1 == 5:
            print ("5 = Magnesio")
        else:
            print("Numero no valido para el primer movimiento")  # Si el numero no es valido, se rechaza.

def segunda_seleccion(carta2): # Dependiendo el numero que el usuario introduzaca, se imprimira diagrama de lewis detras de esa carta.
        if carta2 == 8:
            print ("8 = H·")
        elif carta2 == 10:
            print ("10 = :C:")
        elif carta2 == 6:
            print ("6 = ·B:")
        elif carta2 == 9:
            print ("9 = ¡:O:!")
        elif carta2 == 7:
            print ("7 = Mg:")
        else:
            print("Numero no valido para el segundo movimiento")  # Si el numero no es valido, se rechaza.

def correcto_incorrecto_voltear_cartas(carta1, carta2, matriz, matriz_llena1):
    if carta1 == 1 and carta2 == 8:   # Si los numeros/cartas introducidas son pares, es decir, correspondientes una a la otra:
        print("Correcta, esa es su estructura de lewis ")  # Se imprime el mensaje de correcto
        for i in range(len(matriz)):   # Se toma en cuenta todas las filas y columnas de la matriz
            for j in range(len(matriz[i])):
                if matriz[i][j] == str(carta1) or matriz[i][j] == str(carta2):  # En la posicion [i][j] del numero/carta en la matriz
                    matriz[i][j] = matriz_llena1[i][j]                          # cambiara su impresion por los valores de matriz_llena1, solo
    elif carta1 == 2 and carta2 == 10:                                          # en las posiciones donde se encuentren el par de cartas correspondientes
        print("Correcta, esa es su estructura de lewis ")                       # es decir, se voltean las cartas
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == str(carta1) or matriz[i][j] == str(carta2):
                    matriz[i][j] = matriz_llena1[i][j]
    elif carta1 == 3 and carta2 == 6:
        print("Correcta, esa es su estructura de lewis ")
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == str(carta1) or matriz[i][j] == str(carta2):
                    matriz[i][j] = matriz_llena1[i][j]
    elif carta1 == 4 and carta2 == 9:
        print("Correcta, esa es su estructura de lewis ")
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == str(carta1) or matriz[i][j] == str(carta2):
                    matriz[i][j] = matriz_llena1[i][j]
    elif carta1 == 5 and carta2 == 7:
        print("Correcta, esa es su estructura de lewis ")
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == str(carta1) or matriz[i][j] == str(carta2):
                    matriz[i][j] = matriz_llena1[i][j] 
    else:                                                                           # Si la respuesta no es correcta, la matriz no sufre modificaciones
        print("Incorrecta, esa estructura no le corresponde, vuelve a intentarlo")  # es decir, no se voltean las cartas
        

#----------------------------------------MENU Y MAIN----------------------------------------------------------------------------------------------------------------------------

def menu():                            #Funcion menu para imprimir las opciones del juego
    print("Menu del juego")
    print("Selecciona lo que desees hacer")
    print("1. COMENZAR PARTIDA")
    print("2. SALIR")
    
def main():                    #Funcion main para el control del memorama. 
    file = open("instrucciones.txt", "r")   #se abre el archivo con las instrucciones en modo lectura
    contenido = file.read()
    print(contenido)                        #se imprimen las instrucciones y se cierra el archivo "instrucciones.txt"
    file.close() 
    listo = str(input("¿Estas listo? , ¿si o no? "))
    listos(listo)
    jugador = str(input("¿Cual es tu nombre?"))                        # Se pide el nombre del usuario para ser cortes con el o ella
    continua = True 
    while continua:                                       # funcion while para la reptición del programa
        print("\n")
        menu()
        print("\n")
        cadena_nombre(jugador)                           # Se imprime el nombre del jugador
        opcion = int(input("¿Que opcion del menu deseas hacer?"))
        if opcion == 1:
            print()
            print("¡A jugar!")
            print("IMPORTANTE: el signo ¡ significa que hay un punto arriba de la estructura del elemento y ! significa que hay un punto debajo de la estructura del elemento")
            print()
            continua2 = True           
            while continua2:                        # ciclo while para que el usuario permanezca en el juego y no lo saquen  de este a menos que el lo decida
                print()
                imprime_matriz(matriz)              # se manda llamar la funcion
                print()
                cadena_nombre(jugador)              # se manda llamar la funcion
                carta1 = int(input("¿Que carta de la primera fila quieres voltear?"))
                primera_seleccion(carta1)                                                  # se manda llamar la funcion con la respuesta introduccida por el usuario
                carta2 = int(input("De la segunda finla ¿Que numero quieres voltear?"))
                segunda_seleccion(carta2)                                                  # se manda llamar la funcion con la respuesta introduccida por el usuario
                print()
                cadena_nombre(jugador)
                print('Tu respuesta es: ') 
                correcto_incorrecto_voltear_cartas(carta1, carta2, matriz, matriz_llena1)      # Se manda llamar la funcion para hacer la validacion de la respuesta y voltear o no las cartas
                print()
                cadena_nombre(jugador)
                continuar = str(input("¿deseas continuar? o ¿has terminado? s=si n=no" ))    # El jugador toma la desicion de salirse o permanecer en la partida del juego
                if continuar == "n" or continuar == "N":
                    print("Felicidades por tu aprendizaje, gracias por jugar")
                    continua2 = False                                                         # Si decide salirse, se sale de la partida, pierde el avance del juego y regresa al menu
        elif opcion == 2:
            print("Gracias por jugar, nos vemos")
            continua = False                     # Si el jugador decide salirse del programa, se deja de imprimir el menu y se sale por completo del programa
        else:
            print("Lo siento, tu opcion no es valida, vuelve a seleccionar una opcion")    # Si la opcion no es valida, le vuelve a imprimir el menu preguntadole de nuevo una opcion
        
main()

"""Casos de prueba:
#1:
Input:SI 
Input:denisse
Input:1
Input:1
Input:8
Output: Denisse
Tu respuesta es: 
Correcta, esa es su estructura de lewis
Input:s
Output: Hidrogeno 2 3 4 5 
        6 7 H· 9 10
        
#2:
Input:si 
Input:isa
Input:1
Input:2
Input:7
Output: Isa
Tu respuesta es: 
Incorrecta, esa estructura no le corresponde, vuelve a intentarlo
Input:s
Output: 1 2 3 4 5 
        6 7 8 9 10
        
#3:
Input:Si 
Input:lalo
Input:1
Input:3
Input:6
Output: Lalo
Tu respuesta es: 
Correcta, esa es su estructura de lewis
Input:n
Ouput:Felicidades por tu aprendizaje, gracias por jugar

#4:
Input:no 
Input:pau
Input:2
Output:Gracias por jugar, nos vemos """
