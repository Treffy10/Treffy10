from Autor import Autor
import os

class Autor_negocio:
    listado_autor = []
    registro_autores = "Lista de autores.txt"

    def __init__(self):
        self.listado_autor = []

    def obtener_autores(self):
        try:
            with open(self.registro_autores, 'r') as file:
                contenido = file.read()
                print(contenido)
        except FileNotFoundError:
            print(f"El archivo '{self.registro_autores}' no se encontró.")
    def guardar_autores(self):
        # Verificar si el archivo ya existe antes de crearlo
        if not os.path.isfile(self.registro_autores):
            # Si no existe, crea el archivo
            with open(self.registro_autores, 'w') as archivo:
                archivo.write("Listado de autores:\n")

        # Crear una lista de autores que ya han sido escritos en el archivo
        autores_escritos = set()

        # Leer los autores que ya han sido escritos en el archivo
        with open(self.registro_autores, 'r') as archivo:
            for linea in archivo:
                # Suponiendo que los códigos de autor son únicos y están en la primera columna
                codigo_autor = linea.strip().split(',')[0].strip()
                autores_escritos.add(codigo_autor)

        # Ahora, se agrega los datos del autor si no ha sido escrito previamente
        with open(self.registro_autores, 'a') as archivo:
            for autor in self.listado_autor:
                # Suponiendo que los códigos de autor están en el atributo "codigo"
                if autor.codigo not in autores_escritos:
                    archivo.write(f"\n{autor.codigo}, {autor.nombres}, {autor.ap_paterno}, {autor.ap_materno}"
                                  f", {autor.anio_nacimiento}, {autor.cod_autor}, {autor.pais}, {autor.editorial}")
                    autores_escritos.add(autor.codigo)

    def registrar_autores(self, _codigo, _nombres, _ap_paterno, _ap_materno, _anio, _cod_autor, _pais, _editorial):
        autor = Autor(_codigo, _nombres, _ap_paterno, _ap_materno, _anio, _cod_autor, _pais, _editorial)
        self.listado_autor.append(autor)
        self.guardar_autores()
        print(f"{autor}")
        print("Autor registrado correctamente")

    def obtener_objetos(self):
        try:
            with open(self.registro_autores, 'r') as archivo:
                lineas = archivo.readlines()

            # Verificamos si hay al menos dos líneas para omitir la primera
            if len(lineas) >= 2:
                lineas = lineas[1:]  # Omitir la primera línea

            return lineas
        except FileNotFoundError:
            print(f"El archivo '{self.registro_autores}' no se encontró.")
            return None
    def eliminar_autores(self, indice):
        if not self.listado_autor:
            self.listado_autor.append(self.obtener_autores())
        if 0 <= indice < len(self.listado_autor):
            del self.listado_autor[indice]
            objetos = self.obtener_objetos()  # Obtener las líneas actuales del archivo

            if indice < len(objetos):
                del objetos[indice]  # Eliminar la línea del archivo

                # Guardar las líneas actualizadas en el archivo
                with open(self.registro_autores, 'w') as archivo:
                    archivo.write("Listado de autores:\n")
                    for linea in objetos:
                        archivo.write(linea)

                print("Autor eliminado correctamente")
            else:
                print("Índice fuera de rango")
        else:
            print("Índice fuera de rango en la lista de autores")

    def editar_autores(self, indice, _codigo, _nombres, _ap_paterno, _ap_materno, _anio, _cod_autor, _pais, _editorial):
        # Leer contenido del archivo
        with open(self.registro_autores, 'r') as file:
            lineas = file.readlines()

        # Verificar si el índice está dentro del rango
        if 0 < indice < len(lineas):
            # Crear la nueva línea formateada
            nueva_linea = f"{_codigo}, {_nombres}, {_ap_paterno}, {_ap_materno}, {_anio}, {_cod_autor}, {_pais}, {_editorial}\n"
            # Modificar la línea en el índice especificado
            lineas[indice] = nueva_linea

            # Escribir el contenido modificado nuevamente en el archivo
            with open(self.registro_autores, 'w') as file:
                file.writelines(lineas)
        else:
            print("Índice fuera de rango")







