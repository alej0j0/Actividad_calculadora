def multiplicacion():
    
    print("*" * 50)
    print("Se encuentra en la seccion de multiplicacion")
    print("*" * 50)
    print("\nPara salir de la multiplicacion, escriba 'fin'")
    lista = []
    while True:
        numeros=input("ingrese: ")   
        if numeros.lower() == "fin":
            break
        if numeros == "":
            print("No se ha ingresado nada")
            continue
        try:
            float(numeros)
        except ValueError:
            print("No es un numero")
            continue
        lista.append(float(numeros))
        resultado=lista[0]
        for num in lista[1: ]:
            resultado *= num
    print("La multiplicacion es: ", resultado)
    opcion=input("Desea volver a multiplicar? (s/n): ")
    if opcion == "s":
        multiplicacion()