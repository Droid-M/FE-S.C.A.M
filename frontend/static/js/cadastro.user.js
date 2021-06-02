/**
 * Cadastra novos usuários no sistema
 */
 function cadastro_user(event){

    event.preventDefault();
    
    let cpf = document.getElementById('cpf').value;
    let nome = document.getElementById('nome').value;
    let senha = document.getElementById('senha').value;
    let user_type = document.querySelector('input[name="funcao"]:checked').value;
    
    var user = {
        CPF:cpf,
        nome:nome,
        senha:senha
    }

    var jsonData = {
        user:user,
        user_type:user_type
    }
    console.log(jsonData);

    
    // Envia os dados do cadastro para ser salvo
    // axios.post('/cadastro_usuario',jsonData).then((response)=>{
    //      console.log(response.data);
    // }).catch((error)=>{
    //     console.log(error);
    // });

}

