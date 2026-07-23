from flask import Flask, render_template, request, jsonify

from motor import procesar_consulta
from modelos.modelo_ml import cargar_modelo

app = Flask(__name__)

# ==========================================
# CARGAR MODELO DE MACHINE LEARNING
# ==========================================

try:
    cargar_modelo()
    print("✅ Modelo cargado correctamente.")
except Exception as e:
    print(f"⚠️ No se pudo cargar el modelo: {e}")

# ==========================================
# PÁGINA PRINCIPAL
# ==========================================

@app.route("/")
def inicio():
    return render_template("index.html")


# ==========================================
# CHAT
# ==========================================

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data:
        return jsonify({"respuesta": "No se recibió ningún mensaje."})

    mensaje = data.get("mensaje", "").strip()

    if mensaje == "":
        return jsonify({"respuesta": "Escribe una consulta."})

    respuesta = procesar_consulta(mensaje)

    return jsonify(respuesta)


# ==========================================
# INICIAR SERVIDOR
# ==========================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)