#Iván Ruipérez Benítez
#Funciones

def ListaAutores(datos):
    autores=[]
    print("Lista de autores de recetas.")
    print()
    for receta in datos:
        if receta["author"] not in autores:
            autores.append(receta["author"])
    for autor in autores:
        print(autor)
    print()
        
def CuentaRecetas(datos):
    print("Número de recetas de cada autor.")
    print()
    autores=[]
    for receta in datos:
        if receta["author"] not in autores:
            autores.append(receta["author"])
    for autor in autores:
        contador=0
        for receta in datos:
            if autor == receta["author"]:
                contador+=1
        if contador == 1:
            print(f"{autor}:{contador} receta.")
        else:
            print(f"{autor}:{contador} recetas.")

def RangoCookTime(datos):
    print("Ponga dos valores para ver las recetas que tengan un tiempo de cocina dentro del rango introducido.")
    print()
    valor1=CompruebaValor1()
    valor2=CompruebaValor2()
    while valor1 > valor2:
        print("Valor 1 es el mínimo y valor 2 es el máximo.")
        valor1=CompruebaValor1()
        valor2=CompruebaValor2()
    print()
    recetas=[]
    tiempos=[]
    verificador=False
    for receta in datos:
        if receta["cook_time"] >= valor1 and receta["cook_time"] <= valor2:
            recetas.append(receta["name"])
            tiempos.append(receta["cook_time"])
            verificador=True
    if not verificador:
        print("No se encontraron recetas con dicho rango de tiempo de cocina.")
    recetaMasLarga=max(recetas,key=len)
    print("Receta",(len(recetaMasLarga)-6)*"-","Tiempo de preparacion")
    for receta,tiempo in zip(recetas,tiempos):
        print(receta,len(receta)*"-",tiempo)
def CompruebaValor1():
    while True:
        valor1=input("Valor 1: ")
        try:
            valor1=int(valor1)
            return valor1
        except ValueError:
            print("Error: Ingresa un valor numérico")

def CompruebaValor2():
    while True:
        valor2=input("Valor 2: ")
        try:
            valor2=int(valor2)
            return valor2
        except ValueError:
            print("Error: Ingresa un valor numérico")

def BuscaIngrediente(datos):
    print("Búsqueda de recetas por ingredientes")
    print()
    ingrediente=input("Ingrediente: ")
    while ingrediente.isalpha() == False:
        print("La cadena solo puede contener letras.")
        ingrediente=input("Ingrediente: ")
    print()
    recetas=[]
    for receta in datos:
        for ingredient in receta["ingredients"]:
            if ingrediente.lower() in ingredient["name"].lower() or ingrediente.lower() in ingredient["qty"].lower():
                if receta["name"] not in recetas:
                    recetas.append(receta["name"])
    if len(recetas) == 0:
        print("No se encontraron recetas con dicho ingrediente.")
    else:
        for receta in recetas:
            print("Receta:",receta)


def menu5():
    print('''Menú
    1. Siguiente paso de la receta.
    2. Volver a mostrar los ingredientes.
    3. Salir.''')
    num=input("Elija una opción: ")
    while num.isnumeric() == False or int(num) > 3 or int(num) < 1:
        print("Esa opción no existe.")
        num=input("Elija una opción: ")
    return int(num)

def PasosReceta(datos):
    print("Búqueda de receta, mostrando la foto, los ingredientes y los pasos.")
    print()
    plato=input("Receta: ")
    existe=False
    for receta in datos:
        if plato == receta["name"]:
            existe=True
            print("Imagen:",receta["img"])
            print()
            for ingrediente in receta["ingredients"]:
                print(ingrediente["qty"],ingrediente["name"])
            print()
            opcion=True
            pasos=[]
            for paso in receta["instructions"]:
                pasos.append(paso["id"])
            for paso in receta["instructions"]:
                if opcion:
                    print("Paso",paso["id"])
                    print()
                    print(paso["detail"])
                    print()
                    opcion=Opciones5(datos,plato,opcion,paso)
                    if paso["id"] == max(pasos):
                        print("Este era el último paso.")
    if not existe:
        print("No se encontró dicha receta.")

def Opciones5(datos,plato,opcion,paso):
    num=0
    while num != 1 and num != 3:
        num=menu5() 
        if num == 2:
            for receta in datos:
                if plato == receta["name"]:
                    print()
                    print("Ingredientes")
                    for ingrediente in receta["ingredients"]:
                        print(ingrediente["qty"],ingrediente["name"])
            print()
            print("Paso",paso["id"])
            print()
            print(paso["detail"])
            print()
    if num == 1:
        opcion=True
    elif num == 3:
        opcion=False
    print()
    return opcion

def menu():
    print('''Menú
        1. Mostrar autores de las recetas.
        2. Contar recetas de cada autor.
        3. Buscar recetas por tiempo de cocina.
        4. Buscar recetas por ingredientes.
        5. Pasos de receta.
        6. Salir.''')
    num=input("Elija una opción: ")
    while num.isnumeric() == False or int(num) > 6 or int(num) < 1:
        print("Esa opción no existe.")
        num=input("Elija una opción: ")
        print()
    return int(num)

def Opciones(num,datos):
    if int(num) == 1:
        ListaAutores(datos)
    elif int(num) == 2:
        CuentaRecetas(datos)
    elif int(num) == 3:
        RangoCookTime(datos)
    elif int(num) == 4:
        BuscaIngrediente(datos)
    elif int(num) == 5:
        PasosReceta(datos)