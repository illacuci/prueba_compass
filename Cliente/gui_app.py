from cgitb import text
from msilib.schema import ComboBox
from textwrap import fill
import tkinter as tk
from turtle import bgcolor, width
from unicodedata import numeric
from webbrowser import get
from operator import index, truediv 
from tkinter import END, NW, Grid, Image, Label, filedialog, ttk, messagebox, BOTH
import sqlite3
import Util.util as utl
from Cliente.views import FramesDB

#Configuración base correspondiente a la ventana principal de trabajo de la aplicación base para todos los roles/permisos de usuarios.
class StartingFrame():
    def ventana(self):
        self.window = tk.Tk()
        self.window.title ("Compass")
        self.window.geometry("1000x700")
        self.window.resizable(1,1)

        self.frame = tk.Frame()

        self.logo = utl.read_image("Imagenes/Compass_logo.png", (300, 250))
        self.label = tk.Label(self.frame, image=self.logo, bg="#FFFFFF") 
        self.label.place(x=0, y=0, relwidth=1, relheight=1)
        self.frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.menu_bar = tk.Menu(self.window)
        self.window.config(menu = self.menu_bar)     

    def menu_redes(self):
        self.nn_menu = tk.Menu(self.menu_bar, tearoff = 0)
        self.menu_bar.add_cascade(label="Redes neuronales", menu= self.nn_menu)
        self.nn_menu.add_command(label="Nueva red neuronal", command= lambda:  utl.clean_windows(self.window))
        self.nn_menu.add_command(label="Cargar red propia", command= lambda:  [utl.clean_windows(self.window)])
        self.nn_menu.add_separator()
        self.nn_menu.add_command(label="Predicción de precios", command= lambda:  [utl.clean_windows(self.window)])
        self.nn_menu.add_command(label="Errores de listas", command= lambda:  [utl.clean_windows(self.window)])
        self.nn_menu.add_command(label="Errores de movimientos", command= lambda:  [utl.clean_windows(self.window)])

    def menu_automatizaciones(self):
        automatizaciones = tk.Menu(self.menu_bar, tearoff = 0)
        self.menu_bar.add_cascade(label="Automtizaciones", menu= automatizaciones)
        automatizaciones.add_command(label="Proveedores", command= lambda:  [utl.clean_windows(self.window)])
        automatizaciones.add_command(label="Materiales", command= lambda:  [utl.clean_windows(self.window)])
        automatizaciones.add_command(label="Lista de precios", command= lambda:  [utl.clean_windows(self.window)])
        automatizaciones.add_command(label="Pedidos: Catalinas", command= lambda:  [utl.clean_windows(self.window)])
        automatizaciones.add_command(label="Ordenes de compra: Catalinas", command= lambda:  [utl.clean_windows(self.window)])
        automatizaciones.add_command(label="Ordenes de compra SAP: Catalinas", command= lambda:  [utl.clean_windows(self.window)])
        automatizaciones.add_separator()
        automatizaciones.add_command(label="Generar archivos Catalinas", command= lambda:  [utl.clean_windows(self.window)])
        automatizaciones.add_command(label="Envíos de pedidos", command= lambda:  [utl.clean_windows(self.window)])

    def menu_administracion(self):
        administracion = tk.Menu(self.menu_bar, tearoff = 0)
        self.menu_bar.add_cascade(label="Facturas", menu= administracion)
        administracion.add_command(label="Compras", command= lambda:  [utl.clean_windows(self.window)])
        administracion.add_command(label="Cuentas a pagar", command= lambda:  [utl.clean_windows(self.window), FramesDB(self.window).db_view()])
        administracion.add_separator()
        administracion.add_command(label="...", command= lambda:  [utl.clean_windows(self.window)])
        administracion.add_command(label="....", command= lambda:  [utl.clean_windows(self.window)])

    def menu_ayuda(self):
        general_help = tk.Menu(self.menu_bar, tearoff = 0)    
        self.menu_bar.add_cascade(label="Ayuda", menu= general_help)
        general_help.add_command(label="Redes neuronales", command= lambda:  [utl.clean_windows(self.window)])
        general_help.add_separator()
        general_help.add_command(label="Automatizaciones", command= lambda:  [utl.clean_windows(self.window)])
        general_help.add_separator()
        general_help.add_command(label="Web Scraping", command= lambda:  [utl.clean_windows(self.window)])

    def db_control(self):
        db_control = tk.Menu(self.menu_bar, tearoff = 0)
        self.menu_bar.add_cascade(label="Base de Datos", menu= db_control)
        record_tables = tk.Menu(db_control, tearoff=0)
        db_control.add_cascade(label="Tablas de registros", menu=record_tables)
        record_tables.add_command(label="Pedidos", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base_datos/db.db", "Pedidos")])
        record_tables.add_command(label="Planificaciones", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base_datos/db.db", "Planificaciones")])
        record_tables.add_command(label="Facturas", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base_datos/db.db", "Facturas")])
        primary_tables = tk.Menu(db_control, tearoff=0)
        db_control.add_cascade(label="Tablas primarias", menu=primary_tables)
        primary_tables.add_command(label="Productos", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base_datos/db.db", "Productos")])
        primary_tables.add_command(label="Proveedores", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base_datos/db.db", "Proveedores")])
        primary_tables.add_command(label="Comedores", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base_datos/db.db", "Comedores")])
        primary_tables.add_command(label="Cargos", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base_datos/db.db", "Cargos")])
        primary_tables.add_command(label="Ubicaciones", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base_datos/db.db", "Ubicaciones")])
        primary_tables.add_command(label="Empleados", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base_datos/db.db", "Empleados")])
        primary_tables.add_command(label="Bloqueos", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base_datos/db.db", "Bloqueos")])
        primary_tables.add_command(label="Estados", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base_datos/db.db", "Estados")])
        db_control.add_separator()
        table_views = tk.Menu(db_control, tearoff=0)
        db_control.add_cascade(label="Vistas", menu=table_views)
        table_views.add_command(label="Productos")
        table_views.add_command(label="Proveedores")
        table_views.add_command(label="Comedores")
        table_views.add_command(label="Pedidos")
        table_views.add_command(label="Facturas Bloqueadas")

#Crea la vista para el usuario con rol "administrador", agrega los menu habilitados a este rol a la ventaba base.
class AdminMenu(StartingFrame):
    def create(self):
        self.ventana()
        self.menu_administracion()
        self.menu_automatizaciones()
        self.menu_redes()
        self.db_control()
        self.menu_ayuda()
        self.window.mainloop()