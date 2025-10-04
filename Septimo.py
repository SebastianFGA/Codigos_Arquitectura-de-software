from abc import ABC, abstractmethod

# ------------------------------
# Empresa: Tecnología García
# POO con Abstracción
# ------------------------------

class Empresa:
    def __init__(self):
        self.nombre = "Tecnología García"
        self.nit = "1234567"
        self.ubicacion = "Bogotá, Colombia"

    def mostrar_info(self):
        print(f"Empresa: {self.nombre} | NIT: {self.nit} | Ubicación: {self.ubicacion}\n")


class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo

    def mostrar_info(self):
        return f"Empleado: {self.nombre} ({self.cargo})"


class Cliente:
    def __init__(self, nombre, contacto):
        self.nombre = nombre
        self.contacto = contacto

    def mostrar_info(self):
        return f"Cliente: {self.nombre} | Contacto: {self.contacto}"


# --- Clase abstracta ---
from abc import ABC, abstractmethod

class ServicioBase(ABC):
    def __init__(self, nombre_servicio, precio_base, empleado, cliente):
        self.nombre_servicio = nombre_servicio
        self.precio_base = precio_base
        self.empleado = empleado
        self.cliente = cliente

    @abstractmethod
    def calcular_total(self):
        """Método abstracto: debe implementarse en las clases hijas"""
        pass

    @abstractmethod
    def mostrar_info(self):
        """Método abstracto: mostrar la información del servicio"""
        pass


# --- Clases concretas ---
class ServicioBasico(ServicioBase):
    def calcular_total(self):
        return self.precio_base

    def mostrar_info(self):
        print(f"\n[Servicio Básico] {self.nombre_servicio}")
        print(f"Precio base: ${self.precio_base}")
        print(self.empleado.mostrar_info())
        print(self.cliente.mostrar_info())
        print(f"Total: ${self.calcular_total()}")


class ServicioPremium(ServicioBase):
    def calcular_total(self):
        return self.precio_base * 1.25  # recargo del 25%

    def mostrar_info(self):
        print(f"\n[Servicio Premium] {self.nombre_servicio}")
        print(f"Precio base: ${self.precio_base}")
        print(self.empleado.mostrar_info())
        print(self.cliente.mostrar_info())
        print(f"Total con recargo: ${self.calcular_total()}")


# --- Ejecución principal ---
empresa = Empresa()
empresa.mostrar_info()

cantidad_servicios = int(input("¿Cuántos servicios deseas registrar?: "))
servicios = []

for i in range(cantidad_servicios):
    print(f"\n--- Servicio #{i + 1} ---")
    nombre_servicio = input("Nombre del servicio: ")
    precio = float(input("Precio base del servicio: "))

    print("\n--- Datos del empleado ---")
    nombre_empleado = input("Nombre del empleado: ")
    cargo_empleado = input("Cargo del empleado: ")
    empleado = Empleado(nombre_empleado, cargo_empleado)

    print("\n--- Datos del cliente ---")
    nombre_cliente = input("Nombre del cliente: ")
    contacto_cliente = input("Contacto del cliente: ")
    cliente = Cliente(nombre_cliente, contacto_cliente)

    tipo = input("Tipo de servicio (basico/premium): ").lower()

    if tipo == "premium":
        servicio = ServicioPremium(nombre_servicio, precio, empleado, cliente)
    else:
        servicio = ServicioBasico(nombre_servicio, precio, empleado, cliente)

    servicios.append(servicio)

print("\n===== Servicios registrados =====")
for s in servicios:
    s.mostrar_info()
