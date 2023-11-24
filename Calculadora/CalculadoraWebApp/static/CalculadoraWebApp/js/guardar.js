function guardarOperacionEnDB() {
    var operacion = document.getElementById("inputNumbers").value;

    fetch('/guardar_operacion/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Asegúrate de obtener el token CSRF
        },
        body: JSON.stringify({ operacion: operacion })
    })
    .then(response => {
        if (response.ok) {
            // La operación se guardó exitosamente
            console.log('Operación guardada en la base de datos');
        } else {
            // Manejar el error si la operación no se guardó correctamente
            console.error('Error al guardar la operación en la base de datos');
        }
    })
    .catch(error => {
        // Manejar los errores de conexión o solicitud
        console.error('Error de red:', error);
    });
}