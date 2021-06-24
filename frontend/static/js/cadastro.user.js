

const token = sessionStorage.getItem("access_token");

var state =false;
const url = location.href;
let params = url.split('=');
let id='';
console.log(params[0], 1)
if(params.length>1){
    id = params[1];
    state = true;
    console.log(id)
}
console.log(state)


if(state && id!= undefined){
    carrega_dados();
      
    let btn = document.getElementById('cadastro-salvar');
    btn.innerHTML='Editar'
   
}

/**
 * Método para ediçao do funcionario
 */
function carrega_dados(){
    let usuarios='';
    axios.get(`/lista_usuario/${id}`,{ 
        headers: { Authorization: `Bearer ${token}` }
        }).then((response)=>{
            usuarios = response.data;
            let cpf = document.getElementById('cpf'). value= usuarios.CPF;
            let nome = document.getElementById('nome').value= usuarios.nome;
            let senha = document.getElementById('senha').value;
          //  let user_type = document.querySelector('input[name="funcao"]:checked').value = usuarios.tipo;
            console.log(response.data); 

    }).catch((error)=>{
        console.log(error);
    });
}


/*
 * Cadastra novos usuários no sistema
 */
 function cadastro_edicao_user(event){

    event.preventDefault();
    
    let cpf = document.getElementById('cpf').value;
    let nome = document.getElementById('nome').value;
    let senha = document.getElementById('senha').value;
    let user_type = document.querySelector('input[name="funcao"]:checked').value;


  
    axios({
        method: state ? 'put':'post',
        url: state ?'/edicao_usuario':'/cadastro_usuario',
        headers: { Authorization: `Bearer ${token}` },
        data: 
            {
                CPF:cpf,
                nome:nome,
                senha:senha,
                tipo: user_type
            }
           
        
    }). then((response)=>{
        location.href='/admin';
        if(!state){
            alert('Cadastrado com Sucesso!!');
        }else{
            alert("Edição Realizada com Sucesso")
        }
        console.log(response.data); 
    }).catch((error)=>{
        console.error(error);
    })

}



