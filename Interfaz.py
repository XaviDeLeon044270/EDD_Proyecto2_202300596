import tkinter as tk
from tkinter import ttk, messagebox
# import os

class Interfaz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Llega Rapidito - Sistema de Gestión")
        self.root.geometry("900x700")
        
        # Configuración de estilos personalizados
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
        
        # Color de fondo principal
        self.root.configure(bg="#e8eaf6")
        
        # Frame superior con degradado
        self.header_frame = tk.Frame(
            self.root,
            bg="#1a237e",
            height=100
        )
        self.header_frame.pack(fill="x")
        
        # Título con efecto de sombra
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
        
        # Frame principal para botones con efecto de elevación
        self.main_frame = tk.Frame(
            self.root,
            bg="#e8eaf6"
        )
        self.main_frame.pack(expand=True, fill="both", padx=50, pady=30)
        
        # Configuración de la cuadrícula
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        
        # Iconos para los botones (usando emojis como placeholder)
        self.icons = {
            "Clientes": "👥",
            "Vehículos": "🚗",
            "Viajes": "🛣️",
            "Rutas": "🗺️"
        }
        
        # Botones principales con efectos visuales
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
            
            # Efecto de elevación
            frame.bind('<Enter>', lambda e, f=frame: self.on_enter(f))
            frame.bind('<Leave>', lambda e, f=frame: self.on_leave(f))
            
            # Icono y texto
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
    
    def mostrar_submenu(self, categoria):
        submenu = tk.Toplevel(self.root)
        submenu.title(f"Gestión de {categoria}")
        submenu.geometry("450x600")
        submenu.configure(bg="#e8eaf6")
        
        # Título del submenú
        tk.Label(
            submenu,
            text=f"{self.icons[categoria]} {categoria}",
            font=("Helvetica", 20, "bold"),
            bg="#1a237e",
            fg="white",
            pady=15
        ).pack(fill="x")
        
        # Frame para opciones
        options_frame = tk.Frame(submenu, bg="#e8eaf6")
        options_frame.pack(expand=True, fill="both", padx=30, pady=30)
        
        opciones = [
            ("Agregar", "➕"),
            ("Modificar (Ingresando llave)", "✏️"),
            ("Eliminar (Ingresando llave)", "🗑️"),
            ("Mostrar Información (Ingresando llave)", "📋"),
            ("Mostrar Estructura de Datos", "📊")
        ]
        
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
    
    def ejecutar_accion(self, categoria, accion):
        if "llave" in accion.lower():
            self.solicitar_llave(categoria, accion)
        else:
            messagebox.showinfo(
                "Información",
                f"Función {accion} de {categoria} (en desarrollo)"
            )
    
    def solicitar_llave(self, categoria, accion):
        ventana_llave = tk.Toplevel(self.root)
        ventana_llave.title("Ingresar Llave")
        ventana_llave.geometry("400x250")
        ventana_llave.configure(bg="#e8eaf6")
        
        # Título
        tk.Label(
            ventana_llave,
            text="Ingresar Llave",
            font=("Helvetica", 16, "bold"),
            bg="#1a237e",
            fg="white",
            pady=10
        ).pack(fill="x")
        
        # Frame para entrada
        frame = tk.Frame(ventana_llave, bg="#e8eaf6")
        frame.pack(expand=True, fill="both", padx=30, pady=20)
        
        # Etiqueta
        tk.Label(
            frame,
            text=f"Ingrese la llave del registro de {categoria}:",
            font=("Helvetica", 12),
            bg="#e8eaf6"
        ).pack(pady=10)
        
        # Campo de entrada con estilo
        entrada = tk.Entry(
            frame,
            font=("Helvetica", 12),
            relief="solid",
            bd=1
        )
        entrada.pack(pady=15, ipady=5, ipadx=5)
        
        # Botón de confirmación
        btn_frame = tk.Frame(
            frame,
            bg="#303f9f",
            relief="raised",
            bd=1
        )
        btn_frame.pack(pady=15)
        
        tk.Label(
            btn_frame,
            text="Confirmar",
            font=("Helvetica", 12),
            bg="#303f9f",
            fg="white",
            padx=20,
            pady=8
        ).pack()
        
        btn_frame.bind('<Button-1>', lambda e: self.procesar_llave(
            entrada.get(), categoria, accion, ventana_llave
        ))
        btn_frame.bind('<Enter>', lambda e, f=btn_frame: self.on_enter(f))
        btn_frame.bind('<Leave>', lambda e, f=btn_frame: self.on_leave(f))
    
    def procesar_llave(self, llave, categoria, accion, ventana):
        if llave.strip():
            messagebox.showinfo(
                "Información",
                f"Acción: {accion}\nCategoría: {categoria}\nLlave: {llave}\n(en desarrollo)"
            )
            ventana.destroy()
        else:
            messagebox.showerror("Error", "Por favor ingrese una llave válida")
    
    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TransporteGUI()
    app.iniciar()