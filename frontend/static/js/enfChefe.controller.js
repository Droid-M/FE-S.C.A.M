
const token = sessionStorage.getItem("access_token");
let pacientes={};
get_all_pacientes();

/**
 * Atualiza os dados de um paciente
 */
function update_paciente(id_paci){
    let paci = '';
    if(pacientes.length>0){
        paci = pacientes[id_paci];
    }
    location.href=`/cadastro-paciente/id=${paci.CPF}`;

}

/**
 * Exclui um paciente do sistema da uti
 * @param {*} index 
 */
function delete_paciente(index){
    if(pacientes.length>0){
        let paci = pacientes[index];

        axios.delete(`/paciente/${paci.CPF}`,{
            headers: { Authorization: `Bearer ${token}` }
        }).then((response)=>{
            alert("Usuario Deletado com Sucesso")
            location.href='/enf-chefe';
    
        }).catch((error)=>{
            console.error(error)
        })
    }
}

/**
 * Busca todos os pacientes cadastrados
 */
function get_all_pacientes(){

    axios.get('/paciente',{
        headers: { Authorization: `Bearer ${token}` }
    }).then((response)=>{
        pacientes = response.data;

        cria_tabela_paci(pacientes);
      
    }).catch((error)=>{
        console.error(error);
    })
}

/**
 * Cria uma tabela que lista todos os pacientes cadastrados na UTI
 * @param {*} pacientes Lista de todos os pacientes cadastrados
 */
function cria_tabela_paci(pacientes){
    const tabela = document.getElementById('tBody');

    for(let i=0;i<pacientes.length;i++){

        var newRow = tabela.insertRow();

        var cell_cpf = newRow.insertCell();
        var cell_nome = newRow.insertCell();
        var cell_dataNascimento = newRow.insertCell();
        var cell_dataInternacao = newRow.insertCell();
        var cell_prontuario = newRow.insertCell();
        var cell_editar = newRow.insertCell();
        var cell_delete= newRow.insertCell();

        let btEditar = document.createElement('button');
        btEditar.innerHTML='Editar';
        btEditar.setAttribute('onclick',`update_paciente(${i})`);
        btEditar.setAttribute('id','btnEditar');

        let btDeletar = document.createElement('button');
        btDeletar.innerHTML='Deletar';
        btDeletar.setAttribute('onclick', `delete_paciente(${i})`);
        btDeletar.setAttribute('id','btnDeletar');


        cell_cpf.innerHTML = pacientes[i].CPF;
        cell_nome.innerHTML = pacientes[i].nome;
        cell_dataNascimento.innerHTML =formata_data(pacientes[i].data_nascimento);
        cell_dataInternacao.innerHTML = formata_data(pacientes[i].created_on);
        cell_prontuario.innerHTML= pacientes[i].dados;
        cell_editar.appendChild(btEditar);
        cell_delete.appendChild(btDeletar);
        
    }
    
    document.getElementById('txtBusca').addEventListener("keyup", get_user);
}

/**
 * Formata Data para o formato DD-MM-YYYY
 * @param {*} dados String data
 * @returns string - Data Formatada
 */
function formata_data(dados){
    var data = new Date(dados);
    var dataFormatada = (data.getDate()+"/"+data.getMonth()+"/"+data.getFullYear());
    return dataFormatada;
}


/**
 * Pesquisa um Paciente específico 
 */
 function get_user(){
    var tabela = document.getElementById('tb_paciente');
    
    var busca = document.getElementById("txtBusca").value.toLowerCase();
    const corpo =tabela.childNodes[3];
    console.log(corpo.childNodes)
    for(let i=0; i<corpo.childNodes.length;i++){
        var achou = false;
        var tr = corpo.childNodes[i];
        var td = tr.childNodes;
 
        for(var j =0; j<td.length-3;j++){
            
            var value = td[j].childNodes[0].nodeValue.toLowerCase();
            // console.log(value)
            if(value.indexOf(busca)>=0){
                achou = true;
            }
            
           
        }
        if(achou){
            tr.style.display='table-row'
          
        }else{
            tr.style.display='none'
          
        }

    }

}
