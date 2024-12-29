import os, subprocess

class Vehiculo:
    def __init__(self, placa, marca, modelo, precio):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f'Placa: {self.placa}'
    
class NodoB:
    def __init__(self, hoja = False):
        self.hoja = hoja
        self.pagina = []
        self.hijos = []

    def __str__(self):
        pagina_str = ', '.join(str(vehiculo) for vehiculo in self.pagina)
        hijos_str = ', '.join(str(hijo) for hijo in self.hijos)
        return f"Hoja: {self.hoja} - Página: [{pagina_str}] - Hijos: [{hijos_str}]"
        
class ArbolB:
    def __init__(self, orden):
        self.raiz = NodoB(True)
        self.orden = orden

    def insertarVehiculo(self, vehiculo):
        raiz = self.raiz
        self.insertarEnPagina(raiz, vehiculo)
        if len(raiz.pagina) > self.orden - 1:
            nuevaRaiz = NodoB()
            self.raiz = nuevaRaiz
            nuevaRaiz.hijos.insert(0, raiz)
            self.dividirPagina(nuevaRaiz, 0)

    def insertarEnPagina(self, raiz, vehiculo):
        i = len(raiz.pagina) - 1

        if (raiz.hoja):
            raiz.pagina.append(None)

            while i >= 0 and vehiculo.placa < raiz.pagina[i].placa:
                raiz.pagina[i + 1] = raiz.pagina[i]
                i -= 1
            
            raiz.pagina[i + 1] = vehiculo

        else:
            while i >= 0 and vehiculo.placa < raiz.pagina[i].placa:
                i -= 1

            i += 1
            
            self.insertarEnPagina(raiz.hijos[i], vehiculo)
            if len(raiz.hijos[i].pagina) > self.orden - 1:
                self.dividirPagina(raiz, i)

    def dividirPagina(self, raiz, i):
        mitad = int((self.orden-1)/2)
        nuevoHijo = raiz.hijos[i]
        nuevaRaiz = NodoB(nuevoHijo.hoja)

        raiz.hijos.insert(i + 1, nuevaRaiz)
        raiz.pagina.insert(i, nuevoHijo.pagina[mitad])

        nuevaRaiz.pagina = nuevoHijo.pagina[mitad + 1 : self.orden]
        nuevoHijo.pagina = nuevoHijo.pagina[0 : mitad]

        if not nuevoHijo.hoja:
            nuevaRaiz.hijos = nuevoHijo.hijos[mitad + 1 : self.orden + 1]
            nuevoHijo.hijos = nuevoHijo.hijos[0 : mitad + 1]

    def eliminarNodo(self, nodo, placa, eliminado):
        if nodo is None:
            return None, False

        i = 0
        while i < len(nodo.pagina) and int(placa) > int(nodo.pagina[i].placa):
            i += 1

        if i < len(nodo.pagina) and int(placa) == int(nodo.pagina[i].placa):
            if nodo.hoja:
                nodo.pagina.pop(i)
                return nodo, True
            
            if len(nodo.hijos[i].pagina) > int((self.orden-1)/2):
                actual = nodo.hijos[i]
                while not actual.hoja:
                    actual = actual.hijos[-1]
                nodo.pagina[i] = actual.pagina[-1]
                nodo.hijos[i], eliminado = self.eliminarNodo(nodo.hijos[i], actual.pagina[-1].placa, eliminado)
            else:
                hijo_izq = nodo.hijos[i]
                hijo_der = nodo.hijos[i + 1]
                hijo_izq.pagina.append(nodo.pagina[i])
                hijo_izq.pagina.extend(hijo_der.pagina)
                if not hijo_izq.hoja:
                    hijo_izq.hijos.extend(hijo_der.hijos)
                nodo.pagina.pop(i)
                nodo.hijos.pop(i + 1)
                nodo.hijos[i], eliminado = self.eliminarNodo(hijo_izq, placa, eliminado)
                
            return nodo, True
        
        if nodo.hoja:
            return nodo, False
        
        nodo.hijos[i], eliminado = self.eliminarNodo(nodo.hijos[i], placa, eliminado)
        
        return nodo, eliminado

    def eliminarVehiculo(self, placa):
        eliminado = False
        self.raiz, eliminado = self.eliminarNodo(self.raiz, placa, eliminado)
        
        if len(self.raiz.pagina) == 0 and not self.raiz.hoja:
            self.raiz = self.raiz.hijos[0]
            
        return eliminado


    def buscarNodo(self, nodo, placa):
        
        if nodo is None:
            return None
        
        i = 0
        while i < len(nodo.pagina) and int(placa) > int(nodo.pagina[i].placa):
            i += 1
        
        if i < len(nodo.pagina) and int(placa) == int(nodo.pagina[i].placa):
            return nodo.pagina[i]
        
        if nodo.hoja:
            return None
        
        return self.buscarNodo(nodo.hijos[i], placa)

    def buscarVehiculo(self, placa):
        return self.buscarNodo(self.raiz, placa)
    
    def recorridoReporte(self, nodo, nivel, graphviz_lines):
        if nodo is None:
            return
            
        nodo_id = str(id(nodo))
        
        label_parts = ['<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">']
        label_parts.append('<TR>')
        
        for vehiculo in nodo.pagina:
            label_parts.append(
                f'<TD><TABLE BORDER="0" CELLBORDER="0" CELLPADDING="2">'
                f'<TR><TD>Placa: {vehiculo.placa}</TD></TR>'
                f'<TR><TD>Marca: {vehiculo.marca}</TD></TR>'
                f'<TR><TD>Modelo: {vehiculo.modelo}</TD></TR>'
                f'<TR><TD>Precio: {vehiculo.precio}</TD></TR>'
                f'</TABLE></TD>'
            )
        
        label_parts.append('</TR></TABLE>>')
        node_label = ''.join(label_parts)
        
        graphviz_lines.append(
            f'    "{nodo_id}" [label={node_label}, shape=none];\n'
        )
        
        if not nodo.hoja:
            for i, hijo in enumerate(nodo.hijos):
                if hijo is not None:
                    hijo_id = str(id(hijo))
                    graphviz_lines.append(f'    "{nodo_id}" -> "{hijo_id}";\n')
                    self.recorridoReporte(hijo, nivel + 1, graphviz_lines)

    def generar_reporte(self):
        if self.raiz is None:
            print("El árbol está vacío")
            return
            
        graphviz_lines = [
            "digraph G {\n",
            "    node [fontname=Arial];\n",
            "    edge [fontname=Arial];\n",
            "    rankdir=TB;\n",  
            "    nodesep=1.5;\n", 
            "    ranksep=1.0;\n",
            "    splines=line;\n",  
            '    ordering="out";\n',
            "    edge [dir=forward, arrowsize=0.8];\n"
        ]
        
        try:
            self.recorridoReporte(self.raiz, 0, graphviz_lines)
            graphviz_lines.append("}\n")
            
            reportes_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reportes')
            os.makedirs(reportes_dir, exist_ok=True)
            
            dot_path = os.path.join(reportes_dir, "reporte_arbolB.dot")
            png_path = os.path.join(reportes_dir, "reporte_arbolB.png")
            
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
            else:
                print(f"Error al generar el PNG: {resultado.stderr}")
                
        except Exception as e:
            print(f"Error al generar el reporte: {str(e)}")
            
    

