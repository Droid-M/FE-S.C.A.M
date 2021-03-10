$('#btnSignOut').click(function () {
    Swal.fire({
        title: 'Tem certeza?',
        text: "Você terá de fazer login novamente da próxima vez",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sim'
      }).then((result) => {
        if (result.isConfirmed) {
            // Código para deslogar o usuário
        }
      })
});