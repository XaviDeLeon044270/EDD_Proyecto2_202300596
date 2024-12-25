    def insertarVehiculo(self, vehiculo):
        raiz = self.raiz

        if len(raiz.pagina) == self.orden - 1:
            nuevaRaiz = NodoB()
            self.raiz = nuevaRaiz
            nuevaRaiz.hijos.insert(0, raiz)
            self.dividirPagina(nuevaRaiz, 0)
            self.insertarEnPagina(nuevaRaiz, vehiculo)

        else:
            self.insertarEnPagina(raiz, vehiculo)

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
        hijo = raiz.hijos[i]
        nodo = NodoB(hijo.hoja)

        raiz.hijos.insert(i + 1, nodo)

        raiz.pagina.insert(i, hijo.pagina[mitad])
        nodo.pagina = hijo.pagina[mitad + 1 : self.orden]
        hijo.pagina = hijo.pagina[0 : mitad]

        if not hijo.hoja:
            nodo.hijos = hijo.hijos[mitad + 1 : self.orden]
            hijo.hijos = hijo.hijos[0 : mitad]