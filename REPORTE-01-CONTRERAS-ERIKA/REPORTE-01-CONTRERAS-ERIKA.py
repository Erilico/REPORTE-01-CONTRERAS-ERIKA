from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches


usuario_correcto = "Admin"
contraseña_correcta = "4dm1n"
texto_acceso = """
¡Bienvenida al sistema de Lifestore, Admin!"""
texto_usuario_incorrecto ="""
Usuario incorrecto"""
texto_contraseña_incorrecta = """
Contraseña incorrecta"""
texto_no_usuario_ni_contraseña = """
Tu nombre de usuario y contraseña no están en nuestro sistema"""
texto_adios = "¡Hasta pronto!"
print("Accede con tu nombre de usuario y contraseña")
usuario_ingresado = input("Usuario: ")
contraseña_ingresada = input("Contraseña: ")

if usuario_ingresado != usuario_correcto and contraseña_ingresada != contraseña_correcta:
  print(texto_no_usuario_ni_contraseña)
  intento = 0
elif usuario_ingresado != usuario_correcto:
  print(texto_usuario_incorrecto)
  intento = 0
elif contraseña_ingresada != contraseña_correcta:
  print(texto_contraseña_incorrecta)
  intento = 0
elif usuario_ingresado == usuario_correcto and contraseña_ingresada == contraseña_correcta:
  print(texto_acceso)
  intento = 1
  
n_veces = 0

while intento == 0 and n_veces < 3:
  usuario_ingresado = input("Usuario: ")
  contraseña_ingresada = input("Contraseña: ")
  if usuario_ingresado == usuario_correcto and      contraseña_ingresada == contraseña_correcta:
    respuesta = print(texto_acceso)
    intento = 1
  elif usuario_ingresado != usuario_correcto and contraseña_ingresada != contraseña_correcta:
    n_veces += 1
    respuesta = print(texto_no_usuario_ni_contraseña)
    if n_veces < 3:
      print("Se agotaron tus intentos, vuelve más tarde")
  elif usuario_ingresado != usuario_correcto:
    n_veces += 1
    respuesta = print(texto_usuario_incorrecto)
    if n_veces < 3:
      print("Se agotaron tus intentos, vuelve más tarde")
  elif contraseña_ingresada != contraseña_correcta:
    n_veces += 1
    respuesta = print(texto_contraseña_incorrecta)


print(""" REPORTE MENSUAL DE LA ROTACIÓN DE PRODUCTOS DE LIFESTORE
""")

#vamos a contar las ventas de cada producto
cantidad_de_productos = len(lifestore_products)
ventas_de_prod = []
for x in lifestore_products:
    ventas_de_prod.append(0)
for venta in lifestore_sales:
  if venta[4] == 0:
    id_prod = venta[1]
    valor = ventas_de_prod[id_prod-1]
    valor = valor + 1
    ventas_de_prod[id_prod - 1] = valor

ventas_orden =sorted(ventas_de_prod)
top_5 = [ventas_orden[-1],ventas_orden[-2],ventas_orden[-3],ventas_orden[-4],ventas_orden[-5]]

masvendido1 = top_5[0]
masvendido2 = top_5[1]
masvendido3 = top_5[2]
masvendido4 = top_5[3]
masvendido5 = top_5[4]
index1 = ventas_de_prod.index(masvendido1) + 1
index2 = ventas_de_prod.index(masvendido2) + 1
index3 = ventas_de_prod.index(masvendido3) + 1
index4 = ventas_de_prod.index(masvendido4) + 1
index5 = ventas_de_prod.index(masvendido5) + 1
listamasvendidosid = [index1,index2,index3,index4,index5]

print("Los productos más vendidos son: ")
for nombre_de_prod1 in lifestore_products:
  if nombre_de_prod1[0] == index1:
    print(nombre_de_prod1[1][:20])
for nombre_de_prod2 in lifestore_products:
  if nombre_de_prod2[0] == index2:
    print(nombre_de_prod2[1][:15])
for nombre_de_prod3 in lifestore_products:
  if nombre_de_prod3[0] == index3:
    print(nombre_de_prod3[1][:15])
for nombre_de_prod4 in lifestore_products:
  if nombre_de_prod4[0] == index4:
    print(nombre_de_prod4[1][:15])
for nombre_de_prod5 in lifestore_products:
  if nombre_de_prod5[0] == index5:
    print(nombre_de_prod5[1][:15])    

#10 productos más buscados

cantidad_de_busquedas = len(lifestore_searches)
busquedas_de_productos = []
for i in lifestore_searches:
    busquedas_de_productos.append(0)

for busqueda in lifestore_searches:
  id_prod = busqueda[1]
  valor = busquedas_de_productos[id_prod-1]
  valor = valor + 1
  busquedas_de_productos[id_prod - 1] = valor
