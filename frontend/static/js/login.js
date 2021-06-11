function logar(){  
        //stop submit the form, we will post it manually.
        // event.preventDefault();
    
        var username = document.getElementById("login").value;
        var password = document.getElementById("password").value;
        
        console.log('Usuário e Senha:',username+' '+password);
        
       
        
        var jsonData = {
            CPF: username,
            senha: password,
        };

        // Faz uma requisição post para a api, esperando como resultado o token 
         axios.post('/auth',jsonData).then((response)=>{
            console.log(response.data); // json com os dados
            let status = response.data.status;

        
            if(status == '201'){

                let access_token = response.data.access_token;
                let classe = response.data.classe;
   
                sessionStorage.setItem('access_token',access_token);

                

                if(classe == "ADMINISTRADOR"){
                    location.href='/admin';
                }else if(classe == "ENFERMEIRO_CHEFE"){
                    location.href='/enf-chefe';
                }else if(classe == "ENFERMEIRO"){
                    location.href='/enf';
                }else if(classe == "ESTAGIARIO"){
                    location.href='/estagiario';
                }
            }else if(status == '406'){
                let msg = response.data.msg;
                alert(msg);
                location.href("/");
            }

             
         }).catch((error)=>{
             console.log(error);
         });

        
        // disabled the submit button
        // $("#btnSubmit").prop("disabled", true);
        
        //  axios
        //     .post('/auth', jsonData)
        //     .then(function(response) {

                // let access_token = response.data.access_token;
                // let user_class = response.data.user_class;
                // let first_login = response.data.first_login;
                // let username = response.data.cpf;
                // console.log(response.data);
                // localStorage.setItem("access_token", access_token);
                // localStorage.setItem("user_class", user_class);
                // localStorage.setItem("first_login", first_login);
                // localStorage.setItem("username", username);
                // $("#btnSubmit").prop("disabled", false);
                // if(access_token){
                //     console.log('Sucesso');
                // }
                // if (first_login === true) {
                //     document.location = "/redefine";
                // } else if (user_class === "administrador") {
                //     document.location = "/admin";
                // } else if (user_class === "agente") {
                //     document.location = "/";
                // } else {
                //     Swal.fire({
                //         icon: "error",
                //         title: "Erro desconhecido",
                //         text: "Aconteceu algo inesperado, tente novamente. Caso o erro persista, entre em contato com o suporte.",
                //         confirmButtonColor: "#2f3883"
                //     });
                // }
            // })
            // .catch(function(error) {
                
            //     console.log(error.data);
            // });
        // $("#btnSubmit").prop("disabled", false);
    
}

