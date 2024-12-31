# Manual Técnico

## Proyecto 2

### Estructuras de Datos

### Xavi Alexander De León Perdomo - 202300596

A continucación se presenta el manual técnico del segundo proyecto del curso de estructuras de datos.

# Archivos

Archivos generados para la realización del programa.

# Archivo Interfaz.py

Este archivo contiene todo lo que se visualizara en el momento de la ejecución del programa.

## Clases de Interfaz.py

## class Interfaz

```python
class Interfaz:
```

Clase que contiene todo lo que se visualizara en el momento de la ejecución del programa y que permite al usuario realizar todas las acciones del programa.

### Métodos de class Interfaz

- __ init __

```python
def __init__(self):
```

Método para inicializar la interfaz, contiene una instancia de Árbol AVL, de Árbol B y de Grafo, los cuáles serviran para almacenar todos los datos que se ingresen en el programa. Además, el método genera todos los componentes necesarios para el menú principal de la aplicación.

- on_enter y on_leave

```python
def on_enter(self, frame):

def on_leave(self, frame):
```

Métodos que sirven para aumentar o disminuir el tamaño de los cuadros de las opciones del menú principal (funcinalidad meramente decorativa).

- mostrar_submenu

```python
def mostrar_submenu(self, categoria):
```

Método que muestra el submenú con las opciones que permite realizar cada categoria.

- ejecutar_accion

```python
def ejecutar_accion(self, categoria, accion):
```

Método que permite ejecutar acciones redirigir a otros métodos dependiendo de la categoria que se seleccionó en el menú principal y de la acción que se seleccionó en el submenú.

- agregar_cliente

```python
def agregar_cliente(self):
```

Método que despliega una ventana que permite ingresar los datos de un cliente que se desee agregar al Árbol AVL.

- procesar_cliente

```python
def procesar_cliente(self, dpi, nombres, apellidos, genero, telefono, direccion, ventana):
```

Método que procesa los datos recibidos de agregar_cliente, si los datos son validos permite agregarlos al Árbol AVL, en caso contrario los rechaza.

- agregar_vehiculo

```python
def agregar_vehiculo(self):
```

Método que despliega una ventana que permite ingresar los datos de un vehículo que se desee agregar al Árbol B.

- procesar_vehiculo

```python
def procesar_vehiculo(self, placa, marca, modelo, precio, ventana):
```

Método que procesa los datos recibidos de agregar_vehiculo, si los datos son validos permite agregarlos al Árbol B, en caso contrario los rechaza.

- agregar_ruta

```python
def agregar_ruta(self):
```

Método que despliega una ventana que permite ingresar los datos de un ruta que se desee agregar al Grafo.

- procesar_ruta

```python
def procesar_ruta(self, origen, destino, tiempo, ventana):
```

Método que procesa los datos recibidos de agregar_ruta, si los datos son validos permite agregarlos al Grafo, en caso contrario los rechaza.

- solicitar_llave

```python
def solicitar_llave(self, categoria, accion):
```

Método que solicita una llave para poder eliminar, modificar o mostrar los datos de un cliente o un vehículo.

- modifica_cliente

```python
def modificar_cliente(self, dpi):
```

Método que recibe un dpi (llave), que despliega una ventana la cual permite modificar los datos de un cliente con el mismo dpi.

- modifica_vehiculo

```python
def modificar_vehiculo(self, placa):
```

Método que recibe una placa (llave), que despliega una ventana la cual permite modificar los datos de un vehiculo con la mismo placa.

- mostrar_informacion

```python
def mostrar_informacion(self, llave, categoria):
```

Método que recibe una llave que permite mostrar la información de un cliente o vehículo según su llave.

- carga_masiva

```python
def carga_masiva(self, categoria):
```

Método que permite realizar lectura de archivos .txt para generar una carga masiva de clientes, vehículos o rutas.

-----------------------

# Archivo Cliente.py

