

const access_token = sessionStorage.getItem("access_token");


let usuarios ={}  // Lista de todos os usuarios cadastrados no sistema
get_all_users();


/**
 * Redireciona para a pagina para fazer a edição dos dados
 */
function update_user(index){
    console.log("Cpf usuario clicado " + index)
    let user='';

    if(usuarios.length !=0){

           user = usuarios[index];
    }

    location.href=`/edicao-usuario/id=${user.CPF}`;

}

/**
 * Deleta Usuarios
 */
function delete_user(index){
    let user_del ='';
   if(usuarios.length !=0){
       for(let i=0;i<=index;i++){
            user_del = usuarios[i];
       }
   }
   
   if(user_del!= ''){
       let url = `/edicao_usuario/${user_del.CPF}`
       console.log(user_del.CPF)
       axios.delete(url,
        { headers: { Authorization: `Bearer ${access_token}` }})
            .then((response)=>{
                alert("Usuario Deletado com Sucesso");
                location.href='/admin'
            })
   }
}

/**
 * Busca todos os usuários cadastrados
 */
function get_all_users(){


    axios.get("/lista_usuario",{ 
        headers: { Authorization: `Bearer ${access_token}` }
        }).then((response)=>{
             usuarios = response.data;
        //adicionar condição de validação
            cria_tabela(usuarios);
            
    }).catch((error)=>{
        console.error(error);
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
        btEditar.setAttribute('onclick',`update_user(${i})`);
        btEditar.setAttribute('id','btnEditar');
    
        let btDeletar = document.createElement('button');
        btDeletar.innerHTML='Deletar';
        btDeletar.setAttribute('onclick',`delete_user(${i})`);
        
        
        cell_cpf.innerHTML=usuarios[i].CPF;
        cell_nome.innerHTML = usuarios[i].nome;
        cell_funcao.innerHTML=usuarios[i].tipo;
        cell_editar.appendChild(btEditar);
        cell_deletar.appendChild(btDeletar);
    }
    document.getElementById('txtBusca').addEventListener("keyup", get_user);
    qtd_user(); //carrega os cards
}

/**
 * Pesquisa um usuário específico 
 */
function get_user(){
    var tabela = document.getElementById('tBody');
    
    var busca = document.getElementById("txtBusca").value.toLowerCase();

    for(let i=0; i<tabela.childNodes.length;i++){
        var achou = false;
        var tr = tabela.childNodes[i];
        var td = tr.childNodes;
        // console.log(td)
        for(var j =0; j<td.length-2;j++){
            
            var value = td[j].childNodes[0].nodeValue.toLowerCase();
            if(value.indexOf(busca)>=0){
                achou = true;
            }
            
           
        }
        if(achou){
            tr.style.display = 'table-row';
        }else{
            tr.style.display='none';
        }

    }

}

/**
 * Mostra a quantidade de cada tipo de Usuario cadastrado no sistema
 */

function qtd_user(){
    if(usuarios.length!=0){
        var adm = usuarios.filter((usuario)=>{
            if(usuario.tipo=='ADMINISTRADOR'){
                return true;
            }
        })
        var enf_chefe = usuarios.filter((usuario)=>{
            if(usuario.tipo=='ENFERMEIRO_CHEFE'){
                return true;
            }
        })

        var enf = usuarios.filter((usuario)=>{
            if(usuario.tipo=='ENFERMEIRO'){
                return true;
            }
        })

        var est = usuarios.filter((usuario)=>{
            if(usuario.tipo=='ESTAGIARIO'){
                return true;
            }
        })

        document.getElementById('qtd-adm').innerHTML=`${adm.length}`;
        document.getElementById('qtd-enf-chefe').innerHTML=`${enf_chefe.length}`;
        document.getElementById('qtd-enfe').innerHTML=`${enf.length}`;
        document.getElementById('qtd-est').innerHTML=`${est.length}`;
    
    }
}