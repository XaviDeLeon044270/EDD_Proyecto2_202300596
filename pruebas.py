from Cliente import Cliente, NodoAVL, ArbolAVL

cliente1 = Cliente(10, "Juan", "Pérez", "M", "12345678", "Ciudad")
cliente2 = Cliente(5, "María", "González", "F", "87654321", "Pueblo")

if cliente1.dpi < cliente2.dpi:
    print(f"{cliente1.nombres} es menor que {cliente2.nombres}")
elif cliente1.dpi > cliente2.dpi:
    print(f"{cliente1.nombres} es mayor que {cliente2.nombres}")

