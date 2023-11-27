
    $(document).ready(function () {
        // manejador de eventos a los botones disponibles
        $(".disponible-btn").click(function () {
            const id = $(this).data("id");
            solicitud(id);
        });


        // manejador de eventos a los botones liberar
        $(".liberar-btn").click(function () {
            const id = $(this).data("id");
            liberar(id);
        });


        async function solicitud(id) {
            
            try {
                const response = await fetch(`/motociclistas/solicitud/${id}/`);
                const data = await response.json();
                console.log(data);
                if (data.success === true) {
                    $(`#disponible-${id}-btn`).hide();
                    $(`#liberar-${id}-btn`).show();
                    // Actualiza el valor de motociclistas en la interfaz
                    $(`#motociclistas-${id}`).text(data.nuevo_valor);
                    // Almacena el estado en el almacenamiento local
                    localStorage.setItem(`estado-${id}-${getUserId()}`, 'liberar');
                } else {
                    alert('No encontrado');
                }
            } catch (error) {
                console.error(error);
            }
        }


        async function liberar(id) {
            try {
                const response = await fetch(`/motociclistas/liberar/${id}/`);
                const data = await response.json();
                console.log(data);
                if (data.success === true) {
                    $(`#disponible-${id}-btn`).show();
                    $(`#liberar-${id}-btn`).hide();
                    // Actualiza el valor de motociclistas en la interfaz
                    $(`#motociclistas-${id}`).text(data.nuevo_valor);
                    // Almacena el estado en el almacenamiento local
                    localStorage.setItem(`estado-${id}-${getUserId()}`, 'disponible');
                } else {
                    alert('No encontrado');
                }
            } catch (error) {
                console.error(error);
            }
        }


        // Verifica y restablece el estado almacenado localmente al cargar la página
        $(".disponible-btn").each(function () {
            const id = $(this).data("id");
            const estadoAlmacenado = localStorage.getItem(`estado-${id}-${getUserId()}`);
            if (estadoAlmacenado === 'liberar') {
                $(`#disponible-${id}-btn`).hide();
                $(`#liberar-${id}-btn`).show();
            }
        });

        function getUserId() {
            return userId;
        }
        
    });
