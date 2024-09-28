document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.querySelector('.search-form');

    searchForm.addEventListener('submit', function(event) {
        const nameInput = searchForm.querySelector('input[name="name"]').value.trim();
        if (nameInput === '') {
            alert('Por favor, ingresa un nombre para buscar.');
            event.preventDefault();
        }
    });
});