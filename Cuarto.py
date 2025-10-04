class Empresa:
    def __init__(self, nombre: str, nit: str, ubicacion: str):
        self.nombre = nombre
        self.nit = nit
        self.ubicacion = ubicacion
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_informacion(self):
        print(f"Empresa: {self.nombre}")
        print(f"NIT: {self.nit}")
        print(f"Ubicación: {self.ubicacion}\n")
        print("=== Empleados y Servicios ===")
        for e in self.empleados:
            e.mostrar_resumen()
        print("====================================\n")


class Servicio:
    def __init__(self, tipo_servicio: str, valor_servicio: float, valor_obra: float, cliente: str):
        self.tipo_servicio = tipo_servicio
        self.valor_servicio = valor_servicio
        self.valor_obra = valor_obra
        self.cliente = cliente

    def calcular_total(self) -> float:
        return self.valor_servicio + self.valor_obra


class Empleado:
    def __init__(self, identificacion: str, nombre: str, cargo: str):
        self.identificacion = identificacion
        self.nombre = nombre
        self.cargo = cargo
        self.servicios = []

    def agregar_servicio(self, servicio: Servicio):
        self.servicios.append(servicio)

    def calcular_total_general(self) -> float:
        return sum(servicio.calcular_total() for servicio in self.servicios)

    def mostrar_resumen(self):
        print(f"\nEmpleado: {self.nombre} ({self.cargo})")
        print("Servicios realizados:")
        for s in self.servicios:
            print(f"- Cliente: {s.cliente}, Tipo: {s.tipo_servicio}, Total: ${s.calcular_total():,.2f}")
        print(f"Total general de servicios: ${self.calcular_total_general():,.2f}\n")


def main():
    # Crear la empresa fija
    empresa = Empresa("Tecnología García", "1234567", "Bogotá, Colombia")

    # Crear empleados
    empleado1 = Empleado("1001", "Laura Gómez", "Técnica")
    empleado2 = Empleado("1002", "Juan Pérez", "Ingeniero de campo")

    # Crear servicios realizados por cada empleado
    servicio1 = Servicio("Instalación de red", 60000, 25000, "Empresa Alfa S.A.")
    servicio2 = Servicio("Mantenimiento de servidores", 85000, 30000, "Comunicaciones Beta")
    servicio3 = Servicio("Configuración de routers", 40000, 20000, "Soluciones Gamma")

    # Asignar servicios
    empleado1.agregar_servicio(servicio1)
    empleado1.agregar_servicio(servicio3)
    empleado2.agregar_servicio(servicio2)

    # Agregar empleados a la empresa
    empresa.agregar_empleado(empleado1)
    empresa.agregar_empleado(empleado2)

    # Mostrar toda la información
    empresa.mostrar_informacion()


if __name__ == "__main__":
    main()
