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

class StartingFrame():
    def abc(self):
        self.window = tk.Tk()
        self.window.title ("Compass")
        self.window.geometry("1000x700")
        self.window.resizable(1,1)

        self.frame = tk.Frame()

        self.logo = utl.read_image("Imágenes/Compass_logo.png", (300, 250))
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
        record_tables.add_command(label="Pedidos", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base de datos/db.db", "Pedidos")])
        record_tables.add_command(label="Planificaciones", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base de datos/db.db", "Planificaciones")])
        record_tables.add_command(label="Facturas", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base de datos/db.db", "Facturas")])
        primary_tables = tk.Menu(db_control, tearoff=0)
        db_control.add_cascade(label="Tablas primarias", menu=primary_tables)
        primary_tables.add_command(label="Productos", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base de datos/db.db", "Productos")])
        primary_tables.add_command(label="Proveedores", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base de datos/db.db", "Proveedores")])
        primary_tables.add_command(label="Comedores", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base de datos/db.db", "Comedores")])
        primary_tables.add_command(label="Cargos", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base de datos/db.db", "Cargos")])
        primary_tables.add_command(label="Ubicaciones", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base de datos/db.db", "Ubicaciones")])
        primary_tables.add_command(label="Empleados", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base de datos/db.db", "Empleados")])
        primary_tables.add_command(label="Bloqueos", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base de datos/db.db", "Bloqueos")])
        primary_tables.add_command(label="Estados", command= lambda: [utl.clean_windows(self.window), FramesDB(self.window).create_view("base de datos/db.db", "Estados")])
        db_control.add_separator()
        table_views = tk.Menu(db_control, tearoff=0)
        db_control.add_cascade(label="Vistas", menu=table_views)
        table_views.add_command(label="Productos")
        table_views.add_command(label="Proveedores")
        table_views.add_command(label="Comedores")
        table_views.add_command(label="Pedidos")
        table_views.add_command(label="Facturas Bloqueadas")

class AdminMenu(StartingFrame):
    def __init__(self):
        self.abc()
        self.menu_administracion()
        self.menu_automatizaciones()
        self.menu_redes()
        self.db_control()
        self.menu_ayuda()

        self.window.mainloop()

class FramesDB(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.config(background="#FFFFFF")

    def create_view(self, data_base, table):
        self.create_menu_db(data_base, table)
        self.create_db_tv(data_base, table)
    
    def create_connexion(self, data_base):
        try:
            connexion = sqlite3.connect(data_base)
            return connexion
        except:
            print("Ocurrió un error al intentar la conexión")

    def create_menu_db(self,data_base, table):
        self.general_labelframe = ttk.LabelFrame(self.root, text="Tablero de edición")
        self.general_labelframe.pack( side="left", fill="y")

        self.data_frame2 = ttk.LabelFrame(self.general_labelframe, text="Registro")
        self.data_frame2.pack(fill="x", padx=20, pady=20)

        connexion = self.create_connexion(data_base)
        cursor = connexion.cursor()        
        cursor.execute("SELECT name FROM pragma_table_info('"'{}'"')".format(table))
        list_columns = cursor.fetchall()

        for index_column in range(len(list_columns)):
            list_labels = "self.label"+str(index_column)
            list_labels = Label(self.data_frame2, text=list_columns[index_column], width=20)
            list_labels.grid(row=index_column, column=0, padx=10, pady=10)

            list_entry = "self.entry"+str(index_column)
            list_entry = ttk.Entry(self.data_frame2)
            list_entry.grid(row=index_column, column=1, padx=10, pady=10)




        self.button_frame = ttk.LabelFrame(self.general_labelframe, text="Comandos")
        self.button_frame.pack(expand="no", padx=20, fill="x", pady=20)

        self.update_button = ttk.Button(self.button_frame, text="Actualizar registro", command=self.update_record, width=50)
        self.update_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.add_button = ttk.Button(self.button_frame, text="Agregar registro", command=self.insert_record, width=50)
        self.add_button.grid(row=1, column=0, padx=10, pady=10)

        self.remove_all_button = ttk.Button(self.button_frame, text="Eliminar TODO", command=self.remove_all, width=50)
        self.remove_all_button.grid(row=2, column=0, padx=10, pady=10)

        self.remove_one_button = ttk.Button(self.button_frame, text="Eliminar 1 seleccionado", command=self.remove_one, width=50)
        self.remove_one_button.grid(row=3, column=0, padx=10, pady=10)

        self.remove_many_button = ttk.Button(self.button_frame, text="Eliminar seleccionados", command=self.remove_many, width=50)
        self.remove_many_button.grid(row=4, column=0, padx=10, pady=10)

        self.move_up_button = ttk.Button(self.button_frame, text="Subir", command=self.up, width=50)
        self.move_up_button.grid(row=5, column=0, padx=10, pady=10)

        self.move_down_button = ttk.Button(self.button_frame, text="Bajar", command=self.down, width=50)
        self.move_down_button.grid(row=6, column=0, padx=10, pady=10)

        self.select_record_button = ttk.Button(self.button_frame, text="Limpiar cuadros", command=self.clear_entries, width=50)
        self.select_record_button.grid(row=7, column=0, padx=10, pady=10)

    def create_db_tv(self, data_base, table):

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3")
        style.map('Treeview',
        background=[('selected', "#347083")])

        tree_scroll_y = ttk.Scrollbar(self)
        tree_scroll_y.pack(side="right", fill="y")
        tree_scroll_x = ttk.Scrollbar(self,orient="horizontal")
        tree_scroll_x.pack(side="bottom", fill="x")

        connexion = self.create_connexion(data_base)
        cursor = connexion.cursor()

        cursor.execute("SELECT name FROM pragma_table_info('"'{}'"')".format(table))
        list_columns = cursor.fetchall()
        columns_db_name =[]
        number_column = 0
        for column in list_columns:
            columns_db_name.append("column"+str(number_column))
            number_column +=1

        self.my_tree = ttk.Treeview(self, selectmode="extended", yscrollcommand=tree_scroll_y.set, columns=columns_db_name, show="headings", height=40, xscrollcommand=tree_scroll_x.set )
        self.my_tree.pack()

        tree_scroll_y.config(command=self.my_tree.yview)
        tree_scroll_x.config(command=self.my_tree.xview)

        for index_column in range(len(columns_db_name)):
            self.my_tree.heading(columns_db_name[index_column], text=list_columns[index_column], anchor="w")

        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")

        cursor.execute("SELECT * FROM {}".format(table))
        records = cursor.fetchall()
        count = 0
        for record in records:
            if count % 2 == 0:
                self.my_tree.insert(parent='', index='end', iid=count, text='', values=(record), tags=('evenrow',))
            else:
                self.my_tree.insert(parent='', index='end', iid=count, text='', values=(record), tags=('oddrow',))  
            count += 1

        connexion.commit()
        connexion.close()

        self.pack(fill="both")
                
    def clear_entries(self):
        for children in self.data_frame2.winfo_children():
            if type(children) == tk.ttk.Entry:
                children.delete(0, END)

    def up(self):
        rows = self.my_tree.selection()
        for row in rows:
            self.my_tree.move(row, self.my_tree.parent(row), self.my_tree.index(row)-1)

    def down(self):
        rows = self.my_tree.selection()
        for row in reversed(rows):
            self.my_tree.move(row, self.my_tree.parent(row), self.my_tree.index(row)+1)

    def remove_one(self):
        x = self.my_tree.selection()[0]
        self.my_tree.delete(x)

    def remove_many(self):
        x = self.my_tree.selection()
        for record in x:
            self.my_tree.delete(record)

    def remove_all(self):
        for record in self.my_tree.get_children():
            self.my_tree.delete(record)

            selected = self.my_tree.focus()

    def update_record(self):
        values_to_update = []
        for children in self.data_frame2.winfo_children():
            if type(children) == tk.ttk.Entry:
                values_to_update.append(children.get())
        selected = self.my_tree.focus()
        self.my_tree.item(selected, text="", values=(values_to_update))
        #conn = sqlite3.connect('base de datos/Compass')
        #c = conn.cursor()

    def insert_record(self):
        values_to_update = []
        for children in self.data_frame2.winfo_children():
            if type(children) == tk.ttk.Entry:
                values_to_update.append(children.get()) 
        self.my_tree.tag_configure('salmon', background="salmon") 
        self.my_tree.insert(parent='', index='end', text='', values=(values_to_update), tags=('salmon',))