busquedas_orden =sorted(busquedas_de_productos)
top_10_busquedas = [busquedas_orden[-1],busquedas_orden[-2],busquedas_orden[-3],busquedas_orden[-4],busquedas_orden[-5],busquedas_orden[-6],busquedas_orden[-7],busquedas_orden[-8],busquedas_orden[-9],busquedas_orden[-10]]
masbuscado1 = top_10_busquedas[0]
masbuscado2 = top_10_busquedas[1]
masbuscado3 = top_10_busquedas[2]
masbuscado4 = top_10_busquedas[3]
masbuscado5 = top_10_busquedas[4]
masbuscado6 = top_10_busquedas[5]
masbuscado7 = top_10_busquedas[6]
masbuscado8 = top_10_busquedas[7]
masbuscado9 = top_10_busquedas[8]
masbuscado10 = top_10_busquedas[9]
indexa = busquedas_de_productos.index(masbuscado1) + 1
indexb = busquedas_de_productos.index(masbuscado2) + 1
indexc = busquedas_de_productos.index(masbuscado3) + 1
indexd = busquedas_de_productos.index(masbuscado4) + 1
indexe = busquedas_de_productos.index(masbuscado5) + 1
indexf = busquedas_de_productos.index(masbuscado6) + 1
indexg = busquedas_de_productos.index(masbuscado7) + 1
indexh = busquedas_de_productos.index(masbuscado8) + 1
indexi = busquedas_de_productos.index(masbuscado9) + 1
indexj = busquedas_de_productos.index(masbuscado10) + 1
ID_prod_categoría1 = [indexa, indexb,indexc,indexd,indexe,indexf,indexg,indexh,indexi,indexj]

print("""
Los productos más buscados son: """)
for nombre_prod_buscado1 in lifestore_products:
  if nombre_prod_buscado1[0] == indexa:
    print(nombre_prod_buscado1[1][:25], indexa)
for nombre_prod_buscado2 in lifestore_products:
  if nombre_prod_buscado2[0] == indexb:
    print(nombre_prod_buscado2[1][:25], indexb)
for nombre_prod_buscado3 in lifestore_products:
  if nombre_prod_buscado3[0] == indexc:
    print(nombre_prod_buscado3[1][:25], indexc)
for nombre_prod_buscado4 in lifestore_products:
  if nombre_prod_buscado4[0] == indexd:
    print(nombre_prod_buscado4[1][:25], indexd)
for nombre_prod_buscado5 in lifestore_products:
  if nombre_prod_buscado5[0] == indexe:
    print(nombre_prod_buscado5[1][:25], indexe)
for nombre_prod_buscado6 in lifestore_products:
  if nombre_prod_buscado6[0] == indexf:
    print(nombre_prod_buscado6[1][:25], indexf)
for nombre_prod_buscado7 in lifestore_products:
  if nombre_prod_buscado7[0] == indexg:
    print(nombre_prod_buscado7[1][:25], indexg)
for nombre_prod_buscado8 in lifestore_products:
  if nombre_prod_buscado8[0] == indexh:
    print(nombre_prod_buscado8[1][:25], indexh) 
for nombre_prod_buscado9 in lifestore_products:
  if nombre_prod_buscado9[0] == indexi:
    print(nombre_prod_buscado9[1][:25], indexi) 
for nombre_prod_buscado10 in lifestore_products:
  if nombre_prod_buscado10[0] == indexj and indexj != indexi:
    print(nombre_prod_buscado10[1][:25], indexj) 

print("""
___________________________________________________________________CATEGORIAS______________________________________________________________

""")
#vamos a hacer una lista que contenga el id, número de ventas, categoria, número de búsquedas de cada producto y nombre de cada producto.
id_de_cada_producto = []
ventas_de_cada_producto = []
categoria_de_cada_producto = []
busquedas_de_cada_producto = []
searches_de_cada_producto = []
nombre_de_cada_producto = []
for product in lifestore_products:
  idproduct = product[0]
  id_de_cada_producto.append(idproduct)
for ventaproduct in ventas_de_prod:
  numero_de_ventas = ventaproduct
  ventas_de_cada_producto.append(numero_de_ventas)
for catproductos in lifestore_products:
  cat_de_prod = catproductos[3]
  categoria_de_cada_producto.append(cat_de_prod)
for idbuscado in lifestore_searches:
  listadeidsbuscados = idbuscado[1]
  busquedas_de_cada_producto.append(listadeidsbuscados)
busquedasdeproducto = []
for x in lifestore_products:
    busquedasdeproducto.append(0)
for search in lifestore_searches:
    idprodbuscado = search[1]
    valor = busquedasdeproducto[idprodbuscado-1]
    valor = valor + 1
    busquedasdeproducto[idprodbuscado - 1] = valor
for name in lifestore_products:
  nameproduct = name[1]
  nombre_de_cada_producto.append(nameproduct[:len(lifestore_products)][:30])

