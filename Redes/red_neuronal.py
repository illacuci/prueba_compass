class NN_views(Frames):
    
    def labels_parametros_nn(self):

        #Entry
        self.entry_learning_rate = ttk.Combobox(self,width=25)
        opcions_entry_learning_rate = ["0.001","0.005","0.01","0.05","0.1","0.5","1"]
        self.entry_learning_rate['values'] = opcions_entry_learning_rate
        self.entry_learning_rate.place(rely=0.08,relx=0.2)
        
        self.entry_epochs = ttk.Combobox(self,width=25)
        opcions_entry_epochs = ["100","1000","5000","10000","15000","20000","50000"]
        self.entry_epochs['values'] = opcions_entry_epochs
        self.entry_epochs.place(rely=0.16,relx=0.2)

        self.entry_normalizer = ttk.Combobox(self,width=25)
        opcions_entry_normalizer = ["Nada","MinMaxScaler"]
        self.entry_normalizer['values'] = opcions_entry_normalizer
        self.entry_normalizer.place(rely=0.24,relx=0.2)

        self.entry_loss_function = ttk.Combobox(self,width=25)
        opcions_entry_loss_function = ["Clasificación" , "Regresión"]
        self.entry_loss_function['values'] = opcions_entry_loss_function
        self.entry_loss_function.place(rely=0.32,relx=0.2)

        self.entry_optimizer = ttk.Combobox(self,width=25)
        opcions_entry_optimizer = ["Adam", "SGD"]
        self.entry_optimizer['values'] = opcions_entry_optimizer
        self.entry_optimizer.place(rely=0.40,relx=0.2)

        self.entry_activation_function = ttk.Combobox(self,width=25)
        opcions_entry_activation_function = ["ReLU","Sigmoide"]
        self.entry_activation_function['values'] = opcions_entry_activation_function
        self.entry_activation_function.place(rely=0.48,relx=0.2)

        self.entry_test_size = ttk.Combobox(self,width=25)
        opcions_entry_test_size = ["0.0","0.1","0.2","0.3","0.4" ]
        self.entry_test_size['values'] = opcions_entry_test_size
        self.entry_test_size.place(rely=0.56,relx=0.2)

        self.entry_y_column = ttk.Entry(self,width=28)
        self.entry_y_column.place(rely=0.64,relx=0.2)

        self.entry_model_name = ttk.Entry(self,width=28)
        self.entry_model_name.place(rely=0.72,relx=0.2)


        self.label_learning_rate = ttk.Label(self, text="Learning Rate: ")
        self.label_learning_rate.place(rely=0.08,relx=0.05)
        
        self.label_epochs = ttk.Label(self, text="Epochs: ")
        self.label_epochs.place(rely=0.16,relx=0.05)

        self.label_normalizer = ttk.Label(self, text="Normalizer: ")
        self.label_normalizer.place(rely=0.24,relx=0.05)

        self.label_loss_function = ttk.Label(self, text="Loss Function: ")
        self.label_loss_function.place(rely=0.32,relx=0.05)

        self.label_optimizer = ttk.Label(self, text="Optimizer: ")
        self.label_optimizer.place(rely=0.40,relx=0.05)

        self.label_activation_function = ttk.Label(self, text="Activation Function:")
        self.label_activation_function.place(rely=0.48,relx=0.05)

        self.label_test_size = ttk.Label(self, text="Test Size: ")
        self.label_test_size.place(rely=0.56,relx=0.05)

        self.label_y_column = ttk.Label(self, text="Y Column Name: ")
        self.label_y_column.place(rely=0.64,relx=0.05)

        self.label_model_name = ttk.Label(text="Model name: ")
        self.label_model_name.place(rely=0.72,relx=0.05)

        #capas ocultas
        self.boton_aumentar_neuronas = tk.Button(self, text="↑", command=lambda: [modificar_cantidad_capas(1, self.cantidad_capas, 3), agregar_neuronas_capas(1)])
        self.boton_aumentar_neuronas.place(rely=0.07,relx=0.650)

        self.cantidad_capas = ttk.Label(self,width=3, text="1")
        self.cantidad_capas.place(rely=0.074,relx=0.6865)

        self.titulo_capas = ttk.Label(self, text="Capas ocultas")
        self.titulo_capas.place(rely=0.0402,relx=0.65)

        self.boton_disminuir_neuronas = tk.Button(self, text="↓",command=lambda: [modificar_cantidad_capas(-1, self.cantidad_capas, 3), agregar_neuronas_capas(-1)])
        self.boton_disminuir_neuronas.place(rely=0.07,relx=0.71)

        #capas neuronas por capa
        self.boton_aumentar1= tk.Button(self, text="↑",command=lambda: modificar_cantidad_capas(1, self.cantidad_capas1, 15))
        self.boton_aumentar1.place(rely=0.16,relx=0.65)
        self.cantidad_capas1 = ttk.Label(self,width=3, text="1")
        self.cantidad_capas1.place(rely=0.16,relx=0.6865)
        self.label_titulos1 = ttk.Label(self, text="Capa 1")
        self.label_titulos1.place(rely=0.13,relx=0.67)
        self.boton_disminuir1= tk.Button(self, text="↓",command=lambda: modificar_cantidad_capas(-1, self.cantidad_capas1, 15))
        self.boton_disminuir1.place(rely=0.16,relx=0.71)

        self.boton_aumentar2= tk.Button(self, text="↑",command=lambda: modificar_cantidad_capas(1, self.cantidad_capas2, 15))
        self.cantidad_capas2 = ttk.Label(self,width=3, text="1",background="white")
        self.label_titulos2 = ttk.Label(self, text="Capa 2",background="white")
        self.boton_disminuir2= tk.Button(self, text="↓",command=lambda: modificar_cantidad_capas(-1, self.cantidad_capas2, 15))

        self.boton_aumentar3= tk.Button(self, text="↑",command=lambda: modificar_cantidad_capas(1, self.cantidad_capas3, 15))
        self.cantidad_capas3 = ttk.Label(self,width=3, text="1",background="white")
        self.label_titulos3 = ttk.Label(self, text="Capa 3",background="white")
        self.boton_disminuir3= tk.Button(self, text="↓",command=lambda: modificar_cantidad_capas(-1, self.cantidad_capas3, 15))

        self.boton_aumentar4= tk.Button(self, text="↑",command=lambda: modificar_cantidad_capas(1, self.cantidad_capas4, 15))
        self.cantidad_capas4 = ttk.Label(self,width=3, text="1",background="white")
        self.label_titulos4 = ttk.Label(self, text="Capa 4",background="white")
        self.boton_disminuir4= tk.Button(self, text="↓",command=lambda: modificar_cantidad_capas(-1, self.cantidad_capas4, 15))

        def modificar_cantidad_capas(valor, variable, cantidad):
            capas = int(variable.cget("text"))
            if valor == 1 and capas > cantidad or valor == -1 and capas < 2:
                pass
            else: 
                variable.config(text= capas + valor)

        def agregar_neuronas_capas(valor):
            capas = int(self.cantidad_capas.cget("text"))
            if valor == 1 and capas > 4 or valor == -1 and capas < 1:
                pass
            else:
                botones_aumentar = [self.boton_aumentar1,self.boton_aumentar2,self.boton_aumentar3,self.boton_aumentar4]
                botones_disminuir = [self.boton_disminuir1,self.boton_disminuir2,self.boton_disminuir3,self.boton_disminuir4]
                labels_botones = [self.cantidad_capas1,self.cantidad_capas2,self.cantidad_capas3,self.cantidad_capas4]
                labels_titulos = [self.label_titulos1,self.label_titulos2,self.label_titulos3,self.label_titulos4]
                for i in range(4):

                    if i < capas:
                        x =0.5/(capas+1)
                        botones_aumentar[i].place(rely=0.16,relx=0.4+x*(i+1))
                        labels_botones[i].place(rely=0.16,relx=0.4365+ x *(i+1))
                        botones_disminuir[i].place(rely=0.16,relx=0.46+ x *(i+1))
                        labels_titulos[i].place(rely=0.13,relx=0.42+ x *(i+1))
                    else:
                        botones_aumentar[i].place_forget()
                        labels_botones[i].place_forget()
                        botones_disminuir[i].place_forget()
                        labels_titulos[i].place_forget()
        
        tv =ttk.Treeview(self)
        tv.insert("",END ,text="DATOS")
        tv.place(rely=0.3, relx=0.4)


        self.pack()
        self.config(width="1000", height="700", bg="white")

        for i  in self.place_slaves():
            if type(i) == tkinter.ttk.Label:
                i.config(background="white")

        #Boton generar modelo
        boton_entrenar_nuevo = tk.Button(self, text="Generar Modelo", command=lambda: Redes.model.nn(
        self.entry_normalizer.get(),
        float(self.entry_learning_rate.get()),
        int(self.entry_epochs.get()),
        100,
        self.entry_loss_function.get(),
        self.entry_y_column.get(),
        float(self.entry_test_size.get()),
        self.entry_model_name.get()).entrenar())

        #boton importar datos

        boton_importar_nuevo = tk.Button(self, text="Importar datos", command=lambda: [modelo_importado().describe() ,boton_entrenar_nuevo.place(rely=0.8,relx=0.5),boton_importar_nuevo.place_forget() ])

        boton_importar_nuevo.place(rely=0.8, relx=0.5)

        print(self.data_frame_bruto)

    def frame_importar_modelo (self):

        self.pack(anchor=NW)

        boton_entrenar_nuevo = tk.Button(self, text="Importar modelo", command= lambda: print(self.import_model()))
        boton_entrenar_nuevo.grid(row=0,column=0 ,columnspan=2, pady=20, ipadx=20, ipady=5)

    def frame_importar_modelo_existente (self, path):

        self.pack(anchor=NW)

        boton_entrenar_nuevo = tk.Button(self, text="Obtener predicción", command= lambda: [self.import_model(), print(self.the_model)])
        boton_entrenar_nuevo.grid(row=0,column=0 ,columnspan=2, pady=20, ipadx=20, ipady=5)

        self.the_model = torch.load(path)
        return self.the_model

    def import_model (self):
        self.documento = filedialog.askopenfilename(title="Abrir", filetypes=(("Modelos guardados","*.pt"),("Archivos de EXCEL 2003","*.xls")))

        model = torch.jit.load(self.documento)
        model.eval()

        return model


        

def modelo_importado():
    documento = filedialog.askopenfilename(title="Abrir", filetypes=(("Archivos de EXCEL","*.XLSX"),("Archivos de EXCEL 2003","*.xls")))
    data_frame_bruto = pd.read_excel(documento)
    return data_frame_bruto