# Clase para manejar precio, impuestos y calcular consumo


class Session:
    def __init__(self, provincia, impuestos, tarifa):
        self.provincia = provincia
        self.impuestos = impuestos
        self.tarifa = tarifa
        self.consumo_total = 0.0
        self.consumos = []  # Inicia como lista vacia

    # Metodo para agregar consumos
    def agregar_consumo(
        self, equipo, cantidad, watts, horas_dia, dias_mes, ambiente, icono
    ):
        kwh_mes = (watts / 1000) * horas_dia * dias_mes
        self.consumo_total += kwh_mes

        self.consumos.append(
            {
                "equipo": equipo,
                "cantidad": cantidad,
                "watts": watts,
                "horas_dias": horas_dia,
                "dias_mes": dias_mes,
                "ambiente": ambiente,
                "icono": icono,
            }
        )

    # Metodo para calcular el total de la factura
    def calcular_total_factura(self):
        return self.consumo_total * self.tarifa * self.impuestos


session = Session("Buenos Aires", 1.23, 100)


class Consumo:
    def __init__(self, nombre, ambiente, consumo_kwh, icono):
        self.nombre = nombre
        self.ambiente = ambiente
        self.consumo_kwh = consumo_kwh
        self.icono = icono
