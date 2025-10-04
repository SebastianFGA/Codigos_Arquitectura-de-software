def main():
    identificaciones = []
    Nombre_empleado = []
    nombres_cliente = []
    Tipo_de_servicio = []
    Cantidad_de_servicios = []
    ValorS = []
    ValorO = []
   
    Cantidad_de_servicios = int(input("Digite la cantidad de servicios: "))
    
    identificacion = (input("Digite la identificacion del empleado: "))
   # Nombre_empleado = (input("Digite el nombre del empleado: "))
  #  nombres_cliente = input("Digite el nombre del cliente: ")

    for i in range(Cantidad_de_servicios):
        print(f"Cantidad_de_servicios (1 + 1):")
        Valor_servicio = float(input("Digite El valor del servicio: "))
        Valor_obra = float(input("Digite el valor de la mano de obra: "))

        identificaciones.append(identificacion)
        Nombre_empleado.append(Nombre_empleado)
        nombres_cliente.append(nombres_cliente)
        ValorS.append(Valor_servicio)
        ValorO.append(Valor_obra) 

    Tota_servicio = sum(ValorS[i] + ValorO[i] for i in range(Cantidad_de_servicios))
   
    print(f"el valor del servicio es: {Tota_servicio}")
if __name__ == "__main__":
    main()
