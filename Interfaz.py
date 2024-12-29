import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
from Cliente import Cliente, ArbolAVL
from Vehiculo import Vehiculo, ArbolB
from Ruta import Ruta

import os

class Interfaz:

    def __init__(self):
        self.arbolAVL = ArbolAVL()
        self.arbolB = ArbolB(5)
        self.root = tk.Tk()
        self.root.title("Llega Rapidito - Sistema de Gestión")
        self.root.geometry("900x700")
        
        self.style = ttk.Style()
        self.style.configure(
            "Title.TLabel",
            font=("Helvetica", 28, "bold"),
            padding=20,
            background="#1a237e",
            foreground="white"
        )
        self.style.configure(
            "Menu.TButton",
            font=("Helvetica", 14),
            padding=15,
            background="#303f9f"
        )
        self.style.configure(
            "SubMenu.TButton",
            font=("Helvetica", 12),
            padding=10
        )
        
        self.root.configure(bg="#e8eaf6")
        
        self.header_frame = tk.Frame(
            self.root,
            bg="#1a237e",
            height=100
        )
        self.header_frame.pack(fill="x")
        
        self.title_frame = tk.Frame(
            self.header_frame,
            bg="#1a237e"
        )
        self.title_frame.pack(pady=20)
        
        self.shadow_label = tk.Label(
            self.title_frame,
            text="Manejar Registros",
            font=("Helvetica", 28, "bold"),
            fg="#1a237e",
            bg="#1a237e"
        )
        self.shadow_label.pack()
        
        self.title_label = tk.Label(
            self.title_frame,
            text="Manejar Registros",
            font=("Helvetica", 28, "bold"),
            fg="white",
            bg="#1a237e"
        )
        self.title_label.place(in_=self.shadow_label, x=-2, y=-2)
        
        self.main_frame = tk.Frame(
            self.root,
            bg="#e8eaf6"
        )
        self.main_frame.pack(expand=True, fill="both", padx=50, pady=30)
        
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        
        self.icons = {
            "Clientes": "👥",
            "Vehículos": "🚗",
            "Viajes": "🛣️",
            "Rutas": "🗺️"
        }
        
        self.buttons = {
            "Clientes": {"row": 0, "column": 0, "color": "#303f9f"},
            "Vehículos": {"row": 0, "column": 1, "color": "#1976d2"},
            "Viajes": {"row": 1, "column": 0, "color": "#0288d1"},
            "Rutas": {"row": 1, "column": 1, "color": "#0097a7"}
        }
        
        for texto, info in self.buttons.items():
            frame = tk.Frame(
                self.main_frame,
                bg=info["color"],
                relief="raised",
                bd=1
            )
            frame.grid(
                row=info["row"],
                column=info["column"],
                padx=20,
                pady=20,
                sticky="nsew"
            )
            
            frame.bind('<Enter>', lambda e, f=frame: self.on_enter(f))
            frame.bind('<Leave>', lambda e, f=frame: self.on_leave(f))
            
            icon_label = tk.Label(
                frame,
                text=self.icons[texto],
                font=("Segoe UI Emoji", 36),
                bg=info["color"],
                fg="white"
            )
            icon_label.pack(pady=(20,5))
            
            text_label = tk.Label(
                frame,
                text=texto,
                font=("Helvetica", 14, "bold"),
                bg=info["color"],
                fg="white"
            )
            text_label.pack(pady=(5,20))
            
            frame.bind('<Button-1>', lambda e, t=texto: self.mostrar_submenu(t))
            icon_label.bind('<Button-1>', lambda e, t=texto: self.mostrar_submenu(t))
            text_label.bind('<Button-1>', lambda e, t=texto: self.mostrar_submenu(t))
    
    def on_enter(self, frame):
        frame.configure(relief="raised", bd=3)
    
    def on_leave(self, frame):
        frame.configure(relief="raised", bd=1)
    
    #submenus
    def mostrar_submenu(self, categoria):
        submenu = tk.Toplevel(self.root)
        submenu.title(f"Gestión de {categoria}")
        submenu.geometry("450x600")
        submenu.configure(bg="#e8eaf6")
        
        tk.Label(
            submenu,
            text=f"{self.icons[categoria]} {categoria}",
            font=("Helvetica", 20, "bold"),
            bg="#1a237e",
            fg="white",
            pady=15
        ).pack(fill="x")
        
        options_frame = tk.Frame(submenu, bg="#e8eaf6")
        options_frame.pack(expand=True, fill="both", padx=30, pady=30)
        
        opciones = [
            ("Agregar", "➕"),
            ("Modificar", "✏️"),
            ("Eliminar", "🗑️"),
            ("Mostrar Información", "📋"),
            ("Mostrar Estructura de Datos", "📊")
        ]

        if categoria != "Viajes":
            opciones.append(("Carga masiva", "📤"))
        
        for texto, icono in opciones:
            btn_frame = tk.Frame(
                options_frame,
                bg="#ffffff",
                relief="raised",
                bd=1
            )
            btn_frame.pack(fill="x", padx=10, pady=8)
            btn_frame.bind('<Enter>', lambda e, f=btn_frame: self.on_enter(f))
            btn_frame.bind('<Leave>', lambda e, f=btn_frame: self.on_leave(f))
            
            icon_label = tk.Label(
                btn_frame,
                text=icono,
                font=("Segoe UI Emoji", 20),
                bg="#ffffff"
            )
            icon_label.pack(side="left", padx=15, pady=10)
            
            text_label = tk.Label(
                btn_frame,
                text=texto,
                font=("Helvetica", 12),
                bg="#ffffff"
            )
            text_label.pack(side="left", padx=10, pady=10)
            
            btn_frame.bind('<Button-1>', lambda e, t=texto: self.ejecutar_accion(categoria, t))
            icon_label.bind('<Button-1>', lambda e, t=texto: self.ejecutar_accion(categoria, t))
            text_label.bind('<Button-1>', lambda e, t=texto: self.ejecutar_accion(categoria, t))
    
