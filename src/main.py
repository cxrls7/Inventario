
from inventario import registrar_producto


def main():
    print("--- BIENVENIDO AL INVENTARIO ---")
    print()
    producto = registrar_producto
    print("\nResumen del registro")
    print(F"Se registro: {producto["nombre"]}")
    print(f"Total final: ${producto["total"]}")

    if __name__: "__main__"
    main()

