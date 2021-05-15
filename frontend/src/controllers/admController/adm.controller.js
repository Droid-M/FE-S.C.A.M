import {AdmService} from './adm.service.js';


/**
 * Busca todos os usuários
 */
window.getUsers =function (){
    AdmService.getUsuarios().then((response)=>{

        const produtos = new Array(response[0]);
        const categorias = response[1];      
        // console.log(produtos)
    })
}

/**
 * Busca por um usuário específico
 */

window.getUserById() = function(){
    const cpf = document.getElementById('cpf').value;
    
     AdmService.getUsuarioId(cpf).then((response)=>{
         let usuario = response.data;

        

     })

}


/**
 * Cria novo usuário
 */
window.createUsers =function (){
    const cpf = document.getElementById('cpf').value;
    const nome= document.getElementById('nome').value;
    const email= document.getElementById('email').value;
    const senha=document.getElementById('senha').value;

    const response = AdmService.createUsers(cpf,nome,email,senha);

    response.then((resp)=>{
        console.log(resp.data);  // Mostra a resposta
    })
    
}

/**
 * Atualiza usuário
 */
window.updateUser=function (){
    const cpf = document.getElementById('cpf').value;
    getUserById(cpf); // carrega os dados do usuario na tela

    // const user = AdmService.getUsuarioId(cpf);

    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;

    const resp = AdmService.updateUser(cpf,nome,email,senha);
    resp.then((response)=>{
        console.log(response.data); // Mostra resposta
    }).catch((error)=>{
        console.log(error)
    })
}



/**
 * Deleta um usuário
 */
window.deleteUsuario= function (){
    
}
