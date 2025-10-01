#Funciones 
# Crear una función llamada imprimir_hola_mundo que imprima por patalla el mensaje: "Hola Mundo!". Llamar a esta función desde el programa principal.
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()
    
# Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: "Hola Marcos!". Llamar a esta función desde el programa principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    print("Hola", nombre)
saludar_usuario("Rodrigo")

# Crear una función llamada información_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: "Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]". Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    print("Soy", nombre, apellido + ",", "tengo", edad, "años y vivo en", residencia)
informacion_personal("Rodrigo", "Gatica", 33, "Ciudad de Mendoza, Argentina")  

# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
def calcular_area_circulo(radio):
    area = 3.14 * radio * radio
    return area
def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return perimetro
radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print("El área del círculo es:", area)
print("El perímetro del círculo es:", perimetro)

# Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print("La cantidad de horas es:", horas)

# Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# Crear una función llamada operaciones_basicas(a,b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultdos de forma clara.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicación = a * b
    división = a / b if b != 0 else "Indefinido (no se puede dividir por cero)"
    return (suma, resta, multiplicación, división)
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a,b)
print("Suma:", resultados[0])
print("Resta:", resultados[1])
print("Multiplicación:", resultados[2])
print("División:", resultados[3])

# Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print("Su índice de masa corporal (IMC) es: {:.2f}".format(imc))

# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahtenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print("La temperatura en grados Fahrenheit es:", fahrenheit)

# Crear una función llamada calcular_promedio(a,b,c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultdo usando esta función.
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(a,b,c)
print("El promedio de los números es:", promedio)