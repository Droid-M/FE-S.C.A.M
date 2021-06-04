/**
 * Cadastra novos usuários no sistema
 */
 function cadastro_user(event){

    event.preventDefault();
    
    let cpf = document.getElementById('cpf').value;
    let nome = document.getElementById('nome').value;
    let senha = document.getElementById('senha').value;
    let user_type = document.querySelector('input[name="funcao"]:checked').value;

    let token = sessionStorage.getItem("access_token")

    //Cadastra novo Usuário
    axios({
        method: 'post',
        url: '/cadastro_usuario',
        xsrfHeaderName: token,
        data: 
            {
                CPF:cpf,
                nome:nome,
                senha:senha,
                tipo: user_type
            }
           
        
    }). then((response)=>{
        console.log(response.data);
    }).catch((error)=>{
        console.log(error);
    })

}

