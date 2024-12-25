import os, subprocess

class Cliente:
    def __init__(self, dpi, nombres, apellidos, genero, telefono, direccion):
        self.dpi = dpi
        self.nombres = nombres
        self.apellidos = apellidos
        self.genero = genero
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f'DPI: {self.dpi} - Nombre completo: {self.nombres} {self.apellidos} - Género: {self.genero} - Teléfono: {self.telefono} - Dirección: {self.direccion}'

class NodoAVL:
    def __init__(self, cliente):
        self.cliente = cliente
        self.factorEquilibrio = 0
        self.izquierda = None
        self.derecha = None

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def insertarNodo(self, raiz, nodo):
        if raiz is None:
            raiz = nodo
            raiz.factorEquilibrio = self.calcularFactorEquilibrio(raiz)
            return nodo

        if int(nodo.cliente.dpi) < int(raiz.cliente.dpi):
            raiz.izquierda = self.insertarNodo(raiz.izquierda, nodo)
        elif int(nodo.cliente.dpi) > int(raiz.cliente.dpi):
            raiz.derecha = self.insertarNodo(raiz.derecha, nodo)

        raiz.factorEquilibrio = self.calcularFactorEquilibrio(raiz)

        if raiz.factorEquilibrio <= -2:
            if raiz.izquierda.factorEquilibrio <= 0:
                if self.raiz == raiz:
                    self.raiz = self.rotacionSimpleIzquierda(raiz)
                    return self.raiz
                raiz = self.rotacionSimpleIzquierda(raiz)
            else:
                if self.raiz == raiz:
                    self.raiz = self.rotacionCompuestaIzquierda(raiz)
                    return self.raiz
                raiz = self.rotacionCompuestaIzquierda(raiz)

        if raiz.factorEquilibrio >= 2:
            if raiz.derecha.factorEquilibrio >= 0:
                if self.raiz == raiz:
                    self.raiz = self.rotacionSimpleDerecha(raiz)
                    return self.raiz
                raiz = self.rotacionSimpleDerecha(raiz)
            else:
                if self.raiz == raiz:
                    self.raiz = self.rotacionCompuestaDerecha(raiz)
                    return self.raiz
                raiz = self.rotacionCompuestaDerecha(raiz)
        
        return raiz

    def insertarCliente(self, cliente):
        nuevoNodo = NodoAVL(cliente)
        if self.raiz is None:
            self.raiz = nuevoNodo
        else:
            self.insertarNodo(self.raiz, nuevoNodo)

    def eliminarNodo(self, raiz, dpi, eliminado):
        eliminado = True
        if raiz is None:
            return None, False

        if int(dpi) == int(raiz.cliente.dpi):
            if self.esHoja(raiz):
                return None, True 
                
            if raiz.izquierda is None:
                return raiz.derecha, True 
                
            if raiz.derecha is None:
                return raiz.izquierda, True
                
            raiz.derecha.izquierda = raiz.izquierda.derecha
            raiz.izquierda.derecha = raiz.derecha
            return raiz.izquierda, True

        if int(dpi) < int(raiz.cliente.dpi):
            raiz.izquierda, eliminado = self.eliminarNodo(raiz.izquierda, dpi, eliminado)
        elif int(dpi) > int(raiz.cliente.dpi):
            raiz.derecha, eliminado = self.eliminarNodo(raiz.derecha, dpi, eliminado) 
        else:
            eliminado = False

        return raiz, eliminado

    def eliminarCliente(self, dpi):
        eliminado = False
        self.raiz, eliminado = self.eliminarNodo(self.raiz, dpi, eliminado)
        return eliminado

    def esHoja(self, nodo) -> bool:
        return nodo.izquierda == None and nodo.derecha == None
    
    def obtenerAltura(self, nodo):
        if nodo is None:
            return 0
        
        alturaIzquierda = int(self.obtenerAltura(nodo.izquierda))
        alturaDerecha = int(self.obtenerAltura(nodo.derecha))

        return max(alturaIzquierda, alturaDerecha) + 1
    
    def calcularFactorEquilibrio(self, nodo):
        if nodo is None:
            return 0
        return int(self.obtenerAltura(nodo.derecha)) - int(self.obtenerAltura(nodo.izquierda))

    def rotacionSimpleIzquierda(self, nodo):
        nodoAuxiliar = nodo.izquierda
        nodo.izquierda = nodoAuxiliar.derecha
        nodoAuxiliar.derecha = nodo
        nodo = nodoAuxiliar

        nodo.factorEquilibrio = self.calcularFactorEquilibrio(nodo)
        if nodo.izquierda is not None:
            nodo.izquierda.factorEquilibrio = self.calcularFactorEquilibrio(nodo.izquierda)
        if nodo.derecha is not None:
            nodo.derecha.factorEquilibrio = self.calcularFactorEquilibrio(nodo.derecha)

        return nodo

    def rotacionSimpleDerecha(self, nodo):
        nodoAuxiliar = nodo.derecha
        nodo.derecha = nodoAuxiliar.izquierda
        nodoAuxiliar.izquierda = nodo
        nodo = nodoAuxiliar

        nodo.factorEquilibrio = self.calcularFactorEquilibrio(nodo)
        if nodo.izquierda is not None:
            nodo.izquierda.factorEquilibrio = self.calcularFactorEquilibrio(nodo.izquierda)
        if nodo.derecha is not None:
            nodo.derecha.factorEquilibrio = self.calcularFactorEquilibrio(nodo.derecha)

        return nodo
    
    def rotacionCompuestaIzquierda(self, nodo):
        nodo.izquierda = self.rotacionSimpleDerecha(nodo.izquierda)
        return self.rotacionSimpleIzquierda(nodo)

    def rotacionCompuestaDerecha(self, nodo):
        nodo.derecha = self.rotacionSimpleIzquierda(nodo.derecha)
        return self.rotacionSimpleDerecha(nodo)
    
    def devolverNodo(self, nodo):
        return nodo.cliente.__str__()
    
    def buscarNodo(self, raiz, dpi):
        if raiz is None:
            return None

        if int(dpi) == int(raiz.cliente.dpi):
            return raiz.cliente

        if int(dpi) < int(raiz.cliente.dpi):
            return self.buscarNodo(raiz.izquierda, dpi)
        
        else:
            return self.buscarNodo(raiz.derecha, dpi)

    def buscarCliente(self, dpi):
        return self.buscarNodo(self.raiz, dpi)
    
    def recorridoReporte(self, nodo, resultado, graphviz_lines):
        if nodo is None:
            return
            
        resultado.append(nodo.cliente)
        
        etiqueta = (
            f"{nodo.cliente.dpi}\\n"
            f"{nodo.cliente.nombres} {nodo.cliente.apellidos}\\n"
            f"{nodo.cliente.genero}\\n"
            f"{nodo.cliente.telefono}\\n"
            f"{nodo.cliente.direccion}"
        ).replace('"', '\\"')
        
        graphviz_lines.append(
            f'    "{nodo.cliente.dpi}" [label="{etiqueta}", '
            'shape=box, style=filled, fillcolor=lightblue, '
            'width=2.5, height=1.5];\n'
        )
         
        if nodo.izquierda is not None:
            graphviz_lines.append(f'    "{nodo.cliente.dpi}" -> "{nodo.izquierda.cliente.dpi}" [tailport=s, headport=n];\n')
            self.recorridoReporte(nodo.izquierda, resultado, graphviz_lines)
        
        if nodo.derecha is not None:
            graphviz_lines.append(f'    "{nodo.cliente.dpi}" -> "{nodo.derecha.cliente.dpi}" [tailport=s, headport=n];\n')
            self.recorridoReporte(nodo.derecha, resultado, graphviz_lines)

    def generar_reporte(self):
        if self.raiz is None:
            print("El árbol está vacío")
            return
            
        resultado = []
        graphviz_lines = [
            "digraph G {\n",
            "    node [fontname=Arial, shape=box, style=filled, fillcolor=lightblue];\n",
            "    edge [fontname=Arial];\n",
            "    rankdir=TB;\n",  
            "    nodesep=0.5;\n",  
            "    ranksep=0.7;\n",  
            "    splines=ortho;\n",  
            '    ordering="out";\n'  
        ]
        
        try:
            self.recorridoReporte(self.raiz, resultado, graphviz_lines)
            graphviz_lines.append("}\n")
            
            reportes_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reportes')
            os.makedirs(reportes_dir, exist_ok=True)
            
            dot_path = os.path.join(reportes_dir, "reporte_arbol.dot")
            png_path = os.path.join(reportes_dir, "reporte_arbol.png")
            
            with open(dot_path, "w", encoding="utf-8") as file:
                file.writelines(graphviz_lines)
            
            dot_paths = [
                "dot",
                r"C:\Program Files\Graphviz\bin\dot.exe",
                r"C:\Program Files (x86)\Graphviz\bin\dot.exe"
            ]
            
            dot_executable = None
            for path in dot_paths:
                try:
                    subprocess.run([path, "-V"], capture_output=True)
                    dot_executable = path
                    break
                except FileNotFoundError:
                    continue
            
            if dot_executable is None:
                raise Exception("No se encontró el ejecutable 'dot' de Graphviz. Por favor, asegúrese de que Graphviz está instalado correctamente.")
            
            resultado = subprocess.run(
                [dot_executable, "-Tpng", dot_path, "-o", png_path],
                capture_output=True,
                text=True
            )
            
            if resultado.returncode == 0:
                print(f"Reporte generado exitosamente en: {png_path}")
                if os.name == 'nt':
                    os.startfile(png_path)
                elif os.name == 'posix':
                    subprocess.run(["xdg-open", png_path])
            else:
                print(f"Error al generar el PNG: {resultado.stderr}")
                
        except Exception as e:
            print(f"Error al generar el reporte: {str(e)}")


