from Categoria import Categoria

class Libro:
    cod_libro = ""
    titulo = ""
    anio = ""
    tomo = ""
    categoria = ""
    def __init__(self, cod_libro, titulo, anio, tomo):
        self.cod_libro = cod_libro
        self.titulo = titulo
        self.anio = anio
        self.tomo = tomo
        self.categoria = ""

    def set_cod_libro(self, cod_libro):
        self.cod_libro = cod_libro
    def get_cod_libro(self):
        return self.cod_libro

    def set_titulo(self, titulo):
        self.titulo = titulo
    def get_titulo(self):
        return self.titulo

    def set_anio(self, anio):
        self.anio = anio
    def get_anio(self):
        return self.anio

    def set_tomo(self, tomo):
        self.tomo = tomo
    def get_tomo(self):
        return self.tomo

    def set_categoria(self, categoria):
        categoria = Categoria(categoria.cod_categoria, categoria.nombre)
        self.categoria = categoria
    def get_categoria(self):
        return self.categoria