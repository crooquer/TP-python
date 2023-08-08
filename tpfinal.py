#Importamos bibliotecas para el uso de funcion Random y fecha
import datetime
import random
from random import randint

#Declaro algunas variables
global monto_jugada
global jugada_2_cifras
global arqueo
nombre_quiniela = "Quiniela JC SA"
dni_apostador = ()



#Creo las funciones
#Funcion de generar el ticket
def generar_ticket(nombre_quiniela, dni_apostador, monto_jugada):
    fecha_hora_apuesta = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    numero_comprobante = random.randint(100000, 999999)
    print("")
    print("=== Ticket Comprobante ===")
    print(f"=== {nombre_quiniela} ===")
    print(f"Fecha y Hora de la apuesta: {fecha_hora_apuesta}")
    print(f"Número de comprobante: {numero_comprobante}")
    print(f"DNI del apostador: {dni_apostador}")
    print(f"Cifra apostada: {monto_jugada}"'\n')
              

#Funcion para apostar a la quiniela
def Quiniela():
        
        jugada_2_cifras = []
        while True:
        #ingresamos al menu para apostar de 2; 3; o 4 cifras
         print(" ")
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
      print("")
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


def Comprobar_Apuesta():
            nro_azar_quiniela = 0
            print("Ingrese el sorteo que desee consultar: ")
            print("1. Quiniela")
            print("2. Quini 6")
            print(" ")
            opcion = int(input("Ingrese una opcion: "))

          # VERIFICAR NUMERO GANADOR EN QUINIELA
            if opcion == 1:
              print("Ingrese el sorteo que desee consultar: ")
              print("1. Quiniela 2 cifras")
              print("2. Quiniela 3 cifras")
              print("3. Quiniela 4 cifras")
              opcion1 = int(input("Ingrese una opcion: "))

              if opcion1 == 1:
               jugada1 = int(input("Ingrese el numero de 2 cifras al que aposto: "))
               ganador2cifras = randint(0, 99)
               if jugada1 == ganador2cifras:
                     print("Felicidades ud ha ganado ")
               else:
                     print("Lo sentimos, ud no ha ganado el numero ganador es:", ganador2cifras)

              elif opcion1 == 2:
               jugada2 = int(input("Ingrese el numero de 3 cifras al que aposto: "))
               ganador3cifras = randint(0, 999)
               if jugada2 == ganador3cifras:
                print("Felicidades ud ha ganado")
               else:
                print("Lo sentimos, ud no ha ganado el numero ganador es:", ganador3cifras)
              elif opcion1 == 3:
               jugada3 = int(input("Ingrese el numero de 4 cifras al que aposto: "))
               ganador4cifras = randint(0, 9999)
               if jugada3 == ganador4cifras:
                    print("Felicidades ud ha ganado")
               else:
                    print("Lo sentimos, ud no ha ganado el numero ganador es:", ganador4cifras)

              else:
               print("Opción inválida")

            elif opcion == 2:
             apuesta_quini6 = []
             numeros_ganadores = []
             print("Ingrese seis numeros del 00 al 45 inclusive:")
             while len(apuesta_quini6) < 6:
                  for i in range(6):
                       numeros = int(input("Ingrese el número {}: ".format(i+1)))
                       apuesta_quini6.append(numeros)
                       print(apuesta_quini6[i])
             for i in range (0,6):
              numeros = randint(0,45)
              numeros_ganadores.append (numeros)
             if apuesta_quini6 == numeros_ganadores:
                  print("Felicidades ud ha ganado")
             else:
                  print("Lo sentimos ud no ha ganado, los numeros ganadores son: ",numeros_ganadores)
            else:
             print("Opción inválida")

#funcion para el arqueo de caja, no anda no guarda el monto de la apuesta en la lista

def Arqueo_de_caja():
     arqueo = arqueo + monto_jugada
     print("")
     print("La venta total del dia es: ",arqueo)
     print("")



while True:
     monto_jugada = 0
     arqueo = 0
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
     elif opcion == "3":
          Comprobar_Apuesta()
     elif opcion == "4":
      arqueo = arqueo + monto_jugada
      print("")
      print("La venta total del dia es: ",arqueo)
      print("")
      #Arqueo_de_caja()
      break
     else:
        print("Opción inválida. Por favor, ingrese una opción válida.")