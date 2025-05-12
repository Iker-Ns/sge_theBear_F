document.addEventListener('DOMContentLoaded', () => {
    const usersModule = document.getElementById('usersModule');
    const restaurantModule = document.getElementById('restaurantModule');
    const trabajadorsModule = document.getElementById('trabajadoresModule');
    const comptesModule = document.getElementById('comptesModule');
    const existenciasModule = document.getElementById('existenciasModule');

    usersModule.addEventListener('click', () => {
        window.location.href = '/clients';
    });

    existenciasModule.addEventListener('click', () => {
        window.location.href = '/existencias';
    });

    trabajadorsModule.addEventListener('click', () => {
        // Redireccionem a la pàgina del formulari
        window.location.href = '/trabajadores';
    });

    // Afegim event listener per al clic
    comptesModule.addEventListener('click', () => {
        window.location.href = '/cuenta';
    });
    restaurantModule.addEventListener('click', () => {
        window.location.href = '/restaurant';
    });

    comptesModule.addEventListener('mouseenter', () => {
        comptesModule.style.borderColor = '#714B67';
    });
    comptesModule.addEventListener('mouseleave', () => {
        comptesModule.style.borderColor = '#e0e0e0';
    })

    usersModule.addEventListener('mouseenter', () => {
        usersModule.style.borderColor = '#714B67';
    });
    restaurantModule.addEventListener('mouseleave', () => {
        restaurantModule.style.borderColor = '#e0e0e0';
    })

    existenciasModule.addEventListener('mouseenter', () => {
        existenciasModule.style.borderColor = '#714B67';
    });
    existenciasModule.addEventListener('mouseleave', () => {
        existenciasModule.style.borderColor = '#e0e0e0';
    });

    trabajadorsModule.addEventListener('mouseenter', () => {
        trabajadorsModule.style.borderColor = '#714B67';
    });
    trabajadorsModule.addEventListener('mouseleave', () => {
        trabajadorsModule.style.borderColor = '#e0e0e0';
    });

    usersModule.addEventListener('mouseleave', () => {
        usersModule.style.borderColor = '#e0e0e0';
    });
    restaurantModule.addEventListener('mouseenter', () => {
        restaurantModule.style.borderColor = '#714B67';
    });
});