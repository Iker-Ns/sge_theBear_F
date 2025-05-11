const API_URL = "api/trabajador/";

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

    // Cargar trabajadores al iniciar
    fetch("/trabajadores")
        .then(res => res.json())
        .then(data => {
            const trabajadores = data.Result || [];
            trabajadores.forEach(t => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${t.id}</td>
                    <td>${t.seguridad_social}</td>
                    <td>${t.nombre}</td>
                    <td>${t.apellido}</td>
                    <td>${t.cargo}</td>
                    <td>${t.id_restaurante}</td>
                `;
                tableBody.appendChild(row);
            });
        });

    // Enviar nuevo trabajador
    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const trabajador = Object.fromEntries(formData.entries());

        // Forzamos el ID a 0 o null ya que el backend lo ignora si es autoincremental
        trabajador.id = 0;

        const res = await fetch("/trabajadores", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(trabajador)
        });

        const result = await res.json();
        alert("Treballador afegit!");

        location.reload(); // Recargar per mostrar el nou
    });
});
