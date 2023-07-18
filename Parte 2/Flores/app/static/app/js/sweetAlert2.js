function confirmarEliminar(id){
    Swal.fire({
        title: '¿Quieres eliminar este producto?',
        text: "ADVERTENCIA: ¡No podrás recuperar el producto una vez eliminado!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#4CAF50',
        cancelButtonColor: '#d33',
        confirmButtonText: '¡Sí, eliminar el producto!',
        cancelButtonText: '¡No, me arrepiento!',
        backdrop: true
    }).then((result) => {
        if (result.isConfirmed) {
        Swal.fire(
            '¡Producto eliminado!',
            'Tu producto fue eliminado de la tienda.',
            'success'
        ).then(function(){
            window.location.href = "/eliminar/"+id+"/"
        })
        }
    })
}


function confirmarAgregar(id){
    Swal.fire({
        title: '¿Quieres agregar un nuevo producto?',
        text: "Aparecerá en la categoría 'Productos' una vez agregado.",
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#4CAF50',
        cancelButtonColor: '#d33',
        confirmButtonText: '¡Sí, ir a agregar un producto!',
        cancelButtonText: '¡No, aún no!',
        backdrop: true
    }).then((result) => {
        if (result.isConfirmed) {
        Swal.fire(
            'Abriendo el formulario para crear un producto nuevo...',
            'Haz click abajo para continuar.',
            'success'
        ).then(function(){
            window.location.href = "/agregar/"
        })
        }
    })
}

function confirmarModificar(id){
    Swal.fire({
        title: '¿Quieres modificar los datos de un producto?',
        text: "Se actualizará el producto elegido en la página una vez completado.",
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#4CAF50',
        cancelButtonColor: '#d33',
        confirmButtonText: '¡Sí, ir a modificar un producto!',
        cancelButtonText: '¡No, espera un momento!',
        backdrop: true
    }).then((result) => {
        if (result.isConfirmed) {
        Swal.fire(
            'Abriendo el formulario para modificar un producto...',
            'Haz click abajo para continuar.',
            'success'
        ).then(function(){
            window.location.href = "/modificar/"+id+"/"
        })
        }
    })
}

function exitoRegistro(){
    Swal.fire({
        title: 'Estás a punto de crear una nueva cuenta',
        text: "Confirma dando click abajo y tu cuenta quedará habilitada.",
        icon: 'info',
        showCancelButton: false,
        confirmButtonColor: '#4CAF50',
        cancelButtonColor: '#d33',
        confirmButtonText: '¡Sí, crear cuenta!',
        cancelButtonText: '¡No, olvidé algo!',
        backdrop: true
    }).then((result) => {
        if (result.isConfirmed) {
        Swal.fire(
            '¡Cuenta creada con éxito!',
            'Volviendo al homepage...',
            'success'
        ).then(function(){
            window.location.href = "/index"
        })
        }
    })
}