valornuevo = 0
nuevalista = []
for repeticiones in id_de_cada_producto:
  idnuevo = id_de_cada_producto[valornuevo]
  ventasnuevo = ventas_de_cada_producto[valornuevo]
  categoriasnuevo = categoria_de_cada_producto[valornuevo]
  busquedasnuevo = busquedasdeproducto[valornuevo]
  nombrenuevo = nombre_de_cada_producto[valornuevo]
  elementosdelalistanueva = [idnuevo,ventasnuevo,categoriasnuevo,busquedasnuevo,nombrenuevo]
  nuevalista.append(elementosdelalistanueva)
  valornuevo += 1
#la nueva lista es [id del producto, ventas del producto, categoría del producto, busquedas del producto, nombre del producto]
######################   0                 1                      2                      3                        4           

#con las siguientes instrucciones vamos a sacar las categorías a las que pertenecen los productos de LifeStore
lista_de_categorias = []
for categorias in lifestore_products:
  lista_de_categorias.append(categorias[3])
listacategoriasunicas = []
for i in lista_de_categorias:
  if i not in listacategoriasunicas:
    listacategoriasunicas.append(i)
for a in range(0,len(listacategoriasunicas)):
  categorias_de_productos = listacategoriasunicas
#vamos el nombre de la categoría 1
categoria_1  = categorias_de_productos[0]
#vamos a sacar las ventas de cada producto de cada categoria
print(f"""
Los productos menos vendidos de la categoría {categoria_1} son:""")
idventas_prod_categoria1 = []
nventas_prod_categoria1 = []
#Vamos a sacar los ID de los productos de la categoría 1
valor1 = 0
for y in nuevalista:
  if y[2] == categoria_1:
    idventas_prod_categoria1.append(y[0]) 
#Estas son las ventas de los productos de la categoría 1
for y1 in idventas_prod_categoria1:
  if y1 == nuevalista[valor1][0]:
    añadir = nuevalista[valor1][1]
    nventas_prod_categoria1.append(añadir)
  valor1 += 1
#vamos a ordenar la lista de las ventas de los productos para sacar los productos menos ventidos
orden_nventas_prod_categoria1 = sorted(nventas_prod_categoria1)
#vamos a sacar el ID del top de productos menos vendidos
top1_ventas_categoria1 = orden_nventas_prod_categoria1[0]
top2_ventas_categoria1 = orden_nventas_prod_categoria1[1]
top3_ventas_categoria1 = orden_nventas_prod_categoria1[2]
top4_ventas_categoria1 = orden_nventas_prod_categoria1[3]
top5_ventas_categoria1 = orden_nventas_prod_categoria1[4]
#para sacar el ID del producto vamos a usar un index
indexventascat1 = nventas_prod_categoria1.index(top1_ventas_categoria1)
#ahora que tenemos el ID solo hay que buscar el nombre
for name in nuevalista:
  if name[0] == indexventascat1 + 1:
    nombredelworse1 = name[4]
    print(f"{nombredelworse1} con ID {name[0]}")
#para sacar el ID del producto vamos a usar un index
indexventascat1prod2 = nventas_prod_categoria1.index(top2_ventas_categoria1)
#ahora que tenemos el ID solo hay que buscar el nombre
for name2 in nuevalista:
  if name2[0] == indexventascat1prod2 + 1:
    nombredelworse2 = name2[4]
    print(f"{nombredelworse2} con ID {name2[0]}")
#para sacar el ID del producto vamos a usar un index
indexventascat1prod3 = nventas_prod_categoria1.index(top3_ventas_categoria1)
#ahora que tenemos el ID solo hay que buscar el nombre
for name3 in nuevalista:
  if name3[0] == indexventascat1prod3 + 1:
    nombredelworse3 = name3[4]
    print(f"{nombredelworse3} con ID {name3[0]}")
#para sacar el ID del producto vamos a usar un index
indexventascat1prod4 = nventas_prod_categoria1.index(top4_ventas_categoria1)
#ahora que tenemos el ID solo hay que buscar el nombre
for name4 in nuevalista:
  if name4[0] == indexventascat1prod4 + 1:
    nombredelworse4 = name4[4]
    print(f"{nombredelworse4} con ID {name4[0]}")
#para sacar el ID del producto vamos a usar un index
indexventascat1prod5 = nventas_prod_categoria1.index(top5_ventas_categoria1)
#ahora que tenemos el ID solo hay que buscar el nombre
for name5 in nuevalista:
  if name5[0] == indexventascat1prod5 + 1:
    nombredelworse5 = name5[4]
    print(f"{nombredelworse5} con ID {name5[0]}")

print(f"""
Los productos menos buscados de la categoría {categoria_1} son:""")
idbusquedas_prod_categoria1 = []
nbusquedas_prod_categoria1 = []
#Vamos a sacar los ID de los productos de la categoría 1
valor1 = 0
for y in nuevalista:
  if y[2] == categoria_1:
    idbusquedas_prod_categoria1.append(y[0]) 
