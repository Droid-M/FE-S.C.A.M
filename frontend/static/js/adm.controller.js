
/**
 * Edita e Atualiza usuario 
 */
function update_user(){

}


/**
 * Deleta Usuarios
 */
function delete_user(){

}

/**
 * Busca todos os usuários cadastrados
 */
function get_all_users(){

    axios.get("/lista_usuario").then((response)=>{
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
    var tabela = document.getElementById('table-users');
    for(let i=0; i<usuarios.length;i++){

        //criar elementos
        var linha = document.createElement("tr");
        var campo_cpf = document.createElement("td");
        var campo_nome = document.createElement("td");
        var campo_funcao = document.createElement("td");
        var campo_edite = document.createElement("td");
        var campo_delete = document.createElement("td");

        var link_edita = document.createElement("a");
        var link_deleta = document.createElement("a"); 
        //cria os nós
        var texto_cpf = document.createTextNode(usuarios[i].CPF);
        var texto_nome = document.createTextNode(usuarios[i].nome);
        var texto_funcao = document.createTextNode("-");
        var texto_edite = document.createTextNode(link_edita);
        var texto_delete = document.createTextNode(link_deleta);
    
        //vincular os nós aos elementos
        campo_cpf.appendChild(texto_cpf);
        campo_nome.appendChild(texto_nome);
        campo_funcao.appendChild(texto_funcao);
        campo_edite.appendChild(texto_edite);
        campo_delete.appendChild(texto_delete);
    
        linha.appendChild(campo_cpf);
        linha.appendChild(campo_nome);
        linha.appendChild(campo_funcao);
        linha.appendChild(campo_edite);
        linha.appendChild(campo_delete);
    
        //vincula os elementos ao documento
        tabela.appendChild(linha);
    }

}

/**
 * Pesquisa um usuário específico 
 */
function get_user(){

}

