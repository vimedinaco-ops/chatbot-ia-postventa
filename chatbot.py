import json
from catalogo import buscar_producto, buscar_categoria

# ==========================================
# CARGAR FAQ
# ==========================================

with open("datos/faq.json", "r", encoding="utf-8") as archivo:
    faq = json.load(archivo)

# ==========================================
# CARGAR PEDIDOS
# ==========================================

with open("datos/pedidos.json", "r", encoding="utf-8") as archivo:
    pedidos = json.load(archivo)


# ==========================================
# FUNCIONES DE RESPUESTA
# ==========================================

def responder_saludo(mensaje):
    return {"respuesta": faq["saludo"]}


def responder_producto(mensaje):

    producto = buscar_producto(mensaje)

    if producto:

        return {
            "respuesta":
f"""📦 Producto encontrado

Nombre: {producto['nombre']}

Categoría: {producto['categoria']}

Descripción:
{producto['descripcion']}

Precio: S/. {producto['precio']}

Stock disponible: {producto['stock']} unidades"""
        }

    return None


def responder_categoria(mensaje):

    productos = buscar_categoria(mensaje)

    if productos:

        lista = "\n".join([f"• {p['nombre']}" for p in productos])

        return {
            "respuesta":
f"""📂 Productos encontrados

{lista}"""
        }

    return None


def responder_pedido(mensaje):

    if "pedido" in mensaje.lower():

        return {
            "respuesta":
            "📦 Indícame el código del pedido.\nEjemplo: PED001"
        }

    if mensaje.upper().startswith("PED"):

        codigo = mensaje.upper()

        if codigo in pedidos:

            pedido = pedidos[codigo]

            return {
                "respuesta":
f"""✅ Pedido encontrado

👤 Cliente: {pedido['cliente']}

💻 Producto: {pedido['producto']}

📦 Estado: {pedido['estado']}

🚚 Transportista: {pedido['transportista']}

📅 Fecha: {pedido['fecha']}"""
            }

        return {"respuesta": "❌ No existe ese pedido."}

    return None


def responder_garantia(mensaje):
    return {"respuesta": faq["garantia"]}


def responder_factura(mensaje):
    return {"respuesta": faq["factura"]}


def responder_contacto(mensaje):
    return {"respuesta": faq["contacto"]}


def responder_horario(mensaje):
    return {"respuesta": faq["horario"]}


def responder_despedida(mensaje):
    return {"respuesta": faq["despedida"]}


# ==========================================
# DISPATCHER
# ==========================================

ACCIONES = {
    "SALUDO": responder_saludo,
    "PRODUCTO": responder_producto,
    "CATEGORIA": responder_categoria,
    "PEDIDO": responder_pedido,
    "GARANTIA": responder_garantia,
    "FACTURA": responder_factura,
    "CONTACTO": responder_contacto,
    "HORARIO": responder_horario,
    "DESPEDIDA": responder_despedida
}


# ==========================================
# CHATBOT
# ==========================================

def responder(mensaje):

    mensaje_lower = mensaje.lower().strip()

    if mensaje_lower in ["hola", "buenas", "buenos dias", "buenas tardes", "hello"]:
        return ACCIONES["SALUDO"](mensaje)

    if buscar_producto(mensaje):
        return ACCIONES["PRODUCTO"](mensaje)

    if buscar_categoria(mensaje):
        return ACCIONES["CATEGORIA"](mensaje)

    if "pedido" in mensaje_lower or mensaje.upper().startswith("PED"):
        return ACCIONES["PEDIDO"](mensaje)

    if "garantia" in mensaje_lower or "garantía" in mensaje_lower:
        return ACCIONES["GARANTIA"](mensaje)

    if "factura" in mensaje_lower:
        return ACCIONES["FACTURA"](mensaje)

    if "contacto" in mensaje_lower:
        return ACCIONES["CONTACTO"](mensaje)

    if "horario" in mensaje_lower:
        return ACCIONES["HORARIO"](mensaje)

    if mensaje_lower in [
        "gracias",
        "muchas gracias",
        "adios",
        "adiós",
        "hasta luego"
    ]:
        return ACCIONES["DESPEDIDA"](mensaje)

    return {"respuesta": faq["desconocido"]}