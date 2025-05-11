document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('userForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtenir valors del formulari
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const age = parseInt(document.getElementById('age').value);

         try {
            // Enviar dades al servidor amb body JSON
            const response = await fetch('http://localhost:8000/users/create/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    name: name,
                    email: email,
                    age: age
                })
            });

            if (response.ok) {
                showMessage('Usuari creat correctament!', 'success');
                form.reset(); // Netejar el formulari
            } else {
                showMessage(`Error: ${data.detail || 'Error desconegut'}`, 'error');
            }
        } catch (error) {
            showMessage(`Error de connexió: ${error.message}`, 'error');
        }
    });

    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = 'message ' + type;
    }
});