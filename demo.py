import tkinter as tk
from tkinter import ttk
from tkinter import *
from functools import partial
import subprocess
from subprocess import Popen
from reportlab.pdfgen import canvas
class Estructools(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args, **kwargs)
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0,weight=1)
        tk.Tk.wm_title(self,"Estructool")
        self.frames = {}

        for F in (StartPage, VyBPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

    def other_input_control(self,text_selected = None,entry_element = None):
        if(text_selected=="Otro"):
            entry_element.config(state='enabled')
        else:
            entry_element.config(state='disabled')

    def show_table(self):
        subprocess.Popen(["poliestireno.jpg"],shell=True)
    
    def create_PDF(self,text):
        c = canvas.Canvas("test.pdf")
        c.drawString(100,200, text)
        c.save

    def add_to_PDF(self,text):
        c = canvas.Canvas("test.pdf")
        c.drawString(100,200, "Testing /n this /n library")
        c.save


class StartPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Seleccione la herramienta que desea utilizar")

        viguetas_button = ttk.Button(self, text="Cálculo de vigueta y bovedilla", command=lambda:controller.show_frame(VyBPage))
        table_button = ttk.Button(self, text="Mostrar tabla de vigueta y bovedilla", command =controller.show_table)
        calc_zapata_button = ttk.Button(self, text="Cálculo de zapata")
        des_zapata_button = ttk.Button(self, text="Diseño de zapata")
        trabe_button = ttk.Button(self, text="Cálculo de trabe")
        
        viguetas_button.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        table_button.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        calc_zapata_button.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        des_zapata_button.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        trabe_button.grid(row=1, column=1, padx=10, pady=10, sticky='w')

class VyBPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Ingrese los datos correspondientes")
        
        

        #materials select creation
        materials=["Poliestireno", "Concreto"]
        materials_value = tk.StringVar()
        select_material = ttk.OptionMenu(self,materials_value,materials[0],*materials )
        select_material.grid(row=0, column=0, padx=10,pady=10, sticky='w')

        #materials type select creation
        materials_type=["Entrepiso", "Azotea"]
        materials_type_value = tk.StringVar()
        select_material_type = ttk.OptionMenu(self,materials_type_value,materials_type[0],*materials_type)
        select_material_type.grid(row=1, column=0, padx=10,pady=10, sticky='w')

        #Data required labels creation
        claro_label = ttk.Label(self,text="Claro")
        superior_label = ttk.Label(self,text="Acabado superior")
        inferior_label = ttk.Label(self,text="Acabado inferior")
        plaffon_label = ttk.Label(self,text="Falso plaffón")
        carga_label = ttk.Label(self,text="Carga viva")
        carga_adicional_label = ttk.Label(self,text="Carga adicional")

        #Data required labels positioning
        claro_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        superior_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        inferior_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        plaffon_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        carga_label.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        carga_adicional_label.grid(row=7, column=0, padx=10, pady=10, sticky='w')

         #acabado superior select creation
        claro_options=[2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
        claro_value = tk.StringVar()
        select_claro = ttk.OptionMenu(self,claro_value,claro_options[0],*claro_options)
        select_claro.grid(row=2, column=1, padx=10,pady=10, sticky='w')


        #acabado superior select creation
        superior_options=["Piso de Granito de 40 x 40",	
                        "Mosaico de pasta",
                        "Terrazo de 30 x 30",
                        "Losa Vin. + piso de 5 cm de espesor",
                        "Lozeta Interceramica",
                        "Otro",
                        "Ninguno"]

        superior_entry = ttk.Entry(self,state='disabled')
        superior_entry.grid(row=3,column=2, padx=10, pady=10, sticky='w')
        select_superior = ttk.Combobox(self,values=superior_options)
        select_superior.bind("<<ComboboxSelected>>",lambda event: controller.other_input_control(select_superior.get(),superior_entry))
        select_superior.grid(row=3, column=1, padx=10,pady=10, sticky='w')
        
        #acabado inferior select creation
        inferior_options=["Rich Empaste y Estuco de 2.5 cm",	
                        "Rich Empaste y Estuco de 3 cm",
                        "Rich Empaste y Estuco de 3.5 cm",
                        "Otro",
                        "Ninguno"]
        inferior_entry = ttk.Entry(self,state='disabled')
        inferior_entry.grid(row=4,column=2, padx=10, pady=10, sticky='w')
        select_inferior = ttk.Combobox(self,values=inferior_options)
        select_inferior.bind("<<ComboboxSelected>>",lambda event: controller.other_input_control(select_inferior.get(),inferior_entry))
        select_inferior.grid(row=4, column=1, padx=10,pady=10, sticky='w')

        #Falso plaffon select creation
        plaffon_options=["Tabla Roca de 1.25 cm",	
                        "Mezcla de 2.5cm",
                        "Unicel",
                        "Otro",
                        "Ninguno"]

        plaffon_entry = ttk.Entry(self,state='disabled')
        plaffon_entry.grid(row=5,column=2, padx=10, pady=10, sticky='w')
        select_plaffon = ttk.Combobox(self,values=inferior_options)
        select_plaffon.bind("<<ComboboxSelected>>",lambda event: controller.other_input_control(select_plaffon.get(),plaffon_entry))
        
        select_plaffon.grid(row=5, column=1, padx=10,pady=10, sticky='w')

        #carga viva select creation
        viva_options=["Casa habitación",	
                        "Departamentos"	
                        "Cuartos de hotel",
                        "Cárceles",	
                        "Hospitales",	
                        "Cuarteles",	
                        "Internados",	
                        "Oficinas",	
                        "Despachos",	
                        "Laboratorios",	
                        "Pasillos",	
                        "Escaleras",	
                        "Rampas",	
                        "Vestibulos",	
                        "Pasajes de acceso libre al público",	
                        "Estadios sin asientos individuales",	
                        "Lugar de reunión sin asientos individuales",
                        "Templos",
                        "Cines",
                        "Teatros",	
                        "Gimnasios",
                        "Salones de baile",	
                        "Restaurantes",
                        "Aulas y similares",
                        "Otro"]

        viva_entry = ttk.Entry(self,state='disabled')
        viva_entry.grid(row=6,column=2, padx=10, pady=10, sticky='w')
        select_viva = ttk.Combobox(self,values=viva_options)
        select_viva.bind("<<ComboboxSelected>>",lambda event: controller.other_input_control(select_viva.get(),viva_entry))
        select_viva.grid(row=6, column=1, padx=10,pady=10, sticky='w')
        claro_entry = ttk.Entry(self)

        #carga adicional input
        carga_input = ttk.Entry(self)
        carga_input.grid(row=7,column=1, padx=10, pady=10, sticky = 'w')

        

        calc_button = ttk.Button(self, text="Calcular carga", command=lambda:controller.create_PDF("test"))
        back_button = ttk.Button(self,text="Regresar",command=lambda:controller.show_frame(StartPage))
        calc_button.grid(row=8, column=0, padx=10, pady=10, sticky ='w')

class CalcZapataPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Ingrese los datos correspondientes")

        calc_button = ttk.Button(self, text="Calcular dimensiones", command=lambda:controller.show_frame(VyBPage))
        back_button = ttk.Button(self,text="Regresar")

class DesZapataPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Ingrese los datos correspondientes")

        calc_button = ttk.Button(self, text="Calcular dimensiones", command=lambda:controller.show_frame(VyBPage))
        back_button = ttk.Button(self,text="Regresar")

class TrabePage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Ingrese los datos correspondientes")

        calc_button = ttk.Button(self, text="Cálcular dimensiones", command=lambda:controller.show_frame(VyBPage))
        back_button = ttk.Button(self,text="Regresar",command=controller.show_frame(StartPage))
app = Estructools()
app.mainloop()