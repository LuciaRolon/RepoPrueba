from typing import Optional

from clase_prueba import Persona, Trabajador


def mostrar_numero(numero_uno: Optional[int] = None) -> None:
    if numero_uno == None:
        print("No se cargó el numero")
        return
    print(f"Numero 1: {numero_uno}")


mostrar_numero(0)
# Definimos una persona default
nueva_persona = Persona("lucy", "rolon")
nueva_persona.definir_pais("argentina")
nuevo_trabajador = Trabajador("ame", "lynn")
nuevo_trabajador.definir_pais("argentina")