Este archivo contiene la definicion de la clase de clientes que se manejaran en el programa, además de la estructura de datos Árbol AVL que permite el almacenamiento de los mismos.

## Clases de Cliente.py

## class Cliente

```python
class Cliente:
```

Clase que contiene la definición de un objeto de tipo cliente, esta clase no contiene ningún método aparte del __ init __.

### Métodos de class Cliente

- __ init __

```python
def __init__(self, dpi, nombres, apellidos, genero, telefono, direccion):
```

Método que define que atributos tendrá una instancia de Cliente, los atributos que tiene un cliente son nombres, apellidos, genero, télefono y dirección.

## class NodoAVL

```python
class NodoAVL:
```

Clase que contiene la definición de un nodo que será utilizado en el Árbol AVL, esta clase no contiene ningún método aparte del __ init __.

### Métodos de class NodoAVL

- __ init __

```python
def __init__(self, cliente):
```

Método que define que atributos tendrá una instancia de NodoAVL, los atributos que tiene este nodo son cliente (el valor del nodo será un cliente), factorEquilibrio (el factor de equilibrio del nodo que determina si es necesario que el árbol haga una rotación), izquierda y derecha (que son los nodos hijos a los que apunta el nodo dentro del arbol).

## class ArbolAVL

```python
class ArbolAVL:
```

Clase que contiene la definición de un Árbol AVL.

### Métodos de class ArbolAVL

- __ init __

```python
def __init__(self):
```

Método que define el atributo raiz del Árbol AVL, este atributo es el primer nodo o nodo raiz del Árbol AVL.

- insertarNodo

```python
def insertarNodo(self, raiz, nodo):
```

Método que permite insertar un nodo dentro del Árbol AVL a partir de recibir la raíz del árbol o la raíz de un sub árbol y el nodo que se busca insertar, este método también permite realizar rotaciones en el árbol a partir del factor de equilibrio que contengan los nodos del árbol. 

- insertarCliente

```python
def insertarCliente(self, cliente):
```

Método que es llamado desde la interfaz y recibe un cliente. Este método determina la raíz del Árbol AVL y define un Nodo AVL con el cliente, para llamar al método insertarNodo con estos parámetros.

- eliminarNodo

```python
def eliminarNodo(self, raiz, dpi, eliminado):
```

Método que busca un nodo apartir de la raiz del Árbol AVL o de un sub árbol y del dpi que recibe para comparar con todos los nodos y de esa forma eliminar el nodo dentro del árbol. Este método retorna un valor booleano para determinar si el nodo fue eliminado correctamente o no, este retorno sive para desplegar una alerta en la interfaz.

- eliminarCliente

```python
def eliminarCliente(self, dpi):
```

Método que es llamado desde la interfaz y recibe un dpi como parámetro. Este método determina la raíz del Árbol AVL y declara una variable booleana para llamar llamar al método eliminarNodo con estos parametros y el dpi.

- esHoja

```python
def esHoja(self, nodo):
```

Método que recibe un nodo y determina si es una hoja del Árbol AVL (determina si no tiene hijos).

- obtenerAltura

```python
def obtenerAltura(self, nodo):
```

Método que detemina la altura de un nodo dentro del Árbol AVL, esto con el fin de calcular el facor de equilibrio del nodo padre.

- calcularFactorEquilibrio

```python
def calcularFactorEquilibrio(self, nodo):
```

Método que calcula el factor de equilibrio de un nodo a partir de la resta de las alturas de sus hijos.

- Métodos de rotaciones

```python
def rotacionSimpleIzquierda(self, nodo):

def rotacionSimpleDerecha(self, nodo):

def rotacionCompuestaIzquierda(self, nodo):

def rotacionCompuestaDerecha(self, nodo):
```

Métodos que realizan las diferentes rotaciones del Árbol AVL para ajustar de mejor manera su factor de equilibrio.

- buscarNodo

```python
def buscarNodo(self, raiz, dpi):
```

Método que realiza una busqueda dentro del Árbol AVL para encontrar un nodo que coincida con un dpi.

