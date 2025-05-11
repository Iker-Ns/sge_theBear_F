document.addEventListener('DOMContentLoaded', function() {
    const addBtn = document.getElementById('add-new');
    const addModal = document.getElementById('addCompteModal');
    const editModal = document.getElementById('editCompteModal');
    const addForm = document.getElementById('addCompteForm');
    const editForm = document.getElementById('editCompteForm');
    const searchInput = document.getElementById('searchInput');
    const compteTable = document.getElementById('compteTable').getElementsByTagName('tbody')[0];
    const addProductoModal = document.getElementById('addProductoModal');
    const editProductoModal = document.getElementById('editProductoModal');
    const addProductoForm = document.getElementById('addProductoForm');
    const editProductoForm = document.getElementById('editProductoForm');

    document.querySelectorAll('.close').forEach(function(closeBtn) {
        closeBtn.addEventListener('click', function() {
            addModal.style.display = 'none';
            editModal.style.display = 'none';
            addProductoModal.style.display = 'none';
            editProductoModal.style.display = 'none';
        });
    });

    window.addEventListener('click', function(event) {
        if (event.target == addModal) {
            addModal.style.display = 'none';
        } else if (event.target == editModal) {
            editModal.style.display = 'none';
        } else if (event.target == addProductoModal) {
            addProductoModal.style.display = 'none';
        } else if (event.target == editProductoModal) {
            editProductoModal.style.display = 'none';
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
                <td><button class="btn-expand" data-id="${compte.id}">+</button></td>
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

        addExpandButtonListeners();
        addEditButtonListeners();
        addDeleteButtonListeners();
    }

    function addExpandButtonListeners() {
        document.querySelectorAll('.btn-expand').forEach(button => {
            button.addEventListener('click', function() {
                const compteId = this.getAttribute('data-id');
                const row = this.closest('tr');
                const nextRow = row.nextElementSibling;

                if (nextRow && nextRow.classList.contains('expanded-row')) {
                    nextRow.remove();
                    this.textContent = '+';
                } else {
                    fetch(`api/cuenta/${compteId}`)
                        .then(response => response.json())
                        .then(data => {
                            if (data && data.Result) {
                                const compte = data.Result;
                                const productos = compte.productos || [];

                                const currentIndex = Array.from(compteTable.rows).indexOf(row);
                                const expandedRow = compteTable.insertRow(currentIndex + 1);
                                expandedRow.classList.add('expanded-row');
                                expandedRow.innerHTML = `
                                    <td colspan="6">
                                        <div class="productos-container">
                                            <h3>Productos en esta cuenta</h3>
                                            <div class="productos-lista" id="productos-lista-${compteId}">
                                                ${productos.length === 0 ? '<p>No hay productos en esta cuenta</p>' : ''}
                                            </div>
                                            <button class="btn-primary btn-add-producto" data-cuenta-id="${compteId}">Añadir Producto</button>
                                        </div>
                                    </td>
                                `;

                                const productosLista = document.getElementById(`productos-lista-${compteId}`);
                                if (productos.length > 0) {
                                    productos.forEach(producto => {
                                        const productoItem = document.createElement('div');
                                        productoItem.className = 'producto-item';
                                        productoItem.innerHTML = `
                                            <span>Producto ID: ${producto.producto_id} - Cantidad: ${producto.cantidad}</span>
                                            <div class="producto-actions">
                                                <button class="btn-edit-producto" data-id="${producto.id}" data-cuenta-id="${compteId}" data-producto-id="${producto.producto_id}" data-cantidad="${producto.cantidad}">Editar</button>
                                                <button class="btn-delete-producto" data-id="${producto.id}" data-cuenta-id="${compteId}">Borrar</button>
                                            </div>
                                        `;
                                        productosLista.appendChild(productoItem);
                                    });
                                }

                                addProductoButtonListeners(compteId);
                                addEditProductoButtonListeners();
                                addDeleteProductoButtonListeners();

                                this.textContent = '-';
                            }
                        })
                        .catch(error => console.error('Error fetching compte details:', error));
                }
            });
        });
    }

    function addProductoButtonListeners(compteId) {
        document.querySelectorAll(`.btn-add-producto[data-cuenta-id="${compteId}"]`).forEach(button => {
            button.addEventListener('click', function() {
                const cuentaId = this.getAttribute('data-cuenta-id');
                document.getElementById('addProductoCuentaId').value = cuentaId;
                addProductoForm.reset();
                addProductoModal.style.display = 'block';
            });
        });
    }

    function addEditProductoButtonListeners() {
        document.querySelectorAll('.btn-edit-producto').forEach(button => {
            button.addEventListener('click', function() {
                const productoId = this.getAttribute('data-id');
                const cuentaId = this.getAttribute('data-cuenta-id');
                const productoProdId = this.getAttribute('data-producto-id');
                const cantidad = this.getAttribute('data-cantidad');

                document.getElementById('editProductoId').value = productoId;
                document.getElementById('editProductoCuentaId').value = cuentaId;
                document.getElementById('editProductoProductoId').value = productoProdId;
                document.getElementById('editCantidad').value = cantidad;

                editProductoModal.style.display = 'block';
            });
        });
    }

    function addDeleteProductoButtonListeners() {
        document.querySelectorAll('.btn-delete-producto').forEach(button => {
            button.addEventListener('click', function() {
                const productoId = this.getAttribute('data-id');
                const cuentaId = this.getAttribute('data-cuenta-id');

                if (confirm('¿Estás seguro de que quieres eliminar este producto de la cuenta?')) {
                    fetch(`api/producto_cuenta/${productoId}`, {
                        method: 'DELETE'
                    })
                    .then(response => response.json())
                    .then(data => {
                        // Actualizar la vista expandida
                        const expandBtn = document.querySelector(`.btn-expand[data-id="${cuentaId}"]`);
                        if (expandBtn) {
                            expandBtn.click(); // Cierra
                            expandBtn.click(); // Abre nuevamente para actualizar
                        }
                    })
                    .catch(error => console.error('Error deleting producto:', error));
                }
            });
        });
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

        const compteId = parseInt(document.getElementById('editCompteId').value);
        const compteData = {
            cliente_id: parseInt(document.getElementById('editClienteId').value),
            precio_total: parseInt(document.getElementById('editPrecioTotal').value)
        };

        fetch(`api/cuenta/${compteId}`, {
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

    addProductoForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const productoData = {
            cuenta_id: parseInt(document.getElementById('addProductoCuentaId').value),
            producto_id: parseInt(document.getElementById('addProductoId').value),
            cantidad: parseInt(document.getElementById('addCantidad').value)
        };

        fetch('api/producto_cuenta', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(productoData)
        })
        .then(response => response.json())
        .then(data => {
            addProductoModal.style.display = 'none';

            const expandBtn = document.querySelector(`.btn-expand[data-id="${productoData.cuenta_id}"]`);
            if (expandBtn) {
                expandBtn.click(); // Cierra
                expandBtn.click(); // Abre nuevamente para actualizar
            }
        })
        .catch(error => console.error('Error adding producto to compte:', error));
    });

    editProductoForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const productoData = {
            id: parseInt(document.getElementById('editProductoId').value),
            cuenta_id: parseInt(document.getElementById('editProductoCuentaId').value),
            producto_id: parseInt(document.getElementById('editProductoProductoId').value),
            cantidad: parseInt(document.getElementById('editCantidad').value)
        };

        fetch('api/producto_cuenta', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(productoData)
        })
        .then(response => response.json())
        .then(data => {
            editProductoModal.style.display = 'none';

            const expandBtn = document.querySelector(`.btn-expand[data-id="${productoData.cuenta_id}"]`);
            if (expandBtn) {
                expandBtn.click();
                expandBtn.click();
            }
        })
        .catch(error => console.error('Error updating producto in compte:', error));
    });

    searchInput.addEventListener('input', function() {
        const searchValue = this.value.toLowerCase();
        const rows = compteTable.getElementsByTagName('tr');

        for (let i = 0; i < rows.length; i++) {
            if (!rows[i].classList.contains('expanded-row')) {
                const id = rows[i].cells[1].textContent;
                if (id.includes(searchValue)) {
                    rows[i].style.display = '';
                    if (rows[i+1] && rows[i+1].classList.contains('expanded-row')) {
                        rows[i+1].style.display = '';
                    }
                } else {
                    rows[i].style.display = 'none';
                    if (rows[i+1] && rows[i+1].classList.contains('expanded-row')) {
                        rows[i+1].style.display = 'none';
                    }
                }
            }
        }
    });
});
