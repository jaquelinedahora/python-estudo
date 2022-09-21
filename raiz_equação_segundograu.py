A = float(input('Entre com o coeficiente A: '))
B = float(input('Entre com o coeficiente B: '))
C = float(input('Entre com o coeficiente C: '))

delta = ((B**2) - 4 * A * C)
x1 = (-B + delta **(1/2)) / (2*A)
x2 = (-B - delta **(1/2)) / (2*A)

print(f"x1: {x1} \n x2: {x2}")