# FUNCIONES ESENCIALES

    def ejecutar_accion(self, categoria, accion):
        if accion == "Modificar" or accion == "Eliminar" or accion == "Mostrar Información":
            self.solicitar_llave(categoria, accion)
        elif accion == "Agregar":
            if categoria == "Clientes":
                self.agregar_cliente()
            
            elif categoria == "Vehículos":
                self.agregar_vehiculo()

        elif accion == "Carga masiva":
            self.carga_masiva(categoria)

        elif accion == "Mostrar Estructura de Datos":
            if categoria == "Clientes":
                self.arbolAVL.generar_reporte()

                ventana_reporte = tk.Toplevel(self.root)
                ventana_reporte.title("Reporte del Árbol AVL")
                ventana_reporte.configure(bg="#e8eaf6")
                
                ventana_reporte.state('zoomed')
                
                image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reportes', 'reporte_arbolAVL.png')
                img = Image.open(image_path)
                
                ventana_reporte.update_idletasks()
                window_width = ventana_reporte.winfo_width()
                window_height = ventana_reporte.winfo_height()
                
                img_width, img_height = img.size
                aspect_ratio = img_width / img_height
                
                if window_width / window_height > aspect_ratio:
                    new_height = window_height
                    new_width = int(new_height * aspect_ratio)
                else:
                    new_width = window_width
                    new_height = int(new_width / aspect_ratio)
                
                img = img.resize((new_width, new_height), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)
                
                label_img = tk.Label(ventana_reporte, image=img)
                label_img.image = img 
                label_img.pack(expand=True)

            elif categoria == "Vehículos":
                self.arbolB.generar_reporte()

                ventana_reporte = tk.Toplevel(self.root)
                ventana_reporte.title("Reporte del Árbol B")
                ventana_reporte.configure(bg="#e8eaf6")
                
                ventana_reporte.state('zoomed')
                
                image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reportes', 'reporte_arbolB.png')
                img = Image.open(image_path)
                
                ventana_reporte.update_idletasks()
                window_width = ventana_reporte.winfo_width()
                window_height = ventana_reporte.winfo_height()
                
                img_width, img_height = img.size
                aspect_ratio = img_width / img_height
                
                if window_width / window_height > aspect_ratio:
                    new_height = window_height
                    new_width = int(new_height * aspect_ratio)
                else:
                    new_width = window_width
                    new_height = int(new_width / aspect_ratio)
                
                img = img.resize((new_width, new_height), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)
                
                label_img = tk.Label(ventana_reporte, image=img)
                label_img.image = img 
                label_img.pack(expand=True)
        else:
            messagebox.showinfo(
                "Información",
                f"Función {accion} de {categoria} (en desarrollo)"
            )

    def agregar_cliente(self):
        ventana_cliente = tk.Toplevel(self.root)
        ventana_cliente.title("Agregar Cliente")
        ventana_cliente.geometry("500x500")
        ventana_cliente.configure(bg="#e8eaf6")
        
        tk.Label(
            ventana_cliente,
            text="Agregar Cliente",
            font=("Helvetica", 16, "bold"),
            bg="#1a237e",
            fg="white",
            pady=10
        ).pack(fill="x")
        
        frame = tk.Frame(ventana_cliente, bg="#e8eaf6")
        frame.pack(expand=True, fill="both", padx=30, pady=20)
        
        tk.Label(
            frame,
            text="Ingrese los datos del cliente:",
            font=("Helvetica", 12),
            bg="#e8eaf6"
        ).pack(pady=10)
        
        def crear_campo(parent, label_text, tipo="texto"):
            container = tk.Frame(parent, bg="#e8eaf6")
            container.pack(fill="x", pady=5)
            
            label = tk.Label(
                container,
                text=label_text,
                font=("Helvetica", 12),
                bg="#e8eaf6",
                width=10,
                anchor="e"
            )
            label.pack(side="left", padx=5)
            
            if tipo == "texto":
                entry = tk.Entry(container, font=("Helvetica", 12), relief="solid", bd=1, width=30)
            elif tipo == "numerico":
                entry = tk.Entry(container, font=("Helvetica", 12), relief="solid", bd=1, width=30)
                entry.config(validate="key", validatecommand=(parent.register(lambda val: val.isdigit()), '%P'))
            elif tipo == "telefono":
                entry = tk.Entry(container, font=("Helvetica", 12), relief="solid", bd=1, width=30)
                entry.config(validate="key", validatecommand=(parent.register(lambda val: val.isdigit() and len(val) <= 8), '%P'))
            elif tipo == "opciones":
                opciones = ["Masculino", "Femenino", "Otro"]
                entry = tk.StringVar(container)
                entry.set(opciones[0])
                tk.OptionMenu(container, entry, *opciones).pack(side="left", padx=5)
                return entry
            
            entry.pack(side="left", padx=5)
            return entry
        
        dpi_entry = crear_campo(frame, "DPI:", "numerico")
        nombres_entry = crear_campo(frame, "Nombres:")
        apellidos_entry = crear_campo(frame, "Apellidos:")
        genero_entry = crear_campo(frame, "Género:", "opciones")
        telefono_entry = crear_campo(frame, "Teléfono:", "telefono")
        direccion_entry = crear_campo(frame, "Dirección:")
        
        def enviar_formulario():
            self.procesar_cliente(
                dpi_entry.get(),
                nombres_entry.get(),
                apellidos_entry.get(),
                genero_entry.get(),
                telefono_entry.get(),
                direccion_entry.get(),
                ventana_cliente
            )
        
        btn_container = tk.Frame(frame, bg="#e8eaf6")
        btn_container.pack(pady=20)
        
        btn_frame = tk.Frame(
            btn_container,
            bg="#303f9f",
            relief="raised",
            bd=1,
            cursor="hand2"
        )
        btn_frame.pack()
        
        btn_label = tk.Label(
            btn_frame,
            text="Agregar Cliente",
            font=("Helvetica", 12),
            bg="#303f9f",
            fg="white",
            padx=20,
            pady=8,
            cursor="hand2"
        )
        btn_label.pack()
        
        btn_frame.bind('<Button-1>', lambda e: enviar_formulario())
        btn_label.bind('<Button-1>', lambda e: enviar_formulario())
        btn_frame.bind('<Enter>', lambda e: self.on_enter(btn_frame))
        btn_frame.bind('<Leave>', lambda e: self.on_leave(btn_frame))

    def procesar_cliente(self, dpi, nombres, apellidos, genero, telefono, direccion, ventana):
        if dpi.strip() and nombres.strip() and apellidos.strip() and genero.strip() and telefono.strip() and direccion.strip():
            nuevo_cliente = Cliente(dpi, nombres, apellidos, genero, telefono, direccion)
            self.arbolAVL.insertarCliente(nuevo_cliente)
            messagebox.showinfo(
                "Información",
                f"Cliente agregado:\nDPI: {dpi}\nNombres: {nombres}\nApellidos: {apellidos}\nGénero: {genero}\nTeléfono: {telefono}\nDirección: {direccion}"
            )
            ventana.destroy()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos")
    
    def agregar_vehiculo(self):
        ventana_vehiculo = tk.Toplevel(self.root)
        ventana_vehiculo.title("Agregar Vehículo")
        ventana_vehiculo.geometry("500x500")
        ventana_vehiculo.configure(bg="#e8eaf6")
        
        tk.Label(
            ventana_vehiculo,
            text="Agregar Vehículo",
            font=("Helvetica", 16, "bold"),
            bg="#1a237e",
            fg="white",
            pady=10
        ).pack(fill="x")
        
        frame = tk.Frame(ventana_vehiculo, bg="#e8eaf6")
        frame.pack(expand=True, fill="both", padx=30, pady=20)
        
        tk.Label(
            frame,
            text="Ingrese los datos del vehículo:",
            font=("Helvetica", 12),
            bg="#e8eaf6"
        ).pack(pady=10)
        
        def crear_campo(parent, label_text, tipo="texto"):
            container = tk.Frame(parent, bg="#e8eaf6")
            container.pack(fill="x", pady=5)
            
            label = tk.Label(
                container,
                text=label_text,
                font=("Helvetica", 12),
                bg="#e8eaf6",
                width=10,
                anchor="e"
            )
            label.pack(side="left", padx=5)
            
            if tipo == "texto":
                entry = tk.Entry(container, font=("Helvetica", 12), relief="solid", bd=1, width=30)
            elif tipo == "numerico":
                entry = tk.Entry(container, font=("Helvetica", 12), relief="solid", bd=1, width=30)
                entry.config(validate="key", validatecommand=(parent.register(lambda val: val.isdigit()), '%P'))
            
            entry.pack(side="left", padx=5)
            return entry
        
        placa_entry = crear_campo(frame, "Placa:", "texto")
        marca_entry = crear_campo(frame, "Marca:", "texto")
        modelo_entry = crear_campo(frame, "Modelo:", "texto")
        precio_entry = crear_campo(frame, "Precio:", "numerico")
        
        def enviar_formulario():
            self.procesar_vehiculo(
                placa_entry.get(),
                marca_entry.get(),
                modelo_entry.get(),
                precio_entry.get(),
                ventana_vehiculo
            )
            
            
            ventana_vehiculo.destroy()
        
        btn_container = tk.Frame(frame, bg="#e8eaf6")
        btn_container.pack(pady=20)
        
        btn_frame = tk.Frame(
            btn_container,
            bg="#303f9f",
            relief="raised",
            bd=1,
            cursor="hand2"
        )
        btn_frame.pack()
        
        btn_label = tk.Label(
            btn_frame,
            text="Agregar Vehículo",
            font=("Helvetica", 12),
            bg="#303f9f",
            fg="white",
            padx=20,
            pady=8,
            cursor="hand2"
        )
        btn_label.pack()
        
        btn_frame.bind('<Button-1>', lambda e: enviar_formulario())
        btn_label.bind('<Button-1>', lambda e: enviar_formulario())
        btn_frame.bind('<Enter>', lambda e: self.on_enter(btn_frame))
        btn_frame.bind('<Leave>', lambda e: self.on_leave(btn_frame))

    def procesar_vehiculo(self, placa, marca, modelo, precio, ventana):
        if placa.strip() and marca.strip() and modelo.strip() and precio.strip():
            nuevo_vehiculo = Vehiculo(placa, marca, modelo, precio)
            self.arbolB.insertarVehiculo(nuevo_vehiculo)
            messagebox.showinfo(
                "Información",
                f"Vehículo agregado:\nPlaca: {placa}\nMarca: {marca}\nModelo: {modelo}\nPrecio: {precio}"
            )
            ventana.destroy()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos")
            

    def solicitar_llave(self, categoria, accion):
        ventana_llave = tk.Toplevel(self.root)
        ventana_llave.title("Ingresar Llave")
        ventana_llave.geometry("450x250")
        ventana_llave.configure(bg="#e8eaf6")
        
        tk.Label(
            ventana_llave,
            text="Ingresar Llave",
            font=("Helvetica", 16, "bold"),
            bg="#1a237e",
            fg="white",
            pady=10
        ).pack(fill="x")
        
        frame = tk.Frame(ventana_llave, bg="#e8eaf6")
        frame.pack(expand=True, fill="both", padx=30, pady=20)
        
        tk.Label(
            frame,
            text=f"Ingrese la llave para {accion} el registro de {categoria}:",
            font=("Helvetica", 12),
            bg="#e8eaf6"
        ).pack(pady=10)
        
        entrada = tk.Entry(
            frame,
            font=("Helvetica", 12),
            relief="solid",
            bd=1
        )
        entrada.pack(pady=15, ipady=5, ipadx=5)
        
        btn_frame = tk.Frame(
            frame,
            bg="#303f9f",
            relief="raised",
            bd=1
        )
        btn_frame.pack(pady=15)
        
        btn_label = tk.Label(
            btn_frame,
            text="Confirmar",
            font=("Helvetica", 12),
            bg="#303f9f",
            fg="white",
            padx=20,
            pady=8
        )
        btn_label.pack()
        
        def on_confirmar_click(event):
            llave = entrada.get()
            if accion == "Eliminar":
                respuesta = messagebox.askyesno(
                    "Advertencia",
                    f"¿Desea eliminar el {categoria} con llave {llave}?"
                )
                if respuesta:
                    eliminado = False
                    if categoria == "Clientes":
                        eliminado = self.arbolAVL.eliminarCliente(llave)
                    elif categoria == "Vehículos":
                        eliminado = self.arbolB.eliminarVehiculo(llave)
                        pass
                    elif categoria == "Rutas":
                        # eliminado = self.grafo.eliminarNodo(llave)
                        pass
                    elif categoria == "Viajes":
                        # eliminado = self.lista.eliminarNodo(llave)
                        pass
                    
                    if eliminado:
                        messagebox.showinfo("Éxito", f"Se ha eliminado correctamente el registro de {categoria}.")
                    else:
                        messagebox.showerror("Error", f"No se ha podido eliminar el registro de {categoria}.")
                else:
                    return
            # self.procesar_llave(llave, categoria, accion, ventana_llave)
            elif accion == "Modificar":
                if categoria == "Clientes":
                    self.modificar_cliente(llave)
                    pass
                elif categoria == "Vehículos":
                    self.modificar_vehiculo(llave)
                    pass
                elif categoria == "Rutas":
                    #self.modificar_ruta(llave)
                    pass
                elif categoria == "Viajes":
                    #self.modificar_viaje(llave)
                    pass
            elif accion == "Mostrar Información":
                self.mostrar_informacion(llave, categoria)
                
        
        btn_frame.bind('<Button-1>', on_confirmar_click)
        btn_label.bind('<Button-1>', on_confirmar_click)
        btn_frame.bind('<Enter>', lambda e, f=btn_frame: self.on_enter(f))
        btn_frame.bind('<Leave>', lambda e, f=btn_frame: self.on_leave(f))
    
    def modificar_cliente(self, dpi):
        cliente = self.arbolAVL.buscarCliente(dpi)
        if not cliente:
            messagebox.showerror("Error", f"No se encontró el cliente con DPI {dpi}")
            return
    
        ventana_modificar = tk.Toplevel(self.root)
        ventana_modificar.title("Modificar Cliente")
        ventana_modificar.geometry("500x500")
        ventana_modificar.configure(bg="#e8eaf6")
        
        tk.Label(
            ventana_modificar,
            text=f"Modificar al cliente {dpi}",
            font=("Helvetica", 16, "bold"),
            bg="#1a237e",
            fg="white",
            pady=10
        ).pack(fill="x")
        
        frame = tk.Frame(ventana_modificar, bg="#e8eaf6")
        frame.pack(expand=True, fill="both", padx=30, pady=20)
        
        tk.Label(
            frame,
            text="Ingrese los nuevos datos del cliente:",
            font=("Helvetica", 12),
            bg="#e8eaf6"
        ).pack(pady=10)
        
        def crear_campo(parent, label_text, valor_inicial, tipo="texto"):
            container = tk.Frame(parent, bg="#e8eaf6")
            container.pack(fill="x", pady=5)
            
            label = tk.Label(
                container,
                text=label_text,
                font=("Helvetica", 12),
                bg="#e8eaf6",
                width=10,
                anchor="e"
            )
            label.pack(side="left", padx=5)
            
            if tipo == "texto":
                entry = tk.Entry(container, font=("Helvetica", 12), relief="solid", bd=1, width=30)
                entry.insert(0, valor_inicial)
            elif tipo == "telefono":
                entry = tk.Entry(container, font=("Helvetica", 12), relief="solid", bd=1, width=30)
                entry.insert(0, valor_inicial)
                entry.config(validate="key", validatecommand=(parent.register(lambda val: val.isdigit() and len(val) <= 8), '%P'))
            elif tipo == "opciones":
                opciones = ["Masculino", "Femenino", "Otro"]
                entry = tk.StringVar(container)
                entry.set(valor_inicial)
                tk.OptionMenu(container, entry, *opciones).pack(side="left", padx=5)
                return entry
            
            entry.pack(side="left", padx=5)
            return entry
        
        nombres_entry = crear_campo(frame, "Nombres:", cliente.nombres)
        apellidos_entry = crear_campo(frame, "Apellidos:", cliente.apellidos)
        genero_entry = crear_campo(frame, "Género:", cliente.genero, "opciones")
        telefono_entry = crear_campo(frame, "Teléfono:", cliente.telefono, "telefono")
        direccion_entry = crear_campo(frame, "Dirección:", cliente.direccion)
        
        def enviar_formulario():
            cliente.nombres = nombres_entry.get()
            cliente.apellidos = apellidos_entry.get()
            cliente.genero = genero_entry.get()
            cliente.telefono = telefono_entry.get()
            cliente.direccion = direccion_entry.get()
            messagebox.showinfo("Éxito", "Cliente modificado correctamente")
            ventana_modificar.destroy()
        
        btn_container = tk.Frame(frame, bg="#e8eaf6")
        btn_container.pack(pady=20)
        
        btn_frame = tk.Frame(
            btn_container,
            bg="#303f9f",
            relief="raised",
            bd=1,
            cursor="hand2"
        )
        btn_frame.pack()
        
        btn_label = tk.Label(
            btn_frame,
            text="Modificar Cliente",
            font=("Helvetica", 12),
            bg="#303f9f",
            fg="white",
            padx=20,
            pady=8,
            cursor="hand2"
        )
        btn_label.pack()
        
        btn_frame.bind('<Button-1>', lambda e: enviar_formulario())
        btn_label.bind('<Button-1>', lambda e: enviar_formulario())
        btn_frame.bind('<Enter>', lambda e: self.on_enter(btn_frame))
        btn_frame.bind('<Leave>', lambda e: self.on_leave(btn_frame))

    def modificar_vehiculo(self, placa):
        vehiculo = self.arbolB.buscarVehiculo(placa)
        if not vehiculo:
            messagebox.showerror("Error", f"No se encontró el vehículo con placa {placa}")
            return
    
        ventana_modificar = tk.Toplevel(self.root)
        ventana_modificar.title("Modificar Vehículo")
        ventana_modificar.geometry("500x500")
        ventana_modificar.configure(bg="#e8eaf6")
        
        tk.Label(
            ventana_modificar,
            text=f"Modificar al vehículo {placa}",
            font=("Helvetica", 16, "bold"),
            bg="#1a237e",
            fg="white",
            pady=10
        ).pack(fill="x")
        
        frame = tk.Frame(ventana_modificar, bg="#e8eaf6")
        frame.pack(expand=True, fill="both", padx=30, pady=20)
        
        tk.Label(
            frame,
            text="Ingrese los nuevos datos del vehículo:",
            font=("Helvetica", 12),
            bg="#e8eaf6"
        ).pack(pady=10)
        
        def crear_campo(parent, label_text, valor_inicial, tipo="texto"):
            container = tk.Frame(parent, bg="#e8eaf6")
            container.pack(fill="x", pady=5)
            
            label = tk.Label(
                container,
                text=label_text,
                font=("Helvetica", 12),
                bg="#e8eaf6",
                width=10,
                anchor="e"
            )
            label.pack(side="left", padx=5)
            
            if tipo == "texto":
                entry = tk.Entry(container, font=("Helvetica", 12), relief="solid", bd=1, width=30)
                entry.insert(0, valor_inicial)
            elif tipo == "numerico":
                entry = tk.Entry(container, font=("Helvetica", 12), relief="solid", bd=1, width=30)
                entry.insert(0, valor_inicial)
                entry.config(validate="key", validatecommand=(parent.register(lambda val: val.isdigit()), '%P'))
            
            entry.pack(side="left", padx=5)
            return entry
        
        marca_entry = crear_campo(frame, "Marca:", vehiculo.marca)
        modelo_entry = crear_campo(frame, "Modelo:", vehiculo.modelo)
        precio_entry = crear_campo(frame, "Precio:", vehiculo.precio, "numerico")

        def enviar_formulario():
            vehiculo.marca = marca_entry.get()
            vehiculo.modelo = modelo_entry.get()
            vehiculo.precio = precio_entry.get()
            messagebox.showinfo("Éxito", "Vehículo modificado correctamente")
            ventana_modificar.destroy()

        btn_container = tk.Frame(frame, bg="#e8eaf6")
        btn_container.pack(pady=20)

        btn_frame = tk.Frame(
            btn_container,
            bg="#303f9f",
            relief="raised",
            bd=1,
            cursor="hand2"
        )
        btn_frame.pack()

        btn_label = tk.Label(
            btn_frame,
            text="Modificar Vehículo",
            font=("Helvetica", 12),
            bg="#303f9f",
            fg="white",
            padx=20,
            pady=8,
            cursor="hand2"
        )
        btn_label.pack()

        btn_frame.bind('<Button-1>', lambda e: enviar_formulario())
        btn_label.bind('<Button-1>', lambda e: enviar_formulario())
        btn_frame.bind('<Enter>', lambda e: self.on_enter(btn_frame))
        btn_frame.bind('<Leave>', lambda e: self.on_leave(btn_frame))

    def mostrar_informacion(self, llave, categoria):
        if categoria == "Clientes":
            cliente = self.arbolAVL.buscarCliente(llave)
            if not cliente:
                messagebox.showerror("Error", f"No se encontró el cliente con DPI {llave}")
                return

            ventana_info = tk.Toplevel(self.root)
            ventana_info.title("Información del Cliente")
            ventana_info.geometry("400x400")
            ventana_info.configure(bg="#e8eaf6")
            
            tk.Label(
                ventana_info,
                text=f"Información del cliente {llave}",
                font=("Helvetica", 16, "bold"),
                bg="#1a237e",
                fg="white",
                pady=10
            ).pack(fill="x")
            
            frame = tk.Frame(ventana_info, bg="#e8eaf6")
            frame.pack(expand=True, fill="both", padx=30, pady=20)
            
            def crear_campo_informacion(parent, label_text, valor):
                container = tk.Frame(parent, bg="#e8eaf6")
                container.pack(fill="x", pady=5)
                
                label = tk.Label(
                    container,
                    text=label_text,
                    font=("Helvetica", 12),
                    bg="#e8eaf6",
                    width=15,
                    anchor="e"
                )
                label.pack(side="left", padx=5)
                
                valor_label = tk.Label(
                    container,
                    text=valor,
                    font=("Helvetica", 12),
                    bg="#e8eaf6",
                    anchor="w"
                )
                valor_label.pack(side="left", padx=5)


            crear_campo_informacion(frame, "DPI:", cliente.dpi)
            crear_campo_informacion(frame, "Nombres:", cliente.nombres)
            crear_campo_informacion(frame, "Apellidos:", cliente.apellidos)
            crear_campo_informacion(frame, "Género:", cliente.genero)
            crear_campo_informacion(frame, "Teléfono:", cliente.telefono)
            crear_campo_informacion(frame, "Dirección:", cliente.direccion)
            
            btn_frame = tk.Frame(
                frame,
                bg="#303f9f",
                relief="raised",
                bd=1
            )
            btn_frame.pack(pady=15)
            
            btn_label = tk.Label(
                btn_frame,
                text="Cerrar",
                font=("Helvetica", 12),
                bg="#303f9f",
                fg="white",
                padx=20,
                pady=8
            )
            btn_label.pack()
            
            def cerrar_ventana(event):
                ventana_info.destroy()
            
            btn_frame.bind('<Button-1>', cerrar_ventana)
            btn_label.bind('<Button-1>', cerrar_ventana)
            btn_frame.bind('<Enter>', lambda e, f=btn_frame: self.on_enter(f))
            btn_frame.bind('<Leave>', lambda e, f=btn_frame: self.on_leave(f))

        elif categoria == "Vehículos":
            vehiculo = self.arbolB.buscarVehiculo(llave)
            if not vehiculo:
                messagebox.showerror("Error", f"No se encontró el vehículo con placa {llave}")
                return
            
            ventana_info = tk.Toplevel(self.root)
            ventana_info.title("Información del Vehículo")
            ventana_info.geometry("400x400")
            ventana_info.configure(bg="#e8eaf6")

            tk.Label(
                ventana_info,
                text=f"Información del vehículo {llave}",
                font=("Helvetica", 16, "bold"),
                bg="#1a237e",
                fg="white",
                pady=10
            ).pack(fill="x")

            frame = tk.Frame(ventana_info, bg="#e8eaf6")
            frame.pack(expand=True, fill="both", padx=30, pady=20)

            def crear_campo_informacion(parent, label_text, valor):
                container = tk.Frame(parent, bg="#e8eaf6")
                container.pack(fill="x", pady=5)

                label = tk.Label(
                    container,
                    text=label_text,
                    font=("Helvetica", 12),
                    bg="#e8eaf6",
                    width=15,
                    anchor="e"
                )
                label.pack(side="left", padx=5)

                valor_label = tk.Label(
                    container,
                    text=valor,
                    font=("Helvetica", 12),
                    bg="#e8eaf6",
                    anchor="w"
                )
                valor_label.pack(side="left", padx=5)

            crear_campo_informacion(frame, "Placa:", vehiculo.placa)
            crear_campo_informacion(frame, "Marca:", vehiculo.marca)
            crear_campo_informacion(frame, "Modelo:", vehiculo.modelo)
            crear_campo_informacion(frame, "Precio:", vehiculo.precio)

            btn_frame = tk.Frame(
                frame,
                bg="#303f9f",
                relief="raised",
                bd=1
            )
            btn_frame.pack(pady=15)
            
            btn_label = tk.Label(
                btn_frame,
                text="Cerrar",
                font=("Helvetica", 12),
                bg="#303f9f",
                fg="white",
                padx=20,
                pady=8
            )
            btn_label.pack()
            
            def cerrar_ventana(event):
                ventana_info.destroy()
            
            btn_frame.bind('<Button-1>', cerrar_ventana)
            btn_label.bind('<Button-1>', cerrar_ventana)
            btn_frame.bind('<Enter>', lambda e, f=btn_frame: self.on_enter(f))
            btn_frame.bind('<Leave>', lambda e, f=btn_frame: self.on_leave(f))

        else:
            messagebox.showinfo("Información", f"Mostrar información de {categoria} (en desarrollo)")

    def carga_masiva(self, categoria):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        archivos_dir = os.path.join(current_dir, 'Archivos')
        
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo de clientes",
            initialdir=archivos_dir,
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        
        if not file_path:
            messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo")
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if categoria == "Clientes":
                        if not line.strip().endswith(';'):
                            messagebox.showerror("Error", f"Formato incorrecto en la línea: {line.strip()}")
                            continue

                        datos = line.strip()[:-1].split(',')

                        if len(datos) != 6:
                            messagebox.showerror("Error", f"Formato incorrecto en la línea: {line.strip()}")
                            continue

                        dpi, nombres, apellidos, genero, telefono, direccion = datos
                        nuevo_cliente = Cliente(dpi.strip(), nombres.strip(), apellidos.strip(), genero.strip(), telefono.strip(), direccion.strip())
                        self.arbolAVL.insertarCliente(nuevo_cliente)

                    elif categoria == "Vehículos":

                        if not line.strip().endswith(';'):
                            messagebox.showerror("Error", f"Formato incorrecto en la línea: {line.strip()}")
                            continue

                        datos = line.strip()[:-1].split(':')

                        if len(datos) != 4:
                            messagebox.showerror("Error", f"Formato incorrecto en la línea: {line.strip()}")
                            continue

                        placa, marca, modelo, precio = datos
                        if placa == "HIJ678":
                            print("hola")
                        nuevo_vehiculo = Vehiculo(placa.strip(), marca.strip(), modelo.strip(), precio.strip())
                        #print (f"Vehículo: {nuevo_vehiculo.__str__()} agregado")
                        self.arbolB.insertarVehiculo(nuevo_vehiculo)
                        

                    elif categoria == "Rutas":

                        if not line.strip().endswith('%'):
                            messagebox.showerror("Error", f"Formato incorrecto en la línea: {line.strip()}")
                            continue

                        datos = line.strip()[:-1].split('/')

                        if len(datos) != 3:
                            messagebox.showerror("Error", f"Formato incorrecto en la línea: {line.strip()}")
                            continue

                        origen, destino, tiempo = datos
                        nueva_ruta = Ruta(origen.strip(), destino.strip(), tiempo.strip())
                        print (f"Ruta: {nueva_ruta.__str__()} agregada")
                        # nuevo_nodo = NodoGrafo(nuevo_viaje)
                        # self.grafo.insertarNodo(nuevo_nodo)

            messagebox.showinfo("Éxito", f"Carga masiva de {categoria} completada")
        except Exception as e:
            print(e)
            messagebox.showerror("Error", f"Ocurrió un error al leer el archivo: {e}")
        
    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Interfaz()
    app.iniciar()