#Estas son las busquedas de los productos de la categoría 1
for y1 in idbusquedas_prod_categoria1:
  if y1 == nuevalista[valor1][0]:
    añadir = nuevalista[valor1][3]
    nbusquedas_prod_categoria1.append(añadir)
  valor1 += 1
#vamos a ordenar la lista de las busquedas de los productos para sacar los productos menos ventidos
orden_nbusquedas_prod_categoria1 = sorted(nbusquedas_prod_categoria1)
#vamos a sacar el ID del top de productos menos vendidos
top1_busquedas_categoria1 = orden_nbusquedas_prod_categoria1[0]
top2_busquedas_categoria1 = orden_nbusquedas_prod_categoria1[1]
top3_busquedas_categoria1 = orden_nbusquedas_prod_categoria1[2]
top4_busquedas_categoria1 = orden_nbusquedas_prod_categoria1[3]
top5_busquedas_categoria1 = orden_nbusquedas_prod_categoria1[4]
#para sacar el ID del producto vamos a usar un index
indexbusquedacat1 = nbusquedas_prod_categoria1.index(top1_busquedas_categoria1)
#ahora que tenemos el ID solo hay que buscar el nombre
for name in nuevalista:
  if name[0] == indexbusquedacat1 + 1:
    nombredelworse1 = name[4]
    print(f"{nombredelworse1} con ID {name[0]}")
#para sacar el ID del producto vamos a usar un index
indexbusquedacat1prod2 = nbusquedas_prod_categoria1.index(top2_busquedas_categoria1)
#ahora que tenemos el ID solo hay que buscar el nombre
for name2 in nuevalista:
  if name2[0] == indexbusquedacat1prod2 + 1:
    nombredelworse2 = name2[4]
    print(f"{nombredelworse2} con ID {name2[0]}")
#para sacar el ID del producto vamos a usar un index
indexbusquedascat1prod3 = nbusquedas_prod_categoria1.index(top3_busquedas_categoria1)
#ahora que tenemos el ID solo hay que buscar el nombre
for name3 in nuevalista:
  if name3[0] == indexbusquedascat1prod3 + 1 and indexbusquedascat1prod3 + 1 != indexbusquedacat1prod2 + 1:
    nombredelworse3 = name3[4]
    print(f"{nombredelworse3} con ID {name3[0]}")
#para sacar el ID del producto vamos a usar un index
indexbusquedascat1prod4 = nbusquedas_prod_categoria1.index(top4_busquedas_categoria1)
#ahora que tenemos el ID solo hay que buscar el nombre
for name4 in nuevalista:
  if name4[0] == indexbusquedascat1prod4 + 1:
    nombredelworse4 = name4[4]
    print(f"{nombredelworse4} con ID {name4[0]}")
#para sacar el ID del producto vamos a usar un index
indexbusquedascat1prod5 = nbusquedas_prod_categoria1.index(top5_busquedas_categoria1)
#ahora que tenemos el ID solo hay que buscar el nombre
for name5 in nuevalista:
  if name5[0] == indexbusquedascat1prod5 + 1:
    nombredelworse5 = name5[4]
    print(f"{nombredelworse5} con ID {name5[0]}")

print("""
______________________________________RESEÑAS_______________________________
""")
#la nueva lista es [id del producto, ventas del producto, categoría del producto, busquedas del producto, nombre del producto, reseña del producto, fecha del producto]
######################   0                 1                      2                      3                        4                     5                   6
print("Los 5 productos con mejores reseñas son:")
#Para sacar las mejores reseñas vamos a sacar el promedio de reseña de cada producto
#vamos a sacar una lista de las reseñas de cada producto, luego vamos a promediar dichas reseñas, después vamos a agregar esos promedios a nuestra nueva lista para ordenarla de mayor a menor y encontrar el top de reseñas haciendo que el programa arroje el nombre de esos tops.
listadetodoslospromedios = []
listadereseñasdeproductos = []
for r in lifestore_sales:
    listadereseñasdeproductos.append([r[1],r[2]])
listadereseñasdeprod2 = []
idparareseñas = 1
count = 0
while count <= len(lifestore_products) - 1:
  for cosa in listadereseñasdeproductos:
    if cosa[0] == idparareseñas:
      listadereseñasdeprod2.append(cosa[1])
      suma = sum(listadereseñasdeprod2)
      promedio = suma/len(listadereseñasdeprod2)
  listadetodoslospromedios.append(promedio)
  idparareseñas += 1
  count += 1

#ahora que tenemos una lista con los promedios de todos los productos de LifeStore, vamos a agregarlos a nuestra nueva lista.
orden_listadetodoslospromedios = sorted(listadetodoslospromedios)
top1prodreseñas = orden_listadetodoslospromedios[-1]
top2prodreseñas = orden_listadetodoslospromedios[-2]
top3prodreseñas = orden_listadetodoslospromedios[-3]
top4prodreseñas = orden_listadetodoslospromedios[-4]
top5prodreseñas = orden_listadetodoslospromedios[-5]

