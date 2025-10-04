# ------------------------------
# Empresa: Tecnología García
# POO con 3 clases conectadas con constructor
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


class Servicio:
    def __init__(self, nombre_servicio, precio, empleado, cliente):
        self.nombre_servicio = nombre_servicio
        self.precio = precio
        self.empleado = empleado
        self.cliente = cliente

    def mostrar_info(self):
        print(f"\nServicio: {self.nombre_servicio}")
        print(f"Precio: ${self.precio}")
        print(self.empleado.mostrar_info())
        print(self.cliente.mostrar_info())


# --- Ejecución principal ---
empresa = Empresa()
empresa.mostrar_info()

cantidad_servicios = int(input("¿Cuántos servicios deseas registrar?: "))

servicios = []

for i in range(cantidad_servicios):
    print(f"\n--- Servicio #{i+1} ---")
    nombre_servicio = input("Nombre del servicio: ")
    precio = float(input("Precio del servicio: "))

    print("\n--- Datos del empleado ---")
    nombre_empleado = input("Nombre del empleado: ")
    cargo_empleado = input("Cargo del empleado: ")
    empleado = Empleado(nombre_empleado, cargo_empleado)

    print("\n--- Datos del cliente ---")
    nombre_cliente = input("Nombre del cliente: ")
    contacto_cliente = input("Contacto del cliente: ")
    cliente = Cliente(nombre_cliente, contacto_cliente)

    servicio = Servicio(nombre_servicio, precio, empleado, cliente)
    servicios.append(servicio)

print("\n===== Servicios registrados =====")
for s in servicios:
    s.mostrar_info()
