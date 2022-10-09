from subprocess import call
from tkinter import filedialog
from unicodedata import name
import pandas as pd
from sklearn.preprocessing import *
import torch
from sklearn.model_selection import train_test_split
from torch.utils.data import random_split, TensorDataset
import matplotlib.pyplot as plt
import torch

class new_nn ():

    def __init__(self,normalizer,learning_rate,epochs,estatus_print,loss_function, column_y, test_size, model_name):
         
        self.model_name = model_name
        self.normalizer = normalizer
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.estatus_print = estatus_print
        self.loss_function = loss_function
        self.column_y = column_y
        self.test_size = test_size
        self.optimizer = torch.optim.Adam(params=self.model.parameters(), lr= self.learning_rate)

        class Red(torch.nn.Module):

            def __init__(self):
                super().__init__()
                self.linear1 = torch.nn.Linear(2, 4)
                self.linear2 = torch.nn.Linear(4, 4)
                self.linear3 = torch.nn.Linear(4, 1)
        
            def forward(self, inputs):
                pred_1 = torch.relu(self.linear1(inputs))
                pred_2 = torch.relu(self.linear2(pred_1))
                pred_f = torch.relu(self.linear3(pred_2))
                return pred_f

        self.model = Red()

    def entrenar(self):
        self.import_data()
        self.training()
    
    def import_data(self):

        documento = filedialog.askopenfilename(title="Abrir", filetypes=(("Archivos de EXCEL","*.XLSX"),("Archivos de EXCEL 2003","*.xls")))
        datos = pd.read_excel(documento)

        #NORMALIZADOR
        if self.normalizer == "MinMaxScaler":
            self.normalizer = MinMaxScaler()
        else:
            self.normalizer = 0

        if type(self.normalizer) == type(MinMaxScaler()):
            datos_x = self.normalizer.fit_transform(datos)
        else:
            datos_x = datos.to_numpy()

        datos_y = datos_x[:,-1]
        datos_x = datos.drop(columns=[self.column_y])
        datos_x = pd.DataFrame(datos_x).to_numpy()

        X_train, X_test, y_train, y_test = train_test_split(datos_x, datos_y, test_size = self.test_size, random_state = 2)

        self.t_y_train = torch.from_numpy(datos_y).float()
        self.t_y_test = torch.from_numpy(y_test).float()
        self.t_X_train = torch.from_numpy(datos_x).float()
        self.t_X_test = torch.from_numpy(X_test).float()
        self.t_y_train = self.t_y_train[:,None]
        self.t_y_test = self.t_y_test[:, None]

        self.test = TensorDataset(self.t_X_test, self.t_y_test)

    def training(self):
    
        print("Arquitectura del modelo: {}".format(self.model))
        print("Entranando el modelo")
        historico = pd.DataFrame()

        for epoch in range(1, self.epochs+1):
            y_pred = self.model(self.t_X_train)

            if self.loss_function == "Regresión":
                self.loss_function = torch.nn.MSELoss()
            else:
                self.loss_function =  torch.nn.CrossEntropyLoss()

            loss = self.loss_function(input=y_pred, target=self.t_y_train)
            loss.backward()
            self.optimizer.step()
            self.optimizer.zero_grad()
            
            if epoch % self.estatus_print == 0:
                print(f"\nEpoch {epoch} \t Loss: {round(loss.item(), 4)}")

            with torch.no_grad():

                y_pred = self.model(self.t_X_test)
                y_pred_class = y_pred.round()
                correct = (y_pred_class == self.t_y_test).sum()
                accuracy = 100 * correct / float(len(self.t_y_test))
                if epoch % self.estatus_print == 0:
                    print("Accuracy: {}".format(accuracy.item()))
    
                df_tmp = pd.DataFrame(data={
                'Epoch': epoch,
                'Loss': round(loss.item(), 4),
                'Accuracy': round(accuracy.item(), 4)
                }, index=[0])

                historico = pd.concat(objs=[historico, df_tmp], ignore_index=True, sort=False)

        print("Accuracy final: {}".format(round(accuracy.item(), 4)))

        plt.figure(figsize=(10, 10))
        plt.plot(historico['Epoch'], historico['Loss'], label='Loss')
        plt.title("Loss", fontsize=25)
        plt.xlabel("Epoch", fontsize=12)
        plt.ylabel("Loss", fontsize=12)
        plt.grid()
        plt.show()

        plt.figure(figsize=(10, 10))
        plt.plot(historico['Epoch'], historico['Accuracy'], label='Accuracy')
        plt.title("Accuracy", fontsize=25)
        plt.xlabel("Epoch", fontsize=12)
        plt.ylabel("Accuracy", fontsize=12)
        plt.grid()
        plt.show()

        print(self.model(self.t_X_test))
    
        path_save = "Modelos/{}.pt".format(self.model_name)
        print(self.model.eval())
        print(self.model.parameters())

        model_scripted = torch.jit.script(self.model)
        model_scripted.save(path_save)

      
        self.model



def import_data():
    
    documento = filedialog.askopenfilename(title="Abrir", filetypes=(("Archivos de EXCEL","*.XLSX"),("Archivos de EXCEL 2003","*.xls")))
    datos = pd.read_excel(documento)
    print(datos.describe())

    return datos


