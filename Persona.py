

class Persona:
    codigo = ""
    nombres = ""
    ap_paterno = ""
    ap_materno = ""
    anio_nacimiento = 0
    def __init__(self, codigo, nombres, ap_paterno, ap_materno, anio_nacimiento):
        self.codigo = codigo
        self.nombres = nombres
        self.ap_paterno = ap_paterno
        self.ap_materno = ap_materno
        self.anio_nacimiento = anio_nacimiento

    def set_codigo(self, codigo):
        self.codigo = codigo
    def get_codigo(self):
        return self.codigo

    def set_nombres(self, nombres):
        self.nombres = nombres
    def get_nombres(self):
        return self.nombres

    def set_ap_paterno(self, ap_paterno):
        self.ap_paterno = ap_paterno
    def get_ap_paterno(self):
        return self.ap_paterno

    def set_ap_materno(self, ap_materno):
        self.ap_materno = ap_materno
    def get_ap_materno(self):
        return self.ap_materno

    def set_anio_nacimiento(self, anio_nacimiento):
        self.anio_nacimiento = anio_nacimiento
    def get_anio_nacimiento(self):
        return self.anio_nacimiento

    def imprimir(self):
        nombres = self.nombres
        apellidos = self.ap_paterno + ' ' + self.ap_materno
        anio_nacimiento = self.anio_nacimiento
        return f' {nombres=},  {apellidos=}, {anio_nacimiento=}'