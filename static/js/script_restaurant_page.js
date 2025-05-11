const API_URL = "api/restaurantes/";

function deleteRestaurant(id) {
    fetch(
        `${API_URL}${id}/`,
        {
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
            await fetchRestaurants();
        })
        .catch((error) => {
            console.error("Error al eliminar el restaurante:", error);
        })
}

async function fetchRestaurants() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const restaurants = await response.json();
        displayRestaurants(restaurants);
    } catch (error) {
        console.error("Error al obtener los restaurantes:", error);
    }
}

async function fetchRestaurant(id) {
    try {
        const response = await fetch(`${API_URL}${id}/`);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const restaurant = await response.json();
        return restaurant;
    } catch (error) {
        console.error("Error al obtener el restaurante:", error);
        return null;
    }
}

function clearTable() {
    const tableBody = document.querySelector("#restaurantTable tbody");
    tableBody.innerHTML = "";
}

function displayRestaurants(restaurants) {
    const tableBody = document.querySelector("#restaurantTable tbody");
    console.log(restaurants)
    tableBody.innerHTML = "";

    restaurants.Result.forEach((restaurant) => {
        const row = document.createElement("tr");

        const idCell = document.createElement("td");
        idCell.textContent = restaurant.id
        row.appendChild(idCell);

        const nombreCell = document.createElement("td");
        nombreCell.textContent = restaurant.nombre;
        row.appendChild(nombreCell);

        const direccionCell = document.createElement("td");
        direccionCell.textContent = restaurant.direccion;
        row.appendChild(direccionCell);

        const codigoPostalCell = document.createElement("td");
        codigoPostalCell.textContent = restaurant.codigo_postal;
        row.appendChild(codigoPostalCell);

        const actionsCell = document.createElement("td");
        actionsCell.id = "actionsCell";
        row.appendChild(actionsCell);

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Eliminar";
        deleteButton.classList.add("btn", "btn-danger");
        deleteButton.onclick = () => {
            if (confirm("¿Estás seguro de que deseas eliminar este restaurante?")) {
                deleteRestaurant(restaurant.id);
            }
        }
        actionsCell.appendChild(deleteButton);

        tableBody.appendChild(row);

        const editButton = document.createElement("button");
        editButton.textContent = "Editar";
        editButton.classList.add("btn", "btn-primary");

        editButton.onclick = () => {
            editForm.reset();
            document.getElementById("editRestaurantName").value = restaurant.nombre;
            document.getElementById("editRestaurantAddress").value = restaurant.direccion;
            document.getElementById("editRestaurantPostalCode").value = restaurant.codigo_postal;
            document.getElementById("editRestaurantId").value = restaurant.id;
            editModal.style.display = "block";
        }
        actionsCell.appendChild(editButton);
    })
}

const editModal = document.getElementById("editRestaurantModal");
const editSpanClose = document.getElementsByClassName("close")[1];
const editForm = document.getElementById("editRestaurantForm");

editSpanClose.onclick = function() {
    editModal.style.display = "none";
}

editForm.onsubmit = async function(e) {
    e.preventDefault();

    const errorLabel = document.getElementById("editErrorLabelPostalCode");
    const postalCode = document.getElementById("editRestaurantPostalCode").value;
    const postalCodeRegex = /^[0-9]{5}$/;
    if (!postalCodeRegex.test(postalCode)) {
        errorLabel.style.display = "block";
        errorLabel.innerHTML = "Codi postal incorrecte. Ha de tenir 5 dígits i només números.";
        return;
    } else {
        document.getElementById("addErrorLabelPostalCode").style.display = "none";
    }

    const restaurantId = document.getElementById("editRestaurantId").value;
    const restaurantData = {
        id: restaurantId,
        nombre: document.getElementById("editRestaurantName").value,
        direccion: document.getElementById("editRestaurantAddress").value,
        codigo_postal: document.getElementById("editRestaurantPostalCode").value,
    };

    try {
        const response = await fetch(`${API_URL}${restaurantId}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(restaurantData)
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }

        editModal.style.display = "none";
        await fetchRestaurants();
    } catch (error) {
        console.error("Error al guardar:", error);
    }
}

const addModal = document.getElementById("addRestaurantModal");
const addBtnAdd = document.getElementById("add-new");
const addSpanClose = document.getElementsByClassName("close")[0];
const addForm = document.getElementById("addRestaurantForm");

addBtnAdd.onclick = function() {
    addModal.style.display = "block";
    addForm.reset();
    document.getElementById("addRestaurantId").value = "";
    document.getElementById("addErrorLabelPostalCode").display = "none";
}

addSpanClose.onclick = function() {
    addModal.style.display = "none";
    const errorLabel = document.getElementById("addErrorLabelPostalCode");
    errorLabel.style.display = "none";
}

addForm.onsubmit = async function(e) {
    e.preventDefault();

    const errorLabel = document.getElementById("addErrorLabelPostalCode");
    const postalCode = document.getElementById("addRestaurantPostalCode").value;
    const postalCodeRegex = /^[0-9]{5}$/;
    if (!postalCodeRegex.test(postalCode)) {
        errorLabel.style.display = "block";
        errorLabel.innerHTML = "Codi postal incorrecte. Ha de tenir 5 dígits i només números.";
        return;
    } else {
        document.getElementById("addErrorLabelPostalCode").style.display = "none";
    }

    const restaurantData = {
        nombre: document.getElementById("addRestaurantName").value,
        direccion: document.getElementById("addRestaurantAddress").value,
        codigo_postal: document.getElementById("addRestaurantPostalCode").value,
    };

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(restaurantData)
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }

        addModal.style.display = "none";
        await fetchRestaurants();
    } catch (error) {
        console.error("Error al guardar:", error);
    }
};

const searchByIdInput = document.getElementById("searchInput");
searchByIdInput.addEventListener("keyup", async function(e) {
    const searchValue = e.target.value.trim();
    
    if (searchValue === "") {
        await fetchRestaurants();
        return;
    }

    if (/^\d+$/.test(searchValue)) {
        try {
            const restaurant = await fetchRestaurant(searchValue);
            if (restaurant.Error != null) {
                console.error("Error al buscar restaurante por ID:", restaurant);
                clearTable();
                return;
            }

            if (restaurant) {
                displayRestaurants({
                    Result: [{
                        id: restaurant.Result.id,
                        nombre: restaurant.Result.nombre,
                        direccion: restaurant.Result.direccion,
                        codigo_postal: restaurant.Result.codigo_postal
                    }]
                });
            } else {
                clearTable();
            }
        } catch (error) {
            console.error("Error al buscar restaurante por ID:", error);
            clearTable();
        }
    } else {
        await fetchRestaurants();
    }
});

document.addEventListener("DOMContentLoaded", fetchRestaurants);
