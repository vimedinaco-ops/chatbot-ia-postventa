from chatbot import responder
from modelos.modelo_ml import predecir


def procesar_consulta(mensaje):
    """
    Procesa el mensaje del usuario.

    Si el modelo de Machine Learning está disponible,
    utiliza la intención predicha.

    Si aún no existe el modelo, utiliza las reglas
    del chatbot actual.
    """

    # Intentar obtener intención mediante Machine Learning
    intencion = predecir(mensaje)

    # Si todavía no hay modelo entrenado
    if intencion is None:
        return responder(mensaje)

    # ==================================================
    # AQUÍ MÁS ADELANTE USAREMOS EL DISPATCHER
    # ==================================================
    # Por ahora seguimos utilizando el chatbot basado
    # en reglas para generar la respuesta.
    # Cuando esté listo el modelo de Luis,
    # reemplazaremos esta parte por el Dispatcher.
    # ==================================================

    return responder(mensaje)