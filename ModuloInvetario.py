def agregar_producto(inventario):
    nombre_producto=input("Ingrese el nombre a agregar: ").capitalize()
    cantidad_producto=int(input("ingrese la cantidad: "))
    inventario.append({"nombre":nombre_producto,"cantidad":cantidad_producto})
    print("Producto Agregado  Adecuadamente")
    print(inventario)

def eliminar_producto(inventario):
    nombre_producto=input("Ingrese el nombre  a eliminar: ").capitalize()
    for producto in inventario:
        if producto["nombre"]==nombre_producto:
            inventario.remove(producto)
            print("Producto eliminado correctamente")
    print(inventario)  

def actualizar_producto(inventario):
    nombre_producto=input("Ingrese el nombre a actualizar: ").capitalize()
    cantidad_producto=int(input("ingrese la cantidad actualizar: "))
    for producto in inventario:
        if producto["nombre"]==nombre_producto:
            cantidad_nueva=producto["cantidad"]+cantidad_producto
            if cantidad_nueva>=0:
                producto["cantidad"]=cantidad_nueva
                print("Actualización correctamente realizada")
            else:
                print("Inventario Negativo")
    print(inventario)

def mostrar_inventario(inventario):
    for producto in inventario:
        print(f"Producto - {producto["nombre"]} - Cantidad - {producto["cantidad"]}")


def mostrar_menu():
    print("\n1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Mostrar inventario")
    print("5. Salir")

def main():
    inventario=[]
    print(inventario)
    while True:
        mostrar_menu()
        opcion=input("Seleccione una opción:")
        if opcion=="1":
            agregar_producto(inventario)

        if opcion=="2":
            eliminar_producto(inventario)

        if opcion=="3":
            actualizar_producto(inventario)

        if opcion=="4":
            mostrar_inventario(inventario)


        if opcion=="5":
            break

        


if __name__ == "__main__":
    main()