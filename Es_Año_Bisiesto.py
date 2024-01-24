# función que determina si un año dado es bisiesto o no. Para ello, comprueba si el año es divisible por 4 sin resto y, a continuación, si también es divisible por 100 sin resto o por 400 sin resto. Si se cumple alguna de estas condiciones, el año es bisiesto.
def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
# que calcula el número de años bisiestos entre 1900 y el año especificado. La función utiliza un bucle for para iterar sobre cada año en el rango especificado, e incrementa una variable contador (count) cada vez que encuentra un año bisiesto. La función define una función de ayuda, es_bisiesto, que determina si un año dado es bisiesto o no.
def calcular_anios_bisiestos(year):
    count = 0
    for i in range(1900, year + 1):
        if es_bisiesto(i):
            count += 1
    return count

# Solicitar al usuario que ingrese un año
input_year = int(input("Ingrese un año entre 1900 y 2199: "))

# Verificar si el año ingresado está dentro del rango especificado
if input_year < 1900 or input_year > 2199:
    print("El año ingresado está fuera del rango permitido.")
else:
    # Calcular el número de años bisiestos entre 1900 y el año ingresado
    num_bisiestos = calcular_anios_bisiestos(input_year)
    print(f"El número de años bisiestos entre 1900 y {input_year} es: {num_bisiestos}")
    