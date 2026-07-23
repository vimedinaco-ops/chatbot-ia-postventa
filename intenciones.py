import json

# ==========================================
# CARGAR INTENCIONES
# ==========================================

with open("datos/intenciones.json", "r", encoding="utf-8") as archivo:
    INTENCIONES = json.load(archivo)


# ==========================================
# DETECTAR INTENCIÓN
# ==========================================

def detectar_intencion(mensaje):

    mensaje = mensaje.lower().strip()

    for intencion, palabras in INTENCIONES.items():

        for palabra in palabras:

            if palabra.lower() in mensaje:
                return intencion

    # Si el usuario escribe un código de pedido
    if mensaje.upper().startswith("PED"):
        return "PEDIDO"

    return "DESCONOCIDO"