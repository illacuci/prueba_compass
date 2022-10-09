import tkinter as tk
from tkinter import messagebox, BOTH
import Util.util as utl
import Cliente.gui_app as Gui

class Login_window():
    def __init__(self):

        self.window_login = tk.Tk()
        self.window_login.title ("Login")
        self.window_login.geometry("700x400")
        self.window_login.resizable(0,0)

        self.logo_login = utl.read_image("Imágenes/Compass_logo.png", (250, 180))

        self.image_frame =tk.Label(self.window_login, width= 300, bg= "#FFFFFF", image= self.logo_login)
        self.image_frame.pack(side="left", fill=BOTH)
        self.login_frame =tk.Label(self.window_login, bg= "#E3F2FD")
        self.login_frame.pack(side="right", fill=BOTH, expand="yes")


        self.label_top_frame =tk.Label(self.login_frame, bd=0)
        self.label_top_frame.pack(side="top", fill="x")
        self.label_login= tk.Label(self.label_top_frame,text="Inicio de sesión", font=("Helvetica", 20), bg="#E3F2FD", pady=20)
        self.label_login.pack(expand="yes", fill=BOTH)


        self.label2_frame =tk.Label(self.login_frame, bd=0, bg="#E3F2FD", height=10)
        self.label2_frame.pack(side="bottom", fill="x",expand="yes")

        self.label_user= tk.Label(self.label2_frame,text="Usuario:", font=("Helvetica", 10), bg="#E3F2FD", pady=5, anchor= "w")
        self.label_user.pack(fill="x", padx=20)
        self.entry_user= tk.Entry(self.label2_frame)
        self.entry_user.pack(fill="x", padx= 20, ipady= 5)


        self.label_passw= tk.Label(self.label2_frame,text="Contraseña:", font=("Helvetica", 10), bg="#E3F2FD", pady=5, anchor="w")
        self.label_passw.pack(fill="x", padx=20)
        self.entry_passw= tk.Entry(self.label2_frame)
        self.entry_passw.pack(fill="x", padx= 20, pady=(0,20), ipady=5)
        self.entry_passw.config(show="*" )

        self.button_login= tk.Button(self.label2_frame, text="Iniciar sesión", pady=5, font=("Helvetica 10 bold"), fg="white", bg="#42A5F5")
        self.button_login.pack(fill="x", padx= 20, pady= 20)

        self.window_login.bind("<Return>", self.validation)

        self.window_login.mainloop()

    def validation(self, event):
        user = self.entry_user.get()
        passw = self.entry_passw.get()

        if (user == "Admin" and passw == "1234") :
            self.window_login.destroy()
            Gui.AdminMenu()
        else:
            messagebox.showerror(message="Datos incorrectos", title= "Error de validación")