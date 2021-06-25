
const token = sessionStorage.getItem("access_token");
let pacientes={};
let medicamentos ={};
get_all_pacientes();
get_medicamentos();

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
            alert("Paciente Deletado com Sucesso")
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

/**
 * Função do botão de Cancelar o cadastro do paciente
 */
function cancela_cadastro(){
    location.href='/enf-chefe'
}

/**
 * Busca todos os medicamentos no sistema
 */

 function get_medicamentos(){
    axios.get('/medicamento',{
        headers: { Authorization: `Bearer ${token}` }
    }).then((response)=>{
        medicamentos = response.data;
    }).catch((error)=>{
        console.error(error)
    })
}


function ordem_administracao(){
    let nome_paciente = document.getElementById('nome_paciente').value;
    // let leito_paciente = document.getElementById('leito_paci').value;
    let nome_medicamento = document.getElementById('nome_medicamento').value;
    // let tipo_uso = document.getElementById('tipo_uso').value;
    let orientacao = document.getElementById('orientacao').value;
    let possiveis_reacoes = document.getElementById('possiveis_reacoes').value;
    // let hora_aplicacao = document.getElementById('hora_aplicacao').value;
    // let intervalo_aplicacao = document.getElementById('intervalo_aplicacao').value;
    // let frequencia_diaria = document.getElementById('frequencia_diaria').value;
    let dosagem = document.getElementById('dosagem').value;

    let cpf_paci= busca_paci(nome_paciente); 
    let codi_medi =busca_medicamento(nome_medicamento);

    // let agendamento = {
    //     paciente: nome_paciente,
    //     leito: leito_paciente,
    //     medicamento:nome_medicamento,
    //     uso: tipo_uso,
    //     orientacao:orientacao,
    //     reacoes:possiveis_reacoes,
    //     horaAplicacao: hora_aplicacao,
    //     intAplicacao:intervalo_aplicacao,
    //     frequencia:frequencia_diaria,
    //     quantidade:dosagem

    // }

    let posologia = {
        medicamento: codi_medi,
        paciente:cpf_paci,
        quantidade:dosagem,
        notas: `${orientacao} ${possiveis_reacoes}`
    }
    
    axios.post('/posologia',{
        headers: { Authorization: `Bearer ${token}` },
        posology:{
            medicamento: codi_medi,
            paciente:cpf_paci,
            quantidade:dosagem,
            notas: `${orientacao} ${possiveis_reacoes}`
        }
    }).then((response)=>{
        alert(response.data)
    }).catch((error)=>{
        console.log(error);
    })
    console.log(codi_medi)
    console.log(cpf_paci)
    console.log(posologia)

  
}
/**
 * Retorna o cpf do paciente procurado
 * @param {*} nome_paciente nome do paciente String
 * @returns string cpf
 */
function busca_paci(nome_paciente){
    get_all_pacientes();
   for(let i=0;i<pacientes.length;i++){
       if(pacientes[i].nome == nome_paciente){
           return pacientes[i].CPF;
        }
    }
}

/**
 * Retorna o codigo do medicamento solicitado
 */
function busca_medicamento(medicamento){
    for(let i=0;i<medicamentos.length;i++){
        if(medicamentos[i].nome == medicamento){
            return medicamentos[i].codigo;
        }
    }
}

/**
 * Função Logout
 */
 function logout(){
    let resp = confirm("Tem certeza que deseja Sair?");
    if(resp){
        sessionStorage.removeItem("access_token");
        location.href='/'
    }

}