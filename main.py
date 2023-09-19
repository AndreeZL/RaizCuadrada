from logica.RaizCuadrada import RaizCuadrada

numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))

resultado = RaizCuadrada.calcular_raiz_cuadrada(numero)

print(f"La raíz cuadrada de {numero} es aproximadamente {resultado:.2f}")