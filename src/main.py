
from src.inventario import registrar_producto


def main():
    print("--- BIENVENIDO AL INVENTARIO ---")
    print()
    producto = registrar_producto()

    print("\n=================================")
    print("\nResumen del registro")
    print("=================================")
    print(F"Se registro: {producto["nombre"]}")
    print(f"Cantidad: {producto["cantidad"]}") 
    print(f"Total final: ${producto["total"]}")
    print("=================================")


if __name__ == "__main__":
     main()

