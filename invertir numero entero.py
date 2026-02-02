# programa para invertir un número entero
N = int(input("Ingrese un número entero de 4 dígitos: "))

# proceso de inversión del número
print()
print("procesando...")
print()
N1 = N % 10
N2 = (N // 10) % 10
N3 = (N // 100) % 10
N4 = N // 1000

inversión = N1 * 1000 + N2 * 100 + N3 * 10 + N4

print("El número invertido es:", inversión)

# fin del programa
print()
print()
print("presione 'Enter' para salir")
input()