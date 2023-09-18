

class Categoria:
    cod_categoria = ""
    nombre = ""
    def __init__(self, cod_categoria, nombre):
        self.cod_categoria = cod_categoria
        self.nombre = nombre

    def set_cod_categoria(self, cod_categoria):
        self.cod_categoria = cod_categoria
    def get_cod_categoria(self):
        return self.cod_categoria

    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_nombre(self):
        return self.nombre