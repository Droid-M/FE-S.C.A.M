
// Verifica se uma sessão foi iniciada

let logado = false;

if(localStorage.getItem("acesso")== "true"){
    logado =true;
}

if(logado != true){
    alert("Voce nao esta logado");
    location.href="/src/login.html";
}