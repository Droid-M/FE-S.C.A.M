function logar() {
  var username = document.getElementById("login").value;
  var password = document.getElementById("password").value;

  console.log("Usuário e Senha:", username + " " + password);

  var jsonData = {
    CPF: username,
    senha: password,
  };

  // Faz uma requisição post para a api, esperando como resultado o token
  axios
    .post("/auth", jsonData)
    .then((response) => {
      console.log(response.data); // json com os dados
      let status = response.data.status;

      let access_token = response.data.access_token;
      let classe = response.data.classe;

      sessionStorage.setItem("access_token", access_token);

      if (classe == "ADMINISTRADOR") {
        location.href("/admin");
      } else if (classe == "ENFERMEIRO_CHEFE") {
        location.href("/enf-chefe");
      } else if (classe == "ENFERMEIRO") {
        location.href("/enf");
      } else if (classe == "ESTAGIARIO") {
        location.href("/estagiario");
      }
    })
    .catch((error) => {
      let msg = error.response.data.msg;
      console.error(msg);
      $("#alert_placeholder").html(
        '<div class="alert alert-danger alert-dismissible">' + msg + "</div>"
      );
    });
}
