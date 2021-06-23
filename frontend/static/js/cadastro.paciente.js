const access_token = sessionStorage.getItem("access_token");

const url = location.href;

let state = false;
let params = url.split("=");
let id='';

if(params.length>1){
    id = params[1];
    state=true;
}

if(state && id!=undefined){
    update_paci();
    let btn = document.getElementById('btnCadastrar');
    btn.innerHTML="Salvar";
}


/**
 * Cadastra um novo paciente no sistema
 */
 function cadastro_paciente(){

    let nome = document.getElementById('nome').value;
    let sobrenome = document.getElementById('sobrenome').value;
    let genero = document.getElementById('genero').value;
    let sexo = document.getElementById('sexo').value;
    let cpf = document.getElementById('cpf').value;
    let dataNascimento = document.getElementById('dataNascimento').value;
    let select = document.getElementById('sangue');
    let tipoSangue = select.options[select.selectedIndex].value;

    let endereco = document.getElementById('endereco').value;
    let telefone = document.getElementById('telefone').value;

    let diagnostico = document.getElementById('dados').value;
    let id_func = document.getElementById('responsavel').value;

    let dataFormatada='';

    //verifica se a data nao é vazia e faz a alteração para salvar no BD
    if(dataNascimento.length>0){

        let data_spli = dataNascimento.split("/");
        let date = new Date(data_spli[2],data_spli[1]-1,data_spli[0]);
        dataFormatada =(date.getFullYear()+"-"+date.getMonth()+"-"+date.getDate());

    }

    // verifica se o cpf nao está vazio e faz a alteração para salvar no BD
    if(cpf.length>0){
        let result_cpf = cpf.split(".")
        cpf='';
        result_cpf.forEach(numbers => {
            cpf+=numbers;
        });
       
        let result2_cpf = cpf.split("-")
        cpf='';
        result2_cpf.forEach((n)=>{
            cpf+=n;
        })
    }
   

    let paciente = {
        CPF: cpf,
        nome:nome+" "+ sobrenome,
        sexo: sexo,
        genero: genero,
        data_nascimento:dataFormatada,
        tipo_sangue: tipoSangue,
        endereco: endereco,
        telefone: telefone,
        nome_atendente: id_func,
        dados: diagnostico
    }
    axios({
        method: state ?'put':'post',
        url: state ? `/paciente/${id}` : '/paciente',
        headers: { Authorization: `Bearer ${access_token}` },
        data: paciente
           
        
    }). then((response)=>{
            let nome = response.data.nome;
            let CPF = response.data.CPF;

            if(state){
                alert(`Paciente ${nome} Atualizado com Sucesso`)
            }else{
                alert(`Paciente  ${nome} Cadastrado com Sucesso` );
            }
            location.href='/enf-chefe'
        
        console.log(response.data); 
    }).catch((error)=>{
        console.error(error);
    })
    
    console.log(paciente);
 

  
}

/**
 * Carrega os dados do paciente para ser editado
 */
function update_paci(){
    let paci ='';

        axios.get(`/paciente/${id}`,{
            headers: { Authorization: `Bearer ${access_token}` }
        }).then((response)=>{
            paci = response.data;

            let nome = document.getElementById('nome').value = paci.nome;
            // let sobrenome = document.getElementById('sobrenome').value;
            let genero = document.getElementById('genero').value = paci.genero;
            let sexo = document.getElementById('sexo').value = paci.sexo;
            let cpf = document.getElementById('cpf').value=paci.CPF;
            let dataNascimento = document.getElementById('dataNascimento').value = formata_data(paci.data_nascimento);
            let select = document.getElementById('sangue');
            let tipoSangue = select.options[select.selectedIndex].value;
        
            let endereco = document.getElementById('endereco').value = paci.endereco;
            let telefone = document.getElementById('telefone').value = paci.telefone;
        
            let diagnostico = document.getElementById('dados').value = paci.dados;
            let id_func = document.getElementById('responsavel').value = paci.nome_atendente;
        }).catch((error)=>{
            console.error(error);
        })
    
    
}