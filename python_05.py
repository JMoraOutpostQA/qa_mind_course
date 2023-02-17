def suma(numeros_a, numeros_b):
    return numeros_a + numeros_b

def resta(numeror_a, numeror_b):
    return numeror_a - numeror_b

def multiplicacion(numerom_a, numerom_b):
    return numerom_a * numerom_b

def division(numerod_a, numerod_b):
    return numerod_a / numerod_b

def modulo(numeromod_a, numeromod_b):
    return numeromod_a % numeromod_b

def celsius_a_farenheit(celsiusf):
    return celsiusf * 1.8 + 32

num_a = float(input("Ingresa el primer numero"))
num_b = float(input("Ingresa el segundo numero:"))
celcius = float(input("Ingresa los grados celcius:"))


print(f"Suma {suma(num_a, num_b)}")
print(f"Resta {resta(num_a, num_b)}")
print(f"Multiplicacion {multiplicacion(num_a, num_b)}")
print(f"Division {division(num_a, num_b)}")
print(f"Modulo {modulo(num_a, num_b)}")
print(f"Grados Farenheit {celsius_a_farenheit(celcius)}")

