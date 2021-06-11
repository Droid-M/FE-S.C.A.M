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
    console.log("Token " + token);
    //Cadastra novo Usuário

    // eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjcGYiOiIwMzY1NTg0NjIyMiJ9.MBBVoDE3oemmaNaiwq2cclkttpXaEHtF455vAE8UqcA
    
    // eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjcGYiOiIwMzY1NTg0NjIyMiJ9.MBBVoDE3oemmaNaiwq2cclkttpXaEHtF455vAE8UqcA

    // eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjcGYiOiIwMzY1NTg0NjIyMiJ9.MBBVoDE3oemmaNaiwq2cclkttpXaEHtF455vAE8UqcA


    axios({
        method: 'post',
        url: '/cadastro_usuario',
        headers: { Authorization: `Bearer ${token}` },
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
        console.error(error);
    })

}

