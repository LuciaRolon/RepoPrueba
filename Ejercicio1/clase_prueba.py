from datetime import datetime
from decimal import Decimal


class Persona:
    nombre: str
    apellido: str
    fecha_creacion: datetime
    pais: str
    _contrasena: str

    def __init__(self, nombre: str, apellido: str):
        self.nombre = nombre.title()
        self.apellido = apellido.title()
        self.fecha_creacion = datetime.now()

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, nueva_contrasena):
        if len(nueva_contrasena) < 8:
            raise ValueError("Contraseña erronea")
        self._contrasena = nueva_contrasena

    @contrasena.deleter
    def contrasena(self):
        self._contrasena = ""
        print("Contraseña reiniciada")

    @classmethod
    def nombre_default(cls) -> str:
        return "Ame"

    def definir_pais(self, pais: str) -> None:
        if pais.lower() not in ["argentina", "chile", "uruguay"]:
            raise ValueError("El pais no existe")

        self.pais = pais


class Trabajador(Persona):
    horas_semanales: int
    domicilio_laboral: str
    salario: Decimal

    def definir_pais(self, pais: str) -> None:
        if pais.lower() != "chile":
            raise ValueError("El pais no es laborable")

        self.pais = pais
