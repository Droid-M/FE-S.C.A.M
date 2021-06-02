const baseURL = "http://localhost:3000"

function getAllUsuarios(){
    const usuarios = axios.get(baseURL+'/produtos').then(function(response){
        document.body.addEventListener
        console.log(response.data);

    }).catch(function(error){
        console.log("errou");
    })

    document.querySelector("teste").innerHTML=usuarios
    console.log(getAllUsuarios());
}


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

}

/**
 * Pesquisa um usuário específico 
 */
function get_user(){

}

/**
 * 
 */


// const axios = require('../services/index')



// // retorna todos os usuários cadastrados

//   function getUsuarios(){
//     const usuarios = axios.get('/produtos')
//         .then(function(response){
//             response.data;
//         }).catch((e)=>{
//             console.log("error")
//         });  

// }

// console.log(getUsuarios())


// function cadastroUsuarios(){

// }
