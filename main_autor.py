from Autor_negocio import Autor_negocio

negocio_autor = Autor_negocio()

def registrar_autor():
    codigo = str(input("Ingrese el codigo personal: "))
    nombres = str(input("Ingrese el nombre o nombres: "))
    ap_paterno = str(input("Ingrese el apellido paterno: "))
    ap_materno = str(input("Ingrese el apellido materno: "))
    anio = int(input("Ingrese el año de nacimiento: "))
    cod_autor = str(input("Ingrese el codigo como autor: "))
    pais = str(input("Ingrese el pais: "))
    editorial = str(input("Ingrese la editorial: "))
    negocio_autor.registrar_autores(codigo, nombres, ap_paterno, ap_materno, anio, cod_autor, pais, editorial)
    print("Registro hecho correctamente")

def obtener_autores():
    listado_autor = negocio_autor.obtener_autores()
    for listado_autor in listado_autor:
        print(listado_autor)
def editar_autores():
    indice = int(input('Ingrese el indice a editar: '))
    codigo = str(input("Ingrese el codigo personal: "))
    nombres = str(input('Ingrese nombre o nombres: '))
    ap_paterno = str(input('Ingrese ap_paterno: '))
    ap_materno = str(input('Ingrese ap_materno: '))
    anio_nacimiento = int(input("Ingrese el año de nacimiento: "))
    cod_autor = input('Ingrese el codigo de autor: ')
    pais = input('Ingrese el pais: ')
    editorial = input('Ingrese la editorial: ')
    negocio_autor.editar_autores(indice, codigo, nombres, ap_paterno, ap_materno, anio_nacimiento, cod_autor, pais, editorial)
    print("Autor editado correctamente")

def eliminar_autores():
    indice = int(input('Ingrese el indice a eliminar: '))
    negocio_autor.eliminar_autores(indice)
    print("Autor eliminado :)")

# Diccionario
opciones = {
    "1": registrar_autor,
    "2": obtener_autores,
    "3": editar_autores,
    "4": eliminar_autores,
    "5": exit
}

while True:
    print("##########################")
    print("Menú:")
    print("1. Registrar autor")
    print("2. Listar autores")
    print("3. Editar autor")
    print("4. Eliminar autor :)")
    print("5. Salir")
    print("##########################")

    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

    
