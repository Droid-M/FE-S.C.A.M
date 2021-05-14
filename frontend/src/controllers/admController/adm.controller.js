import {AdmService} from './adm.service.js';


/**
 * Busca todos os usuários
 */
function getUsers(){
    AdmService.getUsuarios().then((response)=>{

        const produtos = new Array(response[0]);
        const categorias = response[1];      
        // console.log(produtos)
    })
}

/**
 * Cria novo usuário
 */
function createUsers(){
    const cpf = document.getElementById('cpf').value;
    const nome= document.getElementById('nome').value;
    const email= document.getElementById('email').value;
    const senha=document.getElementById('senha').value;

    const response = AdmService.createUsers(cpf,nome,email,senha);

    if(response){
        console.log(response);
    }
    
}

/**
 * Atualiza usuário
 */
function updateUser(){

}
/**
 * Deleta um usuário
 */
function deleteUsuario(){

}
getUsers();