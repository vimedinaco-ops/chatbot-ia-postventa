# 🤖 NEXBOT Solutions - Chatbot IA para Atención Postventa

## 📌 Descripción

NEXBOT Solutions es un chatbot inteligente desarrollado como proyecto académico del curso de Machine Learning. Su objetivo es automatizar la atención postventa de los clientes mediante el uso de procesamiento de lenguaje natural y técnicas de aprendizaje automático.

Actualmente el sistema funciona mediante reglas e intenciones predefinidas y está preparado para integrar un modelo de Machine Learning entrenado con Scikit-Learn.

---

## 🎯 Objetivos

- Automatizar la atención postventa.
- Consultar el estado de pedidos.
- Mostrar información de productos.
- Mostrar productos por categoría.
- Responder preguntas frecuentes.
- Integrar un modelo de Machine Learning para detectar intenciones.

---

## 🛠 Tecnologías utilizadas

- Python 3
- Flask
- Scikit-Learn
- HTML5
- CSS3
- JavaScript
- JSON
- Joblib
- Render
- GitHub

---

## 📂 Estructura del proyecto

```
CHATBOT-IA-POSTVENTA
│
├── datos/
│   ├── faq.json
│   ├── intenciones.json
│   ├── pedidos.json
│   └── productos.json
│
├── modelos/
│   └── modelo_ml.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── img/
│
├── templates/
│   └── index.html
│
├── app.py
├── chatbot.py
├── catalogo.py
├── intenciones.py
├── motor.py
├── requirements.txt
└── README.md
```

---

## 🚀 Funcionalidades

- Chat interactivo.
- Consulta de pedidos.
- Consulta de productos.
- Consulta por categorías.
- Información sobre garantía.
- Información sobre facturación.
- Información de contacto.
- Arquitectura preparada para Machine Learning.

---

## ▶ Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar al proyecto:

```bash
cd CHATBOT-IA-POSTVENTA
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:

```bash
python app.py
```

Abrir en el navegador:

```
http://127.0.0.1:5000
```

---

## 🤖 Integración con Machine Learning

El sistema está preparado para utilizar un modelo entrenado mediante Scikit-Learn.

Cuando los archivos:

- modelo.pkl
- tfidf.pkl

se encuentren dentro de la carpeta:

```
modelos/
```

el chatbot utilizará automáticamente el modelo para detectar la intención del usuario.

---

## 👨‍💻 Autores

Proyecto desarrollado para el curso de Machine Learning.

NEXBOT Solutions