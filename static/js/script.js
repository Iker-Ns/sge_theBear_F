// URL del endpoint de la API
const API_URL = "http://localhost:8000/users/read/";

// Función para obtener los datos de los usuarios
async function fetchUsers() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const users = await response.json(); // Convertimos la respuesta a JSON
        displayUsers(users); // Mostramos los datos en la tabla
        //console.log(users)
    } catch (error) {
        console.error("Error al obtener los usuarios:", error);
    }
}

// Función para mostrar los usuarios en la tabla
function displayUsers(users) {
    const tableBody = document.querySelector("#usersTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de usuarios y creamos las filas de la tabla
    users.forEach(user => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del usuario
        const idCell = document.createElement("td");
        idCell.textContent = user.user.id;
        row.appendChild(idCell);

        const nameCell = document.createElement("td");
        nameCell.textContent = user.user.name;
        row.appendChild(nameCell);

        const emailCell = document.createElement("td");
        emailCell.textContent = user.user.email;
        row.appendChild(emailCell);

        const ageCell = document.createElement("td");
        ageCell.textContent = user.user.age;
        row.appendChild(ageCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los usuarios cuando la página se carga
//document.addEventListener("DOMContentLoaded", fetchUsers);