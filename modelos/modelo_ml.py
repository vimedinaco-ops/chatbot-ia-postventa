import os
import joblib

# ==========================================
# VARIABLES GLOBALES
# ==========================================

modelo = None
vectorizador = None


# ==========================================
# CARGAR MODELO
# ==========================================

def cargar_modelo():

    global modelo, vectorizador

    ruta_modelo = "modelos/modelo.pkl"
    ruta_vectorizador = "modelos/tfidf.pkl"

    if os.path.exists(ruta_modelo) and os.path.exists(ruta_vectorizador):

        try:

            modelo = joblib.load(ruta_modelo)
            vectorizador = joblib.load(ruta_vectorizador)

            print("✅ Modelo de Machine Learning cargado correctamente.")

        except Exception as e:

            print(f"❌ Error al cargar el modelo: {e}")

            modelo = None
            vectorizador = None

    else:

        print("⚠ Modelo todavía no disponible.")


# ==========================================
# PREDECIR INTENCIÓN
# ==========================================

def predecir(texto):

    if modelo is None or vectorizador is None:
        return None

    vector = vectorizador.transform([texto])

    prediccion = modelo.predict(vector)

    return prediccion[0]