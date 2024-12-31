class Ruta:
    def __init__(self, origen, destino, tiempo):
        self.origen = origen
        self.destino = destino
        self.tiempo = tiempo

    def __str__(self):
        return f'Lugar de origen: {self.origen} - Lugar de destino: {self.destino} - Tiempo de ruta: {self.tiempo}'

class Vertice:
    def __init__(self, nombre, peso=0):
        self.nombre = nombre
        self.peso = peso
        self.rutas = ListaEnlazada()
    
class NodoLista:
    def __init__(self, vertice):
        self.vertice = vertice
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.inicio = None

    def insertar(self, vertice):
        nuevo = self.inicio
        nuevoVertice = Vertice(vertice)

        if nuevo == None:
            nuevo = NodoLista(nuevoVertice)
            self.inicio = nuevo
            return nuevo

        while nuevo.siguiente != None:
            nuevo = nuevo.siguiente

        nuevo.siguiente = NodoLista(nuevoVertice)

        return nuevo.siguiente

    def buscar(self, vertice):
        auxiliar = self.inicio
        
        if auxiliar == None:
            return None
        
        nuevoVertice = Vertice(vertice)

        while auxiliar != None:
            if auxiliar.vertice.nombre == nuevoVertice.nombre:
                return auxiliar
            auxiliar = auxiliar.siguiente
        
        return None

class ListaAdyacencia:
    def __init__(self):
        self.vertices = ListaEnlazada()

    def insertarVertice(self, ruta):
        origen = Vertice(ruta.origen)
        
        nuevoNodo = self.vertices.buscar(origen)

        destino = Vertice(ruta.destino, ruta.tiempo)

        if nuevoNodo != None:
            nuevoNodo.vertice.rutas.insertar(destino)
        else:
            nuevoNodo = self.vertices.insertar(origen)

            nuevoNodo.vertice.rutas.insertar(destino)

    def recorridoReporte(self, nodo, graphviz_lines):
        if nodo is None:
            return

        vertice_actual = nodo.vertice
        ruta_actual = vertice_actual.rutas.inicio

        while ruta_actual is not None:
            graphviz_lines.append(
                f'    "{vertice_actual.nombre.nombre}" -- "{ruta_actual.vertice.nombre.nombre}" [label="{ruta_actual.vertice.nombre.peso}"];\n'
            )
            ruta_actual = ruta_actual.siguiente

        self.recorridoReporte(nodo.siguiente, graphviz_lines)

    def generar_reporte(self):
        if self.vertices.inicio is None:
            print("El grafo está vacío")
            return
            
        graphviz_lines = [
            "graph G {\n",
            "    layout=neato;\n",
            "    node [fontname=Arial, shape=circle, style=filled, fillcolor=lightblue];\n",
            "    edge [fontname=Arial, len=2.5];\n",
            "    overlap=false;\n",
            "    splines=true;\n"
        ]
            
        nodo_actual = self.vertices.inicio
        while nodo_actual is not None:
            graphviz_lines.append(f'    "{nodo_actual.vertice.nombre.nombre}";\n')
            nodo_actual = nodo_actual.siguiente
            
        try:
            self.recorridoReporte(self.vertices.inicio, graphviz_lines)
            graphviz_lines.append("}\n")
                
            import os
            reportes_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reportes')
            os.makedirs(reportes_dir, exist_ok=True)
                
            dot_path = os.path.join(reportes_dir, "reporte_grafo.dot")
            png_path = os.path.join(reportes_dir, "reporte_grafo.png")
                
            with open(dot_path, "w", encoding="utf-8") as file:
                file.writelines(graphviz_lines)
                
            import subprocess
            try:
                subprocess.run(["neato", "-Tpng", dot_path, "-o", png_path], check=True)
                print(f"Reporte generado exitosamente en: {png_path}")
                return
            except (subprocess.CalledProcessError, FileNotFoundError):
                dot_paths = [
                    r"C:\Program Files\Graphviz\bin\neato.exe",
                    r"C:\Program Files (x86)\Graphviz\bin\neato.exe"
                ]
                    
                for path in dot_paths:
                    try:
                        subprocess.run([path, "-Tpng", dot_path, "-o", png_path], check=True)
                        print(f"Reporte generado exitosamente en: {png_path}")
                        return
                    except (subprocess.CalledProcessError, FileNotFoundError):
                        continue
                    
                raise Exception("No se encontró el ejecutable 'neato' de Graphviz. Por favor, asegúrese de que Graphviz está instalado correctamente.")
                    
        except Exception as e:
            print(f"Error al generar el reporte: {str(e)}")