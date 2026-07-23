// ======================================
// NEXBOT SOLUTIONS - CHATBOT
// ======================================

const chatButton = document.getElementById("chatButton");
const abrirChat = document.getElementById("abrirChat");
const cerrarChat = document.getElementById("cerrarChat");

const chatContainer = document.getElementById("chatContainer");
const chatMessages = document.getElementById("chatMessages");

const input = document.getElementById("mensaje");
const botonEnviar = document.getElementById("enviar");

// ===============================
// ABRIR CHAT
// ===============================

function abrirVentana() {

    chatContainer.style.display = "flex";

    input.focus();

}

chatButton.addEventListener("click", abrirVentana);

abrirChat.addEventListener("click", abrirVentana);

// ===============================
// CERRAR CHAT
// ===============================

cerrarChat.addEventListener("click", () => {

    chatContainer.style.display = "none";

});

// ===============================
// AGREGAR MENSAJE
// ===============================

function agregarMensaje(texto, tipo) {

    const mensaje = document.createElement("div");

    mensaje.className = tipo;

    const hora = new Date().toLocaleTimeString([], {

        hour: "2-digit",
        minute: "2-digit"

    });

    mensaje.innerHTML = `
        <p>${texto.replace(/\n/g, "<br>")}</p>
        <small>${hora}</small>
    `;

    chatMessages.appendChild(mensaje);

    chatMessages.scrollTop = chatMessages.scrollHeight;

}

// ===============================
// ENVIAR MENSAJE
// ===============================

async function enviarMensaje() {

    const texto = input.value.trim();

    if(texto==="") return;

    agregarMensaje(texto,"usuario");

    input.value="";

    const esperando=document.createElement("div");

    esperando.className="bot";

    esperando.id="esperando";

    esperando.innerHTML="<p>🤖 Escribiendo...</p>";

    chatMessages.appendChild(esperando);

    chatMessages.scrollTop=chatMessages.scrollHeight;

    try{

        const respuesta=await fetch("/chat",{

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify({

                mensaje:texto

            })

        });

        const datos=await respuesta.json();

        document.getElementById("esperando").remove();

        agregarMensaje(datos.respuesta,"bot");

    }

    catch(error){

        document.getElementById("esperando").remove();

        agregarMensaje("❌ Error al conectar con el servidor.","bot");

    }

}

botonEnviar.addEventListener("click",enviarMensaje);

input.addEventListener("keypress",function(e){

    if(e.key==="Enter"){

        enviarMensaje();

    }

});