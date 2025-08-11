from db_config import db


def calcular_consumo(consumo):
    tarifas = db.collection("calculos").document("valores").get()

    if not tarifas:
        print("No trae datos la de BD")

    print(f"Resultados: {tarifas}")

    tabla = tarifas.to_dict().get("energia", {})

    print(f"Tabla: {tabla} ")

    cargo_fijo = None
    cargo_variable = None

    for clave, valor in tabla.items():
        min = valor.get("min", 0)
        max = valor.get("max", 1)

        if min <= consumo <= max:
            if clave.startswith("fijo"):
                cargo_fijo = valor["precio"]
            elif clave.startswith("variable"):
                cargo_variable = valor["precio"]

    print(
        f"Consumo = {consumo} - Cargo Fijo = {cargo_fijo} - Cargo Variable = {cargo_variable}"
    )

    return cargo_fijo, cargo_variable
