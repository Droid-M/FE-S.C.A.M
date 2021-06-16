

const access_token = sessionStorage.getItem("access_token");

/**
 * Edita e Atualiza usuario 
 */
function update_user(id_user){
    console.log(id_user)
   
}


/**
 * Deleta Usuarios
 */
function delete_user(id_user){
    alert("Deletar usuario " +id_user);
}

/**
 * Busca todos os usuários cadastrados
 */
function get_all_users(){


    axios.get("/lista_usuario",{ 
        headers: { Authorization: `Bearer ${access_token}` }
        }).then((response)=>{
            var usuarios = response.data;

            cria_tabela(usuarios);

    }).catch((error)=>{
        console.log(error);
    });
    
}
/**
 * Preenche a tabela com os registros do banco de dados
 * @param {*} usuarios 
 */
function cria_tabela(usuarios){
    var tabela = document.getElementById('tBody');

    for(let i=0;i<usuarios.length;i++){

        var newRow = tabela.insertRow();
    
        var cell_cpf = newRow.insertCell();
        var cell_nome = newRow.insertCell();
        var cell_funcao = newRow.insertCell();
        let cell_editar = newRow.insertCell();
        let cell_deletar = newRow.insertCell();
    
    
        let btEditar = document.createElement('button');
        btEditar.innerHTML='Editar';
        btEditar.setAttribute('onclick',`update_user(${usuarios[i].CPF})`);
    
        let btDeletar = document.createElement('button');
        btDeletar.innerHTML='Deletar';
        btDeletar.setAttribute('onclick',`delete_user(${usuarios[i].CPF})`);
        
        
        cell_cpf.innerHTML=usuarios[i].CPF;
        cell_nome.innerHTML = usuarios[i].nome;
        cell_funcao.innerHTML=usuarios[i].tipo;
        cell_editar.appendChild(btEditar);
        cell_deletar.appendChild(btDeletar);
    }

}

/**
 * Pesquisa um usuário específico 
 */
function get_user(){

}

