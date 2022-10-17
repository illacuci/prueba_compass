from binascii import Incomplete
from cgitb import text
from distutils.log import error
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
import Base_datos.connexion as Connection

#Crea un frame en la ventana principal con la vista general para editar y visualizar tablas de la base de datos.
class FramesDB(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.config(background="#FFFFFF")

    def create_view(self, data_base, table):
        self.create_menu_db(data_base, table)
        self.create_db_tv(data_base, table)

    def create_menu_db(self,data_base, table):

        self.table = table
        self.data_base = data_base

        self.general_labelframe = ttk.LabelFrame(self.root, text="Tablero de edición")
        self.general_labelframe.pack( side="left", fill="y")

        self.data_frame2 = ttk.LabelFrame(self.general_labelframe, text="Registro")
        self.data_frame2.pack(fill="x", padx=20, pady=20)

        connexion = Connection.create_connexion(data_base)
        cursor = connexion.cursor()
        cursor.execute("SELECT name, type, pk FROM pragma_table_info('"'{}'"')".format(table))
        self.list_columns = cursor.fetchall()

        for index_column in range(len(self.list_columns)):
            if self.list_columns[index_column][2] == 1:
                list_labels_pk = Label(self.data_frame2, text=self.list_columns[index_column][0] + " - PK", width=20, fg="red")
                list_labels_pk.grid(row=index_column, column=0, padx=10, pady=10)

                self.list_entry_pk = ttk.Entry(self.data_frame2)
                self.list_entry_pk.grid(row=index_column, column=1, padx=10, pady=10)

                self.pk = self.list_columns[index_column][0]
            else:
                list_labels = Label(self.data_frame2, text=self.list_columns[index_column][0], width=20)
                list_labels.grid(row=index_column, column=0, padx=10, pady=10)

                list_entry = ttk.Entry(self.data_frame2)
                list_entry.grid(row=index_column, column=1, padx=10, pady=10)

            type_list_labels = Label(self.data_frame2, text=self.list_columns[index_column][1][0])
            type_list_labels.grid(row=index_column, column=2)

        self.button_frame = ttk.LabelFrame(self.general_labelframe, text="Comandos")
        self.button_frame.pack(expand="no", padx=20, fill="x", pady=20)

        self.update_button = ttk.Button(self.button_frame, text="Actualizar registro", command=self.update_record, width=22)
        self.update_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.add_button = ttk.Button(self.button_frame, text="Agregar registro", command=self.insert_record, width=22)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.remove_all_button = ttk.Button(self.button_frame, text="Eliminar TODO", command=self.remove_all, width=22)
        self.remove_all_button.grid(row=1, column=0, padx=10, pady=10)

        self.remove_one_button = ttk.Button(self.button_frame, text="Eliminar 1 seleccionado", command= self.remove_one, width=22)
        self.remove_one_button.grid(row=1, column=1, padx=10, pady=10)

        self.remove_many_button = ttk.Button(self.button_frame, text="Eliminar seleccionados", command=self.remove_many, width=22)
        self.remove_many_button.grid(row=2, column=0, padx=10, pady=10)

        self.move_up_button = ttk.Button(self.button_frame, text="Subir", command=self.up, width=22)
        self.move_up_button.grid(row=2, column=1, padx=10, pady=10)

        self.move_down_button = ttk.Button(self.button_frame, text="Bajar", command=self.down, width=22)
        self.move_down_button.grid(row=3, column=0, padx=10, pady=10)

        self.select_record_button = ttk.Button(self.button_frame, text="Limpiar cuadros", command=self.clear_entries, width=22)
        self.select_record_button.grid(row=3, column=1, padx=10, pady=10)

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

        connexion = Connection.create_connexion(data_base)
        cursor = connexion.cursor()

        cursor.execute("SELECT name FROM pragma_table_info('"'{}'"')".format(table))
        list_columns = cursor.fetchall()
        columns_db_name =[]
        number_column = 0
        for column in list_columns:
            columns_db_name.append(column)
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
        try:
            connexion = Connection.create_connexion("base_datos/db.db")
            cursor = connexion.cursor()   
            cursor.execute("DELETE from {} WHERE {}={}".format(self.table, self.pk, self.my_tree.set(self.my_tree.focus(), column=self.pk)))
            connexion.commit()
            connexion.close()
            x = self.my_tree.selection()[0]
            self.my_tree.delete(x)
        except sqlite3.OperationalError:
            messagebox.showinfo("NO Eliminado!", "ERROR: Tu registro no ha podido ser eliminado!")
            connexion.close()

    def remove_many(self):
        x = self.my_tree.selection()
        connexion = Connection.create_connexion("base_datos/db.db")
        cursor = connexion.cursor()   
        for record in x:
            try:
                cursor.execute("DELETE from {} WHERE {}={}".format(self.table, self.pk, self.my_tree.set(record, column=self.pk)))
            except sqlite3.OperationalError:
                messagebox.showinfo("NO Eliminado!", "ERROR: Tu registro no ha podido ser eliminado!")
                connexion.close()
            self.my_tree.delete(record)
        
        connexion.commit()
        connexion.close()

    def remove_all(self):

            for record in self.my_tree.get_children():
                self.my_tree.delete(record)
                selected = self.my_tree.focus()
            
            connexion = Connection.create_connexion("base_datos/db.db")
            cursor = connexion.cursor()
            cursor.execute("DELETE from {}".format(self.table))
            connexion.commit()
            connexion.close()


    def update_record(self):
        values_to_update = {}
        column = 0
        for children in self.data_frame2.winfo_children():
            if type(children) == tk.ttk.Entry:
                values_to_update[self.list_columns[column][0]] = (children.get())
                column+=1
        selected = self.my_tree.focus()
        self.my_tree.item(selected, text="", values=(list(values_to_update.values())))

        connexion = Connection.create_connexion("base_datos/db.db")
        cursor = connexion.cursor()
        pk_selected = self.list_entry_pk.get()

        for key,value in values_to_update.items():
            cursor.execute(f"UPDATE {self.table} SET {key} = ? WHERE {self.pk} = {pk_selected}",(value,))
        connexion.commit()
        connexion.close()

    def insert_record(self):
        try:
            if self.list_entry_pk.get() == "":
                messagebox.showinfo("NO agregado!", "ERROR DE INTEGRIDAD: clave primaria no puede ser nula!")
            else:
                try:
                    connexion = Connection.create_connexion("base_datos/db.db")
                    cursor = connexion.cursor()
                    values_to_update = []

                    for children in self.data_frame2.winfo_children():
                        if type(children) == tk.ttk.Entry:
                            values_to_update.append(children.get())
                    signs = utl.columns(len(values_to_update))
                    sql= "INSERT INTO {} VALUES ({})".format(self.table,signs)
                    cursor.execute(sql,values_to_update)
                    connexion.commit()
                    connexion.close()

                    self.my_tree.tag_configure('salmon', background="salmon") 
                    self.my_tree.insert(parent='', index='end', text='', values=(values_to_update), tags=('salmon',))
                except sqlite3.IntegrityError:
                    messagebox.showinfo("NO agregado!", "ERROR DE INTEGRIDAD: clave primaria repetida o incorrecta!")
                    connexion.close()
        except AttributeError:
                try:
                    connexion = Connection.create_connexion("base_datos/db.db")
                    cursor = connexion.cursor()
                    values_to_update = []

                    for children in self.data_frame2.winfo_children():
                        if type(children) == tk.ttk.Entry:
                            values_to_update.append(children.get())
                    signs = utl.columns(len(values_to_update))
                    sql= "INSERT INTO {} VALUES ({})".format(self.table,signs)
                    cursor.execute(sql,values_to_update)
                    connexion.commit()
                    connexion.close()

                    self.my_tree.tag_configure('salmon', background="salmon") 
                    self.my_tree.insert(parent='', index='end', text='', values=(values_to_update), tags=('salmon',))
                except sqlite3.IntegrityError:
                    messagebox.showinfo("NO agregado!", "ERROR DE INTEGRIDAD: clave primaria repetida o incorrecta!")
                    connexion.close()