- buscarCliente

```python
def buscarCliente(self, dpi):
```

Método que es llamada desde la interfaz con un parametro dpi, este método determina la raíz del Árbol AVL y llama al método buscarNodo con estos parametros.

- recorridoReporte

```python
def recorridoReporte(self, nodo, resultado, graphviz_lines):
```

Método que recorre el Árbol AVL para generar su reporte gráfico.

- generar_reporte

```python
def generar_reporte(self):
```

Método que es llamado desde la interfaz y genera el reporte gráfico del Árbol AVL apartir de la llamada al método recorridoReporte.


# Archivo Vehiculo.py

Este archivo contiene la definicion de la clase de vehículos que se manejaran en el programa, además de la estructura de datos Árbol B que permite el almacenamiento de los mismos.

## Clases de Vehiculo.py

## class Vehiculo

```python
class Vehiculo:
```

Clase que contiene la definición de un objeto de tipo vehículo, esta clase no contiene ningún método aparte del __ init __.

### Métodos de class Cliente

- __ init __

```python
def __init__(self, placa, marca, modelo, precio):
```

Método que define que atributos tendrá una instancia de Vehiculo, los atributos que tiene un cliente son placa, marca, modelo y precio.

## class NodoB

```python
class NodoB:
```

Clase que contiene la definición de un nodo que será utilizado en el Árbol B, esta clase no contiene ningún método aparte del __ init __.

### Métodos de class NodoB

- __ init __

```python
def __init__(self, hoja = False):
```

Método que define que atributos tendrá una instancia de NodoB, los atributos que tiene este nodo son hoja (atributo de tipo booleano para determinar si el nodo es una hoja), pagina (contenido del nodo el cual es una lista de vehiculos) e hijos (lista de hijos a los cuales apunta el nodo).

## class ArbolB

```python
class ArbolB:
```

Clase que contiene la definición de un Árbol B.

### Métodos de class ArbolB

- __ init __

```python
def __init__(self, orden):
```

Método que define los atributos del Árbol B, estos son raíz (es el primer nodo que se encuentra en el árbol) y orden (define el orden de nuestro árbol).

- insertarVehiculo

```python
def insertarVehiculo(self, vehiculo):
```

Método llamado desde la interfaz que recibe un vehículo como parámetro y determina la raíz del Árbol B para llamar al método insertarEnPagina con estos parámetros. Este método también calcula si la longitud de la página es mayor al límite de elementos de una página (orden del árbol -1) y si esto es cierto, llama al método dividirPagina.

- insertarEnPagina

```python
def insertarEnPagina(self, raiz, vehiculo):
```

Método que es capaz de insertar un vehiculo en la posición correcta de una página, este método también busca en que nodo en específico debe insertarse el vehículo y determina si es necesario llamar al método dividirPagina.

- dividirPagina

```python
def dividirPagina(self, raiz, i):
```

Método que calcula la mitad de la página y es capaz de dividir la página en 2 partes a partir de esa misma mitad.

- eliminarNodo

```python
def eliminarNodo(self, nodo, placa, eliminado):
```

Método que busca un nodo apartir de un nodo del Árbol B y de la plava que recibe para comparar con todos los elementos de las paginas y de esa forma eliminar el elemento dentro del árbol. Este método retorna un valor booleano para determinar si el nodo fue eliminado correctamente o no, este retorno sive para desplegar una alerta en la interfaz.

- eliminarVehiculo

```python
def eliminarVehiculo(self, placa):
```

Método que es llamada desde la interfaz, este método recibe una placa y determina la raíz del Árbol B para llamar al método eliminarNodo y enviarle estos parametros.

- buscarNodo

```python
def buscarNodo(self, raiz, placa):
```

Método que realiza una busqueda dentro del Árbol B para encontrar un elemento que coincida con una placa.

- buscarCliente

```python
def buscarCliente(self, dpi):
```

Método que es llamado desde la interfaz con un parametro placa, este método determina la raíz del Árbol B y llama al método buscarNodo con estos parametros.

