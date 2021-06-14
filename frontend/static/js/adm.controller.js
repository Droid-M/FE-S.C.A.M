

const access_token = sessionStorage.getItem("access_token");

/**
 * Edita e Atualiza usuario 
 */
function update_user(usuario){
    console.log('hello')

    
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
    var table = document.getElementById('tb_user');
    var tabela = document.getElementById('tBody');
    
    var newRow = tabela.insertRow(table.length);

    var cell_cpf = newRow.insertCell(0);
    var cell_nome = newRow.insertCell(1);
    var cell_funcao = newRow.insertCell(2);
    var cell_edite = newRow.insertCell(3);
    var cell_delete = newRow.insertCell(4);
    const edit = `<a onclick=${update_user(usuarios[0])}>Editar</a>`
    const del = `<a onclick=${update_user(usuarios[0])}>Delete</a>`
    cell_cpf.innerHTML=usuarios[0].CPF;
    cell_nome.innerHTML = usuarios[0].nome;
    cell_funcao.innerHTML=usuarios[0].tipo;
    
    cell_edite.innerHTML=edit;
    cell_delete.innerHTML=del;

    // var link_deleta = document.createElement("a"); 
    // link_deleta.text="Deleta"
    
    // for(let i=0; i<usuarios.length;i++){

    //     //criar elementos
    //     var linha = document.createElement("tr");
    //     var campo_cpf = document.createElement("td");
    //     var campo_nome = document.createElement("td");
    //     var campo_funcao = document.createElement("td");
    //     var campo_edite = document.createElement("td");
    //     var campo_delete = document.createElement("td");
        
    //     var link_edita = document.createElement("a");
    //     var link_deleta = document.createElement("a"); 
        
    //     var btn_edita = document.createElement("button");
        
    //     //cria os nós
    //     var texto_cpf = document.createTextNode(usuarios[i].CPF);
    //     var texto_nome = document.createTextNode(usuarios[i].nome);
    //     var texto_funcao = document.createTextNode(usuarios[i].tipo);
       
    //     link_edita.setAttribute('edita',"edita");
    //     link_edita.text='Edita'
       
    //     btn_edita.textContent='Edita';
        
    //     btn_edita.

    //     link_deleta.setAttribute('delete','delete');
    //     link_deleta.href='#';
    //     link_deleta.text='Delete'

    //     //vincular os nós aos elementos
    //     campo_cpf.appendChild(texto_cpf);
    //     campo_nome.appendChild(texto_nome);
    //     campo_funcao.appendChild(texto_funcao);
    //     campo_edite.appendChild(btn_edita);
    //     campo_delete.appendChild(link_deleta);
    
    //     linha.appendChild(campo_cpf);
    //     linha.appendChild(campo_nome);
    //     linha.appendChild(campo_funcao);
    //     linha.appendChild(campo_edite);
    //     linha.appendChild(campo_delete);

       
    
    //     //vincula os elementos ao documento
    //     tabela.appendChild(linha);


     
    // }

}

/**
 * Pesquisa um usuário específico 
 */
function get_user(){

}

