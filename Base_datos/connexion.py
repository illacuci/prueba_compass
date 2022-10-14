import sqlite3


def create_connexion(data_base):
    try:
        connexion = sqlite3.connect(data_base)
        return connexion
    except:
        print("Ocurrió un error al intentar la conexión")
