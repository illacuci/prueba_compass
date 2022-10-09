from distutils.log import error
from msilib import sequence
from operator import index
from socket import create_connection
import sqlite3
from typing import Sequence
import pandas as pd
from tkinter import filedialog

class compassdb():
    proveedores = ("""CREATE TABLE IF NOT EXISTS Proveedores  (
            Codigo_Sap INTEGER PRIMARY KEY, 
            Razon_Social TEXT,
            Responsable TEXT
            )""")
    comedores = ("""CREATE TABLE IF NOT EXISTS Comedores  (
            Codigo_Sap INTEGER PRIMARY KEY, 
            Nombre TEXT,
            Responsable TEXT
            )""")
    cargos = ("""CREATE TABLE IF NOT EXISTS Cargos  (
            ID INTEGER PRIMARY KEY, 
            Descripción TEXT
            )""")
    empleados = ("""CREATE TABLE IF NOT EXISTS empleados  (
            Legajo INTEGER PRIMARY KEY, 
            Nombre TEXT,
            Apellido TEXT,
            Cargo TEXT
            )""")
    ubicaciones = ("""CREATE TABLE IF NOT EXISTS ubicaciones  (
            ID INTEGER PRIMARY KEY, 
            Nombre TEXT
            )""")
    pedidos = ("""CREATE TABLE IF NOT EXISTS pedidos  (
            Orden_Compra INTEGER PRIMARY KEY, 
            Producto INTEGER,
            Proveedor INTEGER,
            Comedor TEXT
            )""")
    planificaciones = ("""CREATE TABLE IF NOT EXISTS planificaciones  (
            Comedor TEXT, 
            Producto INTEGER,
            Proveedor INTEGER,
            Fecha INTEGER,
            Cantidad REAL
            )""")
    productos = ("""CREATE TABLE IF NOT EXISTS productos  (
            Codigo_Sap INTEGER PRIMARY KEY, 
            Nombre TEXT
            )""")
    bloqueos = ("""CREATE TABLE IF NOT EXISTS bloqueos  (
            Codigo INTEGER PRIMARY KEY, 
            Bloqueo TEXT
            )""")
    estados = ("""CREATE TABLE IF NOT EXISTS estados  (
            Codigo INTEGER PRIMARY KEY, 
            Estadi TEXT
            )""")
    facturas = ("""CREATE TABLE IF NOT EXISTS facturas  (
            Proveedor INTEGER PRIMARY KEY, 
            Referencia TEXT,
            Bloqueo INTEGER,
            Estado INTEGER,
            Importe REAL
            )""")

    def create_connexion(self, data_base):
        try:
            connexion = sqlite3.connect(data_base)
            return connexion
        except:
            print("Ocurrió un error al intentar la conexión")

    def create_table(self, connexion, sql):
            cursor = connexion.cursor()
            cursor.execute(sql)
            connexion.commit()

    def append_excel(self, connexion, table):

        ruta = filedialog.askopenfilename(title="Abrir", filetypes=(("Archivos de EXCEL","*.XLSX"),("Archivos de EXCEL 2003","*.xls")))
        documento = pd.read_excel(ruta)
        cursor = connexion.cursor()

        def columnas(row):
            columns = ""
            i = 1
            while i <= row:
                if i < row:
                    columns = columns +"?,"
                else:
                    columns = columns + "?"
                i+=1
            return columns

        for index, row in documento.iterrows():
            values = []
            columns = columnas(len(row))
            for i in row:
                values.append(i)
            cursor.execute("INSERT INTO {} ({})  VALUES({});".format(table, documento.keys() ,columns), values)

        connexion.commit()
        connexion.close()

    def consulta_tabla(self, table):
        connexion = sqlite3.connect("base de datos/Compass")
        cursor = connexion.cursor()

        print(cursor.execute("SELECT * FROM Materiales"))

        connexion.commit()
        connexion.close()

    def drop_table(self,connexion, table):
        cursor = connexion.cursor()
        cursor.execute("DROP TABLE {}".format(table))
        connexion.commit()
        connexion.close()

db = compassdb()
connexion = db.create_connexion("base de datos/db.db")
# db.create_table(connexion, db.proveedores)
# db.create_table(connexion, db.comedores)
# db.create_table(connexion, db.cargos)
# db.create_table(connexion, db.empleados)
# db.create_table(connexion, db.ubicaciones)
# db.create_table(connexion, db.pedidos)
# db.create_table(connexion, db.planificaciones)
# db.create_table(connexion, db.bloqueos)
# db.create_table(connexion, db.estados)
# db.create_table(connexion, db.facturas)
db.append_excel(connexion, "cargos")

try:
    connexion.close()
except:
    pass

#a.append_excel("Cotizaciones")

