from turtle import shape
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import random_split, TensorDataset
import numpy as np 
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tkinter import filedialog

documento = filedialog.askopenfilename(title="Abrir", filetypes=(("Ficheros de EXCEL","*.XLSX"),("Ficheros de CSV","*.csv")))
datos = pd.read_excel(documento)

escalador = MinMaxScaler()
datos_x = escalador.fit_transform(datos)
datos_y = datos_x[:,4]
datos_x = datos.drop(columns=["median_income", "households","latitude", "longitude","median_house_value"])
datos_x = pd.DataFrame(datos_x).to_numpy()

#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(datos_x, datos_y, test_size = 0.2, random_state = 2)

t_y_train = torch.from_numpy(datos_y).float()
t_y_test = torch.from_numpy(y_test).float()
t_X_train = torch.from_numpy(datos_x).float()
#t_X_test = torch.from_numpy(X_test).float()
t_y_train = t_y_train[:,None]
#t_y_test = t_y_test[:, None]

#test = TensorDataset(t_X_test, t_y_test)


class Red(nn.Module):
    
    def __init__(self):
        super(Red, self).__init__()
        self.linear1 = nn.Linear(4, 4)
        self.linear2 = nn.Linear(4, 4)
        self.linear3 = nn.Linear(4, 1)
    
    def forward(self, inputs):
        pred_1 = torch.relu(self.linear1(inputs))
        pred_2 = torch.relu(self.linear2(pred_1))
        pred_f = torch.relu(self.linear3(pred_2))
        return pred_f

lr = 0.001
epochs = 20000
estatus_print = 100

model = Red()
loss_fn = nn.MSELoss() 
optimizer = torch.optim.Adam(params=model.parameters(), lr=lr)
print("Arquitectura del modelo: {}".format(model))
historico = pd.DataFrame()

print("Entranando el modelo")
for epoch in range(1, epochs+1):
    y_pred= model(t_X_train)
    loss = loss_fn(input=y_pred, target=t_y_train)
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
    
    if epoch % estatus_print == 0:
        print(f"\nEpoch {epoch} \t Loss: {round(loss.item(), 4)}")
    
    #with torch.no_grad():

    #    y_pred = model(t_X_test)
    #    y_pred_class = y_pred.round()
    #    correct = (y_pred_class == t_y_test).sum()
    #    accuracy = 100 * correct / float(len(t_y_test))
    #    if epoch % estatus_print == 0:
    #        print("Accuracy: {}".format(accuracy.item()))
    
    #df_tmp = pd.DataFrame(data={
    #    'Epoch': epoch,
    #    'Loss': round(loss.item(), 4),
    #    'Accuracy': round(accuracy.item(), 4)
    #}, index=[0])
    #historico = pd.concat(objs=[historico, df_tmp], ignore_index=True, sort=False)

#print("Accuracy final: {}".format(round(accuracy.item(), 4)))


#import matplotlib.pyplot as plt

# plt.figure(figsize=(10, 10))
# plt.plot(historico['Epoch'], historico['Loss'], label='Loss')
# plt.title("Loss", fontsize=25)
# plt.xlabel("Epoch", fontsize=12)
# plt.ylabel("Loss", fontsize=12)
# plt.grid()
# plt.show()

# plt.figure(figsize=(10, 10))
# plt.plot(historico['Epoch'], historico['Accuracy'], label='Accuracy')
# plt.title("Accuracy", fontsize=25)
# plt.xlabel("Epoch", fontsize=12)
# plt.ylabel("Accuracy", fontsize=12)
# plt.grid()
# plt.show()

#prediccion = model(t_X_test[5])
#print(prediccion)
