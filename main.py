from src.inventario import registrar_producto
import os

def limpiar():
     os.system("cls" if os.name == "nt" else "clear")

def main():

    inventario = []

    while True:

            print("--- BIENVENIDO AL INVENTARIO ---")
            print()
            
       
            print("\n---- MENU DEL INVENTARIO ----")
            print("1- Agregar producto")
            print("2- Ver inventario")
            print("3- Salir")

            opcion = input("Ingresa una opcion: ")
        


         
        
            if opcion == "1":
             while True:
                limpiar()
                nuevo_producto = registrar_producto()
                inventario.append(nuevo_producto)
                print("\n=================================")
                print("\nResumen del registro")
                print("=================================")
                print(F"Se registro: {nuevo_producto["nombre"]}")
                print(f"Cantidad: {nuevo_producto["cantidad"]}") 
                print(f"Total final: ${nuevo_producto["total"]}")
                print("=================================")
                print("Producto añadido correctamente ✅")

                realizar_otra = input("¿Desea añadir otro producto? si/no: ")
                if realizar_otra != "si":
                 limpiar()
                 break
            
                
                    
                
             
          




   
            elif opcion == "2":
             limpiar()
             if not inventario: 
                    print(" INVENTARIO VACIO 📂 ")
             else:
                for nuevo_producto in inventario: print(f"{nuevo_producto["nombre"]} - {nuevo_producto["cantidad"]}")
                pass
            
     

       
            elif opcion == "3":
             break
            else:
                print("❌ ERROR: Ingrese una opcion valida")
        

   

    


if __name__ == "__main__":
     main()

