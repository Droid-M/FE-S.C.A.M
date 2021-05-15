

function logar(){
    let email = document.getElementById("login");
    let senha = document.getElementById("password")
    
    if(email.value == "admin@admin.com" && senha.value=="123"){
        localStorage.setItem("acesso",true);
        window.location.href = "./templates/adm.html";
        console.log(localStorage.getItem("acesso"))

    } else if(email.value ="enfChefe@enf" && senha.value=="enfe"){
        localStorage.setItem("acesso",true);
        window.location.href = "./templates/enfchefe.html";
        console.log("Logado como Enfermeiro Chefe")
        
    }
     else if(email.value ="enf@enf" && senha.value=="enf" ){
            localStorage.setItem("acesso", true);
            window.location.href="./templates/enf.html";
            console.log("Logado como enfermeiro");
     }   
    else{
        console.log(email+senha)
        alert("Error Inesperado");

    }
}



