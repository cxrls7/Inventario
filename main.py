from src.inventario import registrar_producto, buscar_producto, calcular_estadisticas, actualizar_producto, eliminar_producto
import locale
import os


def formato_cop(valor):
    return locale.currency(valor, symbol=True, grouping=True)


try:
    locale.setlocale(locale.LC_ALL, "es_CO.UTF-8")
except:
    locale.setlocale(locale.LC_ALL, "SPANISH_COLOMBIA")


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def main():

    inventario = []

    while True:

        print("\n--- BIENVENIDO AL INVENTARIO ---")
        print()
        print("-Sistema con diferentes funciones que te facilitara la gestion de los productos de tu inventario.")

        print("\n---- MENU DEL INVENTARIO ----")
        print("\n1-📥 Agregar producto")
        print("2-📦 Ver inventario")
        print("3-🔎 Buscar producto")
        print("4-💱 Actualizar producto")
        print("5-⛔ Eliminar producto")
        print("6-📊 Ver estadisticas")
        print("7-👋 Salir")

        opcion = input("\n-Ingresa una opcion: ")

        if opcion == "1":
            while True:
                limpiar()
                nuevo_producto = registrar_producto()
                inventario.append(nuevo_producto)
                print("\n=================================")
                print("Resumen del registro")
                print("=================================")
                print(F"✅ Se registro: {nuevo_producto["nombre"]}")
                print(f"📥 Cantidad: {nuevo_producto["cantidad"]}")
                print(f"💰 Total final: {formato_cop(nuevo_producto["total"])}")
                print("=================================")
                print("\nProducto añadido correctamente ✅")

                realizar_otra = input("\n¿Desea añadir otro producto? si/no: ")
                if realizar_otra != "si":
                    limpiar()
                    break

        elif opcion == "2":
            limpiar()
            if not inventario:
                limpiar()
                print(" INVENTARIO VACIO 📂 ")
                input("\n-Presiona ENTER para regresar al menu...")
                limpiar()

            else:
                limpiar()
                print("---- MENU VISUALIZAR INVENTARIO ----")
                for nuevo_producto in inventario:
                    print(
                        f"\n| Nombre: {nuevo_producto["nombre"]} | Precio: {formato_cop(nuevo_producto["precio"])} | Cantidad: {nuevo_producto["cantidad"]} |")
                pass

                input("\nPresiona ENTER para volver al menu...")
                limpiar()

        elif opcion == "3":

            while True:
                limpiar()
                print("\n---- MENU BUSQUEDA DE PRODUCTOS ----")
                nombre = input("\n-Ingresa el nombre del producto: ")
                resultado = buscar_producto(inventario, nombre)

                if resultado:

                    print("\n=================================")
                    print("Resumen de busqueda")
                    print("=================================")
                    print(F"🏷️ Producto: {resultado["nombre"]}")
                    print(f"🧺 Stock: {resultado["cantidad"]}")
                    print(f"💵 Valor total: {formato_cop(resultado["total"])}")
                    print("=================================")

                    input("-¿Quieres hacer otra busqueda? si/no: ")
                    if input != "si":
                        limpiar()
                        break

                else:
                    print(f"\n ❕ EL PRODUCTO '{nombre}' NO SE HA ENCONTRADO ❕")
                    input("\n Presiona ENTER para volver al menu...")
                    limpiar()
                    break

        elif opcion == "4":
            limpiar()
            while True:
                actualizar_producto(inventario)
                salir = input("\n¿Quieres actualizar otro producto? si/no: ")
                limpiar()
                if salir == "no":
                 limpiar()
                 break

        elif opcion == "5":
            limpiar()
            while True:
                eliminar_producto(inventario)
                respuesta=input("¿Deseas eliminar otro producto? si/no: ")
                if respuesta == "no":
                    limpiar()
                    break

        elif opcion == "6":
            limpiar()
            total_dinero, total_unidades = calcular_estadisticas(inventario)
            print("---- MENU ESTADISTICAS DEL INVENTARIO ----")
            if not inventario:
                limpiar()
                print("❕NO HAY OBJETOS EN EL INVENTARIO❕")
                input("\nPresiona ENTER para salir...")
                limpiar()

            else:
                print("\n=================================")
                print("Reporte de inventario")
                print("=================================")
                print(f"🗒️ Numero de productos: {len(inventario)}")
                print(f"📋 Unidades totales: {total_unidades}")
                print(f"💰 Valor total: {formato_cop(total_dinero)}")
                print("=================================")
                input("\nPresiona ENTER para volver al menu...")
                limpiar()

        elif opcion == "7":
            print("\nGracias por utilizar el sistema de inventario 👋 ")
            break
        else:
            limpiar()
            print("❌ ERROR: Ingrese una opcion valida")


if __name__ == "__main__":
    main()
