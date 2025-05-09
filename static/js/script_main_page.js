document.addEventListener('DOMContentLoaded', () => {
    // Seleccionem el mòdul d'usuaris
    const usersModule = document.getElementById('usersModule');
    const restaurantModule = document.getElementById('restaurantModule');

    // Afegim event listener per al clic
    usersModule.addEventListener('click', () => {
        // Redireccionem a la pàgina del formulari
        window.location.href = 'usuaris/index_form.html';
    });

    // Afegim event listener per al clic
    restaurantModule.addEventListener('click', () => {
        // Redireccionem a la pàgina del formulari
        window.location.href = '/restaurant';
    });

    // Opcional: Afegir efecte al passar el ratolí
    usersModule.addEventListener('mouseenter', () => {
        usersModule.style.borderColor = '#714B67';
    });
    restaurantModule.addEventListener('mouseleave', () => {
        restaurantModule.style.borderColor = '#e0e0e0';
    })

    usersModule.addEventListener('mouseleave', () => {
        usersModule.style.borderColor = '#e0e0e0';
    });
    restaurantModule.addEventListener('mouseenter', () => {
        restaurantModule.style.borderColor = '#714B67';
    });
});