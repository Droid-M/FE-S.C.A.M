$("#btnCadastroEnfermeiro").click(function (event) {
  event.preventDefault();
  Swal.fire({
    position: "center",
    icon: "success",
    title: "Usuário cadastrado!",
    showConfirmButton: false,
    timer: 1500,
  });
});
$("#btnCadastroPaciente").on("click", function (event) {
  event.preventDefault();
  Swal.fire({
    position: "center",
    icon: "success",
    title: "Usuário cadastrado!",
    showConfirmButton: false,
    timer: 5000,
  });
});
