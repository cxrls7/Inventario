import csv
import os

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def calcular_total(precio,  cantidad):
    return precio * cantidad
    
def registrar_producto():
    print("---- MENU AÑADIR PRODUCTOS ----")
    
    nombre = input("\n-🖋️  Ingresa el nombre del producto: ")
    
    

    precio = 0.0
    cantidad = 0
    
    while True:
        try:
            precio = float(input("-💶  Precio del unitario del producto: "))
            break
        except ValueError:
            print("\n ❌ Ingresa un valor valido ❌")

    while True:
        try:
            cantidad = int(input("-📤 Ingresa la cantidad del producto: "))
            break
        except ValueError:
            print("\n❌ Ingresa un valor valido ❌")  

    total = precio * cantidad

    producto = {"nombre":nombre, "cantidad":cantidad, "precio":precio, "total":total}
    return producto


def buscar_producto(inventario, nombre_buscado):
    for producto in inventario :
       if producto['nombre'].strip().lower() == nombre_buscado.strip().lower():
          return producto
    return None 



def calcular_estadisticas(inventario):
   
    
    if not inventario:
        return 0, 0  

    valor_total_acumulado = 0
    cantidad_total_items = 0
    mas_caro = inventario[0]
    mayor_stock = inventario[0]
    calcular_subtotal = lambda producto: producto["precio"] * producto["cantidad"]

    for producto in inventario:
        subtotal = calcular_subtotal(producto)
        valor_total_acumulado += subtotal
        cantidad_total_items += producto['cantidad']

        if producto['precio'] > mas_caro['precio']: 
            mas_caro = producto     

        if producto['cantidad'] > mayor_stock['cantidad']:
            mayor_stock = producto

  
    return cantidad_total_items, valor_total_acumulado



    
def actualizar_producto(inventario):
   print("--- MENU ACTUALIZAR PRODUCTO ----")

   nombre_buscar = input("\n-Ingrese el nombre del producto a actualizar: ")
   
   for producto in inventario:
            
            if producto['nombre'] == nombre_buscar:
                    print(f"\n-Producto encontrado ✔️ : {producto['nombre']}")
                    print("\n-Parametros actuales")
                    print("\nNombre          Cantidad          Precio")
                    print("------------------------------------------")

                    print(f"{producto['nombre']:10} {producto['cantidad']:10} {producto['precio']:20}")

            try:
            
            
              nueva_cantidad = int(input("\n-Ingrese la nueva cantidad: "))
              nuevo_precio = float(input("-Ingrese el nuevo precio: "))

              producto['cantidad'] = nueva_cantidad
              producto['precio'] = nuevo_precio
              producto['total'] = nueva_cantidad * nuevo_precio

              print("\nProducto actualizado con exito ✅ ")
              return True
                
            except ValueError:
                    print("❌ ERROR: INGRESA NUMEROS VALIDOS")
                    return False
                
   print(f"\n❕ EL PRODUCTO {nombre_buscar} NO EXISTE ❕")
   return False        

def eliminar_producto(inventario):
        print("---- MENU ELIMINAR PRODUCTOS ----")
        print(f"\n-Inventario actual 📦 ")
        for producto in inventario:
             print(f"\nNombre | {producto['nombre']} ")
             
             pass
  
        nombre_eliminar = input("\n-Ingresa el nombre del producto a eliminar: ")

        for producto in inventario: 
            try:
                if producto ['nombre'] == nombre_eliminar:
                    inventario.remove(producto)
                    print("\nProducto eliminado correctamente ✅ ")
                    return True
            except ValueError:
                print("❌ ERROR: Ingresa un nombre valido")

        print(f"\n❕ EL PRODUCTO {nombre_eliminar} NO ESTA DISPONIBLE ❕")
        return False
         

def guardar_csv(inventario, ruta = "data/inventario.csv"):
   print("----- MENU DE EXPORTACION DE ARCHIVOS ----- ")
   

   
   while True:
    exportar = input("\n- Ingrese 1 para exportar: ")

    if not inventario:
        print("\n❌ NO HAY PRODUCTOS PARA EXPORTAR")
        input("\nPresione ENTER para salir al menu....")
        return
    try:
        if exportar == "1":

            with open(ruta, "w", newline="", encoding="utf-8") as archivo:
                

                escritor = csv.writer(archivo)
                escritor.writerow(["nombre", "precio" , "cantidad"])

                for producto in inventario:
                     escritor.writerow([
            producto['nombre'], 
            f"${producto['precio']}", 
            producto['cantidad']
        ])

            print(f"\n- Datos exportados correctamente a {ruta} ✅")
            print(f"\n- Se exportaron {len(inventario)} productos ✅ ")

    except Exception as e:
            print(f"\n❌ ERROR AL EXPORTAR: {e}")
        
    reintentar = input("\n¿Quiere intentarlo de nuevo? si/no: ")

    if reintentar == "no":
            limpiar()
            break
            
def cargar_csv(inventario):
    print("\n---- MENU CARGA DE ARCHIVOS ----")


    while True:

        nombre_archivo = input("\n-📂 Ingresa el nombre o ruta del archivo CSV (ej: datos.csv): ")



        if not os.path.exists(nombre_archivo):
          limpiar()
          print(f"\n ❌ El archivo {nombre_archivo} no existe ")
          return cargar_csv(inventario) 
              
            
        
            
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
             lector = csv.DictReader(archivo)
                        
             productos_nuevos = 0  
             for fila in lector:
                producto = {
                     'nombre': fila['nombre'],
                     'precio': float(fila['precio'].replace("$", "").replace(".", "").replace(",", "")),
                      'cantidad': int(fila['cantidad']) }
                        
                inventario.append(producto)
                productos_nuevos += 1

                print(f"\n-Archivo {nombre_archivo} cargado correctamente ✅")
                print(f"-Se cargaron {productos_nuevos} productos nuevos ✅")
                print(f"\nTotal en inventario: {len(inventario)} productos.")

        except FileNotFoundError:
                print("\n❌ El archivo no existe")
                return producto
        
            
        salir = input("\n¿Desea importar otro archivo? si/no : ")

        if salir == "no":
         limpiar()
         break
                    

    



    

       
        
    



    