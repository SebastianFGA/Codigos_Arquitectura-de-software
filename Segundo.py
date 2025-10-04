from typing import List

class Servicio:
    def __init__(self, identificacion_empleado: str, nombre_empleado: str, nombre_cliente: str, valor_servicio: float, valor_obra: float):
        self.identificacion_empleado = identificacion_empleado
        self.nombre_empleado = nombre_empleado
        self.nombre_cliente = nombre_cliente
        self.valor_servicio = valor_servicio
        self.valor_obra = valor_obra

    def calcular_total(self) -> float:
        return self.valor_servicio + self.valor_obra

def calcular_total_servicios(servicios: List[Servicio]) -> float:
    return sum(servicio.calcular_total() for servicio in servicios)

def main():
    servicios = []
    try:
        cantidad_servicios = int(input("Digite la cantidad de servicios: "))
    except ValueError:
        print("Error. Valor no válido para cantidad de servicios.")
        return

    for i in range(cantidad_servicios):
        print(f"\nServicio #{i + 1}")
        identificacion = input("Digite la identificación del empleado: ")
        nombre_empleado = input("Digite el nombre del empleado: ")
        nombre_cliente = input("Digite el nombre del cliente: ")
        try:
            valor_servicio = float(input("Digite el valor del servicio: "))
            valor_obra = float(input("Digite el valor de la mano de obra: "))
        except ValueError:
            print("Error. Valor no válido para servicio u obra.")
            return

        servicio = Servicio(identificacion, nombre_empleado, nombre_cliente, valor_servicio, valor_obra)
        servicios.append(servicio)

    total = calcular_total_servicios(servicios)
    print(f"\nEl valor total de todos los servicios es: {total}")

if __name__ == "__main__":
    main()