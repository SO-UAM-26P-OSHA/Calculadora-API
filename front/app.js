const formulario = document.getElementById("formulario");
const campoA = document.getElementById("a");
const campoB = document.getElementById("b");
const campoOperacion = document.getElementById("operacion");
const resultado = document.getElementById("resultado");

const API_URL = "http://localhost:8000/api";

formulario.addEventListener("submit", async function (event) {
  event.preventDefault();

  const a = campoA.value;
  const b = campoB.value;
  const operacion = campoOperacion.value;

  let respuesta;

  if (operacion === "power" || operacion === "sqrt" || operacion === "calcular_abs") {
    
    respuesta = await fetch(`${API_URL}/${operacion}`, {
      method: "POST", 
      headers: {
        "Content-Type": "application/json" 
      },
      body: JSON.stringify({ 
        a: Number(a), 
        b: Number(b) 
      })
    });

  } else {
    
    const url_get = `${API_URL}/${operacion}?a=${a}&b=${b}`; 
    respuesta = await fetch(url_get); 
    
  }

  try {
    const datos = await respuesta.json(); //

    if (datos.error) { 
      resultado.textContent = `Error: ${datos.error}`; 
    } else {
      resultado.textContent = `Resultado: ${datos.resultado}`; 
    }
  } catch (error) { 
    resultado.textContent = "No fue posible conectar con la API."; 
  }
}); 