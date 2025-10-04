class Servicio:
    def __init__(self, nombre_cliente: str, tipo_servicio: str, valor_servicio: float, valor_obra: float):
        self.nombre_cliente = nombre_cliente
        self.tipo_servicio = tipo_servicio
        self.valor_servicio = valor_servicio
        self.valor_obra = valor_obra

    def calcular_total(self) -> float:
        """Calcula el valor total del servicio (servicio + mano de obra)."""
        return self.valor_servicio + self.valor_obra


class Empleado:
    def __init__(self, identificacion: str, nombre: str, cargo: str):
        self.identificacion = identificacion
        self.nombre = nombre
        self.cargo = cargo
        self.servicios = []  # Lista para almacenar los servicios del empleado

    def agregar_servicio(self, servicio: Servicio):
        """Agrega un servicio a la lista de servicios del empleado."""
        self.servicios.append(servicio)

    def calcular_total_general(self) -> float:
        """Suma el valor total de todos los servicios realizados por el empleado."""
        return sum(servicio.calcular_total() for servicio in self.servicios)

    def mostrar_resumen(self):
        """Muestra todos los servicios y el total general."""
        print(f"\nEmpleado: {self.nombre} ({self.cargo})")
        print("Servicios realizados:")
        for s in self.servicios:
            print(f"- Cliente: {s.nombre_cliente}, Tipo: {s.tipo_servicio}, Total: {s.calcular_total()}")
        print(f"Total general de servicios: {self.calcular_total_general()}")


def main():
    print("=== REGISTRO DE SERVICIOS DE EMPLEADOS ===")

    # Datos del empleado
    identificacion = input("Ingrese la identificación del empleado: ")
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    cargo = input("Ingrese el cargo del empleado: ")

    empleado = Empleado(identificacion, nombre_empleado, cargo)

    try:
        cantidad = int(input("Digite la cantidad de servicios realizados: "))
    except ValueError:
        print("Error: cantidad no válida.")
        return

    for i in range(cantidad):
        print(f"\n--- Servicio #{i + 1} ---")
        nombre_cliente = input("Nombre del cliente: ")
        tipo_servicio = input("Tipo de servicio: ")
        try:
            valor_servicio = float(input("Valor del servicio: "))
            valor_obra = float(input("Valor de la mano de obra: "))
        except ValueError:
            print("Error: valor inválido.")
            return

        servicio = Servicio(nombre_cliente, tipo_servicio, valor_servicio, valor_obra)
        empleado.agregar_servicio(servicio)

    empleado.mostrar_resumen()


if __name__ == "__main__":
    main()
