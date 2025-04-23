// Agregar nueva sugerencia
document
  .getElementById("addSuggestionForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const suggestion = document.getElementById("suggestion").value;
    const data = { sugerecia: suggestion }; // Notar la clave "sugerecia" acorde al backend

    fetch("/sugerecia", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
        // Agregar la nueva sugerencia a la lista sin recargar la página
        const ul = document.querySelector(".task-list");
        const li = document.createElement("li");
        li.classList.add("task-item");
        li.id = suggestion;
        li.innerHTML = `<span>${suggestion}</span>
          <div class="task-actions">
            <button class="btn btn-edit" onclick="editSuggestion('${suggestion}')">Editar</button>
            <button class="btn btn-delete" onclick="deleteSuggestion('${suggestion}')">Eliminar</button>
          </div>`;
        ul.appendChild(li);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });

// Eliminar sugerencia
function deleteSuggestion(suggestion) {
  fetch("/sugerecias", {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ sugerencia: suggestion }), // Enviamos la clave "sugerencia"
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
      // Eliminar la sugerencia de la lista sin recargar la página
      document.getElementById(suggestion).remove();
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

// Editar sugerencia
function editSuggestion(suggestion) {
  const newSuggestion = prompt("Ingresa la nueva sugerencia:", suggestion);
  if (newSuggestion && newSuggestion !== suggestion) {
    fetch("/sugerencias", {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ old: suggestion, new: newSuggestion }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
        // Actualizar el texto de la sugerencia sin recargar la página
        const suggestionItem = document.getElementById(suggestion);
        suggestionItem.querySelector("span").textContent = newSuggestion;
        // Actualizamos también el id y el onclick de los botones para reflejar el cambio
        suggestionItem.id = newSuggestion;
        suggestionItem
          .querySelector(".btn-edit")
          .setAttribute("onclick", `editSuggestion('${newSuggestion}')`);
        suggestionItem
          .querySelector(".btn-delete")
          .setAttribute("onclick", `deleteSuggestion('${newSuggestion}')`);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
}