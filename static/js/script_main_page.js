document.addEventListener('DOMContentLoaded', () => {
    // Seleccionem els mòduls
    const usersModule = document.getElementById('usersModule');
    const existenciasModule = document.getElementById('existenciasModule');

    // Event listener per a Usuaris
    usersModule.addEventListener('click', () => {
        window.location.href = 'usuaris/index_form.html';
    });

    // Event listener per a Existències
    existenciasModule.addEventListener('click', () => {
        window.location.href = '/existencias';
    });

    // Efectes hover
    usersModule.addEventListener('mouseenter', () => {
        usersModule.style.borderColor = '#714B67';
    });
    usersModule.addEventListener('mouseleave', () => {
        usersModule.style.borderColor = '#e0e0e0';
    });

    existenciasModule.addEventListener('mouseenter', () => {
        existenciasModule.style.borderColor = '#714B67';
    });
    existenciasModule.addEventListener('mouseleave', () => {
        existenciasModule.style.borderColor = '#e0e0e0';
    });
});
