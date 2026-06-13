def resta(a, b):
    return a - b   
print(resta(30, 10))


def resta(a, b):
    return a - b
print(resta(b=10, a=30))

def funcion():
    return "bienvenido a python" 
frase = funcion()
print(frase)


def resta(a=None, b=None):
    if a == None or b == None:
        print ("Error: faltan parametros a la funcion")
        return
    return a - b
print(resta())


def calculo(precio, decuento):
    return precio - (precio * decuento / 100)
datos = [10000, 10]
print("El monto final a pagar es: ", calculo(*datos))


def saludo(nombre, mensaje = 'Python'):
    print(mensaje, nombre)
saludo(mensaje= "buen dia", nombre= "Pedro")


