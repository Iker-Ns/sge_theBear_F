const API_URL = "api/existencias/";

function deleteExistencia(id) {
    fetch(`${API_URL}${id}/`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        return response.json();
    })
    .then(async () => {
        await fetchExistencias();
    })
    .catch((error) => {
        console.error("Error al eliminar la existencia:", error);
    });
}

async function fetchExistencias() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const existencias = await response.json();
        displayExistencias(existencias);
    } catch (error) {
        console.error("Error al obtener las existencias:", error);
    }
}

function displayExistencias(existencias) {
    const tableBody = document.querySelector("#existenciasTable tbody");
    tableBody.innerHTML = "";

    existencias.Result.forEach((existencia) => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${existencia.id}</td>
            <td>${existencia.nombre}</td>
            <td>${existencia.descripcion}</td>
            <td>${existencia.cantidad}</td>
        `;

        const actionsCell = document.createElement("td");
        actionsCell.id = "actionsCell";

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Eliminar";
        deleteButton.classList.add("btn", "btn-danger");
        deleteButton.onclick = () => {
            if (confirm("¿Estás seguro de que deseas eliminar esta existencia?")) {
                deleteExistencia(existencia.id);
            }
        };

        const editButton = document.createElement("button");
        editButton.textContent = "Editar";
        editButton.classList.add("btn", "btn-primary");
        editButton.onclick = () => {
            editForm.reset();
            document.getElementById("editExistenciaId").value = existencia.id;
            document.getElementById("editExistenciaNombre").value = existencia.nombre;
            document.getElementById("editExistenciaDescripcion").value = existencia.descripcion;
            document.getElementById("editExistenciaCantidad").value = existencia.cantidad;
            editModal.style.display = "block";
        };

        actionsCell.appendChild(editButton);
        actionsCell.appendChild(deleteButton);
        row.appendChild(actionsCell);
        tableBody.appendChild(row);
    });
}

const editModal = document.getElementById("editExistenciaModal");
const editSpanClose = document.getElementsByClassName("close")[1];
const editForm = document.getElementById("editExistenciaForm");

editSpanClose.onclick = function() {
    editModal.style.display = "none";
};

editForm.onsubmit = async function (e) {
    e.preventDefault();

    const existenciaId = document.getElementById("editExistenciaId").value;
    const existenciaData = {
        id: existenciaId,
        nombre: document.getElementById("editExistenciaNombre").value,
        descripcion: document.getElementById("editExistenciaDescripcion").value,
        cantidad: document.getElementById("editExistenciaCantidad").value,
    };

    try {
        const response = await fetch(`${API_URL}${existenciaId}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(existenciaData)
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }

        editModal.style.display = "none";
        await fetchExistencias();
    } catch (error) {
        console.error("Error al guardar:", error);
    }
};

const addModal = document.getElementById("addExistenciaModal");
const addBtnAdd = document.getElementById("add-new");
const addSpanClose = document.getElementsByClassName("close")[0];
const addForm = document.getElementById("addExistenciaForm");

addBtnAdd.onclick = function () {
    addModal.style.display = "block";
    addForm.reset();
    document.getElementById("addExistenciaId").value = "";
};

addSpanClose.onclick = function () {
    addModal.style.display = "none";
};

addForm.onsubmit = async function (e) {
    e.preventDefault();

    const existenciaData = {
        nombre: document.getElementById("addExistenciaNombre").value,
        descripcion: document.getElementById("addExistenciaDescripcion").value,
        cantidad: document.getElementById("addExistenciaCantidad").value,
    };

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(existenciaData)
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }

        addModal.style.display = "none";
        await fetchExistencias();
    } catch (error) {
        console.error("Error al guardar:", error);
    }
};

document.addEventListener("DOMContentLoaded", fetchExistencias);
