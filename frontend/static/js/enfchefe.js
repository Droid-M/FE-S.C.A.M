$(function () {
    $("#sidebar-wrapper").addClass("bg-light border-right");
    $("#sidebar-wrapper").load("/sidebarenfchefe");

    $("#navbar").addClass("navbar navbar-expand-lg navbar-light bg-light border-bottom");
    $("#navbar").load("/navbar");
});




function cadastrarPaciente(){
    let nomepaciente = document.getElementById("nome");
    let sobrenomePaciente = document.getElementById("sobrenome");
    let generoPaciente = document.getElementById("genero");
    let cpfPaciente = document.getElementById("cpf");
    let dataPaciente = document.getElementById("dataNascimento");
    let sanguePaciente = document.getElementById("sangue");
}




