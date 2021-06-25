const token = sessionStorage.getItem("access_token");

let enfermeiros = {};
get_all_enf();
function get_all_enf(){
    axios.get('/enfermeiro',{
        headers: { Authorization: `Bearer ${token}` }
    }).then((response)=>{
        enfermeiros=response.data;
        cria_tabela_enf(enfermeiros)
    }).catch((error)=>{
        console.log(error);
    })
}

/**
 * Cria uma tabela que lista todos os pacientes cadastrados na UTI
 * @param {*} pacientes Lista de todos os pacientes cadastrados
 */
 function cria_tabela_enf(enfermeiros){
    const tabela = document.getElementById('tBody');

    for(let i=0;i<enfermeiros.length;i++){

        var newRow = tabela.insertRow();

        var cell_cpf = newRow.insertCell();
        var cell_nome = newRow.insertCell();
        // var cell_dataNascimento = newRow.insertCell();
        // var cell_dataInternacao = newRow.insertCell();
        // var cell_prontuario = newRow.insertCell();
        // var cell_editar = newRow.insertCell();
        // var cell_delete= newRow.insertCell();

        // let btEditar = document.createElement('button');
        // btEditar.innerHTML='Editar';
        // btEditar.setAttribute('onclick',`update_paciente(${i})`);
        // btEditar.setAttribute('id','btnEditar');

        // let btDeletar = document.createElement('button');
        // btDeletar.innerHTML='Deletar';
        // btDeletar.setAttribute('onclick', `delete_paciente(${i})`);
        // btDeletar.setAttribute('id','btnDeletar');


        cell_cpf.innerHTML = enfermeiros[i].CPF;
        cell_nome.innerHTML = enfermeiros[i].nome;
        // cell_dataNascimento.innerHTML =formata_data(pacientes[i].data_nascimento);
        // cell_dataInternacao.innerHTML = formata_data(pacientes[i].created_on);
        // cell_prontuario.innerHTML= pacientes[i].dados;
        // cell_editar.appendChild(btEditar);
        // cell_delete.appendChild(btDeletar);
        
    }
    
    document.getElementById('txtBusca').addEventListener("keyup", get_user);
}

