import json


# =====================================
# CARGAR PRODUCTOS
# =====================================

with open("datos/productos.json", "r", encoding="utf-8") as archivo:

    PRODUCTOS = json.load(archivo)["productos"]


# =====================================
# BUSCAR PRODUCTO
# =====================================

def buscar_producto(nombre):

    nombre = nombre.lower()

    for producto in PRODUCTOS:

        if producto["nombre"].lower() in nombre:

            return producto

    return None


# =====================================
# BUSCAR CATEGORIA
# =====================================

def buscar_categoria(texto):

    texto = texto.lower()

    resultados = []

    for producto in PRODUCTOS:

        if producto["categoria"].lower() in texto:

            resultados.append(producto)

    return resultados


# =====================================
# LISTAR TODO
# =====================================

def listar_productos():

    return PRODUCTOS