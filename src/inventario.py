
def calcular_total(precio,  cantidad):
    return precio * cantidad
    
def registrar_producto():
    print("---- MENU AÑADIR PRODUCTOS ----")
    
    nombre = input("\n-Ingresa el nombre del producto: ")
    
    

    precio = 0.0
    cantidad = 0
    
    while True:
        try:
            precio = float(input("-Precio del unitario del producto: "))
            break
        except ValueError:
            print("\n ❌ Ingresa un valor valido ❌")

    while True:
        try:
            cantidad = int(input("-Ingresa la cantidad del producto: "))
            break
        except ValueError:
            print("\n❌ Ingresa un valor valido ❌")  

    total = precio * cantidad

    producto = {"nombre":nombre, "cantidad":cantidad, "precio":precio, "total":total}
    return producto


def buscar_producto(inventario, nombre_buscado  ):
    for producto in inventario :
       if producto['nombre'].strip().lower() == nombre_buscado.strip().lower():
          return producto
    return None 


def calcular_estadisticas(inventario):
    valor_total_acumulado = 0
    cantidad_total_items = 0

    for producto in inventario:
        valor_total_acumulado += producto['total']
        cantidad_total_items += producto['cantidad']

    return valor_total_acumulado, cantidad_total_items
    
def actualizar_producto(inventario):
   print("--- MENU ACTUALIZAR PRODUCTO ----")

   nombre_buscar = input("\n-Ingrese el nombre del producto a actualizar:").strip().lower()
   
   for producto in inventario:
            
            if producto['nombre'].lower() == nombre_buscar:
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
                    print("Producto eliminado correctamente ✅ ")
                    return True
            except ValueError:
                print("❌ ERROR: Ingresa un nombre valido")

        print(f"\n❕ EL PRODUCTO {nombre_eliminar} NO ESTA DISPONIBLE ❕")
        return False
         
            
       
        
    



    