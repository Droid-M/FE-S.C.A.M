const access_token = sessionStorage.getItem("access_token");

$("#cadastra-farmaco-form").submit(() => {
  // Obtém e  estrutura os dados do medicamento como JSON
  let medicamento = {};

  medicamento[nome] = $("#nome-medicamento").val();
  medicamento[codigo] = $("#cod-medicamento").val();

  // Cria o Medicamento no Banco de Dados
  axios({
    method: "post",
    url: "/medicamento",
    headers: { Authorization: `Bearer ${access_token}` },
    data: medicamento,
  })
    .catch((error) => {
      console.error(error);
      alert(error);
    });

  // Obtém e  estrutura os dados da posologia como JSON
  let posologia = {};

  posologia[medicamento] = parseInt(medicamento.codigo);
  posologia[paciente] = $("#cpf-paciente").val();
  posologia[quantidade] = parseFloat($("#quantidade").val());
  posologia[notas] = $("#aplicacao").val() + "\n\n" + $("#reacao").val();

  axios({
    method: "post",
    url: "/posologia",
    headers: { Authorization: `Bearer ${access_token}` },
    data: posologia,
  })
    .then((response) => {
      alert("Medicamento cadastrado com sucesso");
    })
    .catch((error) => {
      console.error(error);
      alert(error);
    });
});
