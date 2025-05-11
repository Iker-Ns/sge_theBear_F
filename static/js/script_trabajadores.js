const API_URL = "api/trabajadores/";

document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("addTrabajadorModal");
    const btn = document.getElementById("addTrabajadorBtn");
    const span = modal.querySelector(".close");
    const form = document.getElementById("addTrabajadorForm");
    const tableBody = document.querySelector("#trabajadoresTable tbody");

    // Mostrar modal
    btn.onclick = () => modal.style.display = "block";
    span.onclick = () => modal.style.display = "none";
    window.onclick = (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    };

    function loadTrabajadores() {
        fetch(API_URL)
            .then(res => res.json())
            .then(data => {
                const trabajadores = data.Result || [];
                tableBody.innerHTML = ""; // Limpiar tabla antes de cargar

                trabajadores.forEach(t => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${t.id}</td>
                        <td>${t.seguridad_social}</td>
                        <td>${t.nombre}</td>
                        <td>${t.apellido}</td>
                        <td>${t.cargo}</td>
                        <td>${t.restaurante.nombre} (${t.restaurante.id})</td>
                    `;
                    const deleteBtn = document.createElement("button");
                    deleteBtn.classList.add("btn", "btn-danger");
                    deleteBtn.innerText = "Eliminar";
                    deleteBtn.addEventListener("click", (e) => {
                        const row = e.target.closest("tr");
                        const id = row.querySelector("td").innerText;
                        deleteTrabajador(id);
                    });
                    const actionsCell = document.createElement("td");
                    actionsCell.appendChild(deleteBtn);
                    row.appendChild(actionsCell);
                    tableBody.appendChild(row);
                });
            });
    }

    const deleteButtons = document.querySelectorAll(".btn-danger");
    deleteButtons.forEach(button => {
        button.addEventListener("click", (e) => {
            const row = e.target.closest("tr");
            const id = row.querySelector("td").innerText;
            deleteTrabajador(id);
        });
    });

    function deleteTrabajador(id) {
        if (confirm("¿Estás seguro de que deseas eliminar este trabajador?")) {
            fetch(`${API_URL}${id}`, { method: "DELETE" })
                .then(res => res.json())
                .then(data => {
                    loadTrabajadores();
                });
        }
    }

    loadTrabajadores();

    // Enviar nuevo trabajador
    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const trabajador = {
            seguridad_social: formData.get("seguridad_social"),
            nombre: formData.get("nombre"),
            apellido: formData.get("apellido"),
            cargo: formData.get("cargo"),
            id_restaurante: formData.get("id_restaurante")
        }

        const res = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(trabajador)
        });

        const result = await res.json();
        loadTrabajadores();
    });
});
