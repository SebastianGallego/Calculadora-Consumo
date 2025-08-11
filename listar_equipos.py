from db_config import db


def listar_equipos(nombre_ambiente):
    documento = db.collection("ambientes").document(nombre_ambiente.lower())
    listado = documento.get()

    if listado.exists:
        equipos = listado.to_dict().get("equipos", [])
        return equipos

    else:
        print("No hay datos")
