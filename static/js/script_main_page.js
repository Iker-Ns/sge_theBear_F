document.addEventListener('DOMContentLoaded', () => {
    const usersModule = document.getElementById('usersModule');
    const restaurantModule = document.getElementById('restaurantModule');
    const comptesModule = document.getElementById('comptesModule');

    usersModule.addEventListener('click', () => {
        window.location.href = 'usuaris/index_form.html';
    });
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

    usersModule.addEventListener('mouseleave', () => {
        usersModule.style.borderColor = '#e0e0e0';
    });
    restaurantModule.addEventListener('mouseenter', () => {
        restaurantModule.style.borderColor = '#714B67';
    });
});