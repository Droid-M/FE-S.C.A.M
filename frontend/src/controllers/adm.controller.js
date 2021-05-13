const axios = require('axios').default;

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
