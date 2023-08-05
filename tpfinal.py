from random import randint
import random, datetime
monto_jugada = 0
monto = 0
monto = monto + monto_jugada
nombre_quiniela = "Quiniela JC SA"
dni_apostador = ()
generar_ticket_quiniela = (nombre_quiniela, dni_apostador, monto)
fecha_hora_apuesta = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
numero_comprobante = random.randint(100000, 999999)

def generar_ticket_quiniela(nombre_quiniela, dni_apostador, monto_jugada):
    fecha_hora_apuesta = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    numero_comprobante = random.randint(100000, 999999)


#Aca se crea la funcion para la apuesta en quiniela
def Quiniela():
        while True:
        #ingresamos al menu para apostar de 2; 3; o 4 cifras 
         print("1. Para apostar numeros de 2 cifras")
         print("2. Para apostar numeros de 3 cifras")
         print("3. Para apostar numeros de 4 cifras")
         opcion = input("ingrese una opcion: ")
        
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
                             
              monto_jugada = input("Ingrese el monto de la jugada: "'\n')
              generar_ticket_quiniela(nombre_quiniela, dni_apostador, monto_jugada)
              print("=== Ticket Comprobante ===")
              print(f"Quiniela: {nombre_quiniela}")
              print(f"Fecha y Hora de la apuesta: , {fecha_hora_apuesta}")
              print(f"Número de comprobante: {numero_comprobante}")
              print(f"DNI del apostador: {dni_apostador}")
              print(f"Cifra apostada: {monto_jugada}"'\n')
              break
        
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
            generar_ticket_quiniela()
            print("=== Ticket Comprobante ===")
            print(f"Quiniela: {nombre_quiniela}")
            print(f"Fecha y Hora de la apuesta: , {fecha_hora_apuesta}")
            print(f"Número de comprobante: {numero_comprobante}")
            print(f"DNI del apostador: {dni_apostador}")
            print(f"Cifra apostada: {monto_jugada}"'\n')
            break
         elif opcion == "3":
               dni_apostador = input("Ingrese el DNI del apostador: ")
               while True:
                   try:
                        jugada_4_cifras = int(input("Ingrese el numero de 4 cifras: "))
                   except ValueError:
                        print("debes ingresar un numero de 4 cifras")
                   if jugada_2_cifras > 9999:
                             print("Debe escribir un numero de 4 cifras")
                             continue
                   else:
                             break
               monto_jugada = input("Ingrese el monto de la jugada: ")
               generar_ticket_quiniela()
               print("=== Ticket Comprobante ===")
               print(f"Quiniela: {nombre_quiniela}")
               print(f"Fecha y Hora de la apuesta: , {fecha_hora_apuesta}")
               print(f"Número de comprobante: {numero_comprobante}")
               print(f"DNI del apostador: {dni_apostador}")
               print(f"Cifra apostada: {monto_jugada}"'\n')
               break
         else:
               print("Opcion invalida, por favor ingrese una opcion valida")

        
        

#Aca se crea la funcion de quini 6                   
def Quini_6():
      #ingresamos al menu para ingresar apuesta manual o generar numeros aleatorios 
      print("1. Para ingresar los 6 numeros")
      print("2. Para generar los 6 numeros aleatorios")
      print("3. Atras")
      opcion = input("ingrese una opcion: ")
      if opcion == "1":
            numeros_apostados = []
            while len(numeros_apostados) <6:
                   numero = int(input(f"Ingrese número {len(numeros_apostados)}: "))
            if 0 <= numero <= 45 and numero not in numeros_apostados:
                numeros_apostados.append(numero)
      elif opcion == "2":
            dni_apostador = input("Ingrese el DNI del apostador: ")                    
            for i in range (0,6):
             lista1 = randint(0,45)
             print("los 6 numeros se generan automaticamente: ", lista1)
            monto_jugada = input("Ingrese el monto de la jugada: "'\n')
            generar_ticket_quiniela(nombre_quiniela, dni_apostador, monto_jugada)
            print("=== Ticket Comprobante ===")
            print(f"Quiniela: {nombre_quiniela}")
            print(f"Fecha y Hora de la apuesta: , {fecha_hora_apuesta}")
            print(f"Número de comprobante: {numero_comprobante}")
            print(f"DNI del apostador: {dni_apostador}")
            print(f"Cifra apostada: {monto_jugada}"'\n')
            
      
      #elif opcion == "3":
             

      else:
            print("ingrese una opcion correcta")

"""""
def Comprobar_Apuesta():
     for index, apuesta in enumerate(quini6_apuestas):
        aciertos = len(set(apuesta) & set(numeros_ganadores))
        print(f"Apuesta {index+1}: {apuesta}. Aciertos: {aciertos}")
     print("ingrese el numero de la jugada: ")
     """

def arqueo_de_caja():
    recaudacion_diaria = 0
    for monto_jugada in Quiniela, Quini_6:
          recaudacion_diaria += (monto_jugada)

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
        arqueo_de_caja()
        break
     else:
        print("Opción inválida. Por favor, ingrese una opción válida.")


#class La_Quiniela:
 #   Quiniela = ""
  #  Quini6 = ""
   # Comprobar_Apuesta = ""
    #Arqueo_de_caja = 0
