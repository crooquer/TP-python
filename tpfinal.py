#Importamos bibliotecas para el uso de funcion Random y fecha
from random import randint
import random, datetime
#Declaro algunas variables 
monto_jugada = []
monto = 0
nombre_quiniela = "Quiniela JC SA"
dni_apostador = ()

#Creo las funciones
#Funcion de generar el ticket
def generar_ticket(nombre_quiniela, dni_apostador, monto_jugada):
    fecha_hora_apuesta = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    numero_comprobante = random.randint(100000, 999999)
    print("=== Ticket Comprobante ===")
    print(f"=== {nombre_quiniela} ===")
    print(f"Fecha y Hora de la apuesta: {fecha_hora_apuesta}")
    print(f"Número de comprobante: {numero_comprobante}")
    print(f"DNI del apostador: {dni_apostador}")
    print(f"Cifra apostada: {monto_jugada}"'\n')
              

#Funcion para apostar a la quiniela
def Quiniela():
        while True:
        #ingresamos al menu para apostar de 2; 3; o 4 cifras
         print("== Quiniela ==") 
         print("1. Para apostar numeros de 2 cifras")
         print("2. Para apostar numeros de 3 cifras")
         print("3. Para apostar numeros de 4 cifras")
         opcion = input("ingrese una opcion: ")

        #funcion para apostar un numero de 2 cifras
         if opcion == "1":
              dni_apostador = input("Ingrese el DNI del apostador: ")
              while True:
                   try:
                        jugada_2_cifras = int(input("Ingrese el numero de 2 cifras: "))
                   except ValueError:
                        print("debes ingresar un numero de 2 cifras")
                   if jugada_2_cifras > 99:
                             print("Debe escribir un numero de 2 cifras")
                             continue
                   else:
                             break
                             
              monto_jugada = int(input("Ingrese el monto de la jugada: "))
              generar_ticket(nombre_quiniela, dni_apostador, monto_jugada)
              break
         
        #funcion para apostar un numero de 3 cifras
         elif opcion == "2":
            dni_apostador = input("Ingrese el DNI del apostador: ")
            while True:
                   try:
                        jugada_3_cifras = int(input("Ingrese el numero de 3 cifras: "))
                   except ValueError:
                        print("debes ingresar un numero de 3 cifras")
                   if jugada_3_cifras > 999:
                             print("Debe escribir un numero de 3 cifras")
                             continue
                   else:
                             break
            monto_jugada = input("Ingrese el monto de la jugada: ")
            generar_ticket(nombre_quiniela, dni_apostador, monto_jugada)
            break
         
         #funcion para apostar un numero de 4 cifras
         elif opcion == "3":
               dni_apostador = input("Ingrese el DNI del apostador: ")
               while True:
                   try:
                        jugada_4_cifras = int(input("Ingrese el numero de 4 cifras: "))
                   except ValueError:
                        print("debes ingresar un numero de 4 cifras")
                   if jugada_4_cifras > 9999:
                             print("Debe escribir un numero de 4 cifras")
                             continue
                   else:
                             break
               monto_jugada = input("Ingrese el monto de la jugada: ")
               generar_ticket(nombre_quiniela, dni_apostador, monto_jugada,)
               break
         #validacion del menu
         else:
               print("Opcion invalida, por favor ingrese una opcion valida")

        
        

#Aca se crea la funcion de quini 6                   
def Quini_6():
      #ingresamos al menu para ingresar apuesta manual o generar numeros aleatorios 
      print("== Quini 6 ==")
      print("1. Para ingresar los 6 numeros")
      print("2. Para generar los 6 numeros aleatorios")
      print("3. Atras")
      opcion = input("ingrese una opcion: ")

      #En esta funcion ingresamos los 6 numeros de forma manual
      if opcion == "1":
            dni_apostador = input("Ingrese el DNI del apostador: ")
            numeros_apostados = []
            while len(numeros_apostados) <6:
                   numero = int(input(f"Ingrese número {len(numeros_apostados)}: "))
                   if 0 <= numero <= 45 and numero not in numeros_apostados:
                    numeros_apostados.append(numero)
                   else:
                    print("Número inválido o repetido, intenta nuevamente.")
            monto_jugada = int(input("Ingrese el monto de la jugada: "))
            generar_ticket(nombre_quiniela, dni_apostador, monto_jugada)
     
      #En esta funcion el programa escoge los 6 numeros al azar                        
      elif opcion == "2":
            dni_apostador = input("Ingrese el DNI del apostador: ")                    
            for i in range (0,6):
             lista1 = randint(0,45)
             print("los 6 numeros se generan automaticamente: ", lista1)
            monto_jugada = int(input("Ingrese el monto de la jugada: "))
            generar_ticket(nombre_quiniela, dni_apostador, monto_jugada)
            
      
      #elif opcion == "3":
             
     #Validacion para elegir una opcion correcta
      else:
            print("ingrese una opcion correcta")

"""
no se como hacerla :)
def Comprobar_Apuesta():
     for index, apuesta in enumerate(quini6_apuestas):
        aciertos = len(set(apuesta) & set(numeros_ganadores))
        print(f"Apuesta {index+1}: {apuesta}. Aciertos: {aciertos}")
     print("ingrese el numero de la jugada: ")
   """  
#funcion para el arqueo de caja, no anda no guarda el monto de la apuesta en la lista 
def Arqueo_de_caja():
    arqueo = 0
    for total in monto_jugada:
         arqueo += total
    print("La recaudacion del dia de hoy es: ",arqueo)

while True:
     print("=== Menú ===")
     print("1. Quiniela")
     print("2. Quini 6 tradicional")
     print("3. Comprobar apuesta ganadora")
     print("4. Arqueo de caja")
     print("5. Salir")
     opcion = input("ingrese una opcion: ")
     if opcion == "1":
        Quiniela()
     elif opcion == "2":
        Quini_6()
     elif opcion == "4":
        Arqueo_de_caja()
        break
     else:
        print("Opción inválida. Por favor, ingrese una opción válida.")