indextop1 = listadetodoslospromedios.index(top1prodreseñas)
print(f"{nuevalista[indextop1][4]} con ID {nuevalista[indextop1][0]}")
indextop2 = listadetodoslospromedios.index(top2prodreseñas)
print(f"{nuevalista[indextop2][4]} con ID {nuevalista[indextop2][0]}")
indextop3 = listadetodoslospromedios.index(top3prodreseñas)
print(f"{nuevalista[indextop3][4]} con ID {nuevalista[indextop3][0]}")
indextop4 = listadetodoslospromedios.index(top4prodreseñas)
print(f"{nuevalista[indextop4][4]} con ID {nuevalista[indextop4][0]}")
indextop5 = listadetodoslospromedios.index(top5prodreseñas)
if indextop5 != indextop4:
  print(f"{nuevalista[indextop5][4]} con ID {nuevalista[indextop5][0]}")
print("""
""")
print("Los productos con las peores reseñas son")
worse1prodreseñas = orden_listadetodoslospromedios[0]
worse2prodreseñas = orden_listadetodoslospromedios[1]
worse3prodreseñas = orden_listadetodoslospromedios[2]
worse4prodreseñas = orden_listadetodoslospromedios[3]
worse5prodreseñas = orden_listadetodoslospromedios[4]

indextop1a = listadetodoslospromedios.index(worse1prodreseñas)
print(f"{nuevalista[indextop1a][4]} con ID {nuevalista[indextop1a][0]}")
indextop2a = listadetodoslospromedios.index(worse2prodreseñas)
print(f"{nuevalista[indextop2a][4]} con ID {nuevalista[indextop2a][0]}")
indextop3a = listadetodoslospromedios.index(worse3prodreseñas)
print(f"{nuevalista[indextop3a][4]} con ID {nuevalista[indextop3a][0]}")
indextop4a = listadetodoslospromedios.index(worse4prodreseñas)
print(f"{nuevalista[indextop4a][4]} con ID {nuevalista[indextop4a][0]}")
indextop5a = listadetodoslospromedios.index(worse5prodreseñas)
print(f"{nuevalista[indextop5a][4]} con ID {nuevalista[indextop5a][0]}")

print("___________________________Total de ingresos mensuales y ventas mensuales___________________________")
ventas_de_prodcondevoluciones = []
for x in lifestore_products:
    ventas_de_prodcondevoluciones.append(0)
for venta in lifestore_sales:
    id_prod = venta[1]
    valor = ventas_de_prodcondevoluciones[id_prod-1]
    valor = valor + 1
    ventas_de_prodcondevoluciones[id_prod - 1] = valor
valornuevo = 0
nuevalistacondevoluciones = []
for repeticiones in id_de_cada_producto:
  idnuevo = id_de_cada_producto[valornuevo]
  ventasnuevo = ventas_de_prodcondevoluciones[valornuevo]
  categoriasnuevo = categoria_de_cada_producto[valornuevo]
  busquedasnuevo = busquedasdeproducto[valornuevo]
  nombrenuevo = nombre_de_cada_producto[valornuevo]
  elementosdelalistanueva = [idnuevo,ventasnuevo,categoriasnuevo,busquedasnuevo,nombrenuevo]
  nuevalistacondevoluciones.append(elementosdelalistanueva)
  valornuevo += 1
ventas_en_enero = []
ventas_en_febrero = []
ventas_en_marzo = []
ventas_en_abril = []
ventas_en_mayo = []
ventas_en_junio = []
ventas_en_julio = []
ventas_en_agosto = []
ventas_en_septiembre = []
ventas_en_octubre = []
ventas_en_noviembre = []
ventas_en_diciembre = []

for t in lifestore_sales:
  if t[3][4:5] == "1":
    ventas_en_enero.append(t[1])
for t in lifestore_sales:
  if t[3][4:5] == "2":
    ventas_en_febrero.append(t[1])
for t in lifestore_sales:
  if t[3][4:5] == "3":
    ventas_en_marzo.append(t[1])
for t in lifestore_sales:
  if t[3][4:5] == "4":
    ventas_en_abril.append(t[1])
for t in lifestore_sales:
  if t[3][4:5] == "5":
    ventas_en_mayo.append(t[1])
for t in lifestore_sales:
  if t[3][4:5] == "6":
    ventas_en_junio.append(t[1])
for t in lifestore_sales:
  if t[3][4:5] == "7":
    ventas_en_julio.append(t[1])
for t in lifestore_sales:
  if t[3][4:5] == "8":
    ventas_en_agosto.append(t[1])
for t in lifestore_sales:
  if t[3][4:5] == "9":
    ventas_en_septiembre.append(t[1])
for t in lifestore_sales:
  if t[3][3:5] == "10":
    ventas_en_octubre.append(t[1])
for t in lifestore_sales:
  if t[3][3:5] == "11":
    ventas_en_noviembre.append(t[1])
for t in lifestore_sales:
  if t[3][3:5] == "12":
    ventas_en_diciembre.append(t[1])

#vamos a sacar la cantidad de ventas que hubo en cada mes
numero_ventas_en_enero = len(ventas_en_enero)
numero_ventas_en_febrero = len(ventas_en_febrero)
numero_ventas_en_marzo = len(ventas_en_marzo)
numero_ventas_en_abril = len(ventas_en_abril)
numero_ventas_en_mayo = len(ventas_en_mayo)
numero_ventas_en_junio = len(ventas_en_junio)
numero_ventas_en_julio = len(ventas_en_julio)
numero_ventas_en_agosto = len(ventas_en_agosto)
numero_ventas_en_septiembre = len(ventas_en_septiembre)
numero_ventas_en_octubre = len(ventas_en_octubre)
numero_ventas_en_noviembre = len(ventas_en_noviembre)
numero_ventas_en_diciembre = len(ventas_en_diciembre)

#ahora vamos a hacer una lista de las ids de los productos vendidos en cada mes y luego vamos a sacar el precio de cada id de esa lista. Sumamos esa nueva lista de precios para obtener los ingresos de cada mes
listadeingresosdecadaproductovendidoenenero = []
for elem in ventas_en_enero:
  iddeprods = elem
  preciodeprods = lifestore_products[elem-1][2]
  if elem == nuevalistacondevoluciones[elem-1][0]:
    listadeingresosdecadaproductovendidoenenero.append(lifestore_products[elem-1][2])
  ingresos_enero = sum(listadeingresosdecadaproductovendidoenenero)
print(f"En enero hubo {numero_ventas_en_enero} ventas y el ingreso mensual fue de {ingresos_enero} pesos")
listadeingresosdecadaproductovendidofebrero = []
for elem in ventas_en_febrero:
  iddeprods = elem
  preciodeprods = lifestore_products[elem-1][2]
  if elem == nuevalistacondevoluciones[elem-1][0]:
    listadeingresosdecadaproductovendidofebrero.append(lifestore_products[elem-1][2])
  ingresos_febrero = sum(listadeingresosdecadaproductovendidofebrero)
print(f"En febrero hubo {numero_ventas_en_febrero} ventas y el ingreso mensual fue de {ingresos_febrero} pesos")
listadeingresosdecadaproductovendidomarzo = []
for elem in ventas_en_marzo:
  iddeprods = elem
  preciodeprods = lifestore_products[elem-1][2]
  if elem == nuevalistacondevoluciones[elem-1][0]:
    listadeingresosdecadaproductovendidomarzo.append(lifestore_products[elem-1][2])
  ingresos_marzo = sum(listadeingresosdecadaproductovendidomarzo)
print(f"En marzo hubo {numero_ventas_en_marzo} ventas y el ingreso mensual fue de {ingresos_marzo} pesos")
listadeingresosdecadaproductovendidoabril = []
for elem in ventas_en_abril:
  iddeprods = elem
  preciodeprods = lifestore_products[elem-1][2]
  if elem == nuevalistacondevoluciones[elem-1][0]:
    listadeingresosdecadaproductovendidoabril.append(lifestore_products[elem-1][2])
  ingresos_abril = sum(listadeingresosdecadaproductovendidoabril)
print(f"En abril hubo {numero_ventas_en_abril} ventas y el ingreso mensual fue de {ingresos_abril} pesos")
listadeingresosdecadaproductovendidomayo = []
for elem in ventas_en_mayo:
  iddeprods = elem
  preciodeprods = lifestore_products[elem-1][2]
  if elem == nuevalistacondevoluciones[elem-1][0]:
    listadeingresosdecadaproductovendidomayo.append(lifestore_products[elem-1][2])
  ingresos_mayo = sum(listadeingresosdecadaproductovendidomayo)
print(f"En mayo hubo {numero_ventas_en_mayo} ventas y el ingreso mensual fue de {ingresos_mayo} pesos")
listadeingresosdecadaproductovendidojunio = []
for elem in ventas_en_junio:
  iddeprods = elem
  preciodeprods = lifestore_products[elem-1][2]
  if elem == nuevalistacondevoluciones[elem-1][0]:
    listadeingresosdecadaproductovendidojunio.append(lifestore_products[elem-1][2])
  ingresos_junio = sum(listadeingresosdecadaproductovendidojunio)
print(f"En junio hubo {numero_ventas_en_junio} ventas y el ingreso mensual fue de {ingresos_junio} pesos")
listadeingresosdecadaproductovendidojulio = []
for elem in ventas_en_julio:
  iddeprods = elem
  preciodeprods = lifestore_products[elem-1][2]
  if elem == nuevalistacondevoluciones[elem-1][0]:
    listadeingresosdecadaproductovendidojulio.append(lifestore_products[elem-1][2])
  ingresos_julio = sum(listadeingresosdecadaproductovendidojulio)
print(f"En julio hubo {numero_ventas_en_julio} ventas y el ingreso mensual fue de {ingresos_julio} pesos")
listadeingresosdecadaproductovendidoagosto = []
for elem in ventas_en_agosto:
  iddeprods = elem
  preciodeprods = lifestore_products[elem-1][2]
  if elem == nuevalistacondevoluciones[elem-1][0]:
    listadeingresosdecadaproductovendidoagosto.append(lifestore_products[elem-1][2])
  ingresos_agosto = sum(listadeingresosdecadaproductovendidoagosto)
print(f"En agosto hubo {numero_ventas_en_agosto} ventas y el ingreso mensual fue de {ingresos_agosto} pesos")
listadeingresosdecadaproductovendidoseptiembre = []
for elem in ventas_en_septiembre:
  iddeprods = elem
  preciodeprods = lifestore_products[elem-1][2]
  if elem == nuevalistacondevoluciones[elem-1][0]:
    listadeingresosdecadaproductovendidoseptiembre.append(lifestore_products[elem-1][2])
  ingresos_septiembre = sum(listadeingresosdecadaproductovendidoseptiembre)
print(f"En septiembre hubo {numero_ventas_en_septiembre} ventas y el ingreso mensual fue de {ingresos_septiembre} pesos")
listadeingresosdecadaproductovendidooctubre = []
for elem in ventas_en_septiembre:
  iddeprods = elem
  preciodeprods = lifestore_products[elem-1][2]
  if elem == nuevalistacondevoluciones[elem-1][0]:
    listadeingresosdecadaproductovendidooctubre.append(lifestore_products[elem-1][2])
  ingresos_octubre = sum(listadeingresosdecadaproductovendidooctubre)
  if numero_ventas_en_octubre != 0:
    print(f"En octubre hubo {numero_ventas_en_octubre} ventas y el ingreso mensual fue de {ingresos_octubre} pesos")
  else:
    print(f"En octubre no hubo ventas")
listadeingresosdecadaproductovendidoennoviembre = []
for elem in ventas_en_noviembre:
  iddeprods = elem
  preciodeprods = lifestore_products[elem-1][2]
  if elem == nuevalistacondevoluciones[elem-1][0]:
    listadeingresosdecadaproductovendidoennoviembre.append(lifestore_products[elem-1][2])
  ingresos_noviembre = sum(listadeingresosdecadaproductovendidoennoviembre)
  if numero_ventas_en_noviembre != 0:
    print(f"En noviembre hubo {numero_ventas_en_noviembre} ventas y el ingresso mensual fue de {ingresos_noviembre} pesos")
  else:
    print(f"En noviembre no hubo ventas")
listadeingresosdecadaproductovendidodiciembre = []
for elem in ventas_en_septiembre:
  iddeprods = elem
  preciodeprods = lifestore_products[elem-1][2]
  if elem == nuevalistacondevoluciones[elem-1][0]:
    listadeingresosdecadaproductovendidodiciembre.append(lifestore_products[elem-1][2])
  ingresos_diciembre = sum(listadeingresosdecadaproductovendidodiciembre)
  if numero_ventas_en_diciembre != 0:
    print(f"En diciembre hubo {numero_ventas_en_diciembre} ventas y el ingreso mensual fue de {ingresos_diciembre} pesos")
  else:
    print(f"En diciembre no hubo ventas")

print("___________________________Total de ingresos anuales y ventas anuales___________________________")

ventasen2019 = []
for sale in lifestore_sales:
  añodelaventa = sale[3][6:10]
  if añodelaventa == "2019":
    ventasen2019.append(sale[1])
listadepreciosdeproductosvendidosen2019 = []
for venta in ventasen2019:
  iddeventa = venta
  preciodeestaventa = lifestore_products[iddeventa-1][2]
  listadepreciosdeproductosvendidosen2019.append(preciodeestaventa)
  ingresosen2019 = sum(listadepreciosdeproductosvendidosen2019)
numerodeventasen2019 = len(ventasen2019)
print(f"En 2019 hubo {numerodeventasen2019} ventas y el ingreso fue de {ingresosen2019} pesos")

ventasen2020 = []
for sale in lifestore_sales:
  añodelaventa = sale[3][6:10]
  if añodelaventa == "2020":
    ventasen2020.append(sale[1])
listadepreciosdeproductosvendidosen2020 = []
for venta in ventasen2020:
  iddeventa = venta
  preciodeestaventa = lifestore_products[iddeventa-1][2]
  listadepreciosdeproductosvendidosen2020.append(preciodeestaventa)
  ingresosen2020 = sum(listadepreciosdeproductosvendidosen2020)
numerodeventasen2020 = len(ventasen2020)
print(f"En 2020 hubo {numerodeventasen2020} ventas y el ingreso fue de {ingresosen2020} pesos")

ventasen2002 = []
for sale in lifestore_sales:
  añodelaventa = sale[3][6:10]
  if añodelaventa == "2002":
    ventasen2002.append(sale[1])
listadepreciosdeproductosvendidosen2002 = []
for venta in ventasen2002:
  iddeventa = venta
  preciodeestaventa = lifestore_products[iddeventa-1][2]
  listadepreciosdeproductosvendidosen2002.append(preciodeestaventa)
  ingresosen2002 = sum(listadepreciosdeproductosvendidosen2002)
numerodeventasen2002 = len(ventasen2002)
print(f"En 2002 hubo {numerodeventasen2002} ventas y el ingreso fue de {ingresosen2002} pesos")

print("_____________Meses con más ventas al año________________")

#vamos a crear una lista con las ventas de cada mes agregando un decimal que nos ayude a identificar el mes al que pertenece esa cantidad de ventas.
listadeventasalmes = [[.01 + numero_ventas_en_enero], [.02  + numero_ventas_en_febrero], [.03 + numero_ventas_en_marzo], [.04 + numero_ventas_en_abril], [.05 + numero_ventas_en_mayo], [.06+ numero_ventas_en_junio], [.07 + numero_ventas_en_julio],[.08+numero_ventas_en_agosto],[.09+numero_ventas_en_septiembre],[.10 + numero_ventas_en_octubre],[.11 + numero_ventas_en_noviembre],[.12 + numero_ventas_en_diciembre]]
orden_listadeventasalmes = sorted(listadeventasalmes)
print("Los meses con más ventas al año son:")
mesconmasventas = orden_listadeventasalmes[11]
quemesesmesconmasventas = str(mesconmasventas)[3:6]
mesconmasventas2 = orden_listadeventasalmes[10]
quemesesmesconmasventas2 = str(mesconmasventas2)[3:6]
mesconmasventas3 = orden_listadeventasalmes[9]
quemesesmesconmasventas3 = str(mesconmasventas3)[3:6]
#vamos a sacar el mes con más ventas
if quemesesmesconmasventas == ".01":
  print("Enero")
elif quemesesmesconmasventas == ".02":
  print("Febrero")
elif quemesesmesconmasventas == ".03":
  print("Marzo")
elif quemesesmesconmasventas == ".04":
  print("Abril")
elif quemesesmesconmasventas == ".05":
  print("Mayo")
elif quemesesmesconmasventas == ".06":
  print("Junio")
elif quemesesmesconmasventas == ".07":
  print("Julio")
elif quemesesmesconmasventas == ".08":
  print("Agosto")
elif quemesesmesconmasventas == ".09":
  print("Septiembre")
elif quemesesmesconmasventas == ".10":
  print("Octubre")
elif quemesesmesconmasventas == ".11":
  print("Noviembre")
elif quemesesmesconmasventas == ".12":
  print("Diciembre")

#vamos a sacar el segundo mes con más ventas
if quemesesmesconmasventas2 == ".01":
  print("Enero")
elif quemesesmesconmasventas2 == ".02":
  print("Febrero")
elif quemesesmesconmasventas2 == ".03":
  print("Marzo")
elif quemesesmesconmasventas2 == ".04":
  print("Abril")
elif quemesesmesconmasventas2 == ".05":
  print("Mayo")
elif quemesesmesconmasventas2 == ".06":
  print("Junio")
elif quemesesmesconmasventas2 == ".07":
  print("Julio")
elif quemesesmesconmasventas2 == ".08":
  print("Agosto")
elif quemesesmesconmasventas2 == ".09":
  print("Septiembre")
elif quemesesmesconmasventas2 == ".10":
  print("Octubre")
elif quemesesmesconmasventas2 == ".11":
  print("Noviembre")
elif quemesesmesconmasventas2 == ".12":
  print("Diciembre")

#vamos a sacar el tercer mes con más ventas
if quemesesmesconmasventas3 == ".01":
  print("Enero")
elif quemesesmesconmasventas3 == ".02":
  print("Febrero")
elif quemesesmesconmasventas3 == ".03":
  print("Marzo")
elif quemesesmesconmasventas3 == ".04":
  print("Abril")
elif quemesesmesconmasventas3 == ".05":
  print("Mayo")
elif quemesesmesconmasventas3 == ".06":
  print("Junio")
elif quemesesmesconmasventas3 == ".07":
  print("Julio")
elif quemesesmesconmasventas3 == ".08":
  print("Agosto")
elif quemesesmesconmasventas3 == ".09":
  print("Septiembre")
elif quemesesmesconmasventas3 == ".10":
  print("Octubre")
elif quemesesmesconmasventas3 == ".11":
  print("Noviembre")
elif quemesesmesconmasventas3 == ".12":
  print("Diciembre")



  
