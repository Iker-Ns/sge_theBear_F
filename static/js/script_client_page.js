const API_URL = "api/clientes/";

function deleteClient(id) {
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
            await fetchClients();
        })
        .catch((error) => {
            console.error("Error al eliminar el cliente:", error);
        });
}

async function fetchClients() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const clients = await response.json();
        displayClients(clients);
    } catch (error) {
        console.error("Error al obtener los clientes:", error);
    }
}

function displayClients(clients) {
    const tableBody = document.querySelector("#clientTable tbody");
    tableBody.innerHTML = "";

    clients.Result.forEach((client) => {
        const row = document.createElement("tr");

        const idCell = document.createElement("td");
        idCell.textContent = client.id;
        row.appendChild(idCell);

        const nombreCell = document.createElement("td");
        nombreCell.textContent = client.nombre;
        row.appendChild(nombreCell);

        const apellidoCell = document.createElement("td");
        apellidoCell.textContent = client.apellido;
        row.appendChild(apellidoCell);

        const telefonoCell = document.createElement("td");
        telefonoCell.textContent = client.telefono;
        row.appendChild(telefonoCell);

        const restauranteCell = document.createElement("td");
        restauranteCell.textContent = client.restaurante_id;
        row.appendChild(restauranteCell);

        const actionsCell = document.createElement("td");
        actionsCell.id = "actionsCell";
        row.appendChild(actionsCell);

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Eliminar";
        deleteButton.classList.add("btn", "btn-danger");
        deleteButton.onclick = () => {
            if (confirm("¿Estás seguro de que deseas eliminar este cliente?")) {
                deleteClient(client.id);
            }
        };
        actionsCell.appendChild(deleteButton);

        const editButton = document.createElement("button");
        editButton.textContent = "Editar";
        editButton.classList.add("btn", "btn-primary");
        editButton.onclick = () => {
            editForm.reset();
            document.getElementById("editClientName").value = client.nombre;
            document.getElementById("editClientSurname").value = client.apellido;
            document.getElementById("editClientPhone").value = client.telefono;
            document.getElementById("editClientRestaurant").value = client.restaurante_id;
            document.getElementById("editClientId").value = client.id;
            editModal.style.display = "block";
        };
        actionsCell.appendChild(editButton);

        tableBody.appendChild(row);
    });
}

const editModal = document.getElementById("editClientModal");
const editSpanClose = document.getElementsByClassName("close")[1];
const editForm = document.getElementById("editClientForm");

editSpanClose.onclick = function () {
    editModal.style.display = "none";
};

editForm.onsubmit = async function (e) {
    e.preventDefault();

    const clientId = document.getElementById("editClientId").value;
    const clientData = {
        id: clientId,
        nombre: document.getElementById("editClientName").value,
        apellido: document.getElementById("editClientSurname").value,
        telefono: document.getElementById("editClientPhone").value,
        restaurante_id: parseInt(document.getElementById("editClientRestaurant").value),
    };

    try {
        const response = await fetch(`${API_URL}${clientId}/`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(clientData),
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }

        editModal.style.display = "none";
        await fetchClients();
    } catch (error) {
        console.error("Error al guardar:", error);
    }
};

const addModal = document.getElementById("addClientModal");
const addBtnAdd = document.getElementById("add-new");
const addSpanClose = document.getElementsByClassName("close")[0];
const addForm = document.getElementById("addClientForm");

addBtnAdd.onclick = function () {
    addModal.style.display = "block";
    addForm.reset();
    document.getElementById("addClientId").value = "";
};

addSpanClose.onclick = function () {
    addModal.style.display = "none";
};

addForm.onsubmit = async function (e) {
    e.preventDefault();

    const clientData = {
        nombre: document.getElementById("addClientName").value,
        apellido: document.getElementById("addClientSurname").value,
        telefono: document.getElementById("addClientPhone").value,
        restaurante_id: parseInt(document.getElementById("addClientRestaurant").value),
    };

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(clientData),
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }

        addModal.style.display = "none";
        await fetchClients();
    } catch (error) {
        console.error("Error al guardar:", error);
    }
};

document.addEventListener("DOMContentLoaded", fetchClients);