- recorridoReporte

```python
def recorridoReporte(self, nodo, resultado, graphviz_lines):
```

Método que recorre el Árbol B para generar su reporte gráfico.

- generar_reporte

```python
def generar_reporte(self):
```

Método que es llamado desde la interfaz y genera el reporte gráfico del Árbol B apartir de la llamada al método recorridoReporte.

# Archivo Ruta.py

Este archivo contiene la definicion de la clase de rutas que se manejaran en el programa, además de la estructura de datos de Grafo que permite el almacenamiento de los mismos.

## Clases de Ruta.py

## class Ruta

```python
class Ruta:
```

Clase que contiene la definición de un objeto de tipo ruta, esta clase no contiene ningún método aparte del __ init __.

### Métodos de class Ruta

- __ init __

```python
def __init__(self, origen, destino, tiempo):
```

Método que define que atributos tendrá una instancia de Ruta, los atributos que tiene una ruta son origen, destino y tiempo.

## class NodoB

```python
class Vertice:
```

Clase que contiene la definición de un nodo que será utilizado en el Grafo, esta clase no contiene ningún método aparte del __ init __.

### Métodos de class Vertice

- __ init __

```python
def __init__(self, nombre, peso=0):
```

Método que define que atributos tendrá una instancia de Vertice, los atributos que tiene este nodo son nombre (nombre que tiene nuestro vertice), peso (el peso que tendra la arista que una al vertice con otro) y rutas (ListaEnlazada que contiene los vertices a los cuales apunta nuestro vertice).

## class NodoLista

```python
class NodoLista:
```

Clase que contiene la definición de un nodo que será utilizado en la ListaEnlazada, esta clase no contiene ningún método aparte del __ init __.

### Métodos de class Vertice

- __ init __

```python
def __init__(self, vertice):
```

Método que define que atributos tendrá una instancia de NodoLista, los atributos que tiene este nodo son vertice (elemento Vertice que contiene nuestro nodo) y siguiente (siguiente nodo al que apunta nuestro nodo en la ListaEnlazada).

## class ListaEnlazada

```python
class ListaEnlazada:
```

Clase que contiene la definicion de una lista enlazada que utilizaremos en los vertices y en la ListaAdyacencia.

### Métodos de class ListaEnlazada
- __ init __
```python
def __init__(self):
```

Método que define el atributo que tendrá una instancia de ListaEnlazada, este atributo es inicio, el cual es el primer NodoLista de nuestra lista enlazada.

- insertar 

```python
def insertar(self, vertice):
```

Método que nos permite insertar un elemento Vertice en la ListaEnlazada.

- buscar

```python
def buscar(self, vertice):
```

Método que nos permite buscar un elemento Vertice en la ListaEnlazada apartir de comparar el vertice que recibe como parametro con los vertices de la lista enlazada.

## class ListaAdyacencia

```python
class ListaAdyacencia:
```

Clase que contiene la definición de una lista de adyacencia que utilizaremos para la implementación del Grafo.

### Métodos de class ListaAdyacencia

- __ init __

```python
def __init__(self):
```

Método que define el atributo que tendrá una instancia de ListaAdyacencia, este atributo es vertices, el cual es la lista de vertices que contendra nuestra lista de adyacencia.

- insertarVertice

```python
def insertarVertice(self, ruta):
```

Método que recibe una Ruta, de la cual obtiene sus atributos origen, para crear un vertice de origen en la ListaAdyacencia; y destino y tiemp, para crear un vertice y agregarlo a lista rutas de nuestro vertice.

- recorridoReporte

```python
def recorridoReporte(self, nodo, resultado, graphviz_lines):
```

Método que recorre la ListaAdyacencia para generar el reporte gráfico del Grafo.

- generar_reporte

```python
def generar_reporte(self):
```

Método que es llamado desde la interfaz y genera el reporte gráfico del Grafo apartir de la llamada al método recorridoReporte.