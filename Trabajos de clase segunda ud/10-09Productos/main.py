from producto import Producto
from inventario import Inventario

inventario = Inventario()

Producto_uno = Producto(1, "Iphone 16 Pro max", 31000, "Iphone", "rojo")
Producto_dos = Producto(2, "Iphone 15 Pro max", 20000, "Iphone", "negro")
Producto_tres = Producto(3, "Iphone 14 Pro max", 14000, "Iphone", "azul")


inventario.agregar_produto(Producto_uno)
inventario.agregar_produto(Producto_dos)
inventario.agregar_produto(Producto_tres)

print(inventario.productos)
print(inventario.productos[0].nombre)
print(inventario.productos[0].categoria)
print(inventario.productos[0].precio)
print(inventario.productos[0].color)
print(inventario.productos[0].id)
print("*****************")

print(inventario.productos[1].id)
print(inventario.productos[1].nombre)
print(inventario.productos[1].categoria)
print(inventario.productos[1].precio)
print(inventario.productos[1].color)
print("*****************")


print(inventario.productos[2].id)
print(inventario.productos[2].nombre)
print(inventario.productos[2].categoria)
print(inventario.productos[2].precio)
print(inventario.productos[2].color)
print("*****************")


