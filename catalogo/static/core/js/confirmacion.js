
function confirmarEliminacion(id) {
    Swal.fire({
        title: '¿Estas Seguro?',
        text: "Esta acción será permanente!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Eliminar!',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.value) {
            window.location.href = "eliminar_pre/"+id+"/";
        }
      })
}

function confirmarEliminacionP(id) {
  Swal.fire({
      title: '¿Estas Seguro?',
      text: "Esta acción será permanente!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si, Eliminar!',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.value) {
          window.location.href = "eliminar_per/"+id+"/";
      }
    })
}