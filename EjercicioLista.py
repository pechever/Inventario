
# Comentario

lista=[1,2,3,4]
##listaString=["1","2","3"]

#print(lista[0])
#print(lista[1])

#for i in lista:
#    print(i)

#indexlista=0
#while indexlista<len(lista):
#    print(lista[indexlista])
#    indexlista+=1

#print(lista)

#dic={"cedula":"99999"}
#print(dic)


inventario=[{"nombre":"Camisa", "cantidad":2}, {"nombre":"Pantalon", "cantidad":4}]
print(inventario)

#agregar inventario
inventario.append({"nombre":"Zapatos","cantidad":10})
print(inventario)

#eliminar inventario
for producto in inventario:
    if producto["nombre"]=="Camisa":
        inventario.remove(producto)
print(inventario)  

#actualizar 
for producto in inventario:
    if producto["nombre"]=="Zapatos":
        cantidad_nueva=producto["cantidad"]+4
        if cantidad_nueva>0:
            producto["cantidad"]=cantidad_nueva

print(inventario)

#mostrar lista
for producto in inventario:
    print(f"Producto - {producto["nombre"]} - Cantidad - {producto["cantidad"]}")