from multiplicar import multiplicacion
from division import dividir
from sumar import suma
from restar import resta

@@ -11,6 +13,7 @@ def menu():
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        print("*" * 50)

        opcion = input("Ingrese el numero de la opcion que desea utilizar: ")
@@ -22,10 +25,12 @@ def menu():
            resta()
            print("Has elegido la resta")
        elif opcion == "3":
            multiplicacion()
            print("Has elegido la multiplicacion")
        elif opcion == "4":
            dividir()
            print("Has elegido la division")
        elif opcion.lower() == "s":
        elif opcion.lower() == "5":
            print("Saliendo de la calculadora...")
            break