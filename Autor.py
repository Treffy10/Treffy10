from Persona import Persona
from Libro import Libro
class Autor(Persona):
    cod_autor = ""
    pais = ""
    editorial = ""
    libros = []
    def __init__(self, codigo, nombres, ap_paterno, ap_materno, anio_nacimiento, cod_autor, pais, editorial):
        super().__init__(codigo, nombres, ap_paterno, ap_materno, anio_nacimiento)
        self.cod_autor = cod_autor
        self.pais = pais
        self.editorial = editorial
        self.libros = []

    def set_cod_autor(self, cod_autor):
        self.cod_autor = cod_autor
    def get_codigo_autor(self):
        return self.cod_autor

    def set_pais(self, pais):
        self.pais = pais
    def get_pais(self):
        return self.pais

    def set_editorial(self, editorial):
        self.editorial = editorial
    def get_editorial(self):
        return self.editorial

    def set_libro(self, libro):
        libro = Libro(libro.cod_libro, libro.titulo, libro.anio, libro.tomo)
        self.libros.append(libro)
    def get_categoria(self):
        return self.libros

    def imprimir(self):
        per_data = super().imprimir()
        cod_autor = self.cod_autor
        pais = self.pais
        editorial = self.editorial
        return f'datos del alumno es : {per_data}, codigo de ingreso {cod_autor}, {pais=}, el año de ingreso es: {editorial}'
