

function logar(){
    
    function login(event) {
        //stop submit the form, we will post it manually.
        event.preventDefault();
    
        var username = document.getElementById("login").value;
        var password = document.getElementById("password").value;
    
        var jsonData = {
            username: username,
            password: password,
        };
    
        // disabled the submit button
        $("#btnSubmit").prop("disabled", true);
    
        axios
            // .post("/api/v" + VERSION + "/auth", jsonData)
            // .then(function(response) {
            //     console.log(response);
            //     let access_token = response.data.access_token;
            //     let user_class = response.data.user_class;
            //     let first_login = response.data.first_login;
            //     let username = response.data.cpf;
            //     localStorage.setItem("access_token", access_token);
            //     localStorage.setItem("user_class", user_class);
            //     localStorage.setItem("first_login", first_login);
            //     localStorage.setItem("username", username);
            //     $("#btnSubmit").prop("disabled", false);
            //     if (first_login === true) {
            //         document.location = "/redefine";
            //     } else if (user_class === "administrador") {
            //         document.location = "/admin";
            //     } else if (user_class === "agente") {
            //         document.location = "/";
            //     } else {
            //         Swal.fire({
            //             icon: "error",
            //             title: "Erro desconhecido",
            //             text: "Aconteceu algo inesperado, tente novamente. Caso o erro persista, entre em contato com o suporte.",
            //             confirmButtonColor: "#2f3883"
            //         });
            //     }
            // })
            .catch(function(error) {
                if (error.response) {
                    let msg = error.response.data.msg;
                    $("#output").text(msg);
                    if (typeof msg === "string" || msg instanceof String) {
                        Swal.fire({
                            icon: "error",
                            title: "Credenciais erradas",
                            text: msg,
                            confirmButtonColor: "#2f3883"
                        });
                    } else {
                        let completeMsg = '';
                        for (let key in msg) {
                            completeMsg += key + ': ' + msg[key] + '\n';
                        }
                        Swal.fire({
                            icon: "error",
                            title: "Erro",
                            text: completeMsg,
                            confirmButtonColor: "#2f3883"
                        });
                    }
                } else {
                    Swal.fire({
                        icon: "error",
                        title: "Erro desconhecido",
                        text: "Aconteceu algo inesperado, tente novamente. Caso o erro persista, entre em contato com o suporte.",
                        confirmButtonColor: "#2f3883"
                    });
                }
            });
        $("#btnSubmit").prop("disabled", false);
    }
}



