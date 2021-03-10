$("#btnLogin").click(function (event) {
  event.preventDefault();
  var login = $("#inputLogin").val();
  var senha = $("#inputSenha").val();

  if (login === "falhe") {
    console.log("falhe");
    Swal.fire({
      //   position: "top-end",
      icon: "error",
      title: "Oops...",
      text: "Login ou senha inválidos!",
      //   showConfirmButton: false,
      //   timer: 1500,
    });
  } else {
    $(location).attr("href", "/");
  }
});
