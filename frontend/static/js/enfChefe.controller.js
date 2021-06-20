
const token = sessionStorage.getItem("access_token");

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

    if(dataNascimento.length>0){

        let data_spli = dataNascimento.split("/");
        let date = new Date(data_spli[2],data_spli[1]-1,data_spli[0]);
        dataFormatada =(date.getFullYear()+"-"+date.getMonth()+"-"+date.getDate());

    }


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
        atendente_id: id_func,
        dados: diagnostico
    }
    axios({
        method: 'post',
        url:'/paciente',
        headers: { Authorization: `Bearer ${token}` },
        data: paciente
           
        
    }). then((response)=>{
            let nome = response.data.nome;
            let CPF = response.data.CPF;


            alert(`Paciente Cadastrado com Sucesso: ${nome} ${CPF}` );
            location.href='/enf-chefe'
        
        console.log(response.data); 
    }).catch((error)=>{
        console.error(error);
    })
    
    console.log(paciente);
 

  
}


