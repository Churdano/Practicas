#Ejercicio Python #01: 
# Define una función llamada menorque() que nos devuelva en pantalla el 
# número menor entre dos enteros.
# Define una salida de texto en caso de que .

def menor_que(numero1, numero2):
    if numero1 < numero2:
        print(f"El número menor entre los dos es {numero1}")
    elif numero1 > numero2:
        print(f"El número menor entre los dos es {numero2}")
    elif numero1 == numero2:
        print("Los dos números son iguales. Por favor, ingresa números de diferente valor")
    else:
        print("Datos ingresados incorrectos")

def comparar_numeros():
    while True:
        entrada1 = input("Ingresar primer número (o escribir 'salir' para salir): ")

        if entrada1.lower() == "salir":
            break

        entrada2 = input("Ingresar segundo número: ")

        try:
            numero1 = int(entrada1)
            numero2 = int(entrada2)
            menor_que(numero1, numero2)

        except (ValueError, TypeError):
            print("Entrada no válida. Por favor, ingresa números válidos.")

comparar_numeros()

