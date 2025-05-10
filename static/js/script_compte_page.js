document.addEventListener('DOMContentLoaded', function() {
    const addBtn = document.getElementById('add-new');
    const addModal = document.getElementById('addCompteModal');
    const editModal = document.getElementById('editCompteModal');
    const addForm = document.getElementById('addCompteForm');
    const editForm = document.getElementById('editCompteForm');
    const searchInput = document.getElementById('searchInput');
    const compteTable = document.getElementById('compteTable').getElementsByTagName('tbody')[0];

    document.querySelectorAll('.close').forEach(function(closeBtn) {
        closeBtn.addEventListener('click', function() {
            addModal.style.display = 'none';
            editModal.style.display = 'none';
        });
    });

    window.addEventListener('click', function(event) {
        if (event.target == addModal) {
            addModal.style.display = 'none';
        } else if (event.target == editModal) {
            editModal.style.display = 'none';
        }
    });

    addBtn.addEventListener('click', function() {
        addForm.reset();
        addModal.style.display = 'block';
    });

    loadComptes();

    function loadComptes() {
        fetch('api/cuenta')
            .then(response => response.json())
            .then(data => {
                if (data && data.Result) {
                    displayComptes(data.Result);
                }
            })
            .catch(error => console.error("Error loading comptes:", error));
    }

    function displayComptes(comptes) {
        compteTable.innerHTML = '';
        comptes.forEach(compte => {
            const row = compteTable.insertRow();
            row.innerHTML = `
                <td>${compte.id}</td>
                <td>${compte.cliente_id}</td>
                <td>${compte.precio_total}</td>
                <td>${new Date(compte.fecha).toLocaleString()}</td>
                <td>
                    <button class="btn-edit" data-id="${compte.id}">Editar</button>
                    <button class="btn-delete" data-id="${compte.id}">Eliminar</button>
                </td>
            `;
        });


        addEditButtonListeners();
        addDeleteButtonListeners();
    }

    function addEditButtonListeners() {
        document.querySelectorAll('.btn-edit').forEach(button => {
            button.addEventListener('click', function() {
                const compteId = this.getAttribute('data-id');
                fetch(`api/cuenta/${compteId}`)
                    .then(response => response.json())
                    .then(data => {
                        if (data && data.Result) {
                            const compte = data.Result;
                            document.getElementById('editCompteId').value = compte.id;
                            document.getElementById('editClienteId').value = compte.cliente_id;
                            document.getElementById('editPrecioTotal').value = compte.precio_total;
                            editModal.style.display = 'block';
                        }
                    })
                    .catch(error => console.error('Error fetching compte details:', error));
            });
        });
    }

    function addDeleteButtonListeners() {
        document.querySelectorAll('.btn-delete').forEach(button => {
            button.addEventListener('click', function() {
                const compteId = this.getAttribute('data-id');
                if (confirm('¿Estás seguro de que quieres eliminar esta cuenta?')) {
                    fetch(`api/cuenta/${compteId}`, {
                        method: 'DELETE'
                    })
                    .then(response => response.json())
                    .then(data => {
                        loadComptes();
                    })
                    .catch(error => console.error('Error deleting compte:', error));
                }
            });
        });
    }

    addForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const compteData = {
            id_cliente: parseInt(document.getElementById('addClienteId').value),
            precio_total: parseInt(document.getElementById('addPrecioTotal').value)
        };

        fetch('api/cuenta', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(compteData)
        })
        .then(() => {
            addModal.style.display = 'none';
            loadComptes();
        })
        .catch(error => console.error('Error adding compte:', error));
    });

    editForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const compteData = {
            id: parseInt(document.getElementById('editCompteId').value),
            id_cliente: parseInt(document.getElementById('editClienteId').value),
            precio_total: parseInt(document.getElementById('editPrecioTotal').value)
        };

        fetch('api/cuenta/', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(compteData)
        })
        .then(response => response.json())
        .then(data => {
            editModal.style.display = 'none';
            loadComptes();
        })
        .catch(error => console.error('Error updating compte:', error));
    });

    searchInput.addEventListener('input', function() {
        const searchValue = this.value.toLowerCase();
        const rows = compteTable.getElementsByTagName('tr');

        for (let i = 0; i < rows.length; i++) {
            const id = rows[i].cells[0].textContent;
            if (id.includes(searchValue)) {
                rows[i].style.display = '';
            } else {
                rows[i].style.display = 'none';
            }
        }
